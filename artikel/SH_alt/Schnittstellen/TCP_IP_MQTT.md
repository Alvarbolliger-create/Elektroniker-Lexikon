---
title: TCP/IP und MQTT
kategorie: SH
tags: [TCP, IP, UDP, MQTT, IoT, protokoll, socket, broker, QoS, publish-subscribe, ESP32, mosquitto, 3-way-handshake]
symbol: —
einheit: —
---

TCP/IP ist das Fundament des Internets. MQTT ist ein leichtgewichtiges Nachrichtenprotokoll für IoT-Geräte, das auf TCP/IP aufbaut.

:::hbox
:::vbox
**Voraussetzungen**
- [[Ethernet]]
- [[Mikrocontroller]]
:::
:::vbox
**Verwandte Artikel**
- [[Bluetooth]]
- [[LoRaWAN]]
:::
:::

---

## IP (Internet Protocol)

IP ist die Adressierungsschicht. Jedes Gerät hat eine IP-Adresse (z.B. 192.168.1.42). IP-Pakete werden unabhängig geroutet, können verloren gehen oder in falscher Reihenfolge ankommen.

## TCP (Transmission Control Protocol)

TCP läuft über IP und fügt hinzu:
- Verbindungsaufbau (3-Way-Handshake)
- Bestätigung und Wiederholung verlorener Pakete
- Korrekte Reihenfolge
- Flusskontrolle

Zuverlässig aber mit Overhead. Für Web, E-Mail, Dateiübertragung.

## UDP (User Datagram Protocol)

Kein Verbindungsaufbau, keine Bestätigung. Schneller, aber unzuverlässig. Nützlich wenn ein verlorenes Paket weniger schlimm ist als Verzögerung: Videostreaming, DNS, VoIP.

## MQTT

MQTT (Message Queuing Telemetry Transport) ist ein Publish-Subscribe-Protokoll über TCP.

Prinzip:
- **Broker**: Zentraler Server (z.B. Mosquitto, HiveMQ)
- **Publisher**: Sendet Nachrichten zu einem Topic
- **Subscriber**: Empfängt Nachrichten eines Topics

Beispiel: Temperatursensor publiziert `haus/wohnzimmer/temperatur = 22.5`. Ein Display subscribed dasselbe Topic und zeigt 22.5 an.

MQTT braucht sehr wenig Bandbreite und Energie. Ideal für batteriebetriebene IoT-Geräte.

## QoS-Level in MQTT

| Level | Garantie |
|---|---|
| 0 | Einmal senden, kein Nachweis |
| 1 | Mindestens einmal, Duplikate möglich |
| 2 | Genau einmal, kein Duplikat |

## In der Praxis

Arduino/ESP32 mit PubSubClient-Bibliothek. Raspberry Pi mit Paho MQTT. Broker auf Raspberry Pi oder in der Cloud (AWS IoT, Azure IoT Hub).
