---
title: SPI
kategorie: SH
tags: [SPI, seriell, schnittstelle, MOSI, MISO, SCK, CS, mikrocontroller, CPOL, CPHA, daisy-chain, vollduplex, chip-select, synchron]
symbol: —
einheit: —
---

SPI (Serial Peripheral Interface) ist eine synchrone serielle Schnittstelle. Vier Leitungen, hohe Geschwindigkeit, kein Protokoll-Overhead. Standard für Displays, Flash-Speicher und Sensoren.

:::hbox
:::vbox
**Voraussetzungen**
- [[UART]]
:::
:::vbox
**Verwandte Artikel**
- [[I2C]]
- [[UART]]
:::
:::vbox
**Führt weiter zu**
- [[Mikrocontroller]]
:::
:::

---

## Leitungen

| Leitung | Richtung | Bedeutung |
|---|---|---|
| SCK | Master → Slave | Takt |
| MOSI | Master → Slave | Daten vom Master |
| MISO | Slave → Master | Daten vom Slave |
| CS / SS | Master → Slave | Chip Select, aktiv LOW |

Jeder Slave bekommt eine eigene CS-Leitung. Alle anderen teilen SCK, MOSI, MISO.

## Übertragung

Der Master erzeugt den Takt. Bei jedem Taktimpuls wird ein Bit gesendet und empfangen. Gleichzeitig, vollduplex.

Ein Byte braucht 8 Taktimpulse. Keine Startbits, keine Stoppbits.

:::waveform
labels: ,B3,,B2,,B1,,B0,,
CS:   1,0,0,0,0,0,0,0,0,1
SCK:  0,0,1,0,1,0,1,0,1,0
MOSI: 0,1,1,0,0,1,1,0,0,0
MISO: 0,0,0,1,1,1,1,0,0,0
:::

## Vergleich: UART, SPI, I2C

| Merkmal | UART | SPI | I2C |
|---|---|---|---|
| Taktung | Asynchron | Synchron | Synchron |
| Leitungen | 2 (TX, RX) | 4 (SCK, MOSI, MISO, CS) | 2 (SDA, SCL) |
| Teilnehmer | 1:1 | 1 Master, N Slaves (je 1 CS) | 1 Bus, bis 127 Slaves |
| Geschwindigkeit | 115 kBit/s typisch | 1–50 MBit/s | 100 kBit/s – 1 MBit/s |
| Pull-ups nötig? | Nein | Nein | Ja (SDA und SCL) |
| Elektrisch | Push-Pull | Push-Pull | Open-Drain |
| Adressierung | Keine (Punkt-zu-Punkt) | Über CS-Leitungen | 7-Bit-Adresse im Protokoll |

**Asynchron** (UART): Kein gemeinsamer Takt. Sender und Empfänger einigen sich vorher auf die Baudrate.  
**Synchron** (SPI, I2C): Eine Taktleitung (SCK / SCL) synchronisiert Sender und Empfänger.

## Geschwindigkeit

Viel schneller als UART und I2C. Typisch 1 bis 50 MBit/s, je nach IC und Leitungslänge.

## SPI Modi

Vier Modi (0 bis 3) definieren Taktpolarität (CPOL) und -phase (CPHA). Falsch eingestellter Modus: Kommunikation funktioniert nicht. Immer im Datenblatt des Slaves nachschauen.

| Modus | CPOL | CPHA | Takt im Ruhezustand | Abtastung |
|---|---|---|---|---|
| 0 | 0 | 0 | LOW | steigende Flanke |
| 1 | 0 | 1 | LOW | fallende Flanke |
| 2 | 1 | 0 | HIGH | fallende Flanke |
| 3 | 1 | 1 | HIGH | steigende Flanke |

:::tip
Daisy-Chaining: Mehrere SPI-Slaves können in Reihe geschaltet werden (MISO eines Slaves auf MOSI des nächsten). Alle teilen CS. Nützlich wenn die Anzahl CS-Pins begrenzt ist.
:::
