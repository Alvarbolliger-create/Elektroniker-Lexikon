---
title: Sonstige Helfer
kategorie: Funktionen
---

# Sonstige Helfer

Runden, Vorzeichen, komplexe Zahlen.

## Runden

`floor(x)` — Abrunden auf die nächste ganze Zahl
`ceil(x)` — Aufrunden auf die nächste ganze Zahl
`round(x, n)` — Auf `n` Nachkommastellen runden (kaufmännisch)

```
floor(3.7)        ▶  3
floor(-2.3)       ▶  -3
ceil(3.2)         ▶  4
ceil(-2.7)        ▶  -2
round(pi, 3)      ▶  3.142
round(e, 5)       ▶  2.71828
round(2.5, 0)     ▶  2 oder 3   (je nach Implementierung)
```

`floor` und `ceil` sind direkte SymPy-Funktionen — `ceil` ist ein Alias für `ceiling`, damit der TI-Stil gewahrt bleibt.

## Vorzeichen

`sign(x)` — gibt `-1`, `0` oder `1` zurück (SymPy-Standard)

```
sign(-5)          ▶  -1
sign(0)           ▶  0
sign(7)           ▶  1
sign(-pi)         ▶  -1
```

## Komplexe Zahlen

In SymPy heißt die imaginäre Einheit `I`.

`re(z)` — Realteil
`im(z)` — Imaginärteil
`conj(z)` — komplex Konjugiertes (Alias für `conjugate`)
`arg(z)` — Argument (Winkel in der komplexen Ebene)

```
re(3 + 4*I)         ▶  3
im(3 + 4*I)         ▶  4
conj(3 + 4*I)       ▶  3 - 4·I
arg(1 + I)          ▶  pi/4
arg(I)              ▶  pi/2
```

Die Beträge komplexer Zahlen kannst du mit `|z|` (Betrag) oder `norm([re(z), im(z)])` berechnen — beides liefert dasselbe.

```
|3 + 4*I|          ▶  5
norm([3, 4])       ▶  5
```
