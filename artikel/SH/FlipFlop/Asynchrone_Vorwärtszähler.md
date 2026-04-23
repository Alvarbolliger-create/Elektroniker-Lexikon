---
title: Asynchrone Vorwärtszähler
kategorie: Zählerschaltungen
tags: [Zähler, Ripple]
---

# Der Ripple-Counter

Asynchrone Zähler sind die einfachsten Zählerschaltungen. Sie bestehen aus einer Kette von Flipflops.

## Prinzip
Der Takt wird nur an das **erste** Flipflop angelegt. Jedes weitere Flipflop erhält seinen Takt vom Ausgang des vorhergehenden.
- **Vorteil:** Sehr einfacher Schaltungsaufbau.
- **Nachteil (Signallaufzeit):** Da jedes FF eine kurze Zeit zum Schalten braucht, "wandert" das Signal wie eine Welle durch die Kette (Ripple-Effekt). Bei hohen Frequenzen oder vielen Bits führt dies zu kurzzeitigen Fehlzuständen am Ausgang.

## Schaltung
Für einen Vorwärtszähler wird bei negativ flankengesteuerten FFs der Takt vom Ausgang $Q$ des Vorgängers genommen.

---
**Siehe auch:**
- [[Asynchrone Rückwärtszähler]]
- [[Synchrone Vorwärtszähler]]