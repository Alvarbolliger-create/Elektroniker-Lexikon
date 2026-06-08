---
title: Ethernet
kategorie: SH
tags: [ethernet, TCP/IP, MAC, PHY, LAN, RJ45, SPE, EtherCAT, PROFINET, lwIP, W5500, industrial ethernet]
symbol: —
einheit: Mbit/s
---

Ethernet ist der Standard für kabelgebundene lokale Netzwerke. In der Industrie und Embedded-Welt wird es für Hochgeschwindigkeitskommunikation zwischen Geräten eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[UART]]
- [[TCP/IP und MQTT]]
:::
:::vbox
**Verwandte Artikel**
- [[TCP/IP und MQTT]]
- [[CAN-Bus]]
:::
:::

---

## MAC und PHY

**MAC (Media Access Control)**: Verwaltet den Zugriff auf das Medium, bildet Frames, prüft CRC. Meist integriert in MCU oder SoC.

**PHY (Physical Layer)**: Wandelt digitale Signale in das Leitungsformat um (Manchester, PAM4 etc.) und umgekehrt. Externer Chip, verbunden über MII, RMII oder RGMII.

## Ethernet-Varianten

| Standard | Geschwindigkeit | Kabel |
|---|---|---|
| 10BASE-T | 10 Mbit/s | Cat3 |
| 100BASE-TX | 100 Mbit/s | Cat5 |
| 1000BASE-T | 1 Gbit/s | Cat5e |
| 10GBASE-T | 10 Gbit/s | Cat6a |

**Single Pair Ethernet (SPE)**: 10BASE-T1L für Industrie und Feldgeräte. Nur ein Adernpaar, lange Distanzen.

## Frame-Aufbau

Ein Ethernet-Frame enthält:
- Präambel (Synchronisation)
- Ziel-MAC (6 Byte)
- Quell-MAC (6 Byte)
- EtherType (2 Byte, z.B. 0x0800 = IPv4)
- Payload (46-1500 Byte)
- CRC (4 Byte)

## In Embedded-Systemen

Viele MCUs haben integrierten Ethernet-MAC (STM32F4/F7, ESP32). Externer PHY nötig (z.B. LAN8720, KSZ8081). Software-Stack: lwIP (leichtgewichtig), FreeRTOS+TCP.

## Industrial Ethernet

EtherCAT, PROFINET, EtherNet/IP basieren auf Standard-Ethernet-Hardware, nutzen aber eigene Protokolle für Echtzeit-Kommunikation.

:::tip
Für Einsteiger: Der W5500 von Wiznet ist ein SPI-Ethernet-Controller mit eingebautem TCP/IP-Stack. Kein MAC/PHY-Thema, einfacher Einstieg für Mikrocontroller ohne Ethernet-MAC.
:::
