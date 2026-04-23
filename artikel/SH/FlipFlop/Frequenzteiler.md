---
title: Frequenzteiler
kategorie: Sequentielle Logik
tags: [Takt, Timing]
---

# Halbierung der Frequenz

Ein Frequenzteiler reduziert die Eingangsfrequenz eines Taktsignals in einem festen Verhältnis.

## Funktionsweise
Wird ein **JK-Flipflop** oder ein **T-Flipflop** fest auf den Modus "Toggle" geschaltet, wechselt der Ausgang bei jeder aktiven Taktflanke seinen Zustand. 
- Da für eine volle Periode (High und Low) am Ausgang zwei Taktflanken am Eingang nötig sind, wird die Frequenz exakt **halbiert** ($f_{out} = f_{in} / 2$).

## Kenngrößen
- **Duty Cycle (Tastverhältnis):** Das Verhältnis von High-Zeit zur Periodendauer. Bei einfachen Flipflop-Teilern beträgt dieser meist 50%.
- **Kaskadierung:** Schaltet man mehrere Teiler hintereinander, erhält man Teilerfaktoren von 4, 8, 16 usw.

---
**Siehe auch:**
- [[Asynchrone Vorwärtszähler]]
- [[Flipflops]]