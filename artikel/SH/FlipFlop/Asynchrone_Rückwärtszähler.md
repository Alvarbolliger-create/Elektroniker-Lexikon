---
title: Asynchrone Rückwärtszähler
kategorie: Zählerschaltungen
tags: [Zähler, Binär]
---

# Rückwärts zählen im Ripple-Modus

Der Aufbau ist fast identisch zum Vorwärtszähler, jedoch wird die Logik der Taktweiterleitung invertiert.

## Funktionsweise
Damit die Schaltung rückwärts zählt (z.B. von 111 auf 110), muss das nächste Flipflop immer dann schalten, wenn das vorherige von **0 auf 1** springt. 
- Bei Verwendung von negativ flankengesteuerten FFs erreicht man dies, indem man den Takt vom **invertierten Ausgang** $\bar{Q}$ des Vorgängers abgreift.

## Einschränkung
Auch hier gilt: Die Addierung der Gatterlaufzeiten begrenzt die maximale Zählfrequenz und kann für kurze Momente falsche Zwischenwerte auf dem Bus erzeugen.

---
**Siehe auch:**
- [[Asynchrone Vorwärtszähler]]