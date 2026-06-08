---
title: Schmitt-Trigger invertierend symmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, invertierend, symmetrisch, dual supply, mitkopplung, phasenumkehr, schaltschwelle, hysterese]
groessen: U_e_ein|Untere Schaltschwelle|V; U_e_aus|Obere Schaltschwelle|V; U_hys|Hysterese|V; R1|Widerstand (+) nach GND|Ω; R2|Mitkopplungswiderstand|Ω
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

Der invertierende Schmitt-Trigger ist **phasenumgekehrt**: wenn der Eingang steigt, fällt der Ausgang. Er ist der häufigste Typ — das Signal geht direkt auf (−), der (+)-Eingang bildet mit R1 und R2 die Schaltschwelle.

## Schaltung

:::schematic Invertierender Schmitt-Trigger (symmetrisch, ±VCC)
/schaltplaene/OPV/Schmitttriger/opv_schmitttrigger_i.svg
:::

- Signal U_e → invertierender Eingang (−) direkt
- R2 von Ausgang U_a → (+)-Eingang (Mitkopplung)
- R1 von (+)-Eingang → GND (Spannungsteiler für Schwellenpotential)

## Schaltschwellen

Beim Umschalten gilt U_+ = U_− = U_e (da (−) direkt am Signal). Am (+)-Knoten bilden R2 (von U_a) und R1 (nach GND) einen Spannungsteiler, der das Schaltpotential je nach Ausgangszustand verschiebt:

:::formel
U_e_aus = R1 / (R1 + R2) * U_a_High    # obere Schwelle (HIGH→LOW)
U_e_ein = R1 / (R1 + R2) * U_a_Low     # untere Schwelle (LOW→HIGH)
U_hys   = R1 / (R1 + R2) * (U_a_High - U_a_Low)
:::

:::warning
Bei invertierendem ST ist die Benennung umgekehrt: U_e_ein ist die **tiefere** Schwelle (Eingang muss tief sein, damit Ausgang HIGH wird). U_e_aus ist die **höhere** Schwelle (Eingang muss hoch sein, damit Ausgang LOW wird).
:::

## Berechnungsbeispiel

:::monospace
Gesucht: Schwellen ±2 V bei ±5 V Versorgung (Hysterese = 4 V)
→ U_a_High = +5 V, U_a_Low = −5 V

Aus U_e_aus = R1/(R1+R2) × U_a_High:
2 = R1/(R1+R2) × 5
R1/(R1+R2) = 0.4 → z.B. R1 = 10 kΩ, R2 = 15 kΩ

Probe:
  U_e_aus = 10k/(10k+15k) × 5 = +2 V ✓
  U_e_ein = 10k/(10k+15k) × (−5) = −2 V ✓
  U_hys   = 2 − (−2) = 4 V ✓
:::

## Vergleich: invertierend vs. nicht invertierend (symmetrisch)

| Eigenschaft | Nicht invertierend | Invertierend |
|---|---|---|
| Signal an | (+) via R1 | (−) direkt |
| Mitkopplung | U_a → R2 → (+) | U_a → R2 → (+) via R1 |
| Phasenlage | 0° (gleichphasig) | 180° (invertiert) |
| Schwellenformel | −R1/R2 × U_a | R1/(R1+R2) × U_a |
| Einfacher aufzubauen | Ja (Signal direkt) | Braucht Spannungsteiler |
| Häufiger verwendet | Seltener | **Häufiger** |
