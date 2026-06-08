---
title: RLC-Reihenschaltung (Serieschwingkreis)
kategorie: ET
tags: [RLC, reihenschaltung, serieschwingkreis, resonanz, güte, bandbreite, spannungsüberhöhung]
groessen: Z|Impedanz|Ohm; R|Wirkwiderstand|Ohm; X_L|induktive Reaktanz|Ohm; X_C|kapazitive Reaktanz|Ohm; f_r|Resonanzfrequenz|Hz; Q|Güte|—; b|Bandbreite|Hz; omega_0|Resonanzkreisfrequenz|rad/s
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[RL-Reihenschaltung]]
- [[RC-Reihenschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[RLC-Parallelschaltung (Parallelschwingkreis)]]
:::
:::vbox
**Führt weiter zu**
- [[Resonanz & Schwingkreise]]
:::
:::

---

Die RLC-Reihenschaltung vereint Wirkwiderstand, Induktivität und Kapazität in einem Zweig. Bei der Resonanzfrequenz heben sich X_L und X_C auf — die Schaltung verhält sich rein ohmsch und der Strom erreicht sein Maximum.

:::schematic RLC-Reihenschaltung
/schaltplaene/Resonanz/rlc_reihe.svg
:::

## Impedanz

X_L und X_C wirken entgegengesetzt: X_L wächst mit f, X_C sinkt. Die Differenz (X_L − X_C) bestimmt das reaktive Verhalten:

:::formel
Z = sqrt(R^2 + (X_L - X_C)^2)
:::

| Bereich | Bedingung | Verhalten |
|---|---|---|
| f < f_r | X_C > X_L | Kapazitiv: phi < 0° |
| f = f_r | X_C = X_L | Rein ohmsch: phi = 0°, Z = R (Minimum) |
| f > f_r | X_L > X_C | Induktiv: phi > 0° |

## Phasenverschiebung

:::formel
phi = arctan((X_L - X_C) / R)
:::

## Resonanzfrequenz

Bei Resonanz: X_L = X_C, also omega · L = 1/(omega · C):

:::formel
omega_0 = 1 / sqrt(L * C)
:::

:::formel
f_r = 1 / (2 * pi * sqrt(L * C))
:::

## Güte Q

Die Güte Q beschreibt, wie "scharf" der Resonanzpeak ist. Ein hoher Q-Wert bedeutet enge Bandbreite und hohe Spannungsüberhöhung.

:::formel
Q = omega_0 * L / R
:::

## Bandbreite

:::formel
b = f_r / Q    # Bandbreite zwischen den 3-dB-Punkten
:::

## Spannungsüberhöhung bei Resonanz

An L und C entstehen bei Resonanz Spannungen, die Q-fach grösser sind als die Eingangsspannung:

:::formel
U_L = Q * U_ein
:::

:::formel
U_C = Q * U_ein
:::

Die Gesamtspannung U_L + U_C hebt sich auf (sie sind 180° phasenverschoben) — aber die Einzelspannungen können sehr gross werden!

:::warning
Bei hohem Q (z. B. Q = 50) entstehen an L und C Spannungen, die 50× höher sind als die Eingangsspannung. Bauteile müssen für diese Überspannungen ausgelegt sein. In Schwingkreisfiltern können Kondensatoren durch Resonanzüberspannung zerstört werden.
:::

:::monospace
Beispiel: L = 1 mH, C = 10 nF, R = 10 Ohm
omega_0 = 1/sqrt(1e-3 * 10e-9) = 316 228 rad/s
f_r = 316228 / (2*pi) = 50.3 kHz
Q = 316228 * 1e-3 / 10 = 31.6
b = 50300 / 31.6 = 1.59 kHz
U_L = U_C = 31.6 * U_ein bei Resonanz
:::

:::tip
Der RLC-Serieschwingkreis ist das Grundmodell für schmalbandige **Bandpassfilter** und **Bandperrenfilter** (Saugkreise). → [[Resonanz & Schwingkreise]]
:::
