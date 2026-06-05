---
title: Bussystem-Aktor
kategorie: EK
tags: [bussystem, knx, can, modbus, feldbus, smart-home, industrie, aktor, rs485, profibus]
symbol: —
einheit: —
---

Ein Bussystem-Aktor empfängt Steuerbefehle über ein Netzwerk (z.B. KNX, CAN, Modbus) und schaltet oder regelt damit eine Last. Er wird in der Gebäudeautomation und der Industrieautomatisierung eingesetzt, um viele Aktoren mit minimalem Verkabelungsaufwand zu steuern.

:::hbox
:::vbox
**Voraussetzungen**
- [[Aktorik]]
- [[Relais]]
:::
:::vbox
**Verwandte Artikel**
- [[Aktor mit Rückmeldung]]
:::
:::vbox
**Führt weiter zu**
- [[SPS-Grundlagen]]
:::
:::

---

## Warum Bussysteme?

In einfachen Schaltungen verbindet eine Steuerleitung direkt Steuerung und Aktor (Punkt-zu-Punkt). Bei vielen Aktoren wächst das Kabelnetz schnell auf ein unhandliches Mass. Ein Bussystem löst das: Alle Teilnehmer hängen an einer gemeinsamen Leitung und kommunizieren über Adressen.

:::formel
Bus-Leitung
  ├── Sensor 1   (Adresse 0x01)
  ├── Sensor 2   (Adresse 0x02)
  ├── Aktor 1    (Adresse 0x10) → Licht
  ├── Aktor 2    (Adresse 0x11) → Jalousie
  └── Aktor 3    (Adresse 0x12) → Heizventil
:::

---

## Wichtige Bussysteme

| Bus | Einsatz | Physikalisch |
|---|---|---|
| KNX | Gebäudeautomation | Twisted Pair, 29 V DC |
| DALI | Lichtsteuerung | Twisted Pair, eigenes Protokoll |
| Modbus RTU | Industrie | RS485 (2-Draht) |
| Modbus TCP | Industrie | Ethernet |
| CAN | Automotive, Industrie | Twisted Pair, differenziell |
| PROFIBUS | Industrie (älter) | RS485 |
| EtherCAT | Hochleistungs-CNC | Ethernet (Echtzeit) |
| Zigbee / Z-Wave | Smart-Home Funk | 868 MHz / 2,4 GHz, Mesh |

---

## KNX-Aktor

KNX-Aktoren sitzen auf der KNX-Busleitung (Twisted Pair, 29 V DC Busversorgung). Sie empfangen Telegramme vom Bus und schalten angeschlossene Verbraucher (230 V AC).

Typische KNX-Aktoren:
- Schaltaktor (1–8 Kanäle): Licht, Steckdosen
- Jalousieaktor: Rollladen hoch/runter/stopp
- Dimmaktor: Phasenabschnitt oder -anschnitt
- Heizungsaktor: 6-Kanal-Thermostatventil (0–10 V oder PWM)

Inbetriebnahme über ETS-Software (Engineering Tool Software). Physikalische Adresse und Gruppenadressierung werden projektspezifisch vergeben.

---

## Modbus-Aktor

Modbus ist ein einfaches Master-Slave-Protokoll. Der Master sendet Befehle, Aktoren (Slaves) führen sie aus und antworten. Modbus RTU läuft über RS485 (bis 1,2 km, bis 32 Teilnehmer ohne Repeater), Modbus TCP über Ethernet.

:::formel
Befehl: Write Single Coil
Adresse: 0x0010  → Aktor-Register "Ausgang 1"
Wert:    0xFF00  → EIN
:::

Fertige Modbus-Aktor-Module (z.B. 8-Kanal-Relaisboard mit RS485) sind günstig und sofort einsetzbar.

---

## CAN-Bus Aktor

CAN (Controller Area Network) ist für Zuverlässigkeit und Robustheit ausgelegt. Er wird im Fahrzeug (OBD, Motorsteuerung) und in der Industrie (CANopen) eingesetzt. Hohe Busauslastung bis 1 Mbit/s, kollisionsfreier Medienzugriff durch Prioritäten.

---

## Adressierung und Sicherheit

Bussystem-Aktoren sind netzwerkfähig und damit potenziell von aussen erreichbar.

:::warning
In industriellen Anlagen Modbus/CAN-Netzwerke nie direkt ans Internet anbinden. Keine Authentifizierung im Protokoll vorhanden. Immer durch Firewalls oder dedizierte Gateways absichern.
:::
