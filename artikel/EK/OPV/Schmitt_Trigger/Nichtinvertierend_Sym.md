---
title: Schmitt-Trigger nicht invertierend symmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, nichtinvertierend, symmetrisch, dual supply, mitkopplung, schaltschwelle, hysterese, gleichphasig]
groessen: U_e_ein|Obere Schaltschwelle|V; U_e_aus|Untere Schaltschwelle|V; U_hys|Hysterese|V; R1|Eingangswiderstand|Ω; R2|Mitkopplungswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Schmitt-Trigger Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Schmitt-Trigger invertierend symmetrisch]]
- [[Schmitt-Trigger nicht invertierend unsymmetrisch]]
:::
:::vbox
**Führt weiter zu**
- [[Schmitt-Trigger nicht invertierend unsymmetrisch]]
:::
:::

---

Der nicht invertierende Schmitt-Trigger ist **gleichphasig**: wenn der Eingang HIGH ist, ist auch der Ausgang HIGH. Er ist einfach aufgebaut — das Signal kommt direkt auf den (+)-Eingang.

## Schaltung

:::schematic Nicht invertierender Schmitt-Trigger (symmetrisch, ±VCC)
/schaltplaene/OPV/Schmitttriger/opv_schmitttrigger_ni.svg
:::

- Signal U_e → R1 → nichtinvertierender Eingang (+)
- Mitkopplung: Ausgang U_a → R2 → (+)
- Invertierender Eingang (−) auf GND

## Schaltschwellen

Der OPV schaltet, wenn U_+ = U_− = 0 V (da (−) auf GND). Am (+)-Knoten bilden R1 (vom Signal) und R2 (von U_a) einen Spannungsteiler, der je nach Ausgangszustand eine andere Eingangsspannung zum Umschalten erfordert:

:::formel
U_e_ein = -(R1 / R2) * U_a_Low     # obere Schaltschwelle (LOW→HIGH), positiv
U_e_aus = -(R1 / R2) * U_a_High    # untere Schaltschwelle (HIGH→LOW), negativ
U_hys   = (R1 / R2) * (U_a_High - U_a_Low)    # immer > 0
:::

## Berechnungsbeispiel

:::monospace
Gesucht: U_e_ein = +2 V, U_e_aus = −2 V bei ±5 V Versorgung
→ U_a_High = +5 V, U_a_Low = −5 V

Aus U_e_ein = −(R1/R2) × U_a_Low:
2 = −(R1/R2) × (−5)
R1/R2 = 0.4 → z.B. R1 = 10 kΩ, R2 = 25 kΩ

Probe:
  U_e_ein = −(10/25) × (−5) = +2 V ✓
  U_e_aus = −(10/25) × (+5) = −2 V ✓
  U_hys   = 2 − (−2) = 4 V ✓
:::

## Kennlinie

Das Schaltverhalten:

| U_e steigt | U_e fällt |
|---|---|
| Unter U_e_aus: Ausgang LOW | Über U_e_ein: Ausgang HIGH |
| Zwischen U_e_aus und U_e_ein: bleibt LOW | Zwischen U_aus und U_ein: bleibt HIGH |
| Über U_e_ein: schaltet auf HIGH | Unter U_e_aus: schaltet auf LOW |
