---
title: Fehler und Konflikte
kategorie: Fehlerbehandlung
---

# Fehler und Konflikte

Rot markierte Ergebnisse sind Fehler. Es gibt ein paar Kategorien, die der Rechner selbst erkennt, bevor SymPy überhaupt drankommt.

## Doppelte Zuweisungen

Jede Variable darf **nur einmal** mit `:=` zugewiesen werden:

```
a := 2   ▶  Konflikt: »a« wird 2× zugewiesen
a := 3   ▶  Konflikt: »a« wird 2× zugewiesen
```

**Fix:** Eine der beiden Zeilen löschen oder die Variable umbenennen.

Tipp: Wenn du ausprobieren willst, ob `a = 3` passen würde, ohne die globale Zuweisung zu ändern, schreib es als **Gleichung** (siehe [[Gleichungen mit =]]):

```
a := 2
a = 3     ▶  False ✗   (nur lokale Verifikation)
```

## Zirkuläre Abhängigkeiten

Variablen dürfen nicht im Kreis voneinander abhängen:

```
a := b + 1   ▶  Zirkulär: a → b → a
b := a * 2   ▶  Zirkulär: a → b → a
```

Der Pfad in der Fehlermeldung zeigt, welche Variablen den Kreis bilden.

**Fix:** Irgendwo den Kreis aufbrechen — mindestens eine Variable muss auf einen konkreten Wert oder auf ein freies Symbol enden.

## Syntaxfehler

Alles, was SymPy nicht parsen kann, landet als Fehlermeldung in rot:

```
2 * + 3      ▶  invalid syntax
sin(         ▶  unexpected EOF while parsing
```

Häufige Ursachen:

- Klammern nicht geschlossen
- Operator zweimal hintereinander (`+ +`)
- Unbekannte Funktion — SymPy kennt viele Namen, aber nicht alle (z. B. `cot` existiert, `ctg` nicht)

## Laufzeitfehler

Manche Ausdrücke sind formal korrekt, rechnen aber in einen undefinierten Wert:

- `1/0` → `zoo` (komplex-unendlich)
- `log(-1)` → `I*π`
- `asin(2)` → komplexe Zahl

Das sind **keine** Fehler im engeren Sinne — SymPy liefert einfach das mathematisch korrekte Resultat. Aber Vorsicht bei numerischen Interpretationen.
