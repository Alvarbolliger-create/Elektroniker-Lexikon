---
title: Bluetooth
kategorie: SH
tags: [bluetooth, BLE, classic, GATT, GAP, profile, 2.4 GHz, nRF52840, advertising, beacon, A2DP, SPP]
symbol: —
einheit: —
---

Bluetooth ist ein Kurzstrecken-Funkstandard bei 2.4 GHz. Bluetooth Classic für Audio, BLE (Bluetooth Low Energy) für batteriebetriebene Sensoren und IoT.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale]]
- [[Mikrocontroller]]
:::
:::vbox
**Verwandte Artikel**
- [[LoRaWAN]]
- [[TCP/IP und MQTT]]
:::
:::

---

## Classic vs. BLE

**Bluetooth Classic**: Für kontinuierliche Datenübertragung. Audio-Profile (A2DP), Seriell (SPP), Headset. Höherer Strombedarf.

**BLE (Bluetooth Low Energy)**: Für sporadische kleine Datenpakete. Sensoren, Beacons, Wearables. Jahrelanger Batteriebetrieb möglich. Nicht kompatibel mit Classic für Audioprofile.

## BLE Architektur

**GAP (Generic Access Profile)**: Definiert Rollen und Verbindungsaufbau.
- **Peripheral**: Sendet Advertising-Pakete, wartet auf Verbindung (Sensor, Wearable)
- **Central**: Scannt und verbindet sich (Smartphone, Gateway)

**GATT (Generic Attribute Profile)**: Definiert wie Daten organisiert sind.
- **Service**: Gruppe von zusammengehörigen Charakteristiken (z.B. "Heart Rate Service")
- **Characteristic**: Einzelner Datenpunkt mit Wert, Beschreibung und Eigenschaften (Read/Write/Notify)

## Advertising

Ein BLE-Gerät im Advertising-Modus sendet alle paar Millisekunden ein kleines Paket (31 Byte). Darin können Gerätename, UUID und kleine Datenpakete enthalten sein. Beacons funktionieren oft nur im Advertising-Modus ohne Verbindung.

## Module

- **HC-05/HC-06**: Günstige Classic-Module, serieller Durchschleifer
- **HM-10**: BLE-Modul, einfache AT-Befehle
- **nRF52840**: Leistungsfähiger SoC mit ARM + BLE, Zigbee, USB

## Reichweite

Im Freien 10-100 m je nach Sendeleistung. In Gebäuden weniger. BLE Long Range (Coded PHY) bis zu 300 m.
