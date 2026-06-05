---
title: RLC-Parallelschaltung (Parallelschwingkreis)
kategorie: ET
tags: [RLC, parallelschaltung, parallelschwingkreis, resonanz, güte, bandbreite, stromüberhöhung, leitwert]
groessen: Y|Scheinleitwert|S; G|Wirkleitwert|S; B_L|induktiver Blindleitwert|S; B_C|kapazitiver Blindleitwert|S; f_r|Resonanzfrequenz|Hz; Q|Güte|—; b|Bandbreite|Hz; omega_0|Resonanzkreisfrequenz|rad/s
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[RL-Parallelschaltung]]
- [[RC-Parallelschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[RLC-Reihenschaltung (Serieschwingkreis)]]
:::
:::vbox
**Führt weiter zu**
- [[Resonanz & Schwingkreise]]
:::
:::

---

Die RLC-Parallelschaltung ist das Dual zur Reihenschaltung: Alle drei Bauteile liegen parallel an derselben Spannung. Bei Resonanz heben sich B_L und B_C auf — die Impedanz ist maximal, der Gesamtstrom minimal.

## Gesamtstrom und Leitwerte

Alle drei Zweige teilen dieselbe Spannung U. Die Teilströme sind:

:::hbox
:::formel
I_R = U * G
:::
:::formel
I_L = U * B_L
:::
:::formel
I_C = U * B_C
:::
:::

Der Scheinleitwert:

:::formel
Y = sqrt(G^2 + (B_C - B_L)^2)
:::

Dabei: G = 1/R, B_L = 1/X_L = 1/(omega·L), B_C = 1/X_C = omega·C.

## Phasenverschiebung

:::formel
phi = arctan((B_C - B_L) / G)
:::

| Bereich | Bedingung | Verhalten |
|---|---|---|
| f < f_r | B_L > B_C | Induktiv: phi < 0° |
| f = f_r | B_L = B_C | Rein ohmsch: Y = G, Z = R (Maximum) |
| f > f_r | B_C > B_L | Kapazitiv: phi > 0° |

## Resonanzfrequenz

Gleiche Formel wie beim Serieschwingkreis:

:::formel
omega_0 = 1 / sqrt(L * C)
:::

:::formel
f_r = 1 / (2 * pi * sqrt(L * C))
:::

Bei Resonanz ist Y = G → Z = R (Maximalimpedanz). Die Schaltung stellt der Quelle den grössten Widerstand entgegen — der Strom aus der Quelle ist minimal.

## Güte Q

:::formel
Q = R / (omega_0 * L)    # = R * omega_0 * C
:::

## Bandbreite

:::formel
b = f_r / Q
:::

## Stromüberhöhung in L und C

In L und C zirkuliert bei Resonanz ein Kreisstrom, der Q-mal grösser ist als der Quellenstrom:

:::formel
I_L = Q * I_ges
:::
:::formel
I_C = Q * I_ges
:::

Dieser Kreisstrom fliesst zwischen L und C hin und her — die Energie pendelt zwischen magnetischem (L) und elektrischem (C) Feld.

:::warning
Bei hohem Q entstehen in L und C Ströme, die vielfach grösser sind als der Quellenstrom. Bei Blindleistungskompensationsanlagen mit Resonanzgefahr (z. B. durch Oberschwingungen) müssen Kondensatoren und Drosseln entsprechend dimensioniert werden.
:::

:::tip
Der Parallelschwingkreis wird als **Bandpass** oder **Sperrkreis** eingesetzt: In der Abstimmschaltung eines Radios selektiert er genau die gewünschte Frequenz. Bei Resonanz ist seine Impedanz maximal → die Resonanzfrequenz "passiert" durch einen Reihenwiderstand kaum gedämpft.
:::
