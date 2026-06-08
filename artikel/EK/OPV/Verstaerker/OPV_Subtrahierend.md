---
title: OPV Subtrahierender Verstärker
kategorie: EK
kapitel: OPV
tags: [subtrahierender verstärker, differenzverstärker, brückenauswertung, gleichtaktunterdrückung, cmrr, differenz, symmetrisch]
groessen: U_A|Ausgangsspannung|V; R1|Eingangswiderstand Eingang 1|Ω; R2|Gegenkopplungswiderstand|Ω; R3|Eingangswiderstand Eingang 2|Ω; R4|Widerstand (+) nach GND|Ω; CMRR|Gleichtaktunterdrückung|dB
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Invertierender Verstärker]]
:::
:::vbox
**Verwandte Artikel**
- [[Instrumentenverstärker (3-OPV)]]
- [[OPV Summierender Verstärker]]
:::
:::vbox
**Führt weiter zu**
- [[Instrumentenverstärker (3-OPV)]]
:::
:::

---

Der subtrahierende Verstärker gibt die Differenz zweier Eingangssignale verstärkt aus. Voraussetzung: alle vier Widerstände müssen exakt übereinstimmen, sonst leidet die Gleichtaktunterdrückung (CMRR) stark.

## Schaltung

:::schematic Subtrahierer (Differenzverstärker)
/schaltplaene/OPV/Verstärker/opv_subtrahierer.svg
:::

U_E1 über R1 an den invertierenden Eingang (–), R2 von Ausgang zurück auf (–). U_E2 über R3 an den nichtinvertierenden Eingang (+), R4 von (+) nach GND.

## Allgemeine Formel (beliebige Widerstände)

:::formel
U_A = (1 + R2/R1) / (1 + R3/R4) * U_E2 - R2/R1 * U_E1
:::

## Formel für gleiche Widerstände (R1 = R3, R2 = R4)

:::formel
U_A = R2 / R1 * (U_E2 - U_E1)    # Differenzverstärkung
:::

## Berechnungsbeispiel

:::monospace
U_E1 = 1 V, U_E2 = 3 V, v_u = 5, R1 = R3 = 10 kΩ
R2 = R4 = v_u × R1 = 5 × 10 kΩ = 50 kΩ
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
- **Niederohmiger Eingang** (R1/R3, typisch 10 kΩ) — belastet die Quelle
- **CMRR begrenzt durch Widerstandstoleranz** — für Messzwecke oft ungenügend

Für Präzisionsmessungen → [[Instrumentenverstärker (3-OPV)]]

:::warning
Alle vier Widerstände müssen paarweise exakt übereinstimmen (R1 = R3, R2 = R4). 1 % Toleranz-Standardwiderstände geben nur 40 dB CMRR — bei 1 V Gleichtakt kommen 10 mV Störsignal am Ausgang an.
:::
