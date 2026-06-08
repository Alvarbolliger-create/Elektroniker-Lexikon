---
title: OPV Nichtinvertierender Verstärker
kategorie: EK
kapitel: OPV
tags: [nichtinvertierend, nicht-invertierender verstärker, opv, gegenkopplung, spannungsteiler, hochohmiger eingang, gleichphasig, verstärkung]
groessen: v_u|Verstärkung|—; U_A|Ausgangsspannung|V; U_E|Eingangsspannung|V; R_R|Gegenkopplungswiderstand|Ω; R1|Eingangswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Invertierender Verstärker]]
- [[OPV Spannungsfolger]]
:::
:::vbox
**Führt weiter zu**
- [[OPV Summierender Verstärker]]
- [[Instrumentenverstärker (3-OPV)]]
:::
:::

---

Der nichtinvertierende Verstärker gibt das Signal mit definierter Verstärkung wieder — **gleichphasig**. Der Eingangswiderstand ist sehr hoch (Eingang liegt direkt am OPV), die Verstärkung immer ≥ 1.

## Schaltung

:::schematic Nicht-invertierender Verstärker
/schaltplaene/OPV/Verstärker/opv_nichtinvertierender_verstaerker.svg
:::

Signal an den nichtinvertierenden Eingang (+). R1 von invertierendem Eingang (–) nach GND. R_R von Ausgang zurück auf invertierenden Eingang (–).

## Formeln

:::formel
U_A = U_E * (1 + R_R / R1)    # Ausgangsspannung
v_u = 1 + R_R / R1            # Verstärkung; immer ≥ 1, gleichphasig (kein Minuszeichen)
:::

## Herleitung mit goldenen Regeln

Da kein Strom in die Eingänge fliesst, bilden R1 und R_R einen Spannungsteiler: U_- = U_A · R1/(R1 + R_R). Goldene Regel: U_- = U_+ = U_E. Auflösen nach U_A ergibt die Verstärkungsformel.

## Berechnungsbeispiel

:::monospace
Gesucht: v_u = 5, R1 = 10 kΩ
R_R = R1 * (v_u - 1) = 10 kΩ × (5 - 1) = 40 kΩ → Normwert 39 kΩ

Probe: v_u = 1 + 39k/10k = 4.9 → nahe genug
:::

## Wichtige Unterschiede zum invertierenden Verstärker

| Eigenschaft | Nichtinvertierend | Invertierend |
|---|---|---|
| Verstärkung | ≥ 1 | beliebig (auch < 1) |
| Vorzeichen | positiv (gleichphasig) | negativ (180°) |
| Eingangswiderstand | sehr hoch (GΩ) | R1 (wählbar) |
| Virtuelle Masse | — | Ja (am –-Eingang) |

:::tip
Für Verstärkungen < 1 (Abschwächer) den invertierenden Verstärker verwenden (R_R < R1). Der nichtinvertierende Verstärker kann nicht unter Verstärkung 1 betrieben werden — bei R_R = 0 wird er zum Spannungsfolger.
:::
