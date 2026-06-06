---
title: OPV Nichtinvertierender Verstärker
kategorie: EK
kapitel: OPV
tags: [nichtinvertierend, nicht-invertierender verstärker, opv, gegenkopplung, spannungsteiler, hochohmiger eingang, gleichphasig, verstärkung]
groessen: v_u|Verstärkung|—; U_A|Ausgangsspannung|V; U_E|Eingangsspannung|V; R_R|Gegenkopplungswiderstand|Ω; R_E|Eingangswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Invertierend]]
- [[OPV Spannungsfolger]]
:::
:::vbox
**Führt weiter zu**
- [[OPV Summierend]]
- [[Instrumentenverstärker]]
:::
:::

---

Der nichtinvertierende Verstärker gibt das Signal mit definierter Verstärkung wieder — **gleichphasig**. Der Eingangswiderstand ist sehr hoch (Eingang liegt direkt am OPV), die Verstärkung immer ≥ 1.

## Schaltung

:::schematic Nichtinvertierender OPV-Verstärker: OPV-Dreieck. U_E → nichtinvertierender Eingang (+). Spannungsteiler am (−)-Eingang: R_E nach GND, R_R von Ausgang zurück auf (−). Ausgang U_A rechts. Phasenlage 0° (gleichphasig). Verstärkung ≥ 1
/Diagramm/opv_nichtinvertierend.svg
:::

Signal an den nichtinvertierenden Eingang (+). R_E von invertierendem Eingang (–) nach GND. R_R von Ausgang zurück auf invertierenden Eingang (–).

## Formeln

:::formel
U_A = U_E * (1 + R_R / R_E)    # Ausgangsspannung
U_E = U_A / (1 + R_R / R_E)    # Eingangsspannung (Umkehrformel)
R_R = R_E * (U_A - U_E) / U_E  # Gegenkopplungswiderstand
R_E = U_E * R_R / (U_A - U_E)  # Widerstand R_E
:::

Die Verstärkung berechnet sich zu:

:::formel
v_u = 1 + R_R / R_E    # immer ≥ 1, gleichphasig (kein Minuszeichen)
:::

## Herleitung mit goldenen Regeln

Da kein Strom in die Eingänge fliesst, gilt am Spannungsteiler R_E/R_R:

:::formel
U_- = U_A * R_E / (R_E + R_R)    # Spannung am Spannungsteiler
:::

Goldene Regel: U_- = U_+ = U_E. Auflösen nach U_A ergibt die Verstärkungsformel.

## Berechnungsbeispiel

:::monospace
Gesucht: v_u = 5, R_E = 10 kΩ
R_R = R_E * (v_u - 1) = 10 kΩ × (5 - 1) = 40 kΩ → Normwert 39 kΩ

Probe: v_u = 1 + 39k/10k = 4.9 → nahe genug
:::

## Wichtige Unterschiede zum invertierenden Verstärker

| Eigenschaft | Nichtinvertierend | Invertierend |
|---|---|---|
| Verstärkung | ≥ 1 | beliebig (auch < 1) |
| Vorzeichen | positiv (gleichphasig) | negativ (180°) |
| Eingangswiderstand | sehr hoch (GΩ) | R_E (wählbar) |
| Virtuelle Masse | — | Ja (am –-Eingang) |

:::tip
Für Verstärkungen < 1 (Abschwächer) den invertierenden Verstärker verwenden (R_R < R_E). Der nichtinvertierende Verstärker kann nicht unter Verstärkung 1 betrieben werden — bei R_R = 0 wird er zum Spannungsfolger.
:::
