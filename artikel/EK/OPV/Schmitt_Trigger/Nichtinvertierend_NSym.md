---
title: Schmitt-Trigger nicht invertierend unsymmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, nichtinvertierend, unsymmetrisch, single supply, referenzspannung, verschobene schwellen, microcontroller, batterie]
groessen: U_e_ein|Obere Schaltschwelle|V; U_e_aus|Untere Schaltschwelle|V; U_hys|Hysterese|V; U_ref|Referenzspannung|V; R_E|Eingangswiderstand|Ω; R_M|Mitkopplungswiderstand|Ω
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

:::schematic Nicht invertierender Schmitt-Trigger (unsymmetrisch): OPV-Dreieck. U_e → R_E → nichtinvertierender Eingang (+). Ausgang U_a → R_M → (+) (Mitkopplung). Invertierender Eingang (−) an Referenzspannung U_ref (Spannungsteiler oder separate Referenz). Ausgangspegel U_a_High und U_a_Low (z.B. 0 V und +15 V bei Single Supply). Schaltschwellen verschoben um U_ref
/Diagramm/st_nichtinv_nsym.svg
:::

- Signal U_e → R_E → (+)
- Mitkopplung: U_a → R_M → (+)
- (−) an Referenzspannung U_ref (kein GND!)

## Herleitung der Schaltschwellen

Beim Umschalten gilt U_+ = U_− = U_ref. KCL am (+)-Knoten:

:::formel
(U_e - U_ref) / R_E + (U_a - U_ref) / R_M = 0
U_e - U_ref = -(U_a - U_ref) * R_E / R_M
U_e = U_ref - (U_a - U_ref) * R_E / R_M
U_e = U_ref + (U_ref - U_a) * R_E / R_M    # allgemeine Schwellenformel
:::

**Obere Schwelle** (U_a war LOW = U_a_Low, Ausgang schaltet auf HIGH):

:::formel
U_e_ein = U_ref + (U_ref - U_a_Low) * R_E / R_M    # > U_ref (obere Schwelle)
:::

**Untere Schwelle** (U_a war HIGH = U_a_High, Ausgang schaltet auf LOW):

:::formel
U_e_aus = U_ref + (U_ref - U_a_High) * R_E / R_M    # < U_ref (untere Schwelle)
:::

**Hysterese:**

:::formel
U_hys = U_e_ein - U_e_aus = (U_a_High - U_a_Low) * R_E / R_M
:::

Die Hysterese hängt nur vom Verhältnis R_E/R_M und den Ausgangspegeln ab — nicht von U_ref. U_ref verschiebt das gesamte Schwellenpaar, verändert aber nicht die Breite der Hysterese.

## Alle Formeln (gesammelt)

:::formel
U_e_ein = U_ref + (U_ref - U_a_Low)  * R_E / R_M    # obere Schwelle (LOW→HIGH)
U_e_aus = U_ref + (U_ref - U_a_High) * R_E / R_M    # untere Schwelle (HIGH→LOW)
U_hys   = (U_a_High - U_a_Low) * R_E / R_M
R_E     = U_hys * R_M / (U_a_High - U_a_Low)
R_M     = U_hys * R_E / (U_a_High - U_a_Low)        # → R_M aus gewünschter Hysterese
:::

## Berechnungsbeispiel

:::monospace
Single-Supply: V+ = +15 V, GND.
U_a_High = +15 V, U_a_Low = 0 V
Gewünschte Schwellen: U_e_ein = 11.25 V (obere), U_e_aus = 3.75 V (untere)
→ U_hys = 11.25 − 3.75 = 7.5 V
→ U_ref = (11.25 + 3.75) / 2 = 7.5 V (Schwellenmitte)

Schritt 1: R_E/R_M aus Hysterese
  U_hys = (U_a_High − U_a_Low) × R_E/R_M
  R_E/R_M = 7.5 / 15 = 0.5 → z.B. R_E = 10 kΩ, R_M = 20 kΩ

Schritt 2: U_ref einstellen
  U_ref = 7.5 V → Spannungsteiler 2 × 10 kΩ von +15 V nach GND

Probe:
  R_E/R_M = 10k/20k = 0.5
  U_e_ein = 7.5 + (7.5 −  0) × 0.5 = 7.5 + 3.75 = 11.25 V ✓
  U_e_aus = 7.5 + (7.5 − 15) × 0.5 = 7.5 − 3.75 =  3.75 V ✓
  U_hys   = 11.25 − 3.75 = 7.5 V ✓
:::

:::tip
U_ref legt die **Mitte** der Hysterese fest. U_hys wird durch R_E/R_M und die Ausgangspegel bestimmt. Die zwei Parameter können unabhängig gewählt werden.
:::

## Typische Anwendung: Single-Supply Mikrocontroller

Ein Mikrocontroller arbeitet mit 0–3.3 V. Ein Sensor liefert ein langsam steigendes Signal mit Rauschen. Gewünschte Schwellen: 1.5 V (low) und 1.8 V (high). Mitte = 1.65 V → U_ref = 1.65 V (Spannungsteiler).
