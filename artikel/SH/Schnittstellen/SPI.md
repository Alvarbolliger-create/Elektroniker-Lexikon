---
title: SPI
kategorie: SH
kapitel: Schnittstellen
tags: [spi, serial peripheral interface, mosi, miso, sclk, chip select, master slave]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Serielle Datenübertragung (Grundlagen)]]
:::
:::vbox
**Verwandte Artikel**
- [[I2C]]
- [[Protokoll-Decoder]]
- [[Logikanalysator]]
:::
:::

---

→ [[UART|UART]] verbindet immer nur zwei Geräte direkt miteinander — und das auch noch ohne gemeinsamen Takt, was eine genaue Abstimmung der Baudrate erfordert. Für Anwendungen, die hohe Geschwindigkeit und mehrere angeschlossene Bausteine brauchen — Displays, Flash-Speicher, Sensoren — hat sich eine andere Schnittstelle durchgesetzt: **SPI** (Serial Peripheral Interface), eine **synchrone** serielle Schnittstelle mit eigener Taktleitung.

## Vier Leitungen mit klarer Aufgabenteilung

:::merke
SPI verwendet vier Leitungen mit klar getrennten Aufgaben:

| Leitung | Richtung | Bedeutung |
|---|---|---|
| SCK | Master → Slave | Takt |
| MOSI | Master → Slave | Daten vom Master (Master Out, Slave In) |
| MISO | Slave → Master | Daten vom Slave (Master In, Slave Out) |
| CS / SS | Master → Slave | Chip Select, aktiv LOW |

Der **Master** erzeugt den gemeinsamen Takt SCK — genau das ist der entscheidende Unterschied zu UART: Weil beide Seiten exakt im selben Rhythmus arbeiten, ist keine Vereinbarung über eine Baudrate nötig, und es entsteht auch keine Drift, die aufsynchronisiert werden müsste. Bei jedem Taktimpuls wird gleichzeitig ein Bit gesendet **und** empfangen — die Übertragung läuft also **vollduplex**. Ein Byte braucht damit genau acht Taktimpulse, ganz ohne Start- oder Stoppbits.
:::

## Mehrere Slaves an einem Bus: jeder bekommt seine eigene Leitung

:::tip
SCK, MOSI und MISO werden von allen angeschlossenen Bausteinen gemeinsam genutzt. Damit der Master trotzdem gezielt mit einem bestimmten Baustein kommunizieren kann, bekommt **jeder Slave eine eigene CS-Leitung** (Chip Select, aktiv LOW). Nur der Slave, dessen CS-Leitung gerade auf LOW gezogen wird, "hört zu" und antwortet — alle anderen ignorieren den Datenverkehr auf dem Bus vollständig. Diese Lösung ist denkbar einfach, hat aber einen Haken: Bei vielen Slaves braucht man entsprechend viele freie GPIO-Pins am Mikrocontroller.

Eine elegante Alternative bei begrenzter Pin-Anzahl ist das **Daisy-Chaining**: Die Slaves werden in Reihe geschaltet, wobei der MISO-Ausgang des einen auf den MOSI-Eingang des nächsten geführt wird. Alle Slaves teilen sich dann eine gemeinsame CS-Leitung — die Daten "wandern" wie auf einem Förderband von einem Baustein zum nächsten.
:::

## Die vier SPI-Modi: Taktpolarität und -phase

:::warning
Bevor zwei SPI-Bausteine zusammenarbeiten können, müssen sie sich auf denselben **Modus** einigen — definiert durch die Taktpolarität CPOL (Ruhepegel des Takts) und die Taktphase CPHA (an welcher Flanke abgetastet wird). Es gibt vier Kombinationen:

| Modus | CPOL | CPHA | Takt im Ruhezustand | Abtastung |
|---|---|---|---|---|
| 0 | 0 | 0 | LOW | steigende Flanke |
| 1 | 0 | 1 | LOW | fallende Flanke |
| 2 | 1 | 0 | HIGH | fallende Flanke |
| 3 | 1 | 1 | HIGH | steigende Flanke |

Ist der Modus falsch eingestellt, funktioniert die Kommunikation überhaupt nicht — die Bits werden zur falschen Zeit abgetastet und ergeben nur "Datenmüll". Der korrekte Modus für einen bestimmten Baustein steht immer in dessen Datenblatt und muss dort nachgeschlagen werden.
:::

## Geschwindigkeit: die Königsdisziplin unter den seriellen Schnittstellen

:::info
SPI ist deutlich schneller als UART und → [[I2C|I2C]] — typisch sind 1 bis 50 Mbit/s, je nach IC und Leitungslänge. Der Grund liegt in der einfachen, synchronen Architektur ohne Protokoll-Overhead: keine Adressierung, keine Start- und Stoppbits, kein Handshake — nur ein gemeinsamer Takt und zwei Datenleitungen, die vollduplex arbeiten. Diese Schlankheit macht SPI zur ersten Wahl überall dort, wo grosse Datenmengen schnell übertragen werden müssen, etwa bei Displays, Kameramodulen oder externen Flash-Speichern.
:::

## SPI im Vergleich zu UART und I2C

| Merkmal | UART | SPI | I2C |
|---|---|---|---|
| Taktung | Asynchron | Synchron | Synchron |
| Leitungen | 2 (TX, RX) | 4 (SCK, MOSI, MISO, CS) | 2 (SDA, SCL) |
| Teilnehmer | 1:1 | 1 Master, N Slaves (je 1 CS) | 1 Bus, bis 127 Slaves |
| Geschwindigkeit | 115 kBit/s typisch | 1–50 MBit/s | 100 kBit/s – 1 MBit/s |
| Pull-ups nötig? | Nein | Nein | Ja (SDA und SCL) |
| Elektrisch | Push-Pull | Push-Pull | Open-Drain |
| Adressierung | Keine (Punkt-zu-Punkt) | Über CS-Leitungen | 7-Bit-Adresse im Protokoll |

Diese Tabelle macht den grundsätzlichen Zielkonflikt sichtbar: SPI tauscht **Geschwindigkeit gegen Verdrahtungsaufwand** — vier Leitungen plus eine pro Slave. Wer stattdessen mit minimalem Verdrahtungsaufwand auskommen und dabei viele Teilnehmer an denselben zwei Leitungen betreiben will, greift zu jener Schnittstelle, die im nächsten Artikel vorgestellt wird: → [[I2C|I2C]].
