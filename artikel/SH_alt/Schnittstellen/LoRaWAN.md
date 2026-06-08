---
title: LoRaWAN
kategorie: SH
tags: [LoRa, LoRaWAN, LPWAN, IoT, reichweite, spreading factor, duty cycle, TTN, 868 MHz, chirp, gateway]
symbol: —
einheit: —
---

LoRaWAN ist ein Funksystem für sehr grosse Reichweiten bei sehr kleiner Sendeleistung. Geeignet für Sensoren die selten kleine Datenpakete senden.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale]]
- [[TCP/IP und MQTT]]
:::
:::vbox
**Verwandte Artikel**
- [[Bluetooth]]
:::
:::

---

## LoRa vs. LoRaWAN

**LoRa**: Die physikalische Funkschicht. Chirp Spread Spectrum Modulation. Sehr gut in Gebäuden und über weite Distanzen.

**LoRaWAN**: Das Protokoll auf LoRa. Definiert Netzwerkarchitektur, Adressierung, Sicherheit.

## Architektur

- **End-Geräte**: Sensoren und Aktoren mit LoRa-Modul
- **Gateways**: Empfangen Pakete und leiten an Network Server weiter (via IP)
- **Network Server**: Verwaltet Geräte, dedupliziert, leitet weiter
- **Application Server**: Empfängt Daten, verarbeitet

Ein Gateway kann hunderte von Geräten gleichzeitig empfangen.

## Spreading Factor (SF)

Der Spreading Factor bestimmt Reichweite und Datenrate:

| SF | Reichweite | Datenrate | Airtime |
|---|---|---|---|
| SF7 | kurz | hoch | kurz |
| SF12 | sehr weit | sehr niedrig | lang |

SF12 kann mehrere Kilometer überbrücken, sendet aber nur wenige Bytes pro Minute.

## Frequenzen

EU: 868 MHz. USA: 915 MHz. Lizenzfrei, aber Duty-Cycle-Beschränkung: in der EU max. 1 % Sendezeit pro Stunde in vielen Bändern.

## The Things Network (TTN)

Community-LoRaWAN-Netz mit Gateways weltweit. Kostenlos nutzbar für Prototyping und kleine Projekte. In Städten oft gute Abdeckung.

## Typische Anwendungen

Wasserstandsmessung, Parkplatzsensoren, Bodenfeuchtigkeit in der Landwirtschaft, Gasablesung, Tracking von Objekten.

:::tip
Für den Einstieg: RAK Wireless WisBlock oder TTGO LoRa32 sind günstige LoRaWAN-Entwicklungsboards mit integriertem Display und Akku-Laderegler.
:::
