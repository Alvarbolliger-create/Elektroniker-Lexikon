---
title: Digitale Codes
kategorie: Codierung
tags: [ASCII, BCD, Sicherheit]
---

# Darstellung von Informationen

Daten müssen so codiert werden, dass sie effizient übertragen oder sicher gespeichert werden können.

## Gewichtete Codes
- **BCD-Code (Binary Coded Decimal):** Jede Dezimalziffer (0-9) wird einzeln durch 4 Bit (ein Nibble) dargestellt. Werte über 9 nennt man **Pseudotetraden** (ungültig).
- **Excess-3-Code:** Ein BCD-Code, bei dem zu jeder Ziffer 3 addiert wird. Er ist symmetrisch und erleichtert das Bilden des Komplements.

## Einschrittige Codes
- **Gray-Code:** Zwischen zwei aufeinanderfolgenden Werten ändert sich immer nur **genau ein Bit**. 
*Nutzen:* Verhindert Einlesefehler bei mechanischen Sensoren (z.B. Drehgebern).

## Alphanumerische Codes
- **ASCII:** 7-Bit Code für lateinische Buchstaben und Steuerzeichen.
- **Unicode (UTF-8):** Ein variabler Code, der fast alle Schriftzeichen der Welt (inkl. Emojis) umfasst.

## Fehlererkennung
- **Paritätsbit:** Ein zusätzliches Bit wird angehängt, um die Anzahl der Einsen auf "gerade" oder "ungerade" zu ergänzen. Erkennt 1-Bit-Fehler.
- **Hamming-Code:** Ein spezielles Verfahren, das Fehler nicht nur erkennt, sondern 1-Bit-Fehler sogar selbstständig **korrigieren** kann.

---
**Siehe auch:**
- [[Zahlensysteme]]
- [[Codewandler und Anzeigen]]