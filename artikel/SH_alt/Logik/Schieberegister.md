---
title: Schieberegister
kategorie: SH
tags: [schieberegister, SIPO, PISO, 74HC595, seriell, parallel, shift register, daisy-chain, 74HC165, latch, SPI]
symbol: —
einheit: —
---

Ein Schieberegister wandelt serielle in parallele Daten oder umgekehrt. Es erweitert die I/O-Anzahl eines Mikrocontrollers mit wenigen Pins.

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops]]
- [[Logikgatter]]
:::
:::vbox
**Verwandte Artikel**
- [[SPI]]
- [[Asynchrone Zähler]]
:::
:::

---

## Grundprinzip

Flipflops in Reihe: Der Ausgang des ersten ist der Eingang des zweiten. Mit jedem Taktpuls wandert das Datenmuster eine Stelle weiter.

## SIPO (Serial In, Parallel Out)

Serielle Daten werden eingetaktet, alle Ausgänge gleichzeitig gelesen. Einsatz: Mehr Ausgänge an wenigen Pins (z.B. LED-Matrizen).

**74HC595**: Weit verbreiteter 8-Bit-SIPO. Drei Steuerpins (Data, Clock, Latch). Bis zu acht Chips in Reihe für 64 Ausgänge an drei MCU-Pins.

## PISO (Parallel In, Serial Out)

Parallele Eingänge werden eingelesen und seriell ausgegeben. Einsatz: Mehr Eingänge an wenigen Pins (z.B. Tasten).

**74HC165**: Komplementäres IC zum 74HC595.

## Bidirektional

Manche Schieberegister können in beide Richtungen schieben (links, rechts). Nützlich für arithmetische Shifts und bestimmte Signalverarbeitungsoperationen.

## SPI als Schieberegister

SPI ist prinzipiell ein Schieberegister-Protokoll. Der Master sendet Bits seriell, der Slave nimmt sie auf. Ein 74HC595 kann direkt über SPI angesteuert werden (MOSI = Data, SCK = Clock, CS = Latch).

## Anwendungsbeispiel

8 LEDs an einem 74HC595:
- Data-Pin → MCU GPIO
- Clock-Pin → MCU GPIO  
- Latch-Pin → MCU GPIO
- 8 LED-Ausgänge mit je einem Vorwiderstand

Pro Schieberegister: 3 MCU-Pins für 8 Ausgänge. Mit Daisy-Chaining: 3 Pins für beliebig viele Ausgänge.
