---
title: Einstellungen
kategorie: Grundlagen
---

# Einstellungen

Über den Button **⚙ Einstellungen** in der Toolbar erreichst du den Einstellungen-Dialog. Dort kannst du drei Dinge verändern.

Rechts neben dem Einstellungen-Button siehst du jederzeit den Status — z. B. `RAD · ENG` oder `DEG · ·`.

## Winkelmodus

- **RAD** (Standard): Trigonometrische Funktionen arbeiten im Bogenmaß.
  `sin(π/2)` → `1`, `sin(1)` → `sin(1)` ≈ 0,841.
- **DEG**: Trigonometrische Funktionen arbeiten in Grad.
  `sin(30)` → `1/2`, `sin(90)` → `1`, `asin(1/2)` → `30`.

Betroffen sind `sin`, `cos`, `tan`, `cot`, `sec`, `csc` sowie deren Umkehrfunktionen `asin`, `acos`, `atan`, `acot`, `asec`, `acsc` und `atan2`.

**Vorsicht beim Mischen:** Im DEG-Modus ist `sin(π)` nicht etwa 0, sondern `sin(π · π/180)` — weil der Rechner annimmt, dass `π` ein Gradwert sein soll. Im DEG-Modus also keine Vielfachen von π als Argumente benutzen.

## Zahlenformat bei `aprox`

Das Zahlenformat beeinflusst nur `aprox(...)`-Ergebnisse. Ohne `aprox` bleibt die Darstellung exakt (Bruch, Wurzel, π usw.).

### Standard — Dezimalbruch

```
⟦ aprox(1/7) ⟧           ▶  0.142857
⟦ aprox(1500 * _Hz) ⟧    ▶  1500 Hz
```

### SIC — wissenschaftlich

Eine Stelle vor dem Komma, dann der Exponent. Einheiten bleiben unverändert (kein Präfix):

```
⟦ aprox(1/7) ⟧           ▶  1.428571·10⁻¹
⟦ aprox(1500 * _Hz) ⟧    ▶  1.5·10³ Hz
⟦ aprox(0.000022 * _F) ⟧ ▶  2.2·10⁻⁵ F
```

### ENG — Ingenieurs-Notation

Exponent als Vielfaches von 3. Wenn die Einheit ein passendes SI-Präfix hat, wird es direkt angehängt — statt `1.5·10³ Hz` also `1.5 kHz`:

```
⟦ aprox(1/7) ⟧           ▶  142.857·10⁻³
⟦ aprox(1500 * _Hz) ⟧    ▶  1.5 kHz
⟦ aprox(0.000022 * _F) ⟧ ▶  22 µF
⟦ aprox(4700 * _Ohm) ⟧   ▶  4.7 kΩ
```

## Nachkommastellen

Wie viele signifikante Stellen nach dem Komma in `aprox`-Ergebnissen angezeigt werden. Standardwert ist **6**, Bereich 1–15. Trailing-Nullen werden automatisch entfernt.

## Was passiert beim Ändern?

Sobald du **Übernehmen** klickst, wird das Dokument automatisch neu ausgewertet. Box-Ergebnisse mit `aprox` werden im neuen Format dargestellt; Winkel-Ergebnisse im passenden Winkelmodus.

**Abbrechen** verwirft deine Änderungen und lässt alles beim Alten.
