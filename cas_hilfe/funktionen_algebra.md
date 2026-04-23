---
title: Algebra & Gleichungen
kategorie: Funktionen
---

# Algebra & Gleichungen

Termumformungen, Vereinfachung und Lösen von Gleichungen.

## expand — Ausmultiplizieren

```
expand((x+1)^3)        ▶  x³ + 3·x² + 3·x + 1
expand((a+b)*(a-b))    ▶  a² - b²
expand(sin(x+y))       ▶  sin(x)·cos(y) + cos(x)·sin(y)
```

## factor — Faktorisieren

Umkehrung von `expand`.

```
factor(x^2 - 4)        ▶  (x - 2)·(x + 2)
factor(x^3 - 1)        ▶  (x - 1)·(x² + x + 1)
factor(x^2 + 2*x + 1)  ▶  (x + 1)²
```

## simplify — Vereinfachen

Allgemeiner Vereinfacher. Versucht eine einfachere Form zu finden.

```
simplify(sin(x)^2 + cos(x)^2)   ▶  1
simplify((x^2-1)/(x-1))         ▶  x + 1
simplify(log(exp(x)))           ▶  x
```

## solve — Symbolisch lösen

`solve(eq, x)` löst eine Gleichung exakt nach `x`. Statt `=` schreibt man `=` (wird automatisch zu `Eq` konvertiert).

```
solve(x^2 = 4, x)            ▶  [-2, 2]
solve(x^2 + 2*x + 1 = 0, x)  ▶  [-1]
solve(sin(x) = 0, x)         ▶  [0, pi]
```

## nSolve — Numerisch lösen

`nSolve(eq, x)` oder `nSolve(eq, x, x0)` findet eine numerische Lösung mit Newton-Iteration. Der dritte Parameter ist der Startwert (Standard: 0).

Wichtig bei nicht-trivialen Gleichungen: gib einen guten Startwert vor, sonst kann das Verfahren divergieren.

```
nSolve(x^3 - 2*x - 5 = 0, x)         ▶  2.0945514815...
nSolve(cos(x) = x, x, 1)             ▶  0.7390851332...
nSolve(exp(-x) = x, x, 0.5)          ▶  0.5671432904...
```

## zeros — Nullstellen

`zeros(f, x)` ist Kurzschreibweise für `solve(f = 0, x)`.

```
zeros(x^2 - 4, x)        ▶  [-2, 2]
zeros(x^3 - x, x)        ▶  [-1, 0, 1]
zeros(sin(x), x)         ▶  [0, pi]
```

## poly — Polynom aus Koeffizienten

`poly(coeffs, x)` baut aus einer Liste von Koeffizienten (höchste Potenz zuerst) ein Polynom in `x`.

```
poly([1, 0, -4], x)         ▶  x² - 4
poly([1, -3, 3, -1], x)     ▶  x³ - 3·x² + 3·x - 1
poly([2, 5, -3], x)         ▶  2·x² + 5·x - 3
```
