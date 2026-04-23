---
title: Logikgatter
kategorie: Digitale Bausteine
tags: [Logik, Gatter, Hardware]
---

# Grundverknüpfungen

Logikgatter sind die physische Umsetzung der Booleschen Algebra.

## Die drei Grundgatter
1. **UND (AND):** Der Ausgang ist nur 1, wenn **alle** Eingänge 1 sind.
   `Y = A * B`
2. **ODER (OR):** Der Ausgang ist 1, wenn **mindestens ein** Eingang 1 ist.
   `Y = A + B`
3. **NICHT (NOT):** Kehrt das Signal um (Inverter).
   `Y = !A`

## Erweiterte Gatter
- **NAND / NOR:** Invertierte UND/ODER Gatter. Sie sind "Universal-Gatter", mit denen man jede andere Logik aufbauen kann.
- **EXOR (Exklusiv-ODER):** Der Ausgang ist nur 1, wenn die Eingänge **unterschiedlich** sind. Wichtig für Addierer.

## Darstellung
In der Digitaltechnik nutzt man zur Beschreibung:
- **Wahrheitstabellen:** Tabellarische Auflistung aller Zustände.
- **Funktionsgleichungen:** Mathematische Schreibweise.
- **Schaltzeichen:** Symbole nach DIN/ANSI.

---
**Siehe auch:**
- [[Schaltalgebra und Schaltungsvereinfachung]]
- [[Binäre Arithmetik]]