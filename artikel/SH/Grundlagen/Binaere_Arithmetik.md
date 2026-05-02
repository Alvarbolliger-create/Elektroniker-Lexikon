---
title: Binäre Arithmetik
kategorie: SH
tags: [binär, addition, zweierkomplement, überlauf, ALU, subtraktion, carry, overflow, MSB, vorzeichen, shift, einerkomplement]
symbol: —
einheit: —
---

Digitale Schaltungen rechnen im Binärsystem. Die Regeln sind dieselben wie bei der Dezimalrechnung, nur mit zwei Ziffern.

:::hbox
:::vbox
**Voraussetzungen**
- [[Zahlensysteme]]
- [[Logikgatter]]
:::
:::vbox
**Verwandte Artikel**
- [[Digitale Codes]]
- [[Schaltalgebra]]
:::
:::vbox
**Führt weiter zu**
- [[CPU Aufbau]]
- [[Digitale Codes]]
:::
:::

---

## Binäre Addition

```
  0 + 0 = 0
  0 + 1 = 1
  1 + 0 = 1
  1 + 1 = 0, Übertrag 1
```

Beispiel 8-Bit: 0b00110101 (53) + 0b00001110 (14) = 0b01000011 (67)

Der Übertrag (Carry) wandert von Stelle zu Stelle, genau wie beim Dezimalrechnen.

## Zweierkomplement

Negative Zahlen werden im Zweierkomplement dargestellt. Das ermöglicht, dieselbe Additionsschaltung für positive und negative Zahlen zu nutzen.

Bildung des Zweierkomplements:
1. Alle Bits invertieren (Einerkomplement)
2. 1 addieren

Beispiel für -5 in 8 Bit:
- +5 = 0b00000101
- Invertiert = 0b11111010
- +1 = 0b11111011

Das MSB (höchstes Bit) zeigt das Vorzeichen: 0 = positiv, 1 = negativ.

Wertebereich bei 8 Bit: -128 bis +127.

## Überlauf

Wenn das Ergebnis einer Rechnung den darstellbaren Bereich überschreitet, entsteht ein Überlauf. Das Ergebnis ist falsch, aber es gibt kein automatisches Fehlersignal.

In Hardware wird der Carry-Out und das Overflow-Flag gesetzt. Software muss diese Flags prüfen wenn es darauf ankommt.

## Subtraktion

Subtraktion wird als Addition des Zweierkomplements ausgeführt:
```
A - B = A + (-B) = A + (~B + 1)
```

Eine ALU braucht damit nur einen Addierer, keinen separaten Subtrahierer.

## Shift-Operationen

Links-Shift (`<<`) multipliziert mit 2. Rechts-Shift (`>>`) dividiert durch 2.

Schneller als eine echte Multiplikation, daher häufig in Mikrocontroller-Code genutzt.
