---
title: R-2R Netzwerk (DAC)
kategorie: SH
tags: [R-2R, DAC, digital-analog, widerstandsnetzwerk, MSB, LSB, PWM, audio, GPIO]
symbol: —
einheit: —
---

Das R-2R-Netzwerk ist die einfachste Methode einen DAC mit diskreten Widerständen aufzubauen. Es braucht nur zwei Widerstandswerte, egal wie viele Bits.

:::hbox
:::vbox
**Voraussetzungen**
- [[AD/DA Grundlagen]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Sukzessive Approximation]]
:::
:::

---

## Aufbau

Das Netzwerk besteht aus Widerständen R und 2R in einer Leiterstruktur. Jedes Bit steuert einen Schalter der das entsprechende 2R-Glied entweder mit Vref oder GND verbindet.

```
Bit3 --2R-- +--2R-- +--2R-- +--2R-- Ausgang
             |       |       |
             R       R       R
             |       |       |
            GND     GND     GND
```

## Wirkungsprinzip

Durch die R-2R-Struktur liefert jedes Bit genau die Hälfte des Strombeitrags des nächsthöheren Bits. MSB liefert Vref/2, das nächste Bit Vref/4, und so weiter.

Die Ausgangsspannung ist:

```
U_aus = Vref × (Bit_n-1 × 2^(n-1) + ... + Bit_0 × 2^0) / 2^n
```

## Vorteile

- Nur zwei Widerstandswerte nötig
- Einfach zu verstehen und aufzubauen
- Keine getakteten Elemente nötig

## Nachteile

- Genauigkeit hängt stark von der Widerstandstoleranz ab
- Bei 8-Bit braucht man bereits 15 Widerstände mit <0.1 % Toleranz
- Für hohe Auflösungen besser integrierte DACs verwenden

## Anwendung

In einfachen Schaltungen mit Mikrocontrollern: 4-8 GPIO-Pins treiben ein R-2R-Netzwerk und erzeugen ein analoges Audiosignal oder eine variable Referenzspannung.
