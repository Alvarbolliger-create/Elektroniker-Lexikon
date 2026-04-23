---
title: Binäre Arithmetik
kategorie: Grundlagen
tags: [Rechnen, Mathe, CPU]
---

# Wie Computer rechnen

Die binäre Arithmetik bildet die Grundlage für die Rechenwerke (ALU) in Prozessoren.

## Addition
Die Regeln sind simpel, ähneln aber dem dezimalen schriftlichen Addieren:
- $0 + 0 = 0$
- $0 + 1 = 1$
- $1 + 1 = 0$ (Übertrag 1)
- $1 + 1 + 1 = 1$ (Übertrag 1)

## Halbaddierer & Volladdierer
- **Halbaddierer:** Addiert zwei Bits ($A, B$) und liefert Summe ($S$) und Übertrag ($C$).
- **Volladdierer:** Besitzt zusätzlich einen Eingang für den Übertrag der vorherigen Stelle ($C_{in}$). Dies ermöglicht das Hintereinanderschalten für größere Bitbreiten.

## Zweierkomplement
Um negative Zahlen darzustellen, nutzt man das Zweierkomplement:
1. Alle Bits invertieren (Einerkomplement).
2. Den Wert 1 addieren.
*Vorteil:* Man kann Subtraktionen einfach als Additionen mit negativen Zahlen durchführen ($A - B = A + (-B)$).

## Overflow (Überlauf)
Ein Überlauf tritt auf, wenn das Ergebnis einer Rechnung die verfügbare Bitbreite (z.B. 8 Bit) überschreitet und das Vorzeichen dadurch verfälscht wird.

---
**Siehe auch:**
- [[Logikgatter]]
- [[Computerarchitektur]]