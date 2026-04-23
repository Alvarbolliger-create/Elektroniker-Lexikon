---
title: Funktionen — Übersicht
kategorie: Funktionen
---

# Funktionen — Übersicht

Der CAS Rechner stellt eine Sammlung von Funktionen im TI-NSpire-Stil zur Verfügung. Die folgenden Artikel beschreiben sie nach Kategorien gegliedert. Hier ein kompakter Index.

## Analysis

`deriv(f, x)`, `deriv(f, x, n)` — Ableitung
`integral(f, x)`, `integral(f, x, a, b)` — Integral
`taylor(f, x, a, n)` — Taylor-Reihe
`fMin(f, x)`, `fMax(f, x)` — lokale Extremstellen
`fMin(f, x, a, b)`, `fMax(f, x, a, b)` — Extremstellen auf Intervall
`limit(f, x, a)` — Grenzwert (SymPy-Funktion)

## Algebra & Gleichungen

`expand(expr)` — Ausmultiplizieren
`factor(expr)` — Faktorisieren
`simplify(expr)` — Vereinfachen
`solve(eq, x)` — Gleichungen symbolisch lösen
`nSolve(eq, x)`, `nSolve(eq, x, x0)` — Numerisch lösen (Newton)
`zeros(f, x)` — Nullstellen
`poly(coeffs, x)` — Polynom aus Koeffizientenliste

## Vektoren & Matrizen

`dotP(a, b)`, `crossP(a, b)` — Skalar- und Kreuzprodukt
`norm(v)`, `unitV(v)` — Länge und Einheitsvektor
`det(M)`, `trace(M)`, `rank(M)` — Determinante, Spur, Rang
`inv(M)`, `transp(M)` — Inverse, Transponierte
`eigVl(M)`, `eigVc(M)` — Eigenwerte und Eigenvektoren
`identity(n)`, `zeroMat(n, m)` — Standardmatrizen

## Statistik & Kombinatorik

`mean`, `median`, `variance`, `stdDev` — Lage- und Streuungsmaße
`sumL`, `prodL` — Summe und Produkt einer Liste
`nCr(n, r)`, `nPr(n, r)` — Binomialkoeffizient und Permutationen
`gcd(a, b)`, `lcm(a, b)`, `mod(a, b)` — Zahlentheorie

## Sonstige Helfer

`floor(x)`, `ceil(x)`, `round(x, n)` — Runden
`sign(x)` — Vorzeichen
`re(z)`, `im(z)`, `conj(z)`, `arg(z)` — Komplexe Zahlen

## Wichtige Hinweise

- Listen wie `[1, 2, 3]` werden in Vektor-Funktionen automatisch als Spaltenvektor interpretiert.
- Verschachtelte Listen wie `[[1, 2], [3, 4]]` werden als Matrix interpretiert.
- Alternativ kann mit `Alt+V` ein Vektor-/Matrix-Block direkt im Editor erzeugt werden.
- Trigonometrische Funktionen respektieren den eingestellten Winkelmodus (RAD/DEG).
