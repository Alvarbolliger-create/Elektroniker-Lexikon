---
title: Syntax
kategorie: Grundlagen
---

# Syntax

Der Rechner versteht eine an den TI-NSpire angelehnte Schreibweise. Intern wird alles nach SymPy übersetzt.

## Übersicht

| Eingabe | Bedeutung | Beispiel |
|---|---|---|
| `x^2` | Potenz | `x^2 + 2x + 1` |
| `:=` | globale Zuweisung | `R := 220` |
| `=` | Gleichung | `a = 6` oder `solve(x^2 = 4, x)` |
| `√(x)` / `√x` | Wurzel | `√(2)`, `√(16)` → 4 |
| `π` | Pi | `2*π*r` |
| `∞` | Unendlich | `limit(1/x, x, ∞)` |
| &#124;x&#124; | Betrag | &#124;-5&#124; → 5 |
| `2x` | implizite Multiplikation | wird zu `2*x` |
| `#…` | Kommentar | ganze Zeile wird ignoriert |
| `_m`, `_kg`, `_N` … | Einheiten | siehe [[Einheiten]] |
| `aprox(…)` | numerisch auswerten | siehe [[aprox]] |
| `1.5E-6` | wissenschaftliche Notation | `1.5·10⁻⁶` |

## `:=` vs `=` — wichtig!

- `a := 5` ist eine **Zuweisung**: `a` ist ab jetzt überall im Dokument 5.
- `a = 5` ist eine **Gleichung**: „ist `a` gleich 5?". Wird zu `True`/`False` ausgewertet, oder bleibt symbolisch.

Das heißt, `=` funktioniert direkt in `solve` — ohne Komma-Trick:

```
solve(x^2 = 4, x)    ▶  [-2, 2]
```

Details zum Unterschied: [[Gleichungen mit =]].

## Einheiten

Alles, was mit `_` beginnt, ist eine Einheit — nicht eine Variable. Darum können Variablennamen auch nicht mit `_` beginnen.

```
U := 12 * _V          ▶  U := 12 V
I := 20 * _mA         ▶  I := 1/50 A
R := U / I            ▶  R := 600 Ω
aprox(R)              ▶  600 Ω
```

Vollständige Liste: [[Einheiten]].

## Implizite Multiplikation

Eine Zahl direkt vor einem Buchstaben oder einer Klammer wird automatisch als Multiplikation verstanden:

- `2x` → `2*x`
- `3(x + 1)` → `3*(x + 1)`
- `0.5a` → `0.5*a`

Zwischen zwei Buchstaben fügt der Rechner **nichts** ein: `ab` bleibt die Variable `ab`, nicht `a*b`. Und bei Einheiten sicherheitshalber mit Stern: `2 * _kN` statt `2_kN`.

## Zahlen

- Ganze Zahlen und Brüche bleiben exakt: `1/3` → `1/3`.
- Dezimalzahlen werden meist rationalisiert: `0.25` → `1/4`.
- Mit `aprox(...)` bekommst du eine Dezimaldarstellung (siehe [[aprox]]).
- Wissenschaftliche Notation funktioniert direkt: `1.5E-6` wird als Dezimalzahl erkannt.
