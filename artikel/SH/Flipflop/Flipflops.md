---
title: Flipflops
kategorie: SH
tags: [flipflop, RS, D, JK, T, speicher, takt, digital, master-slave, taktflanke, NAND, register, latch]
symbol: Q
einheit: —
---

Ein Flipflop speichert ein einzelnes Bit. Es hat zwei stabile Zustände und wechselt nur auf ein Steuersignal hin. Flipflops sind die Grundlage aller digitalen Speicher und Zähler.

:::hbox
:::vbox
**Voraussetzungen**
- [[Schaltalgebra]]
- [[Logikgatter]]
:::
:::vbox
**Verwandte Artikel**
:::
:::vbox
**Führt weiter zu**
- [[Asynchrone Zähler]]
- [[Schieberegister]]
:::
:::

---

## RS-Flipflop

Das einfachste Flipflop. Zwei Eingänge: S (Set) und R (Reset). S = 1 setzt Q auf 1. R = 1 setzt Q auf 0. Beide auf 1 gleichzeitig ist verboten.

Kann aus zwei NAND- oder NOR-Gattern gebaut werden.

## D-Flipflop

Nur ein Dateneingang D und ein Takteingang CLK. Bei steigender Taktflanke wird D in Q übernommen. Danach gespeichert bis zum nächsten Takt.

Das ist der praktischste Flipfloptype. Fast alle Register in Mikroprozessoren sind D-Flipflops.

### Interner Aufbau aus NAND-Gattern

Ein taktgesteuertes D-Flipflop lässt sich aus 4 NAND-Gattern aufbauen:

:::schematic
/Diagramm/flipflops_0.svg
:::
Vereinfacht: Zwei SR-Flipflops (aus je 2 NAND-Gattern) werden verschaltet. Der Takt steuert, wann D eingelesen werden darf.

### Master-Slave-Konfiguration (flankengetaktetes D-FF)

Ein einfaches taktgesteuertes Flipflop ist **pegelgesteuert**: es übernimmt D solange CLK HIGH ist — bei langen CLK-HIGH-Phasen "sieht" das FF auch Änderungen von D, was unerwünscht ist.

Lösung: **Master-Slave-D-Flipflop**:

:::monospace
D → [Master-Latch (CLK=1)] → [Slave-Latch (CLK=0, invertierter Takt)] → Q
:::
- **Master** ist offen (übernimmt D) wenn CLK = 1
- **Slave** ist offen wenn CLK = 0 (invertierter Takt)
- Q ändert sich nur beim Übergang CLK 1→0 (fallende Flanke)
- Während CLK = 1 hält der Slave Q fest — D kann sich ändern ohne Wirkung auf Q

Moderne Flipflops sind meist **steigende Flanke**: Master reagiert auf CLK=0, Slave auf steigende Flanke — das Ergebnis ist gleich, nur auf der anderen Flanke.

## JK-Flipflop

Wie RS, aber der verbotene Zustand (beide 1) ist definiert: er toggelt den Ausgang. J = Set, K = Reset. J=K=1 wechselt den Zustand.

## T-Flipflop (Toggle)

Ein Eingang T. Bei T = 1 und Taktflanke wechselt Q den Zustand. Grundbaustein für Frequenzteiler und Zähler.

## Wahrheitstabelle D-Flipflop

:::truth CLK,D | Q (nach Flanke)
↑,0 | 0
↑,1 | 1
0,x | Q (unverändert)
:::

:::info
Getaktete (synchrone) Flipflops reagieren nur auf die Taktflanke. Ungetaktete (asynchrone) reagieren sofort auf die Eingänge. Für digitale Schaltungen werden fast immer getaktete Flipflops verwendet.
:::
