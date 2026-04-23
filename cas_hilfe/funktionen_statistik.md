---
title: Statistik & Kombinatorik
kategorie: Funktionen
---

# Statistik & Kombinatorik

Auswertung von Listen, Wahrscheinlichkeiten, Zahlentheorie.

## Lagemaße

`mean(list)` — Arithmetisches Mittel
`median(list)` — Median (mittlerer Wert oder Mittelwert der beiden mittleren)

```
mean([1, 2, 3, 4])        ▶  5/2
mean([10, 20, 30])        ▶  20
median([1, 2, 3, 4, 5])   ▶  3
median([1, 2, 3, 4])      ▶  5/2
```

## Streuungsmaße

`variance(list)` — **Stichproben**-Varianz (Nenner `n-1`)
`stdDev(list)` — Standardabweichung = Wurzel der Varianz

```
variance([1, 2, 3, 4])    ▶  5/3
stdDev([1, 2, 3, 4])      ▶  sqrt(15)/3
stdDev([5, 5, 5, 5])      ▶  0
```

Hinweis: Wer die **Populations**-Varianz braucht (Nenner `n`), kann sie aus der Stichprobenvarianz mit `variance(L) * (n-1)/n` umrechnen.

## Listen-Aggregation

`sumL(list)` — Summe aller Listenelemente
`prodL(list)` — Produkt aller Listenelemente

```
sumL([1, 2, 3, 4])        ▶  10
sumL([1, 2, 3, 4, 5])     ▶  15
prodL([1, 2, 3, 4])       ▶  24
prodL([2, 3, 5])          ▶  30
```

Die Namen sind so gewählt, weil `sum` und `prod` mit Pythons Built-ins kollidieren würden. Wer sich an TI-NSpire-Konventionen orientiert, findet sie damit schnell.

## Kombinatorik

`nCr(n, r)` — Binomialkoeffizient (`n` über `r`)
`nPr(n, r)` — Permutationen (`n!/(n-r)!`)

```
nCr(5, 2)        ▶  10
nCr(10, 3)       ▶  120
nPr(5, 2)        ▶  20
nPr(10, 3)       ▶  720
```

## Zahlentheorie

`gcd(a, b)` — Größter gemeinsamer Teiler (SymPy-Standard)
`lcm(a, b)` — Kleinstes gemeinsames Vielfaches (SymPy-Standard)
`mod(a, b)` — Modulo `a mod b`

```
gcd(12, 18)      ▶  6
lcm(4, 6)        ▶  12
mod(17, 5)       ▶  2
mod(-7, 3)       ▶  2
```

## Beispiel: Klassische Aufgaben

```
L := [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
mean(L)              ▶  26/5
median(L)            ▶  9/2
stdDev(L)            ▶  sqrt(...)
sumL(L) / 10         ▶  mean(L)
```
