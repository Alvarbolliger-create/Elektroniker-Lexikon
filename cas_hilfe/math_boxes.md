---
title: Math Boxes
kategorie: Grundlagen
---

# Math Boxes

Eine Math Box ist ein Textbereich, der als Rechnung ausgewertet wird. Sie ist nicht durch sichtbare Klammern begrenzt, sondern durch ihr **Format**: Text in einer Math Box ist **blau und in Monospace-Schrift**.

## Box erzeugen

- **Ctrl+M** fügt eine leere Box an der Cursor-Position ein. Du erkennst sie am gestrichelten Rahmen.
- Alternativ der Button **+ Math Box** in der Toolbar.

Direkt danach kannst du den Ausdruck tippen — das Tippen „bleibt" automatisch in der Box, solange der Cursor innerhalb des blauen Bereichs steht.

## Box verlassen

Sobald du mit den Pfeiltasten (oder einem Klick) den blauen Bereich rechts verlässt, wird der nächste Tastendruck wieder ganz normaler schwarzer Text. Der Rahmen um die Box verschwindet; der blaue Text bleibt.

## Auswerten

- **Enter in einer Box** → das ganze Dokument wird neu ausgewertet. Der Cursor bleibt, wo er ist; es wird **kein** Zeilenumbruch eingefügt.
- **Enter ausserhalb einer Box** → normale neue Zeile, und danach wird ausgewertet.

## Live-Verhalten

Sobald du den Inhalt einer Box änderst — egal ob du tippst oder löschst —, verschwindet das angezeigte Ergebnis sofort. Es ist ja nicht mehr aktuell. Erst beim nächsten Enter erscheint das neue Ergebnis.

## Backspace rund um Boxen

Backspace hat in der Nähe von Boxen eine spezielle Logik:

- Innerhalb einer Box oder unmittelbar daran angrenzend → der **erste** Backspace löscht das angezeigte Ergebnis. Der Box-Inhalt bleibt erhalten.
- Wenn kein Ergebnis mehr da ist und der Cursor direkt rechts neben einer Box steht → der Backspace markiert die ganze Box.
- Noch einmal Backspace → die markierte Box wird gelöscht.
- Innerhalb einer Box (kein Ergebnis, keine Auswahl): normales zeichenweises Löschen.

## Ergebnisse

Ergebnisse erscheinen rechts neben der Box, getrennt durch `▶`:

- **Grün** — alles gut.
- **Rot** — Fehler (Syntax, Konflikt, Zyklus, …).
- Bei rein numerischen Ausdrücken wird oft zusätzlich eine Dezimalannäherung `≈ …` angehängt.
