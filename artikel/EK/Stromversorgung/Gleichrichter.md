---
title: Gleichrichter
kategorie: EK
kapitel: Stromversorgung
tags: [gleichrichter, einweggleichrichter, brückengleichrichter, brummspannung, siebkondensator, welligkeit, gleichspannung, netzteil, U_mittel, U_spitze, tau, diode]
groessen: U_2|Sekundärspannung Trafo|V; U_spitze|Spitzenspannung|V; U_mittel|Mittelpannung|V; U_Brumm|Brummspannung|V; C_L|Siebkondensator|F; f|Netzfrequenz|Hz
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[Zener-Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[Spannungsstabilisierung]]
:::
:::vbox
**Führt weiter zu**
- [[Spannungsstabilisierung]]
- [[DC-DC-Wandler]]
:::
:::

---

Ein Gleichrichter wandelt Wechselspannung (AC) in pulsierende Gleichspannung um. Mit einem Siebkondensator wird die Welligkeit reduziert.

## Einweggleichrichter

:::schematic Einweggleichrichter mit Siebkondensator: AC-Quelle (Trafo-Sekundär U_2) links. Diode D1 in Reihe (Kathode nach rechts). Siebkondensator C_L und Last R_L parallel nach GND. Oben: AC-Eingangswelle (sinusförmig). Unten: Ausgangsspannung (nur positive Halbwellen, mit Welligkeit). Eingezeichnet: U_spitze, U_mittel, U_Brumm
/Diagramm/gleichrichter_einweg.svg
:::

Eine Diode leitet nur die positive Halbwelle durch. Die negative Halbwelle wird gesperrt.

**Eigenschaften:**
- Grosse Welligkeit (nur jede zweite Halbwelle genutzt)
- Transformator leistungsmässig schlecht ausgenutzt
- Kann auch ohne Transformator betrieben werden

:::formel
U_spitze = U_2_eff * sqrt(2) - U_F        # Spitzenspannung nach Diode (U_F ≈ 0.7 V Si)
U_mittel  = U_spitze / pi                  # Mittelwert Einweggleichrichter ≈ 0.318 * U_spitze
:::

## Brückengleichrichter

:::schematic Brückengleichrichter (Graetz-Schaltung) mit Siebkondensator: Vier Dioden D1–D4 in Brückenanordnung. AC-Eingang an zwei gegenüberliegenden Ecken (links/rechts). DC-Ausgang an den anderen zwei Ecken (oben = + über C_L und R_L nach unten = GND). Positive Halbwelle: D1 und D3 leiten. Negative Halbwelle: D2 und D4 leiten. Ausgangswelligkeit: doppelte Netzfrequenz (100 Hz). U_spitze = U_2_eff × √2 − 2×U_F
/Diagramm/gleichrichter_bruecke.svg
:::

Vier Dioden in Brückenschaltung — beide Halbwellen werden gleichgerichtet (Vollweggleichrichter).

**Eigenschaften:**
- Kleinere Welligkeit (beide Halbwellen nutzbar, doppelte Frequenz)
- Transformator leistungsmässig gut ausgenutzt
- Zwei Dioden in Reihe → 2 × U_F Spannungsabfall

:::formel
U_spitze = U_2_eff * sqrt(2) - 2 * U_F    # Spitzenspannung (2 Dioden in Reihe)
U_mittel  = 2 * U_spitze / pi             # Mittelwert Brückengleichrichter ≈ 0.637 * U_spitze
:::

## Brummspannung

Die Brummspannung U_Brumm ist die verbleibende Welligkeit nach dem Siebkondensator C_L. Je grösser die Zeitkonstante τ = R_L · C_L, desto kleiner die Brummspannung:

:::formel
tau     = R_L * C_L                     # Zeitkonstante Siebglied
U_Brumm = I_L / (f * C_L)              # Näherungsformel Brummspannung
C_L     = I_L / (f * U_Brumm)          # Siebkondensator aus Lastrom und Brumm
f       = 100 Hz                        # Netzfrequenz Brückengleichrichter (2 × 50 Hz)
f       = 50 Hz                         # Netzfrequenz Einweggleichrichter
:::

:::info
Der Brückengleichrichter hat die doppelte Pulsfrequenz (100 Hz statt 50 Hz) — der Siebkondensator wird öfter nachgeladen, die Brummspannung ist bei gleicher Kapazität halb so gross.
:::

## Vergleich Einweg vs. Brücke

| Eigenschaft | Einweggleichrichter | Brückengleichrichter |
|---|---|---|
| Dioden | 1 | 4 |
| Pulsfrequenz | 50 Hz | 100 Hz |
| Welligkeit | gross | klein |
| Trafo-Nutzung | schlecht (50 %) | gut (100 %) |
| Spannungsabfall | 1 × U_F | 2 × U_F |
| Typischer Einsatz | einfache Schaltungen, Ladegeräte | Netzteile, Leistungselektronik |

:::monospace
Designbeispiel Brückengleichrichter: 12 V / 1 A Netzteil
U_2_eff = 12 V → U_spitze = 12 × √2 − 1.4 = 15.6 V
U_mittel = 2 × 15.6 / π = 9.9 V (vor Stabilisierung)
U_Brumm = 1 % von U_mittel = 0.1 V
C_L = I_L / (f × U_Brumm) = 1 / (100 × 0.1) = 100 µF → 220 µF (E6, nächster Wert)
:::
