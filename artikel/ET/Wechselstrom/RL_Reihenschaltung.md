---
title: RL-Reihenschaltung
kategorie: ET
tags: [RL, reihenschaltung, impedanz, phasenverschiebung, spule, widerstand, wechselstrom, grenzfrequenz]
groessen: Z|Impedanz|Ohm; R|Wirkwiderstand|Ohm; X_L|induktive Reaktanz|Ohm; phi|Phasenwinkel|°; U|Spannung|V; I|Strom|A; f|Frequenz|Hz; L|Induktivität|H; omega|Kreisfrequenz|rad/s
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
- [[Spule im Wechselstrom]]
:::
:::vbox
**Verwandte Artikel**
- [[RC-Reihenschaltung]]
- [[Zeigerdiagramm]]
:::
:::vbox
**Führt weiter zu**
- [[RL-Parallelschaltung]]
- [[RLC-Reihenschaltung (Serieschwingkreis)]]
:::
:::

---

Die RL-Reihenschaltung ist der einfachste Wechselstromkreis mit einem reaktiven Bauteil: Widerstand R und Spule L hintereinander. Die Spule erzeugt eine frequenzabhängige Phasenverschiebung — mit steigender Frequenz wird die Schaltung immer "induktiver".

## Induktive Reaktanz

Die Spule hat eine frequenzabhängige Reaktanz, die mit der Frequenz steigt:

:::formel
X_L = omega * L
:::

Bei Gleichstrom (f = 0 Hz, omega = 0) ist X_L = 0 — die Spule ist ein reiner Draht. Bei hohen Frequenzen wird X_L gross und die Spule sperrt den Stromfluss.

## Impedanz

R und X_L addieren sich nicht arithmetisch, weil sie um 90° phasenverschoben sind. Stattdessen gilt Pythagoras:

:::formel
Z = sqrt(R^2 + X_L^2)
:::

## Phasenverschiebung

Die Spannung an der Spule eilt dem Strom um 90° vor. Die Gesamtspannung U liegt deshalb zwischen U_R (in Phase) und U_L (90° vor) — der Phasenwinkel phi liegt zwischen 0° und 90°.

:::formel
phi = arctan(X_L / R)
:::

| Grenzfall | Bedingung | Verhalten |
|---|---|---|
| Rein ohmsch | X_L ≪ R | phi ≈ 0°, Z ≈ R |
| Rein induktiv | X_L ≫ R | phi ≈ 90°, Z ≈ X_L |

## Strom und Teilspannungen

Der Strom ist in einer Reihenschaltung überall gleich:

:::formel
I = U_ges / Z
:::

Die Teilspannungen ergeben sich aus:

:::hbox
:::formel
U_R = I * R
:::

:::formel
U_L = I * X_L
:::
:::

Die vektorielle Summe ergibt die Gesamtspannung (Zeigerdiagramm):

:::formel
U_ges = sqrt(U_R^2 + U_L^2)
:::

:::monospace
Beispiel: U = 230 V, f = 50 Hz, R = 100 Ohm, L = 0.3 H
X_L = 2 * pi * 50 * 0.3 = 94.2 Ohm
Z = sqrt(100^2 + 94.2^2) = 137 Ohm
I = 230 / 137 = 1.68 A
phi = arctan(94.2 / 100) = 43.3°
:::

## Umgekehrte Berechnung

Wenn nur ein Teil der Grössen bekannt ist, lassen sich die Formeln umstellen:

:::formel
U_L = sqrt(U_ges^2 - U_R^2)    # Blindspannung aus Gesamt- und Wirkspannung
X_L = sqrt(Z^2 - R^2)           # Reaktanz aus Impedanz und Wirkwiderstand
:::

**Reale Spule:** Eine reale Spule hat einen Wicklungswiderstand R_Cu (Drahtwiderstand). Sie verhält sich wie eine RL-Reihenschaltung. Typische Messung:

1. Gleichstrom anlegen → R_Cu = U_DC / I_DC
2. Wechselstrom anlegen → Z = U_AC / I_AC
3. X_L = √(Z² − R_Cu²), dann L = X_L / omega

:::monospace
Beispiel: R_Cu = 8 Ω (DC), Z = 3,14 kΩ (AC, f = 10 kHz)
X_L = sqrt(3140^2 - 8^2) ≈ 3140 Ω   (R_Cu ≪ Z → vernachlässigbar)
L = 3140 / (2*pi*10000) = 50 mH
:::

:::tip
Die RL-Reihenschaltung wirkt als **Hochpass** für die Spannung an der Spule (U_L steigt mit f) und als **Tiefpass** für die Spannung am Widerstand (U_R sinkt mit f). Die Grenzfrequenz liegt bei f = R / (2·pi·L), wo X_L = R gilt.
:::
