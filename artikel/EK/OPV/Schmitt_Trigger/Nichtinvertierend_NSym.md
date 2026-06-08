---
title: Schmitt-Trigger nicht invertierend unsymmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, nichtinvertierend, unsymmetrisch, single supply, referenzspannung, verschobene schwellen, microcontroller, batterie]
groessen: U_e_ein|Obere Schaltschwelle|V; U_e_aus|Untere Schaltschwelle|V; U_hys|Hysterese|V; U_ref|Referenzspannung|V; R1|Eingangswiderstand|Ω; R2|Mitkopplungswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Schmitt-Trigger nicht invertierend symmetrisch]]
:::
:::vbox
**Verwandte Artikel**
- [[Schmitt-Trigger invertierend unsymmetrisch]]
- [[Schmitt-Trigger nicht invertierend symmetrisch]]
:::
:::vbox
**Führt weiter zu**
- [[Oszillatoren Grundlagen]]
:::
:::

---

Die unsymmetrische Variante wird verwendet, wenn die Schaltschwellen nicht um 0 V zentriert sein sollen — z.B. bei Single-Supply-Betrieb (0 V … +5 V) oder wenn die Schaltschwellen im positiven Bereich liegen müssen. Der Unterschied zum symmetrischen Fall: am (−)-Eingang liegt eine **Referenzspannung U_ref** statt GND.

## Schaltung

:::schematic Nicht invertierender Schmitt-Trigger (unsymmetrisch, Single Supply mit Referenz U_ref)
/schaltplaene/OPV/Schmitttriger/opv_schmitttrigger_ni_single.svg
:::

- Signal U_e → R1 → (+)
- Mitkopplung: U_a → R2 → (+)
- (−) an Referenzspannung U_ref (kein GND!)

## Schaltschwellen

Beim Umschalten gilt U_+ = U_− = U_ref. R1 (vom Signal) und R2 (von U_a) bilden am (+)-Knoten einen Spannungsteiler, der die Schwellen um U_ref aus der Mitte verschiebt:

:::formel
U_e_ein = U_ref + (U_ref - U_a_Low)  * R1 / R2    # obere Schwelle (LOW→HIGH)
U_e_aus = U_ref + (U_ref - U_a_High) * R1 / R2    # untere Schwelle (HIGH→LOW)
U_hys   = (U_a_High - U_a_Low) * R1 / R2
:::

Die Hysterese hängt nur vom Verhältnis R1/R2 und den Ausgangspegeln ab — nicht von U_ref. U_ref verschiebt das gesamte Schwellenpaar, verändert aber nicht die Breite der Hysterese.

## Berechnungsbeispiel

:::monospace
Single-Supply: V+ = +15 V, GND.
U_a_High = +15 V, U_a_Low = 0 V
Gewünschte Schwellen: U_e_ein = 11.25 V (obere), U_e_aus = 3.75 V (untere)
→ U_hys = 11.25 − 3.75 = 7.5 V
→ U_ref = (11.25 + 3.75) / 2 = 7.5 V (Schwellenmitte)

Schritt 1: R1/R2 aus Hysterese
  U_hys = (U_a_High − U_a_Low) × R1/R2
  R1/R2 = 7.5 / 15 = 0.5 → z.B. R1 = 10 kΩ, R2 = 20 kΩ

Schritt 2: U_ref einstellen
  U_ref = 7.5 V → Spannungsteiler 2 × 10 kΩ von +15 V nach GND

Probe:
  R1/R2 = 10k/20k = 0.5
  U_e_ein = 7.5 + (7.5 −  0) × 0.5 = 7.5 + 3.75 = 11.25 V ✓
  U_e_aus = 7.5 + (7.5 − 15) × 0.5 = 7.5 − 3.75 =  3.75 V ✓
  U_hys   = 11.25 − 3.75 = 7.5 V ✓
:::

:::tip
U_ref legt die **Mitte** der Hysterese fest. U_hys wird durch R1/R2 und die Ausgangspegel bestimmt. Die zwei Parameter können unabhängig gewählt werden.
:::

## Typische Anwendung: Single-Supply Mikrocontroller

Ein Mikrocontroller arbeitet mit 0–3.3 V. Ein Sensor liefert ein langsam steigendes Signal mit Rauschen. Gewünschte Schwellen: 1.5 V (low) und 1.8 V (high). Mitte = 1.65 V → U_ref = 1.65 V (Spannungsteiler).
