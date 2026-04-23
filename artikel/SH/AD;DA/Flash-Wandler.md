---
title: AD-Wandler: Flash-Wandler
kategorie: Wandler
tags: [Highspeed, Komparator]
---

# Der schnellste Wandler

Das Parallelverfahren (Flash-Conversion) wandelt die Spannung fast ohne Zeitverzögerung um.

## Aufbau
Für einen $n$-Bit Wandler benötigt man $2^n - 1$ Komparatoren.
- Ein Spannungsteiler liefert für jeden Komparator eine eigene Referenzschwelle.
- Die Eingangsspannung wird mit allen Schwellen gleichzeitig verglichen.

## Vor- und Nachteile
- **Vorteil:** Extrem schnell (Gigahertz-Bereich möglich).
- **Nachteil:** Hoher Stromverbrauch und Platzbedarf. Ein 8-Bit Wandler braucht bereits 255 Komparatoren.

---
**Siehe auch:**
- [[Codewandler]] (wegen des benötigten Prioritätsencoders am Ausgang)
- [[AD-Wandler: Dual-Slope]]