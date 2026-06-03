---
title: Funktionen — Übersicht
kategorie: Funktionen
---

# Funktionen — Übersicht

Der CAS Rechner stellt eine Sammlung von Funktionen im TI-NSpire-Stil zur Verfügung. Die folgenden Artikel beschreiben sie nach Kategorien gegliedert. Hier ein kompakter Index.

## Trigonometrie & Exponential

**Vorwärts:** `sin`, `cos`, `tan`, `cot`, `sec`, `csc`
**Arkus (Umkehr):** `asin`, `acos`, `atan`, `atan2`, `acot`, `asec`, `acsc`
**Hyperbolisch:** `sinh`, `cosh`, `tanh`, `coth` — Umkehr: `asinh`, `acosh`, `atanh`
**Exponential/Log:** `exp(x)`, `log(x)` (= ln), `log(x, b)`, `log10(x)`
**Wurzeln:** `sqrt(x)`, `cbrt(x)`, `root(x, n)`

> `arcsin` gibt es **nicht** — es heißt `asin`. `log(x)` ist der natürliche Logarithmus.

## Analysis

`deriv(f, x)`, `deriv(f, x, n)` — Ableitung (n-te)
`integral(f, x)`, `integral(f, x, a, b)` — Unbestimmtes / bestimmtes Integral
`taylor(f, x, a, n)` — Taylor-Reihe um Punkt `a` der Ordnung `n`
`fMin(f, x)`, `fMax(f, x)` — lokale Extremstellen
`fMin(f, x, a, b)`, `fMax(f, x, a, b)` — Extremstellen auf Intervall [a, b]
`limit(f, x, a)` — Grenzwert für x → a

## Algebra & Gleichungen

`expand(expr)` — Ausmultiplizieren
`factor(expr)` — Faktorisieren
`simplify(expr)` — Vereinfachen
`apart(f, x)` — Partialbruchzerlegung
`together(f)` — Brüche zusammenfassen
`cancel(f)` — Zähler/Nenner kürzen
`collect(expr, x)` — Nach Potenzen von x sammeln
`nsimplify(x)` — Näherungswert als exakten Ausdruck

**Eine Variable:**
`solve(eq, x)` — Gleichung symbolisch nach x lösen
`zeros(f, x)` — Nullstellen von f
`nSolve(eq, x)`, `nSolve(eq, x, x0)` — Numerisch lösen (Newton, Startwert x0)

**Mehrere Variablen:**
`solve([eq1, eq2], [x, y])` — Gleichungssystem symbolisch lösen

`poly(coeffs, x)` — Polynom aus Koeffizientenliste, z. B. `poly([1,0,-4], x)` → x²-4

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

## Komplexe Zahlen & Phasoren

`j` — imaginäre Einheit (j = √−1)
`re(z)`, `im(z)` — Real- und Imaginärteil
`conj(z)` — Konjugiert-Komplexe
`arg(z)` — Argument (Phase in Radiant)
`abs(z)` — Betrag

`phasor(r, theta)` — Zeiger in Euler-Form: r · e^(j·θ·π/180)
```
Z := phasor(10, 45)     ▶  10·e^(jπ/4)
```

## Mathematische Konstanten

| Name | Bedeutung | Wert |
|---|---|---|
| `pi` | Kreiszahl π | 3.14159… |
| `e` | Euler-Zahl | 2.71828… |
| `phi` | Goldener Schnitt | 1.61803… |
| `j` | Imaginäre Einheit | √−1 |

## Physikalische Konstanten (mit Einheiten)

| Name | Bedeutung | Wert |
|---|---|---|
| `c` | Lichtgeschwindigkeit | 299 792 458 m/s |
| `g_n` | Erdbeschleunigung | 9.80665 m/s² |
| `hP` | Planck-Konstante | 6.626 × 10⁻³⁴ J·s |
| `hbar` | Reduzierte Planck-Konstante | 1.055 × 10⁻³⁴ J·s |
| `kB` | Boltzmann-Konstante | 1.381 × 10⁻²³ J/K |
| `NA` | Avogadro-Konstante | 6.022 × 10²³ /mol |
| `qe` | Elementarladung | 1.602 × 10⁻¹⁹ C |
| `eps0` | Elektrische Feldkonstante ε₀ | 8.854 × 10⁻¹² F/m |
| `mu0` | Magnetische Feldkonstante μ₀ | 1.257 × 10⁻⁶ N/A² |
| `Rgas` | Universelle Gaskonstante | 8.314 J/(mol·K) |
| `sigmaSB` | Stefan-Boltzmann-Konstante | 5.670 × 10⁻⁸ W/(m²·K⁴) |
| `me` | Elektronenmasse | 9.109 × 10⁻³¹ kg |
| `mp` | Protonenmasse | 1.673 × 10⁻²⁷ kg |

```
E := hP * 600E-9_m * c     # Photonenenergie bei λ = 600 nm
aprox(E)                    ▶  3.31 × 10⁻¹⁹ J
```

## Sonstige Helfer

`floor(x)`, `ceil(x)`, `round(x, n)` — Runden
`sign(x)` — Vorzeichen (−1, 0 oder 1)
`abs(x)` — Betrag / Absolutwert
`re(z)`, `im(z)`, `conj(z)`, `arg(z)` — Komplexe Zahlen

## Wichtige Hinweise

- Listen wie `[1, 2, 3]` werden in Vektor-Funktionen automatisch als Spaltenvektor interpretiert.
- Verschachtelte Listen wie `[[1, 2], [3, 4]]` werden als Matrix interpretiert.
- Alternativ kann mit `Alt+V` ein Vektor-/Matrix-Block direkt im Editor erzeugt werden.
- Trigonometrische Funktionen respektieren den eingestellten Winkelmodus (RAD/DEG).
- **Alle SymPy-Funktionen sind direkt verfügbar** — der gesamte SymPy-Namespace ist eingebunden. Nützliche Beispiele: `linsolve`, `diophantine`, `residue`, `series`, `fourier_series`, `laplace_transform`, `inverse_laplace_transform`, `binomial`, `factorial`, `fibonacci`, `prime`, `isprime`, …
- Eine vollständige Liste aller SymPy-Funktionen: [docs.sympy.org](https://docs.sympy.org)
