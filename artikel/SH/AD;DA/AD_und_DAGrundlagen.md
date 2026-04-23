---
title: AD- und DA-Grundlagen
kategorie: Wandler
tags: [Abtastung, Theorie, Nyquist]
---

# Die Brücke zwischen Analog und Digital

Um reale Signale (Temperatur, Ton) zu verarbeiten, müssen sie gewandelt werden.

## Das Abtasttheorem (Nyquist-Shannon)
Damit ein Signal fehlerfrei rekonstruiert werden kann, muss die **Abtastfrequenz ($f_a$)** mehr als doppelt so hoch sein wie die höchste im Signal vorkommende Frequenz ($f_{max}$):
`f_a > 2 * f_max`

## Fehlerquellen
- **Aliasing:** Wenn zu langsam abgetastet wird, entstehen Geisterfrequenzen. Ein **Anti-Aliasing-Filter** (Tiefpass) vor dem Wandler verhindert dies.
- **Quantisierungsfehler:** Die Abweichung zwischen dem echten Analogwert und dem nächstgelegenen digitalen Stufenwert.
- **LSB (Resolution):** Die kleinste Spannungsänderung, die noch erkannt wird.

---
**Siehe auch:**
- [[AD-Wandler: Parallelverfahren]]
- [[DA-Wandler: R-2R-Netzwerk]]