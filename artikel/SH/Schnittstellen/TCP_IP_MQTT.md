---
title: TCP/IP & MQTT
kategorie: SH
kapitel: Schnittstellen
tags: [tcp/ip, mqtt, protokoll, internet, broker, publish subscribe]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Ethernet]]
:::
:::

---

→ [[Ethernet|Ethernet]] sorgt dafür, dass Datenpakete zuverlässig innerhalb eines lokalen Netzwerks von Gerät zu Gerät gelangen — über MAC-Adressen und Frames. Doch das Internet besteht aus Millionen solcher Netzwerke, die weltweit miteinander verbunden sind. Damit ein Datenpaket den Weg von einem Mikrocontroller in der Schweiz zu einem Server irgendwo auf der anderen Seite der Welt findet — und damit Anwendungen sich sinnvoll über diese Strecke unterhalten können — braucht es zusätzliche Protokollschichten: **TCP/IP** als Transport-Fundament des Internets und **MQTT** als schlankes Anwendungsprotokoll, das speziell auf die Bedürfnisse von IoT-Geräten zugeschnitten ist.

## IP-Adressierung: jedes Gerät bekommt eine eindeutige Anschrift

:::merke
Damit ein Datenpaket sein Ziel im weltweiten Netzwerk der Netzwerke findet, braucht jedes Gerät eine eindeutige **IP-Adresse** — vergleichbar mit einer Postanschrift. Bei **IPv4** besteht sie aus vier Zahlenblöcken (z. B. 192.168.1.42), bei **IPv6** aus einer deutlich längeren hexadezimalen Schreibweise, die den seit Jahren spürbaren Mangel an verfügbaren IPv4-Adressen beheben soll. Innerhalb eines lokalen Netzwerks vergibt meist ein **Router** per DHCP automatisch Adressen an alle angeschlossenen Geräte — inklusive Mikrocontroller mit Netzwerkanbindung.
:::

## TCP und UDP: zwei Philosophien des Datentransports

:::tip
Auf der Transportschicht stehen zwei grundverschiedene Protokolle zur Wahl — ganz ähnlich wie bei der Wahl zwischen einer gesicherten und einer ungesicherten Übertragung, die uns schon im Grundlagenartikel begegnet ist:

- **TCP** (Transmission Control Protocol) baut vor jeder Datenübertragung eine **verbindungsorientierte** Verbindung auf — über den klassischen **Drei-Wege-Handschlag (Three-Way-Handshake)**: Der Client sendet ein SYN ("ich möchte eine Verbindung aufbauen"), der Server antwortet mit SYN-ACK ("verstanden, ich bin bereit"), der Client bestätigt mit ACK ("dann legen wir los"). Erst danach beginnt die eigentliche Datenübertragung. TCP überwacht zudem laufend, ob alle Pakete korrekt und in der richtigen Reihenfolge ankommen, und fordert verlorene Pakete automatisch erneut an — **zuverlässig, aber mit etwas Overhead**.
- **UDP** (User Datagram Protocol) verzichtet komplett auf Verbindungsaufbau und Empfangsbestätigung — Pakete werden einfach "auf gut Glück" losgeschickt. Das macht UDP **schnell und schlank**, aber eben auch unzuverlässig: Pakete können verloren gehen oder in falscher Reihenfolge ankommen, ohne dass der Sender etwas davon merkt. UDP eignet sich deshalb vor allem dort, wo Geschwindigkeit wichtiger ist als Vollständigkeit — etwa bei Video-Streams, wo ein einzelnes verlorenes Bild kaum auffällt, ein spürbares Stocken durch Nachforderungen aber sehr wohl.

Für die meisten IoT-Anwendungen, bei denen Daten zuverlässig ankommen sollen, ist TCP die naheliegende Wahl — und genau auf TCP baut auch das im Folgenden vorgestellte MQTT auf.
:::

## MQTT: das schlanke Protokoll für die IoT-Welt

:::info
**MQTT** (Message Queuing Telemetry Transport) ist ein leichtgewichtiges Anwendungsprotokoll, das speziell für Geräte mit begrenzten Ressourcen — wenig Rechenleistung, wenig Bandbreite, knapper Energievorrat — entwickelt wurde. Sein Grundprinzip ist denkbar elegant und basiert auf drei Rollen:

- **Broker**: die zentrale Vermittlungsstelle, über die *alle* Nachrichten laufen (z. B. ein Mosquitto-Server)
- **Publisher**: ein Gerät, das Nachrichten zu einem bestimmten **Thema (Topic)** veröffentlicht — z. B. `wohnzimmer/temperatur`
- **Subscriber**: ein Gerät, das sich für ein bestimmtes Topic interessiert und vom Broker automatisch alle dazu veröffentlichten Nachrichten zugestellt bekommt

Das Entscheidende an diesem **Publish-Subscribe-Muster**: Publisher und Subscriber kennen sich gegenseitig gar nicht — sie kommunizieren ausschliesslich indirekt über den Broker und das gemeinsame Topic. Ein Temperatursensor muss also nicht wissen, wie viele und welche Geräte seine Messwerte gerade auswerten — er veröffentlicht sie einfach, und der Broker kümmert sich um die Verteilung an alle interessierten Empfänger. Das macht Systeme extrem flexibel erweiterbar: Ein neuer Subscriber kann jederzeit hinzukommen, ohne dass am Publisher irgendetwas geändert werden müsste.
:::

## QoS-Level: wie zuverlässig soll die Zustellung sein?

:::warning
MQTT erlaubt es, für jede Nachricht individuell festzulegen, wie zuverlässig sie zugestellt werden soll — über das sogenannte **Quality-of-Service-Level (QoS)**:

| QoS-Level | Bezeichnung | Garantie |
|---|---|---|
| 0 | "At most once" | Nachricht wird höchstens einmal zugestellt — kann verloren gehen, kein erneuter Versand |
| 1 | "At least once" | Nachricht wird mindestens einmal zugestellt — kann aber theoretisch doppelt ankommen |
| 2 | "Exactly once" | Nachricht wird garantiert genau einmal zugestellt — höchste Zuverlässigkeit, aber auch der grösste Protokoll-Overhead |

Welches Level die richtige Wahl ist, hängt stark von der Anwendung ab: Ein Temperaturwert, der ohnehin alle paar Sekunden neu gesendet wird, verkraftet locker QoS 0 — geht eine Nachricht verloren, kommt die nächste ja gleich hinterher. Ein Befehl wie "Tür öffnen" oder "Alarm auslösen" hingegen sollte zuverlässig ankommen — hier ist QoS 1 oder 2 die bessere Wahl.
:::

## MQTT in der Praxis: Broker und Bibliotheken

Für eigene Projekte hat sich eine kleine, bewährte Werkzeugkiste etabliert: Als **Broker** wird häufig **Mosquitto** eingesetzt — ein leichtgewichtiger, quelloffener MQTT-Server, der sich auf praktisch jeder Plattform (vom Raspberry Pi bis zum Cloud-Server) betreiben lässt. Auf der Geräteseite übernimmt häufig die Bibliothek **PubSubClient** die Kommunikation — sie kümmert sich um Verbindungsaufbau, das Veröffentlichen und Abonnieren von Topics sowie das Empfangen eingehender Nachrichten, und lässt sich unkompliziert in Mikrocontroller-Programme einbinden.

## Rückblick: das grosse Bild der Schnittstellen

Damit schliesst sich der Kreis dieses Kapitels: Wir haben den Weg eines einzelnen Bits von der → [[Serielle Datenübertragung (Grundlagen)|seriellen Grundlagen]] über chip-interne Schnittstellen wie → [[UART|UART]], → [[SPI|SPI]] und → [[I2C|I2C]], über klassische Industriestandards wie → [[RS232 & RS485|RS232/RS485]] und → [[RS422 & Current Loop|RS422/Current Loop]], über spezialisierte Bussysteme wie den → [[CAN-Bus|CAN-Bus]] und drahtlose Technologien wie → [[Bluetooth|Bluetooth]] und → [[LoRaWAN|LoRaWAN]] bis hin zu → [[Ethernet|Ethernet]] und schliesslich zur globalen Vernetzung über **TCP/IP** und **MQTT** verfolgt. Jede dieser Schnittstellen löst dasselbe Grundproblem — die zuverlässige Übertragung von Information — auf ihre eigene, für den jeweiligen Einsatzzweck optimierte Art. Mit diesem Werkzeugkasten im Kopf lässt sich für (fast) jede Aufgabenstellung die passende Schnittstelle finden.
