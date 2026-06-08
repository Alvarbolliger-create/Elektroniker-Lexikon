---
title: UART
kategorie: SH
tags: [UART, seriell, schnittstelle, baudrate, RS-232, kommunikation, TX, RX, parität, stoppbit, startbit, frame, USB-UART, FTDI, debug]
symbol: —
einheit: —
---

UART ist die einfachste serielle Schnittstelle. Zwei Leitungen, kein Takt, kein Protokoll-Overhead. Standard für Debug-Ausgaben und einfache Gerätekommunikation.

:::hbox
:::vbox
**Voraussetzungen**
- [[Digitale Codes]]
- [[Signale]]
:::
:::vbox
**Verwandte Artikel**
- [[SPI]]
- [[I2C]]
:::
:::vbox
**Führt weiter zu**
- [[RS-232 / RS-485]]
:::
:::

---

## Grundprinzip

Zwei Leitungen: TX (Senden) und RX (Empfangen). TX des einen Geräts geht auf RX des anderen, und umgekehrt. Kein gemeinsamer Takt.

Die Baudrate (Bits pro Sekunde) muss auf beiden Seiten gleich eingestellt sein.

## Rahmen (Frame)

Jedes Byte wird in einem Rahmen übertragen:

1. **Startbit**: Leitung zieht von HIGH auf LOW
2. **Datenbits**: 5 bis 9 Bit, meistens 8
3. **Paritätsbit**: optional, zur Fehlererkennung
4. **Stoppbit**: 1 oder 2 Bit, Leitung wieder HIGH

:::waveform
labels: Idle,Start,D0,D1,D2,D3,D4,D5,D6,D7,Par,Stop,Idle
TX: 1,0,1,0,1,1,0,1,0,1,0,1,1
:::

## Typische Baudraten

| Baudrate | Bits/s | Bytes/s (ca.) |
|---|---|---|
| 9600 | 9600 | 960 |
| 115200 | 115200 | 11520 |
| 1000000 | 1 MBit | 100000 |

## Pegel

UART-Pegel sind logische Pegel (3.3 V oder 5 V). RS-232 (der ältere Standard auf PC-Seite) verwendet ±12 V. Nie direkt verbinden, sonst wird der Mikrocontroller zerstört.

:::tip
UART ist der einfachste Weg für Debug-Ausgaben auf einem Mikrocontroller. Einfach einen USB-UART-Adapter anschliessen und mit einem seriellen Terminal lesen. Kein Debugger nötig.
:::

:::warning
TX und RX überkreuz verbinden: TX Gerät A auf RX Gerät B und umgekehrt. Das ist der häufigste Verdrahtungsfehler.
:::
