---
title: Impedanz
kategorie: ET
tags: [impedanz, scheinwiderstand, reaktanz, blindwiderstand, wirkwiderstand, komplex, phasenwinkel]
groessen: Z|Impedanz|Ohm; R|Wirkwiderstand|Ohm; X|Reaktanz|Ohm; phi|Phasenwinkel|°; omega|Kreisfrequenz|rad/s
_status: PORT  # ET_alt/Wechselstrom/Impedanz.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen & Effektivwert]]
- [[Kondensator im Wechselstrom]]
- [[Spule im Wechselstrom]]
:::
:::vbox
**Verwandte Artikel**
- [[Zeigerdiagramm]]
:::
:::vbox
**Führt weiter zu**
- [[RL-Reihenschaltung]]
- [[RC-Reihenschaltung]]
:::
:::

---

Impedanz ist der Wechselstromwiderstand — er vereint den ohmschen Wirkwiderstand R und die frequenzabhängige Reaktanz X in einer einzigen Grösse. Im Gegensatz zu R hängt die Impedanz von der Frequenz ab und bewirkt eine Phasenverschiebung zwischen Strom und Spannung.

## Komponenten der Impedanz

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Wirkwiderstand | R | Ω | Ohmscher Anteil, wandelt Energie in Wärme um |
| Reaktanz (Blindwiderstand) | X | Ω | Frequenzabhängiger Anteil, speichert und gibt Energie zurück |
| Impedanz (Scheinwiderstand) | Z | Ω | Kombination aus R und X |

**Reaktanz der Bauteile:**

:::formel
X_C = 1 / (omega * C)    # kapazitive Reaktanz, sinkt mit Frequenz
:::

:::formel
X_L = omega * L    # induktive Reaktanz, steigt mit Frequenz
:::

## Betrag und Phase

:::schematic Impedanzdreieck: Rechtwinkliges Dreieck; Horizontale Kathete = R (Wirkwiderstand); Vertikale Kathete = X (Reaktanz, positiv nach oben für induktiv, negativ nach unten für kapazitiv); Hypotenuse = Z (Impedanz); Winkel phi zwischen Z und R eingezeichnet; Beschriftung: R, X, Z, phi
/abbildungen/wechselstrom/impedanzdreieck.svg
:::

Die Impedanz lässt sich als rechtwinkliges Dreieck darstellen: R horizontal, X vertikal, Z als Hypotenuse (→ [[Zeigerdiagramm]]).

:::formel
Z = sqrt(R^2 + X^2)    # Betrag der Impedanz
:::

:::formel
phi = arctan(X / R)    # Phasenwinkel zwischen U und I
:::

| phi | Bedeutung |
|---|---|
| phi = 0° | Rein ohmsch — Strom und Spannung in Phase |
| phi > 0° (induktiv) | Spannung eilt Strom vor (L dominiert) |
| phi < 0° (kapazitiv) | Strom eilt Spannung vor (C dominiert) |

**Merkregel:** *ELI the ICE man* — bei induktivem Verhalten (L) eilt die Spannung (E) dem Strom (I) vor; bei kapazitivem Verhalten (C) eilt der Strom (I) der Spannung (E) vor.

## Komplexe Darstellung

Für Schaltungsanalyse wird die Impedanz als komplexe Zahl geschrieben: Realteil R, Imaginärteil X. Die komplexe Schreibweise erlaubt, Reihen- und Parallelschaltungen mit normaler Algebra zu berechnen.

| Bauteil | Impedanz (komplex) |
|---|---|
| Widerstand R | Z = R |
| Kondensator C | Z = -j / (omega * C) |
| Spule L | Z = j * omega * L |

Das j (imaginäre Einheit) codiert die Phasenverschiebung: j·X bedeutet 90° Voreilung, −j·X bedeutet 90° Nacheilung gegenüber R.

## Reihen- und Parallelschaltung

Reihenschaltung: Impedanzen addieren sich (wie Widerstände).

:::formel
Z_ges = Z1 + Z2
:::

Parallelschaltung: Kehrwerte addieren sich (wie Leitwerte).

:::formel
Z_ges = Z1 * Z2 / (Z1 + Z2)    # für zwei Glieder
:::

Bei komplexen Zahlen in der Parallelschaltung sind Real- und Imaginärteil getrennt zu behandeln — das CAS übernimmt diese Rechnung.

:::tip
Für EFZ-Prüfungen: Den **Betrag Z** mit Pythagoras berechnen, den **Phasenwinkel phi** mit arctan(X/R). Komplexe Algebra ist nützlich, aber nicht immer nötig.
:::
