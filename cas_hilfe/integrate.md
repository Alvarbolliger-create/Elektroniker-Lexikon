---
title: integrate
kategorie: Funktionen
---

# `integrate` — Integrieren

Berechnet ein unbestimmtes oder bestimmtes Integral.

## Unbestimmt

```
integrate(ausdruck, variable)
```

Beispiele:

```
integrate(x^2, x)       ▶  x^3/3
integrate(sin(x), x)    ▶  -cos(x)
integrate(1/x, x)       ▶  log(x)
integrate(exp(x), x)    ▶  exp(x)
```

Hinweis: SymPy lässt die Integrationskonstante weg.

## Bestimmt

Grenzen werden als Tupel `(variable, unten, oben)` angegeben:

```
integrate(x^2, (x, 0, 1))        ▶  1/3
integrate(sin(x), (x, 0, π))     ▶  2
integrate(1/x^2, (x, 1, ∞))      ▶  1
```

Uneigentliche Integrale mit `∞` oder `-∞` als Grenze funktionieren direkt, solange sie konvergieren.

## Mehrfachintegrale

Zwei Tupel → Doppelintegral:

```
integrate(x*y, (x, 0, 1), (y, 0, 2))   ▶  1
```

## Wenn SymPy aufgibt

Nicht jedes Integral hat eine geschlossene Form. In so einem Fall gibt SymPy den Ausdruck unausgewertet zurück. Dann hilft oft ein numerisches Integral:

```
integrate(exp(-x^2), (x, 0, 1))           ▶  sqrt(π)*erf(1)/2
integrate(exp(-x^2), (x, 0, 1)).evalf()   ▶  0.746824…
```

Oder — für rein numerische Integrale — direkt `nsimplify` oder `.evalf()` draufwerfen.
