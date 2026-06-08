---
title: CAN-Bus
kategorie: SH
tags: [CAN, bus, differenziell, automobil, industriekommunikation, rahmen, frame, CAN-FD, arbitrierung, CSMA, feldbus, bit-stuffing, abschlusswiderstand, transceiver, SAE J1939, embedded]
symbol: —
einheit: —
---

CAN (Controller Area Network) ist ein robuster Feldbus für störungsreiche Umgebungen. Entwickelt für Automobile, heute auch in Industrie und Medizintechnik weit verbreitet.

:::hbox
:::vbox
**Voraussetzungen**
- [[UART]]
:::
:::vbox
**Verwandte Artikel**
- [[RS-232 / RS-485]]
:::
:::

---

## Besonderheiten

**Multi-Master**: Jeder Knoten kann senden wenn der Bus frei ist. Kollisionen werden durch Prioritäten aufgelöst — ohne Datenverlust (CSMA/CR, siehe unten).

**Differenziell**: CAN_H und CAN_L. Störungen auf beiden Leitungen gleich, werden subtrahiert. Sehr störfest.

**Nachrichtenbasiert**: Keine Adressen. Jede Nachricht hat eine ID. Alle Knoten entscheiden selbst welche Nachrichten sie verarbeiten.

## CSMA/CR — Arbitrierung ohne Kollision

CAN verwendet **CSMA/CR** (Carrier Sense Multiple Access / Collision Resolution — auch: Collision Avoidance mit Bitarbitrierung).

**Wie es funktioniert**:
- Der Bus hat zwei Pegel: **dominant** (0) und **rezessiv** (1)
- Dominant überschreibt rezessiv — wie eine Wired-AND-Logik
- Jeder sendende Knoten schreibt sein Bit und liest sofort zurück was auf dem Bus liegt
- Stimmt das gelesene Bit nicht mit dem gesendeten überein, hat ein anderer Knoten ein dominantes Bit gesendet → der Knoten mit dem höheren ID-Bit zieht sich zurück

**Ergebnis**: Der Rahmen mit der **kleinsten ID-Nummer gewinnt** (mehr Nullen = mehr dominante Bits = höhere Priorität). Der Gewinner sendet ungestört weiter, die Verlierer versuchen es später erneut. **Kein Datenverlust, keine Wiederholung nötig**.

## Bit-Stuffing

CAN-Daten enthalten keine eigene Taktsynchronisation. Der Empfänger synchronisiert sich auf die Flanken des Signals.

**Problem**: Lange Sequenzen ohne Flanke (viele gleiche Bits) → Empfänger verliert Synchronisation.

**Lösung: Bit-Stuffing**: Nach 5 gleichen Bits in Folge fügt der Sender automatisch ein inverses Bit (Stuff-Bit) ein. Der Empfänger erkennt und entfernt dieses Bit automatisch.

:::formel
Datenbits: 1 1 1 1 1 | 0 1 1 0 0 ...
                         ↑ Stuff-Bit (invertiert nach 5x '1')
:::
Bit-Stuffing vergrössert die übertragene Datenmenge um maximal 25 %, erlaubt aber den Betrieb ohne separate Taktleitung.

## Rahmenaufbau

ID (11 oder 29 Bit) + DLC (Datenlänge) + bis zu 8 Byte Daten + CRC + ACK.

Die ID bestimmt die Priorität. Kleinere ID-Nummer = höhere Priorität.

## Bitraten

| Bitrate | Maximale Buslänge |
|---|---|
| 1 MBit/s | 40 m |
| 500 kBit/s | 100 m |
| 250 kBit/s | 250 m |
| 125 kBit/s | 500 m |

CAN FD (Flexible Data Rate): bis 5 MBit/s für den Datenteil, bis 64 Byte pro Rahmen.

## Abschlusswiderstände

Am Ende jeder Busleitung 120 Ω zwischen CAN_H und CAN_L. Verhindert Reflexionen. Ohne Abschluss: Kommunikationsfehler bei höheren Bitraten.

:::tip
CAN-Transceiver-ICs (z.B. MCP2551, SN65HVD230) wandeln die logischen Pegel des Mikrocontrollers in die differenziellen CAN-Pegel. Nie direkt verbinden.
:::
