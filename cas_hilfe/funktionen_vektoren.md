---
title: Vektoren & Matrizen
kategorie: Funktionen
---

# Vektoren & Matrizen

Operationen auf Vektoren und Matrizen.

## Eingabe

Es gibt zwei gleichwertige Wege:

**Listen-Syntax** — direkt eingeben:

```
[1, 2, 3]            ▶  Spaltenvektor (3 Zeilen, 1 Spalte)
[[1, 2], [3, 4]]     ▶  2×2-Matrix
```

**Visueller Block** — Tastenkürzel `Alt+V` erzeugt einen Vektor-/Matrix-Block. Mit `Tab` in der letzten Zelle werden Zeilen, mit `Ctrl+Shift+Tab` Spalten ergänzt.

Beide Eingabeformen werden gleich behandelt: alle Funktionen unten akzeptieren beides.

## Skalar- und Kreuzprodukt

```
dotP([1, 2, 3], [4, 5, 6])      ▶  32
crossP([1, 0, 0], [0, 1, 0])    ▶  [0, 0, 1]
```

`crossP` ist nur für 3D-Vektoren definiert.

## Norm und Einheitsvektor

```
norm([3, 4])           ▶  5
norm([1, 2, 2])        ▶  3
unitV([3, 4])          ▶  [3/5, 4/5]
```

`norm(M)` berechnet bei Matrizen die Frobenius-Norm.

## Determinante, Spur, Rang

```
det([[1, 2], [3, 4]])         ▶  -2
trace([[1, 2], [3, 4]])       ▶  5
rank([[1, 2], [2, 4]])        ▶  1
rank([[1, 0], [0, 1]])        ▶  2
```

## Inverse und Transponierte

```
inv([[1, 2], [3, 4]])         ▶  [[-2, 1], [3/2, -1/2]]
transp([[1, 2], [3, 4]])      ▶  [[1, 3], [2, 4]]
```

`inv(M)` wirft einen Fehler, wenn `M` singulär ist (also `det(M) = 0`).

## Eigenwerte und Eigenvektoren

```
eigVl([[2, 0], [0, 3]])       ▶  [2, 3]
eigVc([[2, 0], [0, 3]])       ▶  [[1, 0], [0, 1]]
```

`eigVl(M)` gibt die Eigenwerte als Liste zurück (mit Vielfachheit).
`eigVc(M)` gibt eine Matrix zurück, deren Spalten die Eigenvektoren sind, in derselben Reihenfolge wie `eigVl`.

## Standardmatrizen

```
identity(3)         ▶  [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
zeroMat(2, 3)       ▶  [[0, 0, 0], [0, 0, 0]]
zeroMat(3)          ▶  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

Wenn `zeroMat` mit nur einem Argument aufgerufen wird, ist die Matrix quadratisch.

## Kombination mit anderen Funktionen

```
A := [[1, 2], [3, 4]]
det(A) * trace(A)              ▶  -10
inv(A) * A                     ▶  [[1, 0], [0, 1]]
sumL(eigVl(A))                 ▶  trace(A)
prodL(eigVl(A))                ▶  det(A)
```
