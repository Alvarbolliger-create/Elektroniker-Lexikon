---
title: CAN-Bus
kategorie: SH
kapitel: Schnittstellen
tags: [can-bus, controller area network, arbitrierung, fehlererkennung, automotive]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Serielle Datenübertragung (Grundlagen)]]
:::
:::

---

Stell dir ein modernes Auto vor: Motorsteuerung, ABS, Airbag, Klimaanlage, Fensterheber, Tachometer — gut hundert kleine Steuergeräte, die ständig Informationen austauschen müssen, oft in Sekundenbruchteilen und unter rauen Bedingungen (Vibration, Temperaturschwankungen, elektromagnetische Störungen). Würde man jedes Gerät einzeln verkabeln, entstünde ein unüberschaubares Kabelgewirr. Die Lösung dafür heisst **CAN-Bus** (Controller Area Network) — ein Bussystem, das genau für solche Anforderungen entwickelt wurde und heute weit über die Automobilindustrie hinaus in Maschinen, Anlagen und der Gebäudetechnik verbreitet ist.

## Multi-Master statt fester Hierarchie

:::merke
Der CAN-Bus ist ein **Multi-Master-Bussystem**: Es gibt keinen zentralen Master, der den Datenverkehr steuert — jeder Teilnehmer ("Knoten") kann jederzeit eigenständig senden, sobald der Bus frei ist. Übertragen wird **differenziell** über ein verdrilltes Adernpaar **CAN_H** und **CAN_L** — dasselbe robuste Prinzip wie bei → [[RS422 & Current Loop|RS422 und RS485]]: Störungen, die auf beide Leitungen gleichermassen einwirken, heben sich beim Empfänger gegenseitig auf. An beiden Enden des Busses sitzen **Abschlusswiderstände von 120 Ω**, die Signalreflexionen unterdrücken.
:::

## Arbitrierung: wie der Bus Kollisionen elegant auflöst

:::tip
Was passiert, wenn zwei Knoten gleichzeitig senden wollen? Beim CAN-Bus führt das nicht etwa zu einer Kollision wie bei anderen Bussystemen, sondern zu einer fairen, verlustfreien **Arbitrierung** nach dem CSMA/CR-Prinzip (Carrier Sense Multiple Access / Collision Resolution):

Jede Nachricht trägt eine **Identifier (ID)**, die gleichzeitig ihre Priorität festlegt. Auf dem Bus gibt es zwei Zustände: **dominant** (logisch 0) und **rezessiv** (logisch 1) — wobei "dominant" sich gegen "rezessiv" immer durchsetzt, sobald beide gleichzeitig auf den Bus gelegt werden (vergleichbar mit einer Wired-AND-Verknüpfung). Senden zwei Knoten gleichzeitig, vergleichen beide bitweise ihre ID mit dem tatsächlichen Buspegel: Sobald ein Knoten ein rezessives Bit sendet, auf dem Bus aber ein dominantes Bit erscheint (weil ein anderer Knoten gleichzeitig eine niedrigere — also wichtigere — ID sendet), erkennt er, dass er den Wettbewerb verloren hat, und zieht sich sofort zurück. Der Knoten mit der **niedrigsten ID** (= höchste Priorität) sendet ungestört weiter — **ohne jeden Datenverlust**! Diese Eigenschaft macht den CAN-Bus ideal für zeitkritische Anwendungen wie die Übertragung von Bremssignalen.
:::

## Der Rahmenaufbau: kompakt und mit eingebauter Fehlerkontrolle

Eine CAN-Nachricht (Frame) ist kompakt aufgebaut und enthält dabei bereits eine eingebaute Fehlerkontrolle:

| Feld | Bedeutung |
|---|---|
| Start of Frame | Kennzeichnet den Beginn der Nachricht |
| Identifier (ID) | Bestimmt Priorität und Bedeutung der Nachricht |
| DLC (Data Length Code) | Anzahl der folgenden Datenbytes (0–8) |
| Daten | Die eigentlichen Nutzdaten (max. 8 Byte beim klassischen CAN) |
| CRC | Prüfsumme zur Fehlererkennung |
| ACK | Bestätigung durch mindestens einen Empfänger |
| End of Frame | Kennzeichnet das Ende der Nachricht |

:::info
Ein cleverer Mechanismus zur Sicherstellung der Synchronisation ist das **Bit-Stuffing**: Sobald **fünf gleiche Bits** in Folge gesendet werden, fügt der Sender automatisch ein zusätzliches Bit mit dem entgegengesetzten Pegel ein (ein sogenanntes "Stuff-Bit"). Der Empfänger entfernt dieses Bit beim Empfang wieder. Dadurch entstehen garantiert regelmässige Flankenwechsel auf dem Bus — wichtig, damit sich alle Teilnehmer zuverlässig auf den gemeinsamen Takt synchronisieren können, obwohl CAN ganz ohne separate Taktleitung auskommt.
:::

## Geschwindigkeit hängt von der Leitungslänge ab

:::warning
Beim CAN-Bus stehen **Bitrate und maximale Leitungslänge** in einem direkten Zusammenhang: Je länger der Bus, desto länger braucht ein Signal, um von einem Ende zum anderen zu gelangen — und desto langsamer muss folglich übertragen werden, damit die Arbitrierung noch zuverlässig funktioniert.

| Bitrate | Max. Leitungslänge |
|---|---|
| 1 MBit/s | ca. 40 m |
| 500 kBit/s | ca. 100 m |
| 250 kBit/s | ca. 250 m |
| 125 kBit/s | ca. 500 m |

Wer einen CAN-Bus plant, muss also stets einen Kompromiss zwischen gewünschter Geschwindigkeit und der räumlichen Ausdehnung der Anlage finden.
:::

## CAN FD: mehr Daten, mehr Tempo

Die Weiterentwicklung **CAN FD** (Flexible Data-Rate) erlaubt grössere Datenfelder (bis zu 64 Byte statt 8) und schaltet während der Übertragung der Nutzdaten auf eine höhere Bitrate um — ein cleverer Weg, die Vorteile des bewährten CAN-Protokolls (Arbitrierung, Fehlererkennung) mit deutlich höherem Datendurchsatz zu verbinden. CAN FD findet zunehmend Verbreitung in modernen Fahrzeugen und Industrieanlagen, in denen grössere Datenmengen anfallen als noch vor wenigen Jahren.

Der CAN-Bus zeigt eindrücklich, wie sich aus einfachen Grundprinzipien — Differenzsignal, Priorisierung über IDs, eingebaute Fehlerkontrolle — ein extrem robustes und bewährtes System für anspruchsvolle Echtzeitanwendungen aufbauen lässt. Während CAN auf kabelgebundene Verbindungen setzt, verlagert sich die Kommunikation in vielen modernen Anwendungen zunehmend in die **Funkwelt**. Der nächste Artikel stellt eine der bekanntesten Funktechnologien für die Nahbereichskommunikation vor: → [[Bluetooth|Bluetooth]].
