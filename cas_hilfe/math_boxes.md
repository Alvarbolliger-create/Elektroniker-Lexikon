---
title: Zeileneditor
kategorie: Grundlagen
---

# Zeileneditor

Der CAS Rechner verwendet einen **zeilenbasierten** Formel-Editor. Jede Zeile ist ein eigenständiger Ausdruck — einfach eintippen, kein spezielles Format oder Zeichen nötig.

## Wie es funktioniert

- Ausdruck eintippen und **Enter** drücken → das ganze Dokument wird ausgewertet, das Ergebnis erscheint rechts nach `▶`, der Cursor springt in die nächste Zeile.
- Alle Zeilen werden bei jeder Auswertung gleichzeitig neu berechnet.

```
R := 220
I := 0.005
U := R * I      ▶  U := 11/10
```

## Ergebnisse

Ergebnisse erscheinen rechts neben der Zeile, getrennt durch `▶`:

- **Grün** — alles gut.
- **Rot** — Fehler (Syntax, Konflikt, Zyklus, …).
- Bei exakten Ergebnissen mit einem numerisch abweichenden Wert wird `≈ …` angehängt.

## Kommentare

Jede Zeile, die mit `#` beginnt, ist ein Kommentar — sie wird nicht ausgewertet und grau dargestellt:

```
# Widerstandsberechnung
R := 220
I := 0.005
```

## Ctrl+Enter — numerisch auswerten

Mit **Ctrl+Enter** wird die aktuelle Zeile einmalig numerisch (aprox) ausgewertet, ohne den Text zu verändern. Das nächste **Enter** setzt zur exakten Darstellung zurück.

## Strukturierter Backspace

Wenn der Cursor direkt rechts neben einem strukturellen Element (Bruch, Wurzel, Exponent, …) steht:

1. Erstes `Backspace` — das Element wird **markiert**.
2. Zweites `Backspace` — das Element wird gelöscht.
3. Jede andere Taste — Markierung wird aufgehoben.

So vermeidet man versehentliches Löschen verschachtelter Konstrukte.
