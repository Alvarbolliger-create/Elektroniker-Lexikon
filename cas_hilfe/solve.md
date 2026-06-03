---
title: solve
kategorie: Funktionen
---

# `solve` — Gleichungen lösen

Löst eine Gleichung (oder ein Gleichungssystem) algebraisch nach einer oder mehreren Variablen auf.

## Grundform

```
solve(gleichung, variable)
```

Dank des `=`-Operators kannst du Gleichungen direkt hinschreiben:

```
solve(x^2 = 4, x)       ▶  [-2, 2]
solve(2x + 3 = 7, x)    ▶  [2]
solve(x^2 - 9 = 0, x)   ▶  [-3, 3]
```

Falls nur ein Ausdruck dasteht, wird er implizit `= 0` gesetzt:

```
solve(x^2 - 9, x)       ▶  [-3, 3]
```

## Gleichungssysteme

Mehrere Gleichungen und mehrere Unbekannte kommen jeweils in eine Liste:

```
solve([x + y = 3, x - y = 1], [x, y])
                             ▶  {x: 2, y: 1}
solve([x^2 + y^2 = 25, x + y = 7], [x, y])
```

## Mit globalen Variablen

Mit `:=` fixierte Variablen werden vor der Auswertung eingesetzt. Die freien Symbole — also das, wonach aufgelöst wird — sollten nicht mit `:=` gebunden sein:

```
a := 2
b := 5
solve(a*x + b = 0, x)   ▶  [-5/2]
```

## Keine Lösung gefunden?

Wenn `solve` leer zurückgibt, ist das oft ein Hinweis darauf, dass die Gleichung nicht algebraisch lösbar ist. Für transzendente Gleichungen (z. B. mit `exp`, `log`, `sin` gemischt mit polynomialen Teilen) hilft manchmal:

- `solveset(eq, x)` — liefert Mengen statt Listen
- `nsolve(eq, x, start)` — numerische Lösung, braucht einen Startwert

```
nsolve(cos(x) = x, x, 1)   ▶  0.739085…
```

## Einschränkungen

`solve` versucht, **alle** Lösungen zu finden. Bei komplizierten Gleichungen kann das lange dauern oder unerwartete Komplexe zurückgeben. Falls du nur reelle Lösungen willst:

```
solve(x^2 = -1, x)                    ▶  [-I, I]
solveset(x^2 = -1, x, domain=S.Reals) ▶  EmptySet
```
