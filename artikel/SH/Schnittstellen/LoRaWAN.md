---
title: LoRaWAN
kategorie: SH
kapitel: Schnittstellen
tags: [lorawan, lpwan, funknetz, iot, reichweite]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Serielle Datenübertragung (Grundlagen)]]
:::
:::

---

→ [[Bluetooth|Bluetooth]] überbrückt typischerweise nur einige Dutzend Meter — ideal für Kopfhörer oder Fitness-Tracker, aber völlig ungeeignet, wenn ein Sensor mitten auf einem Acker, in einem Parkhaus oder am Stadtrand seine Messwerte über mehrere Kilometer hinweg an eine Zentrale senden soll. Für genau diese Aufgabe — **lange Reichweite, wenig Daten, minimaler Energieverbrauch** — wurde **LoRaWAN** entwickelt, eine der bekanntesten Vertreter der sogenannten **LPWAN**-Technologien (Low Power Wide Area Network).

## LoRa und LoRaWAN: zwei Begriffe, die oft verwechselt werden

:::merke
Es lohnt sich, zwei Begriffe sauber zu trennen:

- **LoRa** (Long Range) bezeichnet das zugrundeliegende **physikalische Funkverfahren** — also *wie* die Bits über die Luft moduliert und übertragen werden.
- **LoRaWAN** bezeichnet das darauf aufbauende **Netzwerkprotokoll** — also *wie* Geräte sich anmelden, Daten organisiert werden und wer mit wem kommuniziert.

Man kann sich das wie bei einer Strasse (LoRa, das physische Übertragungsmedium) und den Verkehrsregeln darauf (LoRaWAN, das Protokoll, das den Verkehr ordnet) vorstellen. Betrieben wird LoRaWAN typischerweise im lizenzfreien Frequenzband bei **868 MHz** (Europa) bzw. **915 MHz** (Nordamerika).
:::

## Die Architektur: vier Bausteine

:::tip
Ein LoRaWAN-Netzwerk besteht aus vier klar getrennten Bausteinen, die jeweils eine eigene Aufgabe übernehmen:

1. **End-Geräte** — die eigentlichen Sensoren oder Aktoren, die Messwerte erfassen und per Funk versenden (z. B. Temperatursensoren, Wasserzähler, GPS-Tracker)
2. **Gateways** — empfangen die Funksignale der End-Geräte in ihrer Umgebung und leiten sie über eine konventionelle Internetverbindung (WLAN, Ethernet, Mobilfunk) weiter
3. **Network Server** — verwaltet das gesamte Netzwerk, prüft Berechtigungen, filtert doppelt empfangene Pakete (oft empfangen mehrere Gateways dasselbe Signal) und leitet die Daten weiter
4. **Application Server** — verarbeitet die eigentlichen Nutzdaten und stellt sie der Anwendung (App, Dashboard, Datenbank) zur Verfügung

Ein einzelnes Gateway kann dabei gleichzeitig Tausende von End-Geräten in seinem Empfangsbereich bedienen — ein enormer Unterschied zu den bisher behandelten Punkt-zu-Punkt- oder kleinen Bus-Systemen.
:::

## Spreading Factor: der Kompromiss zwischen Reichweite und Geschwindigkeit

:::info
Ein zentrales Konzept von LoRa ist der **Spreading Factor (SF)**, der den Kompromiss zwischen Reichweite, Übertragungsdauer und Energieverbrauch steuert:

| Spreading Factor | Datenrate | Reichweite | Übertragungsdauer |
|---|---|---|---|
| SF7 | hoch | gering | kurz |
| SF9 | mittel | mittel | mittel |
| SF12 | gering | sehr gross | lang |

Je höher der Spreading Factor, desto "langsamer und ausführlicher" wird ein Signal codiert — das macht es für den Empfänger leichter, es selbst aus dem Rauschen herauszufiltern, und erhöht damit die erreichbare Distanz drastisch (mehrere Kilometer im ländlichen Gebiet sind keine Seltenheit). Der Preis dafür: längere Übertragungszeiten und ein höherer Energieverbrauch pro gesendetem Paket.
:::

## Duty-Cycle: die Bremse im lizenzfreien Frequenzband

:::warning
Da LoRaWAN ein **lizenzfreies** Frequenzband nutzt, das sich auch andere Funkdienste teilen, gilt eine wichtige gesetzliche Beschränkung: der **Duty-Cycle** von typischerweise **1 %**. Das bedeutet, ein Gerät darf innerhalb einer Stunde insgesamt nur etwa 36 Sekunden lang senden! Diese Regel zwingt zu einem bewussten, sparsamen Umgang mit der Funkschnittstelle — LoRaWAN eignet sich deshalb explizit *nicht* für Anwendungen mit hohem Datenaufkommen oder Echtzeitanforderungen, sondern für gelegentliche, kleine Datenpakete (z. B. ein Messwert alle paar Minuten oder Stunden).
:::

## The Things Network und passende Hardware

Eine bekannte, frei nutzbare LoRaWAN-Infrastruktur ist **The Things Network (TTN)** — eine globale, community-betriebene Sammlung von Gateways, an die sich eigene Projekte kostenlos anbinden lassen. Für eigene Experimente eignen sich fertige Boards wie die **RAK-Wireless**-Module oder das **TTGO LoRa32**, die einen Mikrocontroller direkt mit einem LoRa-Funkmodul kombinieren.

Typische Anwendungsfelder von LoRaWAN sind die **Landwirtschaft** (Bodenfeuchte- und Wettersensoren über grosse Felder verteilt), das **Smart-Building** (Zählerstände, Füllstandsmessung), das **Smart-City**-Umfeld (Parkplatzsensoren, Strassenbeleuchtung) sowie die Umweltüberwachung — überall dort, wo viele Sensoren über grosse Flächen verteilt werden müssen, aber jeweils nur wenige Bytes pro Tag zu übertragen sind.

Während LoRaWAN auf grosse Reichweiten bei kleinen Datenmengen spezialisiert ist, gibt es auch kabelgebundene Netzwerktechnologien, die das genaue Gegenteil leisten — riesige Datenmengen über stabile, schnelle Verbindungen. Die wohl bekannteste davon stellt der nächste Artikel vor: → [[Ethernet|Ethernet]].
