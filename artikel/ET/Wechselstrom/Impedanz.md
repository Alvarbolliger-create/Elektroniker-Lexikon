---
title: Impedanz
kategorie: ET
tags: [impedanz, wechselstrom, widerstand, reaktanz, phasenwinkel, admittanz, scheinwiderstand, komplexe zahl, j-operator, blindwiderstand, wirkleitwert, blindleitwert]
symbol: Z
einheit: Ω
---

Impedanz ist der Gesamtwiderstand im Wechselstromkreis. Sie fasst den ohmschen Widerstand und die frequenzabhängigen Anteile von Kondensator und Spule zusammen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Kondensator im Wechselstrom]]
- [[Spule im Wechselstrom]]
:::
:::vbox
**Verwandte Artikel**
- [[Zeigerdiagramm]]
:::
:::vbox
**Führt weiter zu**
- [[RLC-Schaltungen]]
- [[Filter Grundlagen]]
:::
:::

---

## Zusammensetzung

Impedanz besteht aus zwei Teilen: dem Wirkwiderstand R (ohmsch, frequenzunabhängig) und der Reaktanz X (frequenzabhängig).

```
Z = sqrt(R^2 + X^2)     # Betrag der Impedanz; X = X_L - X_C
X_L = 2 * pi * f * L    # Induktiver Anteil
X_C = 1 / (2 * pi * f * C)  # Kapazitiver Anteil
```

| Grösse | Symbol | Einheit |
|---|---|---|
| Impedanz | Z | Ω |
| Wirkwiderstand | R | Ω |
| Reaktanz | X | Ω |
| Phasenwinkel | phi | ° |

## Phasenwinkel

```
phi = arctan(X / R)
```

phi gibt an, wie stark Strom und Spannung zeitlich versetzt sind. Bei phi = 0° ist die Last rein ohmsch. Bei phi = 90° rein reaktiv.

## Ohmsches Gesetz für Wechselstrom

```
U = Z * I
```

Dieselbe Form wie beim Ohmschen Gesetz, aber Z ist komplex und frequenzabhängig.

:::tip
Bei niedrigen Frequenzen dominiert der kapazitive Anteil (X_C gross). Bei hohen Frequenzen dominiert der induktive Anteil (X_L gross). Dazwischen liegt die Resonanzfrequenz wo X_L = X_C.
:::

## Komplexe Darstellung

Der Betrag allein reicht für Phasenberechnungen nicht aus. Die vollständige komplexe Schreibweise:

```
Z   = R + j*X              # komplexe Impedanz (R = Realteil, X = Imaginärteil)
|Z| = sqrt(R^2 + X^2)      # Betrag (wie oben)
φ   = arctan(X / R)        # Phasenwinkel

Z_R = R                    # ohmscher Widerstand (rein reell)
Z_L = j * ω * L            # Spule (rein imaginär, positiv)
Z_C = 1 / (j * ω * C)      # Kondensator (rein imaginär, negativ)
```

In Reihenschaltung addieren sich Impedanzen direkt: `Z_ges = Z1 + Z2 + Z3`

In Parallelschaltung gilt: `1/Z_ges = 1/Z1 + 1/Z2` — oder einfacher über die Admittanz Y = 1/Z, die sich wie Leitwerte addieren lässt.

## Parallelschaltung: Admittanz

Für Parallelschaltungen ist der Leitwertansatz einfacher. Statt Impedanzen zu kombinieren, addiert man Leitwerte direkt:

```
Y   = 1 / Z              # Admittanz (Scheinleitwert) in S (Siemens)
G   = 1 / R              # Wirkleitwert
B_L = 1 / X_L            # Induktiver Blindleitwert
B_C = 1 / X_C            # Kapazitiver Blindleitwert

Y = sqrt(G^2 + B^2)      # Betrag der Admittanz
I = U * Y                # Ohmsches Gesetz mit Admittanz
```

Die Ströme im Parallelkreis:
```
I_R = U / R              # Strom durch Widerstand
I_L = U / X_L            # Strom durch Spule
I_C = U / X_C            # Strom durch Kondensator
I   = sqrt(I_R^2 + I_L^2)   # RL-Parallel
I   = sqrt(I_R^2 + I_C^2)   # RC-Parallel
```

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Admittanz | Y | S | Kehrwert der Impedanz |
| Wirkleitwert | G | S | G = 1/R |
| Induktiver Blindleitwert | B_L | S | B_L = 1/X_L |
| Kapazitiver Blindleitwert | B_C | S | B_C = 1/X_C |
