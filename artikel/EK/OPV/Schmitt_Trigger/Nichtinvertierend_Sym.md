---
title: Schmitt-Trigger nicht invertierend symmetrisch
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, nichtinvertierend, symmetrisch, dual supply, mitkopplung, schaltschwelle, hysterese, gleichphasig]
groessen: U_e_ein|Obere Schaltschwelle|V; U_e_aus|Untere Schaltschwelle|V; U_hys|Hysterese|V; R1|Eingangswiderstand|Ω; R_M|Mitkopplungswiderstand|Ω
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

:::schematic Nicht invertierender Schmitt-Trigger (symmetrisch, ±VCC): OPV-Dreieck. Eingangssignal U_e über R1 auf den nichtinvertierenden Eingang (+). Ausgang U_a über R_M zurück auf den (+)-Eingang (Mitkopplung). Invertierender Eingang (−) direkt auf GND (0 V). Versorgung ±VCC. Schaltschwellen symmetrisch um 0 V
/Diagramm/st_nichtinv_sym.svg
:::

- Signal U_e → R1 → nichtinvertierender Eingang (+)
- Mitkopplung: Ausgang U_a → R_M → (+)
- Invertierender Eingang (−) auf GND

## Herleitung der Schaltschwellen

Der OPV schaltet, wenn U_+ = U_− = 0 V (da (−) auf GND). Beim Umschalten gilt KCL am (+)-Knoten:

:::formel
(U_e - U_+) / R1 + (U_a - U_+) / R_M = 0    # KCL am (+), mit U_+ = 0:
U_e / R1 + U_a / R_M = 0
U_e = -(R1 / R_M) * U_a                       # allgemeine Schwellenformel
:::

**Obere Schwelle** (U_a war LOW = U_a_Low, z.B. −VCC):

:::formel
U_e_ein = -(R1 / R_M) * U_a_Low    # positiver Wert, da U_a_Low negativ
:::

**Untere Schwelle** (U_a war HIGH = U_a_High, z.B. +VCC):

:::formel
U_e_aus = -(R1 / R_M) * U_a_High    # negativer Wert, da U_a_High positiv
:::

**Hysterese:**

:::formel
U_hys = U_e_ein - U_e_aus = (R1 / R_M) * (U_a_High - U_a_Low)    # immer > 0
:::

## Alle Formeln (gesammelt)

:::formel
U_e_ein = -(R1 / R_M) * U_a_Low     # obere Schaltschwelle (LOW→HIGH)
U_e_aus = -(R1 / R_M) * U_a_High    # untere Schaltschwelle (HIGH→LOW)
U_hys   = (R1 / R_M) * (U_a_High - U_a_Low)
R1      = R_M * U_e_ein / (-U_a_Low)
R_M     = R1 * (-U_a_Low) / U_e_ein
:::

Bei symmetrischer Versorgung (U_a_High = +VCC, U_a_Low = −VCC):

:::formel
U_e_ein = (R1 / R_M) * VCC     # vereinfacht: VCC positiv, VCC und -VCC gleich gross
U_e_aus = -(R1 / R_M) * VCC
U_hys   = 2 * (R1 / R_M) * VCC
:::

## Berechnungsbeispiel

:::monospace
Gesucht: U_e_ein = +2 V, U_e_aus = −2 V bei ±5 V Versorgung
→ U_a_High = +5 V, U_a_Low = −5 V

Aus U_e_ein = −(R1/R_M) × U_a_Low:
2 = −(R1/R_M) × (−5)
R1/R_M = 0.4 → z.B. R1 = 10 kΩ, R_M = 25 kΩ

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
