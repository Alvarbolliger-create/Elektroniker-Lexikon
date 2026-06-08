---
title: Zahlensysteme
kategorie: SH
tags: [zahlensysteme, binär, hexadezimal, dezimal, oktal, nibble, byte, bit, MSB, LSB, basis, umrechnung]
symbol: —
einheit: —
---

Computer rechnen in Binär. Menschen rechnen in Dezimal. Hexadezimal ist die Brücke zwischen beiden. Wer mit Elektronik arbeitet, begegnet allen drei ständig.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale]]
:::
:::vbox
**Verwandte Artikel**
- [[Logikgatter]]
- [[Binäre Arithmetik]]
:::
:::vbox
**Führt weiter zu**
- [[Binäre Arithmetik]]
- [[Digitale Codes]]
:::
:::

---

## Dezimal (Basis 10)

Ziffern 0 bis 9. Jede Stelle ist eine Potenz von 10. Das kennt jeder.

## Binär (Basis 2)

Ziffern nur 0 und 1. Jede Stelle ist eine Potenz von 2. Ein Bit ist eine binäre Stelle.

| Dezimal | Binär | Hex |
|---|---|---|
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 5 | 0101 | 5 |
| 10 | 1010 | A |
| 15 | 1111 | F |
| 16 | 0001 0000 | 10 |
| 255 | 1111 1111 | FF |

## Hexadezimal (Basis 16)

Ziffern 0 bis 9 und A bis F. Jede Hexstelle entspricht genau 4 Bit (einem Nibble). Zwei Hexstellen entsprechen einem Byte (8 Bit).

Schreibweise: 0xFF, 0x1A, #FF oder einfach FF je nach Kontext.

## Umrechnen

Binär zu Hex: vier Bit gruppieren, jede Gruppe als eine Hexstelle schreiben.

1010 1101 → A D → 0xAD

Hex zu Dezimal: jede Stelle mit ihrer Potenz von 16 multiplizieren und addieren.

0xAD = 10 × 16 + 13 = 173

:::tip
Potenzen von 2 auswendig kennen ist nützlich: 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024. Wer diese kennt, kann schnell im Kopf umrechnen.
:::
