---
title: Synchrone Zähler
kategorie: SH
tags: [zähler, synchron, flipflop, takt, glitch-frei, binärzähler, 74HC163, 74HC193, modulo, up-down, PWM, JK-flipflop]
symbol: —
einheit: —
---

Bei synchronen Zählern werden alle Flipflops gleichzeitig vom selben Takt gesteuert. Kein Ripple, keine Glitches. Besser für schnelle und präzise Schaltungen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Asynchrone Zähler]]
:::
:::vbox
**Verwandte Artikel**
- [[Schieberegister]]
:::
:::vbox
**Führt weiter zu**
- [[FPGA]]
:::
:::

---

## Unterschied zu asynchronen Zählern

Beim asynchronen Zähler taktet jeder Ausgang das nächste Flipflop. Die Bits schalten nacheinander, mit Verzögerung.

Beim synchronen Zähler erhalten alle Flipflops denselben Takt. Logik vor jedem Flipflop entscheidet ob es schaltet oder nicht. Alle Bits wechseln gleichzeitig.

## Vorwärtszähler (synchron)

Das erste Flipflop toggelt immer. Das zweite toggelt wenn Q0 = 1. Das dritte wenn Q0 und Q1 = 1. Das vierte wenn Q0, Q1 und Q2 = 1.

Das ergibt einen klaren Binärzähler ohne Zwischenzustände.

## Rückwärtszähler

Selbes Prinzip, aber mit invertierten Ausgängen (Q_quer) für die UND-Bedingungen.

## Vor- und Rückwärtszähler

Ein steuerbares Signal (UP/DOWN) wählt ob Q oder Q_quer für die Bedingungen verwendet wird. Standard-Zähler-ICs wie der 74HC193 implementieren das.

## Anwendungen

Zeitgeber, Frequenzteiler, Adressgeneratoren in Speicher-Controllern, Zustands-Automaten (FSM), PWM-Erzeugung.

## ICs

74HC163 (4-Bit, synchrones Rücksetzen), 74HC193 (Vor-/Rückwärtszähler), CD4017 (Dezimalzähler mit Dekodierung).
