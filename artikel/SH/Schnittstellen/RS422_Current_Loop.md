---
title: RS422 & Current Loop
kategorie: SH
kapitel: Schnittstellen
tags: [rs422, current loop, 20ma-schnittstelle, differenzsignal, stromschleife]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[RS232 & RS485]]
:::
:::

---

→ [[RS232 & RS485|RS232 und RS485]] markieren zwei Eckpunkte der seriellen Schnittstellen-Welt: kurze Punkt-zu-Punkt-Verbindung versus langer Mehrpunkt-Bus. Dazwischen — und für ganz besondere Anforderungen — existieren noch zwei weitere genormte Lösungen, die in der Praxis immer wieder auftauchen: **RS422**, der "kleine Bruder" von RS485, und die **Current-Loop-Schnittstelle**, die das Problem der Datenübertragung auf eine völlig andere Art löst — über einen Strom statt über eine Spannung.

## RS422: differenziell, aber nur mit einem Sender

:::merke
**RS422** überträgt — genau wie RS485 — **differenziell** über ein verdrilltes Adernpaar: Statt eines einzelnen Spannungspegels gegen Masse wird die *Differenz* zwischen zwei Leitungen ausgewertet. Das macht die Übertragung extrem unempfindlich gegenüber Gleichtaktstörungen, die auf beide Leitungen gleichermassen einwirken — ein riesiger Vorteil in elektrisch verseuchten Industrieumgebungen. Im Gegensatz zu RS485 erlaubt RS422 jedoch nur **einen einzigen Sender**, an den dafür mehrere Empfänger angeschlossen werden können (bis zu 10). RS422 ist gewissermassen die unidirektionale Vorstufe von RS485 — wer ein echtes Mehrpunkt-Bussystem mit vielen gleichberechtigten Teilnehmern braucht, greift zu RS485; wer "nur" eine störsichere, lange Punkt-zu-Mehrpunkt-Verbindung benötigt, kommt mit RS422 aus.

Wichtig: Bei differenziellen Schnittstellen wie RS422 und RS485 wird **kein gemeinsamer Massebezug (GND)** zwischen den Geräten benötigt — die Information steckt vollständig in der *Differenz* der beiden Signalleitungen. Auch hier sorgen **Abschlusswiderstände** an den Leitungsenden dafür, dass keine störenden Signalreflexionen auftreten.
:::

## Current Loop: Information als Strom statt als Spannung

:::tip
Die **Current-Loop-Schnittstelle** (auch als "20-mA-Schnittstelle" bekannt) verfolgt einen fundamental anderen Ansatz: Statt Information über eine *Spannung* zu codieren, wird sie über einen **Strom** übertragen — konkret unterscheidet man zwischen "Strom fliesst" (logisch 1, typischerweise 20 mA) und "kein Strom fliesst" (logisch 0, 0 mA). Dieses Prinzip hat einen entscheidenden Vorteil: Ein eingeprägter Strom bleibt über die gesamte Leitungslänge **konstant**, unabhängig von Leitungswiderständen oder kleineren Spannungsabfällen — die Übertragung wird dadurch erstaunlich robust gegenüber langen Kabelstrecken und elektromagnetischen Störungen.

Mit Current Loop lassen sich auf diese Weise Distanzen von etwa **1000 m bei 1200 Bit/s** überbrücken — eine Hausnummer, die viele andere serielle Schnittstellen weit hinter sich lässt. Ein weiterer Pluspunkt: Da die Schnittstelle über Optokoppler realisiert werden kann, lässt sich eine **galvanische Trennung** zwischen Sender und Empfänger erreichen — die beiden Stromkreise sind elektrisch vollständig voneinander isoliert. Das schützt empfindliche Elektronik zuverlässig vor Ausgleichsströmen, Erdschleifen und Spannungsspitzen, wie sie in industriellen Anlagen häufig auftreten.
:::

## Die EIA-Schnittstellen im Gesamtüberblick

:::info
Damit lässt sich die Familie der klassischen seriellen EIA-Schnittstellen vollständig einordnen:

| Norm | Übertragungsart | Max. Länge | Max. Datenrate | Sender | Empfänger | Signalspannung |
|---|---|---|---|---|---|---|
| RS232 | asymmetrisch | 15 m | 20 kBit/s | 1 | 1 | ±15 V |
| RS423 | asymmetrisch | 1200 m | 100 kBit/s | 1 | 10 | ±5 V |
| RS422 | symmetrisch (differenziell) | 1200 m | 10 Mbit/s | 1 | 10 | ±5 V |
| RS485 | symmetrisch (differenziell) | 1200 m | 10 Mbit/s | 32 | 32 | ±5 V |

Die Tabelle macht das grundlegende Entwicklungsmuster sichtbar: Mit jedem Schritt — von RS232 über RS423 und RS422 bis zu RS485 — wachsen Reichweite, Geschwindigkeit und Teilnehmerzahl, während gleichzeitig die Störsicherheit zunimmt (asymmetrisch → symmetrisch/differenziell). RS485 bildet dabei den Höhepunkt dieser Entwicklung und ist heute die Basis unzähliger Feldbussysteme in der Industrie.
:::

## Warnung: nicht jede "alte" Schnittstelle ist obsolet

:::warning
Auch wenn RS232, RS422, RS485 und Current Loop auf den ersten Blick wie Technik aus vergangenen Jahrzehnten wirken — in der industriellen Praxis sind sie alles andere als ausgestorben! Unzählige Maschinen, SPS-Steuerungen, Messgeräte und Sensoren, die seit Jahrzehnten zuverlässig im Einsatz stehen, kommunizieren nach wie vor über genau diese Schnittstellen. Wer in der Instandhaltung, Inbetriebnahme oder im Anlagenbau arbeitet, wird ihnen mit Sicherheit begegnen — ein solides Verständnis dieser "klassischen" Standards bleibt deshalb auch heute unverzichtbar.
:::

Damit ist die Familie der klassischen, leitungsgebundenen seriellen Schnittstellen vollständig erkundet — von der einfachen Punkt-zu-Punkt-Verbindung bis zum robusten Industriebus. Die nächsten Artikel widmen sich spezialisierten Bussystemen und Funktechnologien, die in modernen Anwendungen — vom Fahrzeug bis zum IoT-Sensor — eine immer wichtigere Rolle spielen, beginnend mit einem Bus, der speziell für die Anforderungen der Automobilindustrie entwickelt wurde: → [[CAN-Bus|CAN-Bus]].
