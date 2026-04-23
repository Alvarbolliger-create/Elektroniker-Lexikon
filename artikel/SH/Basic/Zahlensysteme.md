---
title: Zahlensysteme
kategorie: Grundlagen
tags: [Binär, Hex, Informatik]
---

# Mathematische Grundlagen

Computer arbeiten intern ausschließlich mit zwei Zuständen. Um diese für uns Menschen lesbar zu machen, nutzen wir verschiedene Zahlensysteme.

## Dezimalsystem (Basis 10)
Unser Alltagssystem mit den Ziffern 0-9.

## Dualsystem / Binärsystem (Basis 2)
Besteht nur aus **0** und **1**. Jede Stelle entspricht einer Zweierpotenz ($2^n$).

## Hexadezimalsystem (Basis 16)
Nutzt die Ziffern 0-9 und die Buchstaben A-F (A=10, B=11 ... F=15). Es ist sehr kompakt: Zwei Hex-Stellen können genau ein Byte (8 Bit) darstellen.

## Wichtige Begriffe
- **Bit:** Kleinste Einheit (0 oder 1).
- **Nibble:** 4 Bit (eine Hex-Ziffer).
- **Byte:** 8 Bit.
- **MSB:** Most Significant Bit (das höchstwertige Bit ganz links).
- **LSB:** Lowest Significant Bit (das niederwertigste Bit ganz rechts).

## Exkurs: C-Datentypen
In der Programmierung (z. B. C) hängen Datentypen direkt von der Bitbreite ab:
- `unsigned char`: 8 Bit, Bereich 0 bis 255.
- `char`: 8 Bit, Bereich -128 bis 127 (wegen des Vorzeichen-Bits).

---
**Siehe auch:**
- [[Signale]]
- [[Digitale Codes und Fehlererkennung]]