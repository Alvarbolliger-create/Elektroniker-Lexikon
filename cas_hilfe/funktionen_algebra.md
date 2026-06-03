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

## solve — Mehrere Variablen

`solve([eq1, eq2, ...], [x, y, ...])` löst ein Gleichungssystem mit mehreren Unbekannten symbolisch.

```
solve([x + y = 5, x - y = 1], [x, y])   ▶  [{x: 3, y: 2}]
solve([U = R*I, P = U*I], [I, P])        ▶  [{I: U/R, P: U²/R}]
```

Mit `Alt+G` lässt sich das Gleichungssystem `{...}` bequem im Editor einfügen; das `solve([...], [...])` tippt man dann drumherum.

## apart — Partialbruchzerlegung

`apart(f, x)` zerlegt einen rationalen Ausdruck in Partialbrüche.

```
apart(1/(x^2 - 1), x)       ▶  -1/(2·(x+1)) + 1/(2·(x-1))
apart((x+2)/(x*(x+1)), x)   ▶  2/x - 1/(x+1)
```

## together — Brüche zusammenfassen

`together(f)` fasst einen Ausdruck zu einem einzigen Bruch zusammen (Umkehrung von `apart`).

```
together(1/x + 1/(x+1))     ▶  (2·x+1) / (x·(x+1))
```

## cancel — Kürzen

`cancel(f)` kürzt gemeinsame Faktoren im Zähler und Nenner.

```
cancel((x^2 - 1)/(x - 1))   ▶  x + 1
```

## collect — Nach Variable sammeln

`collect(expr, x)` ordnet einen Ausdruck nach Potenzen von `x`.

```
collect(x^2 + 2*x*y + x*z + y, x)   ▶  x²  + x·(2·y+z) + y
```

## nsimplify — Näherung als Bruch

`nsimplify(x)` findet einen exakten symbolischen Ausdruck für einen Näherungswert.

```
nsimplify(0.5)       ▶  1/2
nsimplify(0.1)       ▶  1/10
nsimplify(3.14159)   ▶  pi  (näherungsweise)
```
