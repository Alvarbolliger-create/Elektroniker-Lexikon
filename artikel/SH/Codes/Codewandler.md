---
title: Codewandler
kategorie: Codierung
tags: [7-Segment, Display, Logik]
---

# Schnittstelle zum Menschen

Codewandler übersetzen Informationen von einem Maschinencode in einen anderen (z.B. für Displays).

## BCD-zu-7-Segment-Decoder
Dieser Wandler macht aus einer 4-Bit-Binärzahl die Ansteuersignale für eine Ziffernanzeige (Segmente a-g).

## 7-Segment-Anzeigen
Es gibt zwei Hardware-Varianten:
1. **Gemeinsame Kathode (CC):** Alle Minus-Pole der LEDs sind verbunden (aktiv bei High-Signal).
2. **Gemeinsame Anode (CA):** Alle Plus-Pole sind verbunden (aktiv bei Low-Signal).

## Prioritätsencoder
Wandelt mehrere Einzelsignale in eine Binärzahl um. Wenn mehrere Eingänge gleichzeitig aktiv sind, gewinnt der mit der höchsten Wertigkeit.
- **Wichtig für:** [[AD-Wandler: Parallelverfahren]].

---
**Siehe auch:**
- [[Multiplexer und Demultiplexer]]
- [[Digitale Codes]]