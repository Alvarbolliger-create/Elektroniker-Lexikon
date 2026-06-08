---
title: RL-Parallelschaltung
kategorie: ET
tags: [RL, parallelschaltung, leitwert, blindleitwert, wirkleitwert, scheinleitwert, wechselstrom]
groessen: Y|Scheinleitwert|S; G|Wirkleitwert|S; B_L|induktiver Blindleitwert|S; phi|Phasenwinkel|°; I|Strom|A; U|Spannung|V; Z|Impedanz|Ohm
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[RL-Reihenschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[RC-Parallelschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[RLC-Parallelschaltung (Parallelschwingkreis)]]
:::
:::

---

Bei der RL-Parallelschaltung teilt sich der Gesamtstrom in den Wirkstrom (durch R) und den Blindstrom (durch L) auf. Die gemeinsame Spannung ist die Referenzgrösse — alle Ströme werden dazu in Beziehung gesetzt.

:::schematic RL-Parallelschaltung
/schaltplaene/Filter/rl_parallel.svg
:::

## Spannung und Teilströme

An beiden Zweigen liegt dieselbe Spannung U. Die Teilströme sind:

:::hbox
:::formel
I_R = U / R    # in Phase mit U
:::

:::formel
I_L = U / X_L    # 90° hinter U (Strom eilt Spannung nach)
:::
:::

## Gesamtstrom

I_R und I_L sind 90° phasenverschoben — sie addieren sich vektoriell:

:::formel
I_ges = sqrt(I_R^2 + I_L^2)
:::

## Scheinleitwert Y

Für Parallelschaltungen arbeitet man mit **Leitwerten** (Y = 1/Z, G = 1/R, B = 1/X):

:::hbox
:::formel
Y = sqrt(G^2 + B_L^2)
:::

:::formel
G = 1 / R
:::

:::formel
B_L = 1 / X_L
:::
:::

Das Leitwert-Dreieck: G horizontal, B_L vertikal, Y als Hypotenuse.

## Phasenverschiebung

Der Gesamtstrom I_ges eilt der Spannung um phi nach:

:::formel
phi = arctan(-B_L / G)    # negativ: Strom nacheilend (induktiv)
:::

## Impedanz der Parallelschaltung

Die Gesamtimpedanz ergibt sich aus dem Kehrwert des Scheinleitwerts:

:::formel
Z_ges = 1 / Y
:::

Alternativ direkt:

:::formel
Z_ges = R * X_L / sqrt(R^2 + X_L^2)
:::

:::monospace
Beispiel: U = 230 V, f = 50 Hz, R = 500 Ohm, L = 1 H
X_L = 2*pi*50*1 = 314 Ohm
I_R = 230 / 500 = 0.46 A
I_L = 230 / 314 = 0.73 A
I_ges = sqrt(0.46^2 + 0.73^2) = 0.86 A
phi = arctan(-0.73/0.46) = -57.7°  (induktiv)
:::

## Umgekehrte Berechnung

Wenn Gesamtstrom und Wirkstrom bekannt sind, lässt sich der Blindstrom berechnen:

:::formel
I_L = sqrt(I_ges^2 - I_R^2)
X_L = U / I_L
L   = X_L / omega
:::

Ebenso für den Leitwert: Wenn Y und B_L bekannt, ergibt sich G = √(Y² − B_L²), R = 1/G.

:::tip
RL-Parallelschaltungen treten häufig als Modell für Motoren und Transformatoren auf: Der Wirkwiderstand R repräsentiert die Nutzleistung, die Induktivität L die magnetische Feldenergie. Der Phasenwinkel zeigt direkt den Leistungsfaktor cos phi.
:::
