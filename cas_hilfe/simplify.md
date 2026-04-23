---
title: simplify & Co.
kategorie: Funktionen
---

# Umformungsfunktionen

SymPy bietet eine ganze Familie von Funktionen, um Ausdrücke umzuformen. Welche passt, hängt davon ab, was du erreichen willst.

## `simplify`

Der Allrounder. Versucht, einen Ausdruck „möglichst einfach" zu machen. Funktioniert gut für gemischte Ausdrücke, kann aber bei sehr grossen Ausdrücken langsam sein.

```
⟦ simplify(sin(x)^2 + cos(x)^2) ⟧     ▶  1
⟦ simplify((x^2 - 1)/(x - 1)) ⟧       ▶  x + 1
```

## `expand`

Multipliziert aus, verteilt Produkte:

```
⟦ expand((x + 1)^3) ⟧       ▶  x^3 + 3*x^2 + 3*x + 1
⟦ expand(sin(x + y), trig=True) ⟧   ▶  sin(x)*cos(y) + sin(y)*cos(x)
```

## `factor`

Das Gegenteil: faktorisiert Polynome.

```
⟦ factor(x^3 - 1) ⟧            ▶  (x - 1)*(x^2 + x + 1)
⟦ factor(x^2 + 5x + 6) ⟧       ▶  (x + 2)*(x + 3)
```

## `collect`

Sammelt Terme nach einer Variable.

```
⟦ collect(x*y + x^2 + x*z, x) ⟧   ▶  x^2 + x*(y + z)
```

## `apart` / `together`

Partialbruchzerlegung vs. gemeinsamer Nenner.

```
⟦ apart(1/((x-1)*(x-2))) ⟧     ▶  -1/(x - 1) + 1/(x - 2)
⟦ together(1/x + 1/(x+1)) ⟧    ▶  (2*x + 1)/(x*(x + 1))
```

## `trigsimp`

Spezialisiert auf trigonometrische Identitäten.

```
⟦ trigsimp(sin(x)^2 + cos(x)^2) ⟧    ▶  1
⟦ trigsimp(2*sin(x)*cos(x)) ⟧        ▶  sin(2*x)
```

## Wann was?

| Ich will… | Funktion |
|---|---|
| möglichst einfach, ohne mich festzulegen | `simplify` |
| ausmultiplizieren | `expand` |
| faktorisieren | `factor` |
| nach einer Variable sortieren | `collect` |
| in Partialbrüche zerlegen | `apart` |
| auf einen Nenner bringen | `together` |
| trig. Identität anwenden | `trigsimp` |
