---
title: Schmitt-Trigger invertierend unsymmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, invertierend, unsymmetrisch, single supply, referenzspannung, verschobene schwellen, phasenumkehr]
groessen: U_e_ein|Untere Schaltschwelle|V; U_e_aus|Obere Schaltschwelle|V; U_hys|Hysterese|V; U_ref|Referenzspannung|V; R1|Widerstand (+) nach U_ref|Ω; R2|Mitkopplungswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Schmitt-Trigger invertierend symmetrisch]]
:::
:::vbox
**Verwandte Artikel**
- [[Schmitt-Trigger nicht invertierend unsymmetrisch]]
- [[Schmitt-Trigger invertierend symmetrisch]]
:::
:::vbox
**Führt weiter zu**
- [[Oszillatoren Grundlagen]]
:::
:::

---

Der invertierende unsymmetrische Schmitt-Trigger verschiebt die Schaltschwellen mit einer Referenzspannung U_ref aus der Mitte um 0 V heraus. Typisch für Single-Supply-Schaltungen oder wenn die Schwellen in einem bestimmten Spannungsbereich liegen müssen.

## Schaltung

:::schematic Invertierender Schmitt-Trigger (unsymmetrisch, Single Supply mit Referenz U_ref)
/schaltplaene/OPV/Schmitttriger/opv_schmitttrigger_i_single.svg
:::

- Signal U_e → (−) direkt
- R2 von Ausgang U_a → (+) (Mitkopplung)
- R1 von U_ref → (+) (Referenzverschiebung)

**Vergleich zu symmetrisch**: Im symmetrischen Fall geht R1 nach GND (U_ref = 0 V). Hier geht R1 nach einer beliebigen Referenz.

## Schaltschwellen

Beim Umschalten gilt U_+ = U_− = U_e. Am (+)-Knoten verschieben R2 (von U_a) und R1 (von U_ref) das Schaltpotential um U_ref aus der Mitte:

:::formel
U_e_aus = U_a_High * R1/(R1 + R2) + U_ref * R2/(R1 + R2)    # obere Schwelle (HIGH→LOW)
U_e_ein = U_a_Low  * R1/(R1 + R2) + U_ref * R2/(R1 + R2)    # untere Schwelle (LOW→HIGH)
U_hys   = (U_a_High - U_a_Low) * R1 / (R1 + R2)
:::

Die Hysterese hängt nur von R1/R2 und den Ausgangspegeln ab — nicht von U_ref. U_ref verschiebt beide Schwellen zusammen.

**Sonderfall U_ref = 0** (symmetrischer Betrieb): vereinfacht zu den Formeln der [[Schmitt-Trigger invertierend symmetrisch|symmetrischen Variante]].

## Berechnungsbeispiel

:::monospace
Single-Supply: V+ = 5 V, GND.
U_a_High = 5 V, U_a_Low = 0 V.
Gewünschte Schwellen: U_e_ein = 1.5 V (untere), U_e_aus = 2.5 V (obere)
→ U_hys = 2.5 − 1.5 = 1.0 V

R1/(R1+R2) = U_hys / (U_a_High − U_a_Low) = 1.0 / 5.0 = 0.2
→ z.B. R1 = 10 kΩ, R2 = 40 kΩ (R1/R2 = 1/4, R1/(R1+R2) = 10/50 = 0.2) ✓

U_ref = U_e_ein − U_a_Low × R1/(R1+R2)
     = 1.5 − 0 × 0.2 = ...

Besser: aus U_e_ein-Formel:
1.5 = 0 × 0.2 + U_ref × 0.8
U_ref = 1.5 / 0.8 = 1.875 V → Spannungsteiler: R_refA = 62.5 kΩ, R_refB = 37.5 kΩ von 5V

Probe:
  U_e_aus = 5 × 0.2 + 1.875 × 0.8 = 1.0 + 1.5 = 2.5 V ✓
  U_e_ein = 0 × 0.2 + 1.875 × 0.8 = 0   + 1.5 = 1.5 V ✓
  U_hys   = 2.5 − 1.5 = 1.0 V ✓
:::

:::tip
Dimensionierungsstrategie: Zuerst R1/R2 aus der gewünschten Hysterese berechnen. Dann U_ref aus der gewünschten Schwellenmitte bestimmen. Zuletzt Normwerte wählen und alle Schwellen gegenprüfen.
:::
