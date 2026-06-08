---
title: Ethernet
kategorie: SH
kapitel: Schnittstellen
tags: [ethernet, mac-adresse, csma-cd, twisted pair, netzwerk]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Serielle Datenübertragung (Grundlagen)]]
:::
:::vbox
**Führt weiter zu**
- [[TCP/IP & MQTT]]
:::
:::

---

→ [[LoRaWAN|LoRaWAN]] und → [[Bluetooth|Bluetooth]] zeigen, wie leistungsfähig drahtlose Übertragung heute sein kann — solange man mit begrenztem Datendurchsatz und gewissen Reichweiteneinschränkungen leben kann. Wer hingegen grosse Datenmengen schnell, stabil und über kurze bis mittlere Distanzen übertragen will — vom Heimnetzwerk bis zur Industrieanlage —, landet praktisch immer bei derselben Technologie: **Ethernet**, dem Rückgrat praktisch jedes kabelgebundenen Netzwerks.

## MAC und PHY: zwei Schichten mit getrennten Aufgaben

:::merke
Ethernet lässt sich in zwei Schichten unterteilen, die sauber getrennte Aufgaben übernehmen:

- **MAC (Media Access Control)**: regelt, *wer* wann auf das gemeinsame Übertragungsmedium zugreifen darf, organisiert die Daten in **Frames** und versieht jedes Gerät mit einer eindeutigen **MAC-Adresse** (eine weltweit einmalige 48-Bit-Kennung, die fest in die Netzwerk-Hardware eingebrannt ist).
- **PHY (Physical Layer)**: kümmert sich um die *elektrische* bzw. *optische* Übertragung der Bits über das physische Medium — Kupferkabel, Twisted-Pair-Leitung oder Glasfaser.

Diese Trennung erlaubt es, dieselbe MAC-Logik mit ganz unterschiedlicher Übertragungs-Hardware zu kombinieren — vom alten Koaxialkabel bis zur modernen Glasfaser.
:::

## Ethernet-Varianten: vom Klassiker bis zum Hochgeschwindigkeitsnetz

:::tip
Über die Jahrzehnte sind zahlreiche Ethernet-Varianten entstanden, die sich vor allem in Geschwindigkeit und Kabeltyp unterscheiden:

| Variante | Geschwindigkeit | Kabeltyp |
|---|---|---|
| 10BASE-T | 10 Mbit/s | Twisted Pair (Kupfer) |
| 100BASE-TX (Fast Ethernet) | 100 Mbit/s | Twisted Pair (Kupfer) |
| 1000BASE-T (Gigabit Ethernet) | 1 Gbit/s | Twisted Pair (Kupfer) |
| 10GBASE-T | 10 Gbit/s | Twisted Pair (Kupfer, Cat 6a/7) |

Eine besonders interessante neuere Entwicklung ist **Single Pair Ethernet (SPE)**, etwa **10BASE-T1L** — hier genügt ein einziges verdrilltes Adernpaar (statt der bisher üblichen vier Paare), um Ethernet-Signale über Distanzen von bis zu 1 km zu übertragen. Das macht Ethernet zunehmend auch für Sensoren und Feldgeräte interessant, die bisher klassische Feldbus-Technologien wie RS485 oder CAN nutzten.
:::

## Der Frame-Aufbau: wie Daten verpackt werden

Wie bei jeder seriellen Übertragung müssen auch bei Ethernet die Nutzdaten in einen klar definierten Rahmen verpackt werden:

| Feld | Bedeutung |
|---|---|
| Präambel | Synchronisationsmuster, kündigt den Beginn des Frames an |
| Ziel-MAC-Adresse | Adresse des Empfängers |
| Quell-MAC-Adresse | Adresse des Senders |
| EtherType | Kennzeichnet das verwendete Protokoll der nächsten Schicht (z. B. IPv4) |
| Payload (Nutzdaten) | Die eigentlichen zu übertragenden Daten (46–1500 Byte) |
| CRC (Prüfsumme) | Erkennt Übertragungsfehler |

## CSMA/CD: das historische Buszugriffsverfahren

:::warning
In den Anfangstagen von Ethernet teilten sich alle Geräte ein gemeinsames Kabel — und mussten sich deshalb auf eine Regel einigen, wer wann senden darf. Diese Regel heisst **CSMA/CD** (Carrier Sense Multiple Access / Collision Detection): Ein Gerät "horcht" zunächst, ob das Medium frei ist (Carrier Sense), beginnt dann zu senden — und falls es trotzdem zu einer **Kollision** mit einem anderen gleichzeitig sendenden Gerät kommt, erkennen beide Geräte dies (Collision Detection), brechen die Übertragung ab und versuchen es nach einer zufälligen Wartezeit erneut.

In modernen Netzwerken mit **Switches** spielt CSMA/CD praktisch keine Rolle mehr — jedes Gerät erhält eine eigene, exklusive Verbindung zum Switch (Vollduplex), wodurch Kollisionen von vornherein ausgeschlossen sind. Das Verfahren bleibt aber ein wichtiges Stück Netzwerkgeschichte und erklärt, warum bestimmte Begriffe (z. B. "Kollisionsdomäne") bis heute in der Netzwerktechnik gebräuchlich sind.
:::

## Ethernet auf dem Mikrocontroller

:::info
Auch kleine eingebettete Systeme lassen sich heute problemlos ans Ethernet anbinden. Verbreitete Lösungen sind etwa der **W5500**-Chip (ein eigenständiger Ethernet-Controller mit komplettem TCP/IP-Stack in Hardware, der sich einfach über → [[SPI|SPI]] ansteuern lässt) oder Software-Stacks wie **lwIP** (lightweight IP), die auf Mikrocontrollern mit eigenem Ethernet-Anschluss laufen.

Im industriellen Umfeld hat sich aus dem klassischen Ethernet zudem eine ganze Familie von **Industrial-Ethernet**-Protokollen entwickelt — etwa **EtherCAT** oder **PROFINET** — die zusätzliche Echtzeitfähigkeit und deterministisches Zeitverhalten mitbringen, wie es Maschinensteuerungen benötigen.
:::

Ethernet sorgt also dafür, dass Daten zuverlässig von einem Gerät zum nächsten innerhalb eines lokalen Netzwerks gelangen — über MAC-Adressen, Frames und (heute meist) kollisionsfreie Switch-Verbindungen. Doch ein lokales Netzwerk ist erst die halbe Miete: Damit Geräte über das **Internet** miteinander reden und ihre Daten in einer für IoT-Anwendungen geeigneten Form austauschen können, braucht es weitere Protokollschichten obendrauf. Genau diese stellt der letzte Artikel dieses Kapitels vor: → [[TCP/IP & MQTT|TCP/IP und MQTT]].
