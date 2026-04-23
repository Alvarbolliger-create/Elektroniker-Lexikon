---
title: Flipflops
kategorie: Sequentielle Logik
tags: [Speicher, Takt, Basics]
---

# Bistabile Kippstufen

Im Gegensatz zu Kombinatorik (Gatter) können Flipflops (FF) Informationen speichern. Sie bilden das Gedächtnis der Digitaltechnik.

## Grundtypen
- **RS-Flipflop:** Einfachster Speicher mit Setzen (S) und Rücksetzen (R). Problem: Der "verbotene Zustand" (beide Eingänge 1).
- **D-Flipflop:** Übernimmt den Wert am Dateneingang (D) erst bei einer Taktflanke. Ideal zur Datenspeicherung.
- **JK-Flipflop:** Der Allrounder. Kann Setzen, Rücksetzen, Speichern und **Toggeln** (Zustand wechseln).
- **T-Flipflop:** Wechselt bei jedem Taktimpuls seinen Zustand (Toggle).

## Taktsteuerung & Timing
- **Pegelgesteuert:** Reagiert, solange der Takt auf High (oder Low) ist.
- **Flankengesteuert:** Reagiert nur im Moment des Wechsels (positive oder negative Flanke).
- **Setup-Zeit ($t_s$):** Zeit, die das Datensignal vor der Taktflanke stabil anliegen muss.
- **Hold-Zeit ($t_h$):** Zeit, die das Datensignal nach der Flanke stabil bleiben muss.

---
**Siehe auch:**
- [[Frequenzteiler]]
- [[Schieberegister]]