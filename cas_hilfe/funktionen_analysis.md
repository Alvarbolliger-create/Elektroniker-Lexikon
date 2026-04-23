---
title: Analysis (Differential & Integral)
kategorie: Funktionen
---

# Analysis

Differential- und Integralrechnung, Reihen, Extremwertbestimmung.

## deriv — Ableitung

`deriv(f, x)` bildet die erste Ableitung von `f` nach `x`. Mit drittem Argument `n` die n-te Ableitung.

```
deriv(x^2, x)         ▶  2·x
deriv(sin(x), x)      ▶  cos(x)
deriv(x^4, x, 2)      ▶  12·x²
deriv(exp(x*y), x)    ▶  y·exp(x·y)
```

## integral — Integral

`integral(f, x)` ist das unbestimmte Integral. Mit den zusätzlichen Argumenten `a, b` wird es zum bestimmten Integral von `a` bis `b`.

Hinweis: Es gibt auch den 2D-Integral-Block (`Alt+I`), der dieselbe Funktion grafisch repräsentiert.

```
integral(2*x, x)            ▶  x²
integral(x^2, x, 0, 1)      ▶  1/3
integral(1/x, x, 1, e)      ▶  1
integral(sin(x), x, 0, pi)  ▶  2
```

## taylor — Taylor-Reihe

`taylor(f, x, a, n)` gibt die Taylor-Reihe von `f` um `x = a` bis Grad `n` als Polynom zurück (ohne Restterm).

```
taylor(exp(x), x, 0, 4)   ▶  1 + x + x²/2 + x³/6 + x⁴/24
taylor(sin(x), x, 0, 5)   ▶  x - x³/6 + x⁵/120
taylor(1/(1-x), x, 0, 4)  ▶  1 + x + x² + x³ + x⁴
```

## fMin und fMax — Extremstellen

Geben den **x-Wert** einer Extremstelle der Funktion `f(x)` zurück.

`fMin(f, x)` und `fMax(f, x)` suchen lokale Extrema über die Bedingung `f'(x) = 0` und das Vorzeichen der zweiten Ableitung.

`fMin(f, x, a, b)` und `fMax(f, x, a, b)` suchen das **globale** Extremum auf dem Intervall `[a, b]` (Vergleich der kritischen Punkte und der Randwerte).

```
fMin(x^2 - 4*x, x)         ▶  2
fMax(-x^2 + 4*x, x)        ▶  2
fMin(x^2, x, -3, 5)        ▶  0
fMax(sin(x), x, 0, pi)     ▶  pi/2
```

Wenn keine reelle Extremstelle existiert, wird `nan` zurückgegeben.

## limit — Grenzwert (SymPy)

`limit(f, x, a)` ist die SymPy-Standardfunktion und steht ohne Wrapper zur Verfügung.

```
limit(sin(x)/x, x, 0)      ▶  1
limit((1+1/x)^x, x, oo)    ▶  E
limit(1/x, x, 0)           ▶  oo
```
