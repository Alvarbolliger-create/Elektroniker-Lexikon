---
title: Einstieg
kategorie: Grundlagen
---

# Einstieg

Der **CAS Rechner** ist ein fliessender Texteditor, in dem Notizen und Rechnungen direkt nebeneinander stehen. Rechnungen stehen in **Math Boxes** — blau dargestellte Textbereiche, in denen der Rechner Ausdrücke auswertet.

## Der Workflow

- **Ctrl+M** drücken → eine leere Math Box erscheint an der Cursor-Position, mit gestricheltem Rahmen.
- Ausdruck eintippen, z. B. `2 + 2` oder `R := 220`.
- **Enter** → das ganze Dokument wird ausgewertet, das Ergebnis erscheint grün rechts neben der Box.

## Die wichtigsten Bausteine

- **Box erkennen:** Blauer Text = Math Box. Gestrichelter Rahmen = Cursor ist drin oder Box ist leer.
- **Zuweisen:** `R := 220` setzt `R` **dokumentweit** auf 220. Siehe [[Zuweisungen]].
- **Gleichung:** `a = 6` fragt „ist a gleich 6?". Auch in `solve(x^2 = 4, x)` einsetzbar. Siehe [[Gleichungen mit =]].
- **Einheiten:** Alles mit `_` davor: `_m`, `_kg`, `_V`, `_Ohm`, `_Hz`, `_kN`, `_µF`, … Siehe [[Einheiten]].
- **Numerisch machen:** `aprox(...)` oder **Ctrl+Enter** in der Box. Siehe [[aprox]].
- **Modus wechseln:** RAD/DEG, SIC/ENG und Nachkommastellen über **⚙ Einstellungen**. Siehe [[Einstellungen]].

## Ein vollständiges Beispiel

```
# RC-Tiefpass: Grenzfrequenz berechnen
⟦ R := 4.7 * _kOhm ⟧          ▶  R := 47/10 kΩ
⟦ C := 100 * _nF ⟧            ▶  C := 1/10000000 F
⟦ fc := 1 / (2 * π * R * C) ⟧
⟦ aprox(fc) ⟧                 ▶  338.628 Hz   (ENG)
```

## Tastaturkürzel

| Taste | Wirkung |
|---|---|
| **Ctrl+M** | Neue Math Box |
| **Enter** in Box | Auswerten |
| **Ctrl+Enter** in Box | In `aprox(...)` einwickeln / auswickeln |
| **Ctrl+L** | Dokument leeren |
| **Backspace** | Siehe [[Math Boxes]] für die spezielle Logik |
