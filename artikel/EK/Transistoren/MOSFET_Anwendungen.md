---
title: MOSFET Anwendungen
kategorie: EK
kapitel: Transistoren
tags: [mosfet, schalten, leistungselektronik, gate-treiber, bootstrap, body-diode, r_ds_on, h-brücke, low-side, high-side, shoot-through, totzeit, gate-ladung]
groessen: R_DS(on)|Einschaltwiderstand|mΩ; Q_g|Gate-Ladung|nC; U_th|Schwellspannung|V; t_d|Totzeit|ns; P_v|Verlustleistung|W
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[FET Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[IGBT]]
- [[H-Brücke]]
- [[DC-DC Wandler Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[H-Brücke]]
- [[DC-DC Wandler Grundlagen]]
:::
:::

---

Der MOSFET ist der Standardschalter in der Leistungselektronik. Im Gegensatz zum BJT braucht er keinen Dauersteuerstrom, schaltet sehr schnell und hat im eingeschalteten Zustand nur einen kleinen Widerstand R_DS(on). Dieser Artikel zeigt die praktische Anwendung als Leistungsschalter.

## Verlustleistungen im Schaltbetrieb

Im MOSFET-Schalter entstehen zwei Arten von Verlusten:

**Durchlassverluste** (I² · R):
:::formel
P_durch = I_D² * R_DS(on) * D    # D = Tastverhältnis (Einschaltzeit / Periode)
:::

**Schaltverluste** (entstehen beim Ein-/Ausschalten):
:::formel
P_schalt = 0.5 * U_DS * I_D * (t_ein + t_aus) * f_s    # steigen linear mit Frequenz
:::

Bei niedrigen Frequenzen dominieren Durchlassverluste → kleinen R_DS(on) wählen.
Bei hohen Frequenzen dominieren Schaltverluste → schnell schaltende MOSFETs wählen.

## Gate-Ladung und Treiberstrom

Das Gate ist eine Kapazität (Eingangskapazität C_iss = 1–10 nF). Um schnell zu schalten, muss sie schnell umgeladen werden:

:::formel
t_schalt = Q_g / I_Treiber    # Schaltzeit; Q_g aus Datenblatt
P_gate   = Q_g * U_GS * f_s  # Gate-Treiberverluste (steigen mit Frequenz)
:::

Ein einfacher Mikrocontroller-I/O (10 mA) reicht bei kleinen Q_g und niedrigen Frequenzen. Für grosse MOSFETs oder hohe Frequenzen braucht es einen **Gate-Treiber-IC** (IR2110, TC4420 — 1–4 A Treiberstrom).

**Gate-Widerstand R_G** (10–47 Ω in Reihe): dämpft Schwingungen durch Leitungsinduktivität, verlangsamt aber leicht das Schalten. Im Layout Gate-Leitungen kurz halten.

## Low-Side vs. High-Side

**Low-Side** (Source auf GND): Einfach — U_GS = Gate-Spannung relativ zu GND. Standard-Gate-Treiber reichen.

**High-Side** (Source auf Schaltspannung): Source liegt auf U_Bat statt GND. Das Gate muss höher als U_Bat getrieben werden (U_GS = U_Gate – U_Source). Problem: der Treiber hat keinen Bezug zu GND.

**Bootstrap-Schaltung** löst das:

:::schematic Bootstrap Gate-Treiber: U_VCC → D_boot → C_boot → Source des High-Side MOSFET. Wenn Low-Side leitet (Schaltknoten auf GND): C_boot lädt sich auf U_VCC. Wenn High-Side schalten soll: C_boot schwimmt auf U_Bat, treibt Gate über U_Bat. Schaltknoten-Potential eingezeichnet
/Diagramm/mosfet_bootstrap.svg
:::

1. Kleiner Kondensator C_boot (100 nF – 1 µF) lädt sich auf U_VCC auf wenn Low-Side leitet
2. Wenn High-Side schalten soll, wird C_boot als floating Supply für den Gate-Treiber genutzt
3. C_boot kann sich bei > 95 % Tastverhältnis entleeren — nicht für Vollaussteuerung geeignet

**Isolierter Gate-Treiber** (HCPL-314J, ADuM3223) für 100 % Tastverhältnis und galvanische Trennung.

## Body-Diode und Freilaufdiode

Jeder N-Kanal MOSFET hat eine interne **Body-Diode** (Source-Substrat-Diode) in Gegenrichtung. Sie leitet wenn U_DS negativ wird. In Halbbrücken übernimmt sie den Freilaufstrom beim Schalten.

Nachteil: Die Body-Diode ist langsam (schlechte Sperrschicht-Sperrerholzeit). In schnellen Schaltreglern wird sie durch eine externe Schottky-Diode parallel überbrückt.

## Shoot-Through und Totzeit

:::schematic Halbbrücke mit Totzeit: U_Bat oben, GND unten. High-Side MOSFET (oben) und Low-Side MOSFET (unten) in Reihe. Gemeinsamer Schaltknoten in der Mitte zur Last. Gate-Signale: High-Side EIN / Low-Side AUS, dann Totzeit (beide AUS), dann High-Side AUS / Low-Side EIN. Shoot-Through markiert: beide gleichzeitig EIN = Kurzschluss
/Diagramm/mosfet_halbbruecke.svg
:::

In einer **Halbbrücke** (High-Side + Low-Side MOSFET) dürfen nie beide gleichzeitig leiten — direkter Kurzschluss der Versorgungsspannung ("Shoot-Through"):

:::formel
t_tot ≥ t_aus(max)    # Totzeit > maximale Ausschaltzeit des abschaltenden MOSFET
:::

Der Gate-Treiber muss beide Kanäle mit einer **Totzeit** verzögern (typisch 100–300 ns). Zu kurze Totzeit: Shoot-Through. Zu lange Totzeit: erhöhte Verluste durch Body-Dioden-Leitung.

## Typische Bauteile

| Typ | U_DS | I_D | R_DS(on) | Q_g | Einsatz |
|---|---|---|---|---|---|
| 2N7000 | 60 V | 0.2 A | 5 Ω | 5 nC | Logik, Kleinsignal |
| IRLZ44N | 55 V | 47 A | 22 mΩ | 140 nC | 5V-Logik Leistung |
| IRF540N | 100 V | 33 A | 44 mΩ | 71 nC | 12V Schaltregler |
| IPD50N04 | 40 V | 50 A | 5 mΩ | 40 nC | DC-DC, H-Brücke |
| SiC C3M0065090 | 900 V | 36 A | 65 mΩ | 10 nC | PV-Wechselrichter |

:::tip
R_DS(on) und Q_g sind gegenläufig: kleiner R_DS(on) → grosser MOSFET → grosse Q_g → mehr Schaltverluste. Das optimale Bauteil minimiert P_durch + P_schalt bei der jeweiligen Schaltfrequenz.
:::
