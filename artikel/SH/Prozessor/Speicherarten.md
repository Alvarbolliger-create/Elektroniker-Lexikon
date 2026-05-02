---
title: Speicherarten
kategorie: SH
tags: [RAM, ROM, flash, SRAM, DRAM, EEPROM, speicher, nichtflüchtig, NOR-flash, NAND-flash, DDR, eMMC, SSD]
symbol: —
einheit: Byte
---

Digitale Systeme nutzen verschiedene Speichertypen mit unterschiedlichen Eigenschaften. Die Wahl hängt von Geschwindigkeit, Kapazität, Flüchtigkeit und Kosten ab.

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops]]
- [[CPU Aufbau]]
:::
:::vbox
**Verwandte Artikel**
- [[Mikrocontroller]]
- [[AD/DA Grundlagen]]
:::
:::

---

## Flüchtig vs. nichtflüchtig

**Flüchtig**: Inhalt geht beim Abschalten verloren. Braucht ständig Strom zum Halten.  
**Nichtflüchtig**: Inhalt bleibt ohne Strom erhalten.

## SRAM (Static RAM)

Flüchtig. Jede Speicherzelle aus 6 Transistoren (Flipflop). Sehr schnell, kein Auffrischen nötig. Teuer und gross. Einsatz: Cache, kleine Puffer, interne Register-Dateien.

## DRAM (Dynamic RAM)

Flüchtig. Jede Zelle aus 1 Transistor + 1 Kondensator. Muss regelmässig aufgefrischt werden (Refresh). Viel dichter als SRAM, günstiger. Einsatz: Haupt-RAM in Computern (DDR4, DDR5).

## Flash

Nichtflüchtig. Elektrisch löschbar und programmierbar. Daten bleiben ohne Strom. Begrenzte Schreibzyklen (typisch 10.000-100.000 mal).

**NOR-Flash**: Direkter Zugriff auf jede Adresse, wie RAM. Für Programmcode. Kleiner, teurer.  
**NAND-Flash**: Seitenweiser Zugriff. Für Massendaten. Günstiger, höhere Kapazität. Basis für SSDs, SD-Karten, eMMC.

## EEPROM

Elektrisch löschbar, byteweise schreibbar. Sehr langsam beim Schreiben. Wenige KB Kapazität. Einsatz: Konfigurationsdaten, Kalibrierwerte, die selten geändert werden.

## ROM

Einmal beschrieben, dann nur lesbar. Heutzutage kaum noch separat verwendet. Ersetzte durch Flash.

## Im Mikrocontroller

Typischer MCU-Aufbau:
- Flash: Programmspeicher (16 kB bis mehrere MB)
- SRAM: Arbeitsspeicher (2 kB bis 512 kB)
- EEPROM: Konfigurationsdaten (optional, 0.5-4 kB)
