---
title: diff
kategorie: Funktionen
---

# `diff` — Ableiten

Bildet die Ableitung eines Ausdrucks nach einer oder mehreren Variablen.

## Grundform

```
diff(ausdruck, variable)
```

Beispiele:

```
⟦ diff(x^2, x) ⟧           ▶  2*x
⟦ diff(sin(x), x) ⟧        ▶  cos(x)
⟦ diff(exp(x^2), x) ⟧      ▶  2*x*exp(x^2)
⟦ diff(ln(x), x) ⟧         ▶  1/x
```

## Höhere Ableitungen

Eine Zahl nach der Variable gibt die Ordnung an:

```
⟦ diff(x^4, x, 2) ⟧   ▶  12*x^2
⟦ diff(x^4, x, 3) ⟧   ▶  24*x
```

Oder man wiederholt die Variable:

```
⟦ diff(x^4, x, x) ⟧   ▶  12*x^2
```

## Partielle Ableitungen

Einfach eine andere Variable angeben:

```
⟦ f := x^2 * y + y^3 ⟧
⟦ diff(f, x) ⟧   ▶  2*x*y
⟦ diff(f, y) ⟧   ▶  x^2 + 3*y^2
```

## Mit globalen Variablen

Alles, was mit `:=` gebunden ist, wird vor dem Ableiten eingesetzt:

```
⟦ f := x^2 + 3x - 1 ⟧
⟦ diff(f, x) ⟧          ▶  2*x + 3
⟦ diff(f, x).subs(x, 2) ⟧   ▶  7
```

## Extremstellen finden

Klassisches Muster: Ableitung nullsetzen und lösen (`=` funktioniert in `solve`):

```
⟦ f := x^3 - 3x ⟧
⟦ solve(diff(f, x) = 0, x) ⟧   ▶  [-1, 1]
```
