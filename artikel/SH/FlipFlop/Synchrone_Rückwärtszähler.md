---
title: Synchrone Rückwärtszähler
kategorie: Zählerschaltungen
tags: [Logik, Highspeed]
---

# Rückwärtszählen im Gleichtakt

Ein synchroner Rückwärtszähler nutzt wie sein Vorwärts-Pendant einen gemeinsamen Takt für alle Flipflops, unterscheidet sich aber in der Ansteuerlogik.

## Funktionsweise
Damit die Schaltung rückwärts zählt (z. B. von `100` auf `011`), muss ein Bit immer dann seinen Zustand ändern (toggeln), wenn **alle niederwertigeren Bits auf 0** stehen.

- Bei JK-Flipflops wird dies erreicht, indem man die **invertierten Ausgänge** ($\bar{Q}$) der vorherigen Stufen mit UND-Gattern verknüpft und auf die J-K-Eingänge der nächsten Stufe führt.
- Dies stellt sicher, dass alle Flipflops exakt gleichzeitig schalten, sobald die Bedingung erfüllt ist.

---
**Siehe auch:**
- [[Synchrone Vorwärtszähler]]
- [[Logikgatter]]