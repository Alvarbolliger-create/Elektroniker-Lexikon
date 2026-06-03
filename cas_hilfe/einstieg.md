---
title: Einstieg
kategorie: Grundlagen
---

# Einstieg

Der **CAS Rechner** ist ein zeilenbasierter Formel-Editor, in dem Notizen und Rechnungen direkt untereinander stehen. Jede Zeile wird beim Drücken von **Enter** ausgewertet — kein spezielles Format nötig.

## Der Workflow

- Ausdruck eintippen, z. B. `2 + 2` oder `R := 220`.
- **Enter** → das ganze Dokument wird ausgewertet, das Ergebnis erscheint grün rechts neben der Zeile.

## Die wichtigsten Bausteine

- **Zeile erkennen:** Jede Zeile ist ein Ausdruck. Zeilen mit `#` am Anfang sind Kommentare (grau).
- **Zuweisen:** `R := 220` setzt `R` **dokumentweit** auf 220. Siehe [[Zuweisungen]].
- **Gleichung:** `a = 6` fragt „ist a gleich 6?". Auch in `solve(x^2 = 4, x)` einsetzbar. Siehe [[Gleichungen mit =]].
- **Einheiten:** Alles mit `_` davor: `_m`, `_kg`, `_V`, `_Ohm`, `_Hz`, `_kN`, `_µF`, … Siehe [[Einheiten]].
- **Numerisch machen:** `aprox(...)` oder **Ctrl+Enter** in der Zeile. Siehe [[aprox]].
- **Modus wechseln:** RAD/DEG, SIC/ENG und Nachkommastellen über **⚙ Einstellungen**. Siehe [[Einstellungen]].

## Ein vollständiges Beispiel

```
# RC-Tiefpass: Grenzfrequenz berechnen
R := 4.7 * _kOhm          ▶  R := 47/10 kΩ
C := 100 * _nF             ▶  C := 1/10000000 F
fc := 1 / (2 * π * R * C)
aprox(fc)                  ▶  338.628 Hz   (ENG)
```

## Tastaturkürzel

| Taste | Wirkung |
|---|---|
| **Enter** | Auswerten und neue Zeile anlegen |
| **Ctrl+Enter** | Aktuelle Zeile numerisch (aprox) auswerten |
| **Ctrl+L** | Dokument leeren |
| **Backspace** | Strukturiert: erst markieren, dann löschen. Siehe [[Zeileneditor]] |
