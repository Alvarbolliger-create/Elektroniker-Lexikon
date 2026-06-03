---
title: Tastatur-Referenz
kategorie: Grundlagen
---

# Tastatur-Referenz

Übersicht aller Tastenkürzel des 2D-Editors.

## Eingabe & Auswertung

- `Enter` — alle Zeilen auswerten und neue Zeile darunter anlegen
- `Ctrl+Enter` — aktuelle Zeile numerisch (`aprox`) auswerten, Cursor bleibt
- `Tippen` — Zeichen an Cursor-Position einfügen
- `Backspace` — links vom Cursor löschen; am Zeilenanfang mit voriger Zeile zusammenführen
- `Delete` — rechts vom Cursor löschen

## Bearbeiten

- `Ctrl+Z` — Rückgängig (bis 100 Schritte)
- `Ctrl+Y` — Wiederholen
- `Ctrl+C` — Aktuelle Zeile + Ergebnis kopieren (oder markierten Text)
- `Ctrl+X` — Aktuelle Zeile ausschneiden (oder markierten Text)
- `Ctrl+V` — Einfügen

## Strukturen einfügen

- `/` oder `Ctrl+F` — Bruch (Tail bis zum letzten Trennzeichen wird Zähler)
- `^` — Exponent (hochgestellter Slot)
- `Ctrl+_` — Subscript (tiefgestellter Slot, für Variablen-Indizes)
- `Ctrl+R` — Quadratwurzel
- `Ctrl+Shift+R` — n-te Wurzel
- `Alt+S` — Summe Σ
- `Alt+I` — Integral ∫
- `Alt+V` — Vektor (initial 2×1)
- `Alt+L` — Logarithmus log_n(x)
- `Alt+G` — Gleichungssystem (2 Zeilen, geschweifte Klammer)

## Navigation

- `←` `→` — horizontal, taucht in Container ein und springt zwischen Zeilen
- `Shift+←` `Shift+→` — Auswahl zeichenweise erweitern
- `↑` `↓` — vertikal: zwischen Slots eines Containers (z. B. Zähler ↔ Nenner) oder zwischen Top-Level-Zeilen
- `Tab` — nächster Slot innerhalb des Containers
- `Home` `End` — Anfang/Ende der aktuellen Zeile
- Mausklick — Cursor an die geklickte Position setzen (auch in tief verschachtelten Strukturen)

## Matrix-Operationen

- `Tab` in der letzten Matrix-Zelle — neue Zeile anhängen
- `Ctrl+Tab` — Matrix: Zeile anhängen (egal wo der Cursor steht)
- `Ctrl+Shift+Tab` — Matrix: Spalte anhängen
- `Backspace` in einer komplett leeren Matrix-Zeile/-Spalte — diese entfernen

## Gleichungssystem-Operationen

- `Ctrl+Tab` — neue Gleichungszeile anhängen
- `Tab` in der letzten Zeile — neue Gleichungszeile anhängen
- `Backspace` in einer leeren Gleichungszeile — diese entfernen (wenn mehr als eine Zeile)

## Tabs

- `Ctrl+T` — neuen Tab anlegen

## Strukturierter Backspace

Wenn der Cursor direkt rechts neben einem strukturellen Element (Bruch, Wurzel, Summe, …) steht und `Backspace` gedrückt wird:

1. Erstes `Backspace` — das Element wird **markiert** (blau hervorgehoben)
2. Zweites `Backspace` — das Element wird gelöscht
3. Jede andere Taste — Markierung wird wieder aufgehoben

So vermeidet man versehentliches Löschen umfangreicher Konstrukte.

## Kommentare

Eine Zeile, die mit `#` beginnt, wird als Kommentar grau dargestellt und nicht ausgewertet.

```
# das ist ein Kommentar
2 + 3        ▶  5
```
