---
title: Encoder & Prioritätsencoder
kategorie: SH
kapitel: Digitaltechnik
tags: [encoder, prioritaetsencoder, codierer, kodierung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Demultiplexer & Decoder]]
:::
:::

---

Ein → [[Demultiplexer & Decoder|Decoder]] übersetzt ein Binärwort in genau ein aktives Ausgangssignal. Der **Encoder** geht den umgekehrten Weg: Er nimmt eines von mehreren aktiven Eingangssignalen entgegen und setzt es in das passende Binärwort um — er "kodiert" also eine aktive Leitung in eine Adresse.

## Funktionsprinzip

Ein einfacher 8-zu-3-Encoder besitzt acht Eingänge E0…E7 und drei Ausgänge A2A1A0. Wird genau ein Eingang aktiviert, erscheint an den Ausgängen das zugehörige Binärwort — aktiviert man z. B. E5, liegt am Ausgang das Wort 101 (= 5):

:::merke
Ein Encoder lässt sich als reine ODER-Verknüpfung aufbauen: Jedes Ausgangsbit ist genau dann High, wenn mindestens einer der Eingänge aktiv ist, deren Index an der entsprechenden Binärstelle eine 1 trägt. So liegt z. B. A0 (LSB) genau dann High, wenn einer der ungeraden Eingänge E1, E3, E5 oder E7 aktiv ist. Damit lässt sich ein Encoder vollständig ohne UND-Gatter — nur mit ODER-Gattern — realisieren.
:::

## Das Problem mehrerer gleichzeitig aktiver Eingänge

Der einfache Encoder hat eine Schwäche: Werden **mehrere** Eingänge gleichzeitig aktiv, entsteht ein undefiniertes Ausgangswort, das keinem der ursprünglichen Eingänge eindeutig zugeordnet werden kann — die Information geht verloren oder wird verfälscht. In der Praxis ist das aber ein häufiger Fall: Drückt jemand z. B. gleichzeitig zwei Tasten einer Tastatur, müssen beide Eingänge irgendwie "sortiert" behandelt werden.

:::warning
Ein gewöhnlicher Encoder darf deshalb nur dort eingesetzt werden, wo garantiert ist, dass zu jedem Zeitpunkt **höchstens ein** Eingang aktiv ist. Sind mehrere Eingänge gleichzeitig möglich — etwa bei Tastaturen, Interrupt-Leitungen oder Sensorfeldern —, ist ein gewöhnlicher Encoder ungeeignet und es muss ein **Prioritätsencoder** verwendet werden.
:::

## Der Prioritätsencoder

Ein **Prioritätsencoder** löst das Mehrfach-Aktivierungsproblem, indem er seinen Eingängen eine feste Rangfolge zuweist: Sind mehrere Eingänge gleichzeitig aktiv, setzt er stets nur denjenigen mit der **höchsten Priorität** in das entsprechende Binärwort um — alle niederwertigeren aktiven Eingänge werden in diesem Moment ignoriert.

:::tip
Ein bekannter Vertreter ist der IC **74148** (8-zu-3-Prioritätsencoder): Der Eingang E7 besitzt die höchste, E0 die niedrigste Priorität. Liegen z. B. gleichzeitig E3 und E6 auf aktivem Pegel, erscheint am Ausgang das Binärwort für 6 — der Eingang E3 wird in diesem Augenblick "übergangen". Zusätzlich liefert ein **GS-Ausgang (Group Select)** die Information, ob überhaupt ein Eingang aktiv ist, und ein **EO-Ausgang (Enable Output)** ermöglicht das Kaskadieren mehrerer Bausteine zu grösseren Prioritätsencodern (z. B. 16-zu-4).
:::

## Anwendung: Tastaturcodierung und Interrupt-Verwaltung

Prioritätsencoder finden sich überall dort, wo eine grosse Zahl gleichberechtigter Signalquellen auf wenige Verarbeitungsleitungen reduziert werden muss:

- **Tastaturcodierung**: Eine Tastatur mit 64 Tasten lässt sich nicht mit 64 separaten Leitungen an einen Mikroprozessor anschliessen — ein Prioritätsencoder reduziert die Information auf ein 6-Bit-Binärwort, das die gedrückte Taste eindeutig identifiziert (selbst dann, wenn versehentlich mehrere Tasten gleichzeitig betätigt werden).
- **Interrupt-Controller**: Fordern mehrere Peripheriebausteine gleichzeitig die Aufmerksamkeit eines Prozessors an, entscheidet ein Prioritätsencoder, welche Anfrage zuerst bearbeitet wird — eine Aufgabe, die in modernen Systemen von spezialisierten Interrupt-Controllern übernommen wird, die nach demselben Grundprinzip arbeiten.

Encoder und Decoder bilden damit ein komplementäres Paar: Der eine reduziert viele Leitungen auf wenige Adressbits, der andere expandiert wenige Adressbits wieder auf viele Leitungen — beide Prinzipien begegnen einem in nahezu jedem digitalen System wieder.
