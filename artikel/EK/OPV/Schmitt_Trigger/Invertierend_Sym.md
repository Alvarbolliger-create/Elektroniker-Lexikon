---
title: Schmitt-Trigger invertierend symmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, invertierend, symmetrisch, dual supply, mitkopplung, phasenumkehr, schaltschwelle, hysterese]
groessen: U_e_ein|Untere Schaltschwelle|V; U_e_aus|Obere Schaltschwelle|V; U_hys|Hysterese|V; R1|Widerstand (+) nach GND|Ω; R_M|Mitkopplungswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Schmitt-Trigger Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Schmitt-Trigger nicht invertierend symmetrisch]]
- [[Schmitt-Trigger invertierend unsymmetrisch]]
:::
:::vbox
**Führt weiter zu**
- [[Schmitt-Trigger invertierend unsymmetrisch]]
:::
:::

---

Der invertierende Schmitt-Trigger ist **phasenumgekehrt**: wenn der Eingang steigt, fällt der Ausgang. Er ist der häufigste Typ — das Signal geht direkt auf (−), der (+)-Eingang bildet mit R1 und R_M die Schaltschwelle.

## Schaltung

:::schematic Invertierender Schmitt-Trigger (symmetrisch, ±VCC): OPV-Dreieck. Eingangssignal U_e direkt auf den invertierenden Eingang (−). Am nichtinvertierenden Eingang (+): Spannungsteiler aus R_M (von Ausgang U_a) und R1 (nach GND). Versorgung ±VCC. Schaltschwellen symmetrisch um 0 V. Phasenumkehr 180°
/Diagramm/st_inv_sym.svg
:::

- Signal U_e → invertierender Eingang (−) direkt
- R_M von Ausgang U_a → (+)-Eingang (Mitkopplung)
- R1 von (+)-Eingang → GND (Spannungsteiler für Schwellenpotential)

## Herleitung der Schaltschwellen

Beim Umschalten gilt U_+ = U_− = U_e (da (−) direkt am Signal). Am (+)-Knoten herrscht ein Spannungsteiler aus R_M (von U_a) und R1 (nach GND):

:::formel
U_+ = U_a * R1 / (R1 + R_M)    # Spannungsteiler-Gleichung für U_+
:::

Umschalten tritt auf wenn U_+ = U_e:

:::formel
U_e = U_a * R1 / (R1 + R_M)    # allgemeine Schwellenformel
:::

**Obere Schwelle** (U_a war HIGH = U_a_High, z.B. +VCC, Ausgang schaltet auf LOW):

:::formel
U_e_aus = R1 / (R1 + R_M) * U_a_High    # positiver Wert (obere Schwelle)
:::

**Untere Schwelle** (U_a war LOW = U_a_Low, z.B. −VCC, Ausgang schaltet auf HIGH):

:::formel
U_e_ein = R1 / (R1 + R_M) * U_a_Low    # negativer Wert (untere Schwelle)
:::

:::warning
Bei invertierendem ST ist die Benennung umgekehrt: U_e_ein ist die **tiefere** Schwelle (Eingang muss tief sein, damit Ausgang HIGH wird). U_e_aus ist die **höhere** Schwelle (Eingang muss hoch sein, damit Ausgang LOW wird).
:::

**Hysterese:**

:::formel
U_hys = U_e_aus - U_e_ein = R1 / (R1 + R_M) * (U_a_High - U_a_Low)
:::

## Alle Formeln (gesammelt)

:::formel
U_e_aus = R1 / (R1 + R_M) * U_a_High    # obere Schwelle (HIGH→LOW)
U_e_ein = R1 / (R1 + R_M) * U_a_Low     # untere Schwelle (LOW→HIGH)
U_hys   = R1 / (R1 + R_M) * (U_a_High - U_a_Low)
R1      = R_M * U_e_aus / (U_a_High - U_e_aus)
R_M     = R1 * (U_a_High / U_e_aus - 1)
:::

Bei symmetrischer Versorgung (U_a_High = +VCC, U_a_Low = −VCC):

:::formel
U_e_aus = +VCC * R1 / (R1 + R_M)     # positiv
U_e_ein = -VCC * R1 / (R1 + R_M)     # negativ
U_hys   = 2 * VCC * R1 / (R1 + R_M)
:::

## Berechnungsbeispiel

:::monospace
Gesucht: Schwellen ±2 V bei ±5 V Versorgung (Hysterese = 4 V)
→ U_a_High = +5 V, U_a_Low = −5 V

Aus U_e_aus = R1/(R1+R_M) × U_a_High:
2 = R1/(R1+R_M) × 5
R1/(R1+R_M) = 0.4 → z.B. R1 = 10 kΩ, R_M = 15 kΩ

Probe:
  U_e_aus = 10k/(10k+15k) × 5 = +2 V ✓
  U_e_ein = 10k/(10k+15k) × (−5) = −2 V ✓
  U_hys   = 2 − (−2) = 4 V ✓
:::

## Vergleich: invertierend vs. nicht invertierend (symmetrisch)

| Eigenschaft | Nicht invertierend | Invertierend |
|---|---|---|
| Signal an | (+) via R1 | (−) direkt |
| Mitkopplung | U_a → R_M → (+) | U_a → R_M → (+) via R1 |
| Phasenlage | 0° (gleichphasig) | 180° (invertiert) |
| Schwellenformel | −R1/R_M × U_a | R1/(R1+R_M) × U_a |
| Einfacher aufzubauen | Ja (Signal direkt) | Braucht Spannungsteiler |
| Häufiger verwendet | Seltener | **Häufiger** |
