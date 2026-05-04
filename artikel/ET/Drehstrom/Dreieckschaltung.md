---
title: Dreieckschaltung
kategorie: ET
tags: [dreieckschaltung, drehstrom, strangstrom, verkettete spannung, delta-schaltung, stern-dreieck-anlauf, 400V]
symbol: Δ
einheit: —
---

Bei der Dreieckschaltung sind die drei Wicklungen oder Lasten in einem geschlossenen Dreieck verbunden. Jede Wicklung liegt direkt an der verketteten Spannung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Drehstrom: Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Sternschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[Verkettete Spannung]]
:::
:::

---

## Aufbau

:::schematic Dreieckschaltung
/schaltplaene/drehstrom_dreieck.svg
:::

Drei Wicklungen bilden ein Dreieck. Jeder Eckpunkt ist an einen Aussenleiter angeschlossen. Kein Neutralleiter.

Symbol: Δ (Delta)

## Spannungsverhältnisse

Jede Wicklung liegt an der vollen verketteten Spannung. Im Netz sind das 400 V.

:::monospace
U_strang = U_verkettet      # in Dreieck: Strangspannung = verkettete Spannung
I_aussen = sqrt(3) * I_strang   # Aussenleiterstrom aus Strangstrom
:::
## Vergleich mit Stern

| | Stern (Y) | Dreieck (Δ) |
|---|---|---|
| Spannung an Wicklung | 230 V | 400 V |
| Neutralleiter | möglich | keiner |
| Strom Aussenleiter | I_strang | √3 × I_strang |
| Leistung | gleich | gleich |

Gleiche Leistung, aber andere Spannungen und Ströme an den Wicklungen.

## Motorwicklung in Dreieck

Höhere Spannung pro Wicklung, mehr Leistung. Betriebsschaltung nach dem Stern-Dreieck-Anlauf.

## Transformatoren

Transformatoren können primär und sekundär je in Stern oder Dreieck geschaltet sein. Die Kombination bestimmt die Phasenlage der Ausgangsspannung. Das ist wichtig wenn Transformatoren parallel betrieben werden.
