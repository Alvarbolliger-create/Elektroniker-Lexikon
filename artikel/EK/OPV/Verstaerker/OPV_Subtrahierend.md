---
title: OPV Subtrahierender Verstärker
kategorie: EK
kapitel: OPV
tags: [subtrahierender verstärker, differenzverstärker, brückenauswertung, gleichtaktunterdrückung, cmrr, differenz, symmetrisch]
groessen: U_A|Ausgangsspannung|V; R_R|Gegenkopplungswiderstand|Ω; R_E|Eingangswiderstand|Ω; CMRR|Gleichtaktunterdrückung|dB
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Invertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[Instrumentenverstärker]]
- [[OPV Summierend]]
:::
:::vbox
**Führt weiter zu**
- [[Instrumentenverstärker]]
:::
:::

---

Der subtrahierende Verstärker gibt die Differenz zweier Eingangssignale verstärkt aus. Voraussetzung: alle vier Widerstände müssen exakt übereinstimmen, sonst leidet die Gleichtaktunterdrückung (CMRR) stark.

## Schaltung mit gleichen Widerständen

:::schematic Subtrahierender OPV-Verstärker: OPV-Dreieck. U_E1 → R_E1 → invertierender Eingang (−). R_R1 von Ausgang zurück auf (−). U_E2 → R_E2 → nichtinvertierender Eingang (+). R_R2 von (+) nach GND. Alle vier Widerstände gleich: R_E1 = R_E2 = R_R1 = R_R2. Ausgang U_A = R_R/R_E × (U_E2 − U_E1)
/Diagramm/opv_subtrahierend.svg
:::

U_E1 über R_E an den invertierenden Eingang (–), R_R von Ausgang zurück auf (–). U_E2 über R_E an den nichtinvertierenden Eingang (+), R_R von (+) nach GND.

## Formeln (gleiche Widerstände R_E1 = R_E2 = R_E, R_R1 = R_R2 = R_R)

:::formel
U_A = R_R / R_E * (U_E2 - U_E1)    # Differenzverstärkung
U_E1 = U_E2 * R_R / (U_A * R_E)    # Eingang 1
U_E2 = U_A * R_E / R_R + U_E1      # Eingang 2
R_R  = U_A * R_E / (U_E2 - U_E1)   # Gegenkopplungswiderstand
R_E  = R_R / U_A * (U_E2 - U_E1)   # Eingangswiderstand
:::

## Allgemeine Formel (ungleiche Widerstände)

:::formel
U_A = (1 + R_R1/R_E1) / (1 + R_E2/R_R2) * U_E2 - R_R1/R_E1 * U_E1
:::

Für gleiche Widerstände vereinfacht sich das zur obigen Formel.

## Berechnungsbeispiel

:::monospace
U_E1 = 1 V, U_E2 = 3 V, v_u = 5, R_E = 10 kΩ
R_R = v_u × R_E = 5 × 10 kΩ = 50 kΩ
U_A = 50k/10k × (3 V - 1 V) = 5 × 2 V = 10 V ✓
:::

## CMRR und Widerstandstoleranz

Die **Gleichtaktunterdrückung (CMRR)** gibt an, wie gut Gleichtaktsignale (gleiche Spannung an beiden Eingängen) unterdrückt werden. Sie hängt extrem von der Widerstandspaarung ab:

| Widerstandstoleranz | Erreichbarer CMRR |
|---|---|
| 1 % | ca. 40 dB |
| 0.1 % | ca. 60 dB |
| 0.01 % | ca. 80 dB |
| Präzisions-INA | > 100 dB |

## Abgrenzung zum Instrumentenverstärker

Der einfache Subtrahierverstärker hat zwei Schwächen:
- **Niederohmiger Eingang** (R_E, typisch 10 kΩ) — belastet die Quelle
- **CMRR begrenzt durch Widerstandstoleranz** — für Messzwecke oft ungenügend

Für Präzisionsmessungen → [[Instrumentenverstärker (3-OPV)]]

:::warning
Alle vier Widerstände müssen paarweise exakt übereinstimmen (R_E1 = R_E2, R_R1 = R_R2). 1 % Toleranz-Standardwiderstände geben nur 40 dB CMRR — bei 1 V Gleichtakt kommen 10 mV Störsignal am Ausgang an.
:::
