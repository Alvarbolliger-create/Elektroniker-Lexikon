---
title: Gleichungen mit =
kategorie: Grundlagen
---

# Gleichungen mit `=`

Der Operator `=` ist **keine** Zuweisung, sondern eine Gleichung. `a = b` bedeutet „ist `a` gleich `b`?".

## Wahrheitswerte

Wenn beide Seiten einen konkreten Wert haben, wird die Gleichung zu `True` oder `False` ausgewertet:

```
a := 5
a = 6        ▶  False ✗
a = 5        ▶  True  ✓
2 + 2 = 4    ▶  True  ✓
```

Nützlich als **Verifikation** — du kannst eine Zeile benutzen, um zu prüfen, ob ein Wert stimmt, ohne ihn global festzuschreiben.

## Symbolische Gleichungen

Wenn eine Seite ein freies Symbol enthält, bleibt die Gleichung symbolisch:

```
x^2 + 1 = 0   ▶  x² + 1 = 0
```

Das ist keine Lösung, sondern die Gleichung selbst — ideal als Ausgangspunkt für `solve` oder `dsolve`.

## In `solve` und Freunden

Weil `=` eine echte Gleichung erzeugt, kannst du es direkt in Löserfunktionen einsetzen — ohne Komma-Trick:

```
solve(x^2 = 4, x)            ▶  [-2, 2]
solve(sin(x) = 1/2, x)       ▶  [π/6, 5π/6]
solve([x + y = 3, x - y = 1], [x, y])
```

Die früher übliche SymPy-Form `solve(expr - wert, x)` funktioniert natürlich weiterhin.

## Abgrenzung zu `:=`

| Situation | `:=` | `=` |
|---|---|---|
| `a := 5` | setzt `a` auf 5 (global) | — |
| `a = 6` | — | fragt: ist `a = 6`? |
| Gleichung lösen | nicht passend | `solve(x^2 = 4, x)` |
| Variable definieren | `R := 220` | nein, dafür `:=` |

Wenn du unsicher bist: **Soll die Variable danach „verankert" sein?** → `:=`. **Ist das eine Aussage, die wahr oder falsch sein kann?** → `=`.
