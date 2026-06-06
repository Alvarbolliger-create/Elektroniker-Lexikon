---
title: IGBT
kategorie: EK
kapitel: Halbleiter
tags: [igbt, insulated gate bipolar transistor, leistungshalbleiter, wechselrichter, frequenzumrichter, gate-treiber, schaltverhalten, sättigungsspannung, gate-spannung]
groessen: U_CE|Kollektor-Emitter-Spannung|V; I_C|Kollektorstrom|A; U_GE|Gate-Emitter-Spannung|V; U_CE(sat)|Sättigungsspannung|V; R_th|Wärmewiderstand|K/W
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BJT Grundlagen]]
- [[FET Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[MOSFET Anwendungen]]
- [[Frequenzumrichter]]
:::
:::vbox
**Führt weiter zu**
- [[Frequenzumrichter]]
- [[H-Brücke]]
:::
:::

---

Der IGBT (Insulated Gate Bipolar Transistor) kombiniert die Vorteile von MOSFET und Bipolartransistor: spannungsgesteuerte Gate-Ansteuerung wie ein MOSFET, aber niedrige Durchlassspannung wie ein BJT bei hohen Strömen. Er dominiert die Leistungselektronik im Bereich 600 V bis 6.5 kV.

## Aufbau und Funktionsprinzip

:::schematic IGBT-Ersatzschaltbild: N-MOSFET (Gate-Eingang) steuert Basis eines PNP-Transistors (BJT). Kollektor am oberen Pol, Emitter unten — kombiniert Spannungssteuerung mit niedrigem Sättigungswiderstand
/Diagramm/igbt_ersatzschaltbild.svg
:::

Der IGBT hat drei Anschlüsse: **Gate (G)**, **Kollektor (C)** und **Emitter (E)**. Intern ist er ein MOSFET-Gate auf einem p-n-p-Bipolartransistor — der MOSFET steuert den Basisstrom des BJTs.

**Ansteuerung**: Wie ein MOSFET. Spannung ans Gate → schaltet ein (U_GE(th) typisch 4–6 V). Spannung weg → sperrt. Kein Treiberstrom nötig (nur Ladestrom für Gate-Kapazität).

**Leitverhalten**: Wie ein BJT. Niedrige Sättigungsspannung U_CE(sat) ≈ 1.5–3 V, unabhängig von der Stromstärke — bei hohen Strömen deutlich besser als ein MOSFET (R_DS(on) · I²).

## IGBT vs. MOSFET

| Eigenschaft | MOSFET | IGBT |
|---|---|---|
| Ansteuerung | Spannungsgesteuert | Spannungsgesteuert |
| Durchlassverluste | R_DS(on) · I² (steigt stark) | U_CE(sat) · I (günstiger bei hohen I) |
| Schaltgeschwindigkeit | sehr schnell (< 100 ns) | langsamer (0.5–5 µs) |
| Sperrspannung | bis 900 V | bis 6.5 kV |
| Strom | bis 100 A | bis 3.6 kA |
| Einsatz | < 600 V, hohe Freq. | > 600 V, mittlere Freq. |

**Break-even-Strom** — unter welchem der MOSFET besser ist:

:::formel
I_break = U_CE(sat) / R_DS(on)    # Gleichgewicht der Durchlassverluste
:::

Beispiel: R_DS(on) = 45 mΩ, U_CE(sat) = 2.3 V → I_break = 51 A. Unter 51 A liefert der MOSFET weniger Verlustleistung, darüber der IGBT.

**Faustregeln**:
- Unter 200 V → MOSFET
- 200–600 V → je nach Schaltfrequenz und Strom
- Über 600 V → IGBT

## Schaltverhalten

Der IGBT hat einen sogenannten **Schweif (Tail)** beim Ausschalten: Nach dem Abschalten des Gate-Impulses fliesst noch für einige Mikrosekunden ein Reststrom, bis die injizierten Minoritätsträger im BJT-Teil ausgeräumt sind. Dieser Tail erzeugt Schaltverluste, die mit der Frequenz steigen.

:::formel
P_Schalt = f * (E_ein + E_aus)    # Schaltverluste; E aus Datenblatt (µJ)
P_Durch = U_CE(sat) * I_C * D     # Durchlassverluste; D = Einschaltzeitraum
:::

## Gate-Ansteuerung

IGBTs brauchen spezielle **Gate-Treiber** (IR2110, TLP250, IXDD614):
- Gate-Spannung: typisch +15 V / –5 V (gegenüber Emitter)
- Negative Spannung verhindert parasitäres Einschalten (Miller-Kapazität)
- Treiberstrom für Umladung der Gate-Kapazität: einige Ampere (kurz)
- Gate-Widerstand R_G dämpft Schwingungen (typisch 10–47 Ω)

:::warning
Der IGBT hat keine integrierte Freilaufdiode. In Halbbrücken-Schaltungen (Wechselrichter, H-Brücke) muss immer eine antiparallele **Freilaufdiode (Body-Diode)** in den Schaltplan eingebaut werden — entweder intern (bei modernen IGBTs oft vorhanden) oder extern.
:::

## Anwendungen

**Frequenzumrichter**: Dreiphasige Wechselrichter für Drehstrommotoren arbeiten fast ausschliesslich mit IGBTs (3-phasige H-Brücke mit 6 IGBTs + 6 Dioden). → [[Frequenzumrichter]]

**Schweissgeräte**: Inverterschweissgeräte (800 Hz bis 100 kHz) mit IGBTs sind deutlich kleiner und leichter als netzfrequente Trafo-Geräte.

**Solare Wechselrichter**: PV-Strings umgewandelt zu 50 Hz Netzspannung.

**Zugantriebe / E-Fahrzeuge**: Traktionsinverter mit 400–800 V DC und mehreren 100 kW.
