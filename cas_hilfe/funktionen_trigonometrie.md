---
title: Trigonometrie & Exponential
kategorie: Funktionen
---

# Trigonometrie & Exponential

Alle trigonometrischen, hyperbolischen und Exponentialfunktionen aus dem SymPy-Paket stehen direkt zur Verfügung. Der Winkelmodus (RAD/DEG) gilt für alle Winkelfunktionen.

## Trigonometrische Funktionen

| Funktion | Bedeutung |
|---|---|
| `sin(x)` | Sinus |
| `cos(x)` | Kosinus |
| `tan(x)` | Tangens |
| `cot(x)` | Kotangens |
| `sec(x)` | Sekans (1/cos) |
| `csc(x)` | Kosekans (1/sin) |

```
sin(30)     ▶  1/2          (DEG-Modus)
cos(pi/3)   ▶  1/2          (RAD-Modus)
tan(45)     ▶  1            (DEG-Modus)
```

## Inverse Trigonometrie (Arkusfunktionen)

| Funktion | Bedeutung | Ausgabe |
|---|---|---|
| `asin(x)` | Arkussinus | Winkel |
| `acos(x)` | Arkuskosinus | Winkel |
| `atan(x)` | Arkustangens | Winkel |
| `atan2(y, x)` | Arkustangens (2 Argumente) | Winkel im richtigen Quadrant |
| `acot(x)` | Arkuskotangens | Winkel |
| `asec(x)` | Arkussekans | Winkel |
| `acsc(x)` | Arkuskosekans | Winkel |

```
asin(1)         ▶  90       (DEG-Modus)
acos(1/2)       ▶  60       (DEG-Modus)
atan(1)         ▶  45       (DEG-Modus)
atan2(1, 1)     ▶  45       (DEG-Modus, entspricht atan(y/x) mit Quadranteninfo)
asin(1)         ▶  pi/2     (RAD-Modus)
```

> **Hinweis:** `arcsin`, `arccos`, `arctan` gibt es **nicht** — es muss `asin`, `acos`, `atan` heißen.

## Hyperbolische Funktionen

| Funktion | Bedeutung |
|---|---|
| `sinh(x)` | Sinus Hyperbolicus |
| `cosh(x)` | Kosinus Hyperbolicus |
| `tanh(x)` | Tangens Hyperbolicus |
| `coth(x)` | Kotangens Hyperbolicus |
| `sech(x)` | Sekans Hyperbolicus |
| `csch(x)` | Kosekans Hyperbolicus |

```
sinh(0)     ▶  0
cosh(0)     ▶  1
tanh(oo)    ▶  1
```

## Inverse Hyperbolische Funktionen

| Funktion | Bedeutung |
|---|---|
| `asinh(x)` | Areasinus Hyperbolicus |
| `acosh(x)` | Areakosinus Hyperbolicus |
| `atanh(x)` | Areatangens Hyperbolicus |

```
asinh(0)    ▶  0
acosh(1)    ▶  0
atanh(0)    ▶  0
```

## Exponential & Logarithmus

| Funktion | Bedeutung |
|---|---|
| `exp(x)` | e^x |
| `log(x)` | Natürlicher Logarithmus ln(x) |
| `log(x, b)` | Logarithmus zur Basis b |
| `log10(x)` | Dekadischer Logarithmus (Basis 10) |
| `sqrt(x)` | Quadratwurzel |
| `cbrt(x)` | Kubikwurzel (3. Wurzel) |
| `root(x, n)` | n-te Wurzel |

```
exp(1)              ▶  E         (Euler-Zahl)
log(E)              ▶  1
log(100, 10)        ▶  2
log10(1000)         ▶  3
sqrt(2)             ▶  √2
cbrt(8)             ▶  2
root(32, 5)         ▶  2
```

> **Achtung:** `log(x)` ist der **natürliche** Logarithmus (ln), nicht der dekadische! Für Basis 10 → `log10(x)`.

## Weitere Wurzel- und Potenzen

| Funktion | Bedeutung |
|---|---|
| `sqrt(x)` | √x (identisch mit `x^(1/2)`) |
| `x^(1/n)` | n-te Wurzel als Potenz |
| `Abs(x)` | Betrag (auch `abs(x)`) |

```
Abs(-5)             ▶  5
Abs(3 + 4*j)        ▶  5
sqrt(9)             ▶  3
8^(1/3)             ▶  2
```
