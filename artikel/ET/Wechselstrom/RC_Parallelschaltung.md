---
title: RC-Parallelschaltung
kategorie: ET
tags: [RC, parallelschaltung, leitwert, blindleitwert, wirkleitwert, scheinleitwert, wechselstrom]
groessen: Y|Scheinleitwert|S; G|Wirkleitwert|S; B_C|kapazitiver Blindleitwert|S; phi|Phasenwinkel|°; I|Strom|A; U|Spannung|V; Z|Impedanz|Ohm
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[RC-Reihenschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[RL-Parallelschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[RLC-Parallelschaltung (Parallelschwingkreis)]]
:::
:::

---

Bei der RC-Parallelschaltung teilt sich der Strom in den Wirkstrom (durch R) und den kapazitiven Blindstrom (durch C) auf. Der kapazitive Strom eilt der Spannung vor — entgegen dem induktiven Fall bei der RL-Parallelschaltung.

## Spannung und Teilströme

An beiden Zweigen liegt dieselbe Spannung U. Die Teilströme sind:

:::hbox
:::formel
I_R = U / R    # in Phase mit U
:::

:::formel
I_C = U / X_C    # 90° vor U (kapazitiver Strom eilt vor)
:::
:::

## Gesamtstrom

I_R und I_C sind 90° phasenverschoben — sie addieren sich vektoriell:

:::formel
I_ges = sqrt(I_R^2 + I_C^2)
:::

## Scheinleitwert Y

:::hbox
:::formel
G = 1 / R
:::

:::formel
B_C = 1 / X_C    # = omega * C
:::

:::formel
Y = sqrt(G^2 + B_C^2)
:::
:::

## Phasenverschiebung

Der Gesamtstrom I_ges eilt der Spannung um phi vor (kapazitive Last):

:::formel
phi = arctan(B_C / G)    # positiv: Strom voreilend (kapazitiv)
:::

## Impedanz

:::formel
Z_ges = 1 / Y
:::

:::monospace
Beispiel: U = 100 V, f = 1 kHz, R = 1 kOhm, C = 100 nF
X_C = 1 / (2*pi*1000*100e-9) = 1592 Ohm
I_R = 100 / 1000 = 100 mA
I_C = 100 / 1592 = 62.8 mA
I_ges = sqrt(100^2 + 62.8^2) = 118 mA
phi = arctan(62.8/100) = 32.1°  (kapazitiv)
:::

## Umgekehrte Berechnung

Wenn Gesamtstrom und Wirkstrom bekannt sind, lässt sich der Blindstrom berechnen:

:::formel
I_C = sqrt(I_ges^2 - I_R^2)
X_C = U / I_C
C   = 1 / (omega * X_C)
:::

Ebenso für den Leitwert: G = √(Y² − B_C²), R = 1/G.

## Vergleich RL und RC Parallelschaltung

| Eigenschaft | RL-Parallel | RC-Parallel |
|---|---|---|
| Blindkomponente | I_L (nacheilend) | I_C (voreilend) |
| Phasenwinkel phi | < 0° (induktiv) | > 0° (kapazitiv) |
| B | B_L = 1/X_L | B_C = omega·C |
| Anwendung | Motormodell | Kompensation, Filter |

:::tip
Die RC-Parallelschaltung ist das Grundmodell der **Blindleistungskompensation**: Kondensatoren (kapazitiv, positives Q) werden parallel zu induktiven Lasten (Motoren, Trafos) geschaltet. Der kapazitive Blindstrom kompensiert den induktiven — der Netzstrom sinkt und der Leistungsfaktor steigt. → [[Blindleistungskompensation]]
:::
