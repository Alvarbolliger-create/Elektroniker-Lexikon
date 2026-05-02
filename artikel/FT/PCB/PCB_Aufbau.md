---
title: PCB Aufbau & Material
kategorie: FT
tags: [PCB, leiterplatte, FR4, aufbau, material, lagen, multilayer, kupfer, lötstoppmaske, via, leiterbahnbreite, EMV, silkscreen]
symbol: —
einheit: —
---

Eine Leiterplatte (PCB) trägt und verbindet elektronische Bauteile. Aufbau und Material beeinflussen Signalqualität, Wärmeableitung und mechanische Festigkeit.

:::hbox
:::vbox
**Voraussetzungen**
- [[Widerstand]]
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Verwandte Artikel**
- [[SMD vs. THT]]
- [[Durchkontaktierung]]
:::
:::vbox
**Führt weiter zu**
- [[Signalintegrität]]
:::
:::

---

## Aufbau

Eine Leiterplatte besteht aus mehreren Schichten:

**Trägermaterial**: Isolierendes Basismaterial, meistens FR4 (Glasfasergewebe mit Epoxidharz). Günstig, robust, bis ca. 130 °C.

**Kupferschicht**: 35 µm bis 70 µm dünne Kupferfolie, geätzt zur Leiterbahnstruktur.

**Lötstoppmaske**: Grüne (oder andere) Schutzschicht über den Leiterbahnen. Schützt vor Lötbrücken und Oxidation. Öffnungen nur an Lötpads.

**Bestückungsaufdruck (Silkscreen)**: Weisse Beschriftung für Bauteilbezeichnungen.

## Lagenzahl

**Einlagig**: Leiterbahnen nur auf einer Seite. Einfach, günstig. Für einfache Schaltungen.

**Zweilagig**: Beide Seiten genutzt, verbunden durch Vias. Standard für die meisten Schaltungen.

**Multilayer**: Vier oder mehr Lagen. Innere Lagen oft als Masse- und Versorgungsebene. Für komplexe Schaltungen, Hochfrequenz, hohe Dichte.

## Leiterbahnbreite und Strom

Kupfer hat einen Widerstand. Zu schmale Leiterbahnen erhitzen sich bei hohem Strom.

| Leiterbahnbreite | Max. Strom (35 µm Kupfer, Aussenlagen) |
|---|---|
| 0.3 mm | ca. 0.7 A |
| 0.5 mm | ca. 1.0 A |
| 1.0 mm | ca. 1.7 A |
| 2.0 mm | ca. 2.8 A |

:::tip
Masseflächen (Copper Pours) auf freien Flächen verbessern Wärmeableitung und EMV. Standard in allen professionellen Designs.
:::
