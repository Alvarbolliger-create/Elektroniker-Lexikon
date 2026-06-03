---
title: Kommentare
kategorie: Grundlagen
---

# Kommentare

Jede Zeile, die mit `#` beginnt, ist ein **Kommentar**. Sie wird beim Auswerten komplett ignoriert, erscheint im Editor aber leicht gräulich/kursiv und bleibt als Notiz erhalten.

## Beispiel

```
# Ohmsches Gesetz durchrechnen
R := 220
I := 0.005
# U = R * I
U := R * I   ▶  U := 11/10
```

## Wofür Kommentare gut sind

- **Abschnitte markieren** — „Teil 1: Widerstände berechnen"
- **Erklären, woher ein Wert stammt** — „aus Datenblatt Seite 3"
- **Zeilen temporär deaktivieren** — `# ` an den Anfang der Zeile setzen, um sie als Kommentar zu markieren.

## Einschränkungen

Der `#` muss am **Anfang der Zeile** (nach optionalen Leerzeichen) stehen. Am Ende einer Zeile, hinter einem Ausdruck, gilt er **nicht** als Kommentar — dort wäre er ein Syntaxfehler.

Also **nicht** so:

```
R := 220   # Widerstand in Ohm   ▶  Fehler
```

Sondern so:

```
# Widerstand in Ohm
R := 220
```
