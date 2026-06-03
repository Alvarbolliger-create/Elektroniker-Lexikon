---
title: Zuweisungen
kategorie: Grundlagen
---

# Zuweisungen

Eine Zuweisung verknüpft eine Variable fest mit einem Wert. Der Operator ist `:=`:

```
name := ausdruck
```

Nur `:=` zählt als Zuweisung. Ein einfaches `=` ist eine **Gleichung** und tut etwas anderes — siehe Artikel [[Gleichungen mit =]] und [[Syntax]].

## Beispiele

- `R := 220` → eine Zahl
- `U := R * I` → nutzt andere Variablen
- `f := x^2 + 1` → eine Formel mit freier Variable `x`

## Gültigkeitsbereich

Alle `:=`-Zuweisungen gelten **dokumentweit**. Die Reihenfolge der Zeilen ist egal:

```
U := R * I
R := 220
I := 0.005
```

Alle drei Zeilen werden korrekt aufgelöst, auch wenn `U` ganz oben definiert wird und seine Zutaten erst weiter unten.

## Eine Variable — nur eine Zuweisung

Jede Variable darf nur mit *einer* `:=`-Zuweisung belegt werden. Kommt dieselbe Variable in zwei `:=`-Zuweisungen vor, werden beide als Konflikt markiert:

```
a := 2   ▶  Konflikt: »a« wird 2× zugewiesen
a := 3   ▶  Konflikt: »a« wird 2× zugewiesen
```

Willst du einen neuen Wert ausprobieren, ändere die bestehende Zuweisung, statt eine zweite hinzuzufügen.

## Nicht zugewiesene Variablen

Variablen, die nirgends mit `:=` zugewiesen werden, bleiben **freie Symbole**. Das ist nützlich für algebraische Manipulation:

```
f := x^2 - 4
solve(f, x)   ▶  [-2, 2]
```

Hier ist `x` absichtlich frei, damit `solve` darüber variieren kann.
