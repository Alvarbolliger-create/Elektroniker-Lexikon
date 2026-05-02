---
title: Protokoll-Decoder
kategorie: MT
tags: [protokoll, decoder, UART, SPI, I2C, oszilloskop, logikanalysator, JTAG, saleae, CAN, LIN]
symbol: —
einheit: —
---

Protokoll-Decoder übersetzen digitale Signalverläufe in lesbare Daten. Was als 0-1-Folge aus dem Messsystem kommt, erscheint als Bytes, Adressen oder Klartext.

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikanalysator]]
- [[Oszilloskop: Aufbau & Bedienung]]
- [[UART]]
- [[SPI]]
- [[I2C]]
:::
:::vbox
**Verwandte Artikel**
- [[CAN-Bus]]
:::
:::

---

## Im Oszilloskop

Moderne Digitaloszilloskope (DSO) haben Protokoll-Decoder eingebaut oder als Option. Konfiguration am Beispiel UART:

1. Kanal wählen, Schwellwert einstellen (typisch 1.5 V für 3.3-V-Logik)
2. Baudrate eingeben oder automatisch erkennen lassen
3. Parität, Datenbits, Stoppbits einstellen
4. Dekodierte Bytes erscheinen als Overlay über dem Signal

Vorteil: Zusammen mit dem Analogsignal sichtbar. Ideal um Signalqualität und Datenwert gleichzeitig zu beurteilen.

## Im Logikanalysator

Logikanalysatoren wie Saleae Logic oder PulseView (sigrok) dekodieren auf einem PC. Die Software erkennt viele Protokolle automatisch:

- UART, SPI, I2C, CAN, LIN
- 1-Wire, Dallas DS18B20
- SMBus, PMBus
- JTAG, SWD
- WS2812 (LED-Protokoll)
- Modbus, DMX

Die dekodierten Werte können exportiert werden (CSV, binär).

## SPI-Dekodierung: Fallstrick

SPI hat keine feste Schnittstellen-Definition für Taktpolarität und Phase (CPOL/CPHA). Beim Einrichten immer im Datenblatt des Zielbauteils nachschlagen.

Falsches CPOL/CPHA liefert zwar einen Bitstrom, aber falschen Inhalt.

## I2C: Adresserkennung

I2C-Decoder zeigen Adresse und R/W-Bit separat an. Nützlich um zu prüfen welche Adressen auf dem Bus aktiv sind. Bei Adresskonflikten (zwei Geräte mit gleicher Adresse) hilft der Decoder sofort.

:::tip
PulseView mit einem günstigen FX2-Logikanalysator dekodiert die meisten Protokolle kostenlos. Für SPI-Flash-Bausteine gibt es sogar Decoder die den Flash-Inhalt direkt auslesen und anzeigen.
:::
