---
title: I2C
kategorie: SH
tags: [I2C, seriell, schnittstelle, SDA, SCL, adresse, bus, open-drain, pull-up, ACK, start-condition, 7-bit, EEPROM, sensor]
symbol: —
einheit: —
---

I2C (Inter-Integrated Circuit) verbindet viele Geräte mit nur zwei Leitungen. Jeder Teilnehmer hat eine Adresse. Typisch für Sensoren, EEPROMs und Displays auf kurzen Strecken.

:::hbox
:::vbox
**Voraussetzungen**
- [[UART]]
:::
:::vbox
**Verwandte Artikel**
- [[SPI]]
- [[UART]]
:::
:::vbox
**Führt weiter zu**
- [[Embedded Software]]
:::
:::

---

## Leitungen

Nur zwei: SDA (Daten) und SCL (Takt). Beide sind bidirektional und benötigen Pull-up-Widerstände nach VCC.

Alle Geräte hängen parallel am selben Bus. Adressierung unterscheidet sie.

## Adressierung

Jeder Slave hat eine 7-Bit-Adresse (0x00 bis 0x7F). Der Master schickt die Adresse zu Beginn jeder Transaktion. Nur der angesprochene Slave antwortet.

Manche Adressen sind reserviert. Einige ICs erlauben die Adresse per Pin zu konfigurieren, sodass mehrere gleiche ICs am Bus hängen können.

## Übertragungsablauf

1. Start-Condition (SDA fällt während SCL HIGH)
2. 7-Bit Adresse + R/W-Bit
3. ACK vom Slave
4. Datenbytes, je mit ACK
5. Stop-Condition

:::waveform
labels: Idle,Start,A3,,A2,,A1,,A0,,ACK,,Stop
SCL: 1,1,0,1,0,1,0,1,0,1,0,1,1
SDA: 1,0,1,1,0,0,1,1,0,0,0,0,1
:::

## Geschwindigkeit

Standard: 100 kBit/s. Fast: 400 kBit/s. Fast-Plus: 1 MBit/s. High-Speed: 3.4 MBit/s (selten).

Viel langsamer als SPI, aber dafür nur zwei Leitungen und viele Teilnehmer möglich.

## Pull-up-Widerstände

Ohne Pull-ups funktioniert I2C nicht. Typisch 4.7 kΩ bei 100 kHz, 2.2 kΩ bei 400 kHz.

Zu grosse Widerstände: Flanken werden langsam, bei hohen Frequenzen versagt die Kommunikation. Zu kleine: höherer Strom, aber schnellere Flanken.

:::warning
Adresskonflikte erkennen: Wenn zwei Slaves dieselbe Adresse haben, kollisionieren beide Antworten auf dem Bus. Die Kommunikation schlägt fehl. Adressen aller Busteilnehmer immer prüfen.
:::
