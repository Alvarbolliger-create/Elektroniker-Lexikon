---
title: Schmitt-Trigger invertierend unsymmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, invertierend, unsymmetrisch, single supply, referenzspannung, verschobene schwellen, phasenumkehr]
groessen: U_e_ein|Untere Schaltschwelle|V; U_e_aus|Obere Schaltschwelle|V; U_hys|Hysterese|V; U_ref|Referenzspannung|V; R1|Widerstand (+) nach U_ref|Ω; R_M|Mitkopplungswiderstand|Ω
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

:::schematic Invertierender Schmitt-Trigger (unsymmetrisch): OPV-Dreieck. Eingangssignal U_e direkt auf den invertierenden Eingang (−). Am nichtinvertierenden Eingang (+): R_M von Ausgang U_a, R1 von Referenzspannung U_ref. U_ref bestimmt die Mitte der Hysterese. Versorgung V+ und GND (Single-Supply). Ausgangspegel U_a_High und U_a_Low (z.B. 0 V und V+)
/Diagramm/st_inv_nsym.svg
:::

- Signal U_e → (−) direkt
- R_M von Ausgang U_a → (+) (Mitkopplung)
- R1 von U_ref → (+) (Referenzverschiebung)

**Vergleich zu symmetrisch**: Im symmetrischen Fall geht R1 nach GND (U_ref = 0 V). Hier geht R1 nach einer beliebigen Referenz.

## Herleitung der Schaltschwellen

Beim Umschalten gilt U_+ = U_− = U_e. Am (+)-Knoten gilt KCL (R_M von U_a, R1 von U_ref):

:::formel
(U_a - U_+) / R_M + (U_ref - U_+) / R1 = 0
U_a / R_M + U_ref / R1 = U_+ * (1/R_M + 1/R1)
U_+ = (U_a * R1 + U_ref * R_M) / (R1 + R_M)    # Potential am (+)-Eingang
:::

Beim Umschalten U_+ = U_e:

:::formel
U_e = U_a * R1/(R1 + R_M) + U_ref * R_M/(R1 + R_M)    # allgemeine Schwellenformel
:::

**Obere Schwelle** (U_a war HIGH = U_a_High, Ausgang schaltet zu LOW wenn U_e steigt):

:::formel
U_e_aus = U_a_High * R1/(R1 + R_M) + U_ref * R_M/(R1 + R_M)    # obere Schwelle
:::

**Untere Schwelle** (U_a war LOW = U_a_Low, Ausgang schaltet zu HIGH wenn U_e fällt):

:::formel
U_e_ein = U_a_Low * R1/(R1 + R_M) + U_ref * R_M/(R1 + R_M)    # untere Schwelle
:::

**Hysterese:**

:::formel
U_hys = U_e_aus - U_e_ein = (U_a_High - U_a_Low) * R1/(R1 + R_M)
:::

Die Hysterese hängt nur von R1/R_M und den Ausgangspegeln ab — nicht von U_ref. U_ref verschiebt beide Schwellen zusammen.

## Alle Formeln (gesammelt)

:::formel
U_e_aus = U_a_High * R1/(R1 + R_M) + U_ref * R_M/(R1 + R_M)    # obere Schwelle (HIGH→LOW)
U_e_ein = U_a_Low  * R1/(R1 + R_M) + U_ref * R_M/(R1 + R_M)    # untere Schwelle (LOW→HIGH)
U_hys   = (U_a_High - U_a_Low) * R1 / (R1 + R_M)
R1      = R_M * U_hys / (U_a_High - U_a_Low - U_hys)
:::

**Sonderfall U_ref = 0** (symmetrischer Betrieb): vereinfacht zu den Formeln der [[Schmitt-Trigger invertierend symmetrisch|symmetrischen Variante]].

## Berechnungsbeispiel

:::monospace
Single-Supply: V+ = 5 V, GND.
U_a_High = 5 V, U_a_Low = 0 V.
Gewünschte Schwellen: U_e_ein = 1.5 V (untere), U_e_aus = 2.5 V (obere)
→ U_hys = 2.5 − 1.5 = 1.0 V

R1/(R1+R_M) = U_hys / (U_a_High − U_a_Low) = 1.0 / 5.0 = 0.2
→ z.B. R1 = 10 kΩ, R_M = 40 kΩ (R1/R_M = 1/4, R1/(R1+R_M) = 10/50 = 0.2) ✓

U_ref = U_e_ein − U_a_Low × R1/(R1+R_M)
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
Dimensionierungsstrategie: Zuerst R1/R_M aus der gewünschten Hysterese berechnen. Dann U_ref aus der gewünschten Schwellenmitte bestimmen. Zuletzt Normwerte wählen und alle Schwellen gegenprüfen.
:::
