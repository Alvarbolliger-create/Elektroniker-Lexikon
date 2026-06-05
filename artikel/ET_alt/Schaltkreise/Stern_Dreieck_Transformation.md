---
title: Stern-Dreieck-Transformation
kategorie: ET
tags: [Stern-Dreieck, Y-Delta, Transformation, Widerstandsnetzwerk, Brückenschaltung]
symbol: —
einheit: Ω
---

Die Stern-Dreieck-Transformation ersetzt ein Dreieck-Netzwerk durch ein äquivalentes Stern-Netzwerk (oder umgekehrt). Damit lassen sich Brückenschaltungen in einfache Reihen- und Parallelschaltungen auflösen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
- [[Kirchhoffsche Gesetze]]
:::
:::vbox
**Verwandte Artikel**
- [[Wheatstone-Brücke]]
- [[Leistungsanpassung]]
:::
:::vbox
**Führt weiter zu**
- [[Drehstrom Grundlagen]]
- [[Knotenpotenzialanalyse]]
:::
:::

---

## Wann wird die Transformation gebraucht?

In manchen Netzwerken sind Widerstände so verschalten, dass sie weder in Reihe noch parallel liegen — z.B. in einer Wheatstone-Brücke oder komplexen Maschennetzen. Die Stern-Dreieck-Transformation macht diese Schaltungen berechenbar.

## Das Dreieck (Δ): Drei Knoten, drei Widerstände aussen

:::formel
    A
   / \
 R12  R13
 /     \
B--R23--C
:::
Drei Widerstände R12, R23, R13 verbinden die drei Knoten A, B, C im Dreieck.

## Der Stern (Y): Drei Knoten, ein Mittelpunkt

:::formel
    A
    |
   Ra
    |
B--Rb--M--Rc--C
:::
Drei Widerstände Ra, Rb, Rc verbinden jeden der drei Knoten A, B, C mit einem Mittelpunkt M.

## Dreieck → Stern (Δ → Y)

:::formel
Ra = (R12 * R13) / (R12 + R23 + R13)
Rb = (R12 * R23) / (R12 + R23 + R13)
Rc = (R13 * R23) / (R12 + R23 + R13)
:::
**Merkhilfe**: Ra hängt an Knoten A. Im Zähler stehen die beiden Dreieckswiderstände, die an A angeschlossen sind (R12 und R13). Im Nenner stehen alle drei.

## Stern → Dreieck (Y → Δ)

:::formel
R12 = (Ra*Rb + Rb*Rc + Ra*Rc) / Rc
R23 = (Ra*Rb + Rb*Rc + Ra*Rc) / Ra
R13 = (Ra*Rb + Rb*Rc + Ra*Rc) / Rb
:::
**Merkhilfe**: Im Zähler steht immer die Summe aller Stern-Produkte. Im Nenner steht der Stern-Widerstand am gegenüberliegenden Knoten.

## Sonderfall: Alle Widerstände gleich

Wenn alle Dreieckswiderstände gleich sind (R12 = R23 = R13 = R_Δ):

:::formel
R_Y = R_Δ / 3    # Sternwiderstand = Dreieckswiderstand / 3
:::
Und umgekehrt:
:::formel
R_Δ = 3 × R_Y
:::
Das gilt auch für die Drehstrom-Stern/Dreieck-Schaltung bei Motoren.

## Anwendungsbeispiel: Unabgeglichene Wheatstone-Brücke

Eine Wheatstone-Brücke mit R1, R2, R3, R4 und Brückenwiderstand R5 lässt sich nicht direkt vereinfachen. Mit der Stern-Dreieck-Transformation wird z.B. das obere Dreieck (R1, R2, R5) in einen Stern umgewandelt. Danach liegen alle Widerstände in einfachen Reihen-/Parallelkombinationen.

:::info
Die Transformation gilt für Gleichstrom und Wechselstrom (dann mit komplexen Impedanzen Z statt Widerständen R). Die Formeln sind identisch.
:::
