---
title: Digitale Codes
kategorie: SH
tags: [BCD, gray-code, ASCII, parität, codierung, hamming, fehlerkennung, encoder, 7-segment, unicode]
symbol: —
einheit: —
---

Neben dem reinen Binärcode gibt es spezielle Codes für bestimmte Zwecke: einfachere Fehlerkennung, direktere Darstellung von Ziffern oder sichere Übertragung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Zahlensysteme]]
- [[Binäre Arithmetik]]
:::
:::vbox
**Verwandte Artikel**
- [[UART]]
- [[Logikgatter]]
:::
:::

---

## BCD (Binary Coded Decimal)

Jede Dezimalziffer wird einzeln als 4-Bit-Binärzahl codiert.

| Dezimal | BCD |
|---|---|
| 0 | 0000 |
| 5 | 0101 |
| 9 | 1001 |

Vorteil: Direkte Anzeige auf 7-Segment-Displays, einfache Dezimalarithmetik.  
Nachteil: Verschwendet Kombinationen (1010 bis 1111 ungültig), braucht mehr Bits als reines Binär.

Typisch in Taschenrechnern, Zählern und Anzeigen.

## Gray-Code

Zwei benachbarte Werte unterscheiden sich immer in genau einem Bit.

| Dezimal | Binär | Gray |
|---|---|---|
| 0 | 000 | 000 |
| 1 | 001 | 001 |
| 2 | 010 | 011 |
| 3 | 011 | 010 |

Vorteil: Bei Positions-Encodern kann kein falscher Zwischenwert entstehen wenn zwei Bits sich ändern. Im normalen Binärcode würde der Übergang von 3 (011) auf 4 (100) drei Bits gleichzeitig ändern, was bei leichten Zeitunterschieden zu Fehlesungen führt.

Einsatz: Drehgeber (Encoder), Position Sensing.

## ASCII

7-Bit-Code für Buchstaben, Ziffern und Steuerzeichen. 128 Zeichen total.

- 'A' = 65 (0x41)
- 'a' = 97 (0x61)
- '0' = 48 (0x30)

ASCII ist die Grundlage für UART-Textübertragung und viele Protokolle.

## Parität

Ein zusätzliches Bit macht die Gesamtanzahl der Einsen gerade (Even Parity) oder ungerade (Odd Parity). Einfache Fehlerkennung, keine Fehlerkorrektur.

Ein Einzelbitfehler wird erkannt, aber ein Doppelbitfehler nicht.
