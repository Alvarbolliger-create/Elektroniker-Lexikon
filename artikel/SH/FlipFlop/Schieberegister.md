---
title: Schieberegister
kategorie: Sequentielle Logik
tags: [Speicher, Datentransport]
---

# Daten in Bewegung

Schieberegister bestehen aus einer Kette von D-Flipflops, bei denen der Ausgang eines FFs mit dem Eingang des nächsten verbunden ist. Mit jedem Takt wandert die Information eine Stelle weiter.

## Betriebsarten (Modi)
Man unterscheidet vier Grundkonfigurationen, je nachdem wie Daten ein- und ausgegeben werden:

1. **SISO (Serial-In, Serial-Out):** Ein Bit nach dem anderen. Dient oft als Verzögerungsleitung.
2. **SIPO (Serial-In, Parallel-Out):** Wandelt einen seriellen Datenstrom in ein paralleles Wort um (wichtig für Empfänger).
3. **PISO (Parallel-In, Serial-Out):** Wandelt parallele Daten in einen seriellen Strom um (wichtig für Sender).
4. **PIPO (Parallel-In, Parallel-Out):** Fungiert als Zwischenspeicher (Register).

---
**Siehe auch:**
- [[Flipflops]]
- [[Datenübertragung (Grundlagen)]]