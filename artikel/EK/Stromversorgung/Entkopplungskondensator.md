---
title: Entkopplungskondensator (Decoupling)
kategorie: EK
tags: [Decoupling, Bypass, Entkopplung, 100nF, Keramik, Versorgungsspannung, PCB]
symbol: C_bypass
einheit: F
---

Jedes digitale IC benötigt einen Keramikkondensator direkt an den Versorgungspins. Er liefert kurzfristig Strom wenn das IC schaltet und hält die Versorgungsspannung stabil.

:::hbox
:::vbox
**Voraussetzungen**
- [[Kondensator Übersicht]]
- [[PCB Aufbau]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator Typen]]
- [[Wellenwiderstand]]
:::
:::vbox
**Führt weiter zu**
- [[Signalintegrität]]
- [[EMV Pre-Compliance]]
:::
:::

---

## Das Problem: Stromspitzen beim Schalten

Ein digitales IC zieht beim Wechsel eines Ausgangs kurz einen hohen Strom aus der Versorgung. Dieser Strompuls fliesst durch die Leitungsimpedanz der Versorgungsleitungen. Das erzeugt einen kurzen Spannungseinbruch.

Leitungsimpedanz ist nicht nur der ohmschen Widerstand — bei hohen Frequenzen dominiert die Induktivität. Bereits 10 nH Leitungsinduktivität und 100 mA in 1 ns ergeben:

:::monospace
U = L × dI/dt = 10 nH × 100 mA / 1 ns = 1 V    # massiver Einbruch
:::
## Lösung: Lokaler Energiespeicher

Der Entkopplungskondensator sitzt direkt am IC und liefert den Strom lokal. Der lange Weg zur Versorgungsquelle wird überbrückt.

**Faustregel**: 100 nF Keramikkondensator pro VCC-Pin, direkt am IC platziert.

## Warum Keramik?

Keramikkondensatoren haben eine sehr niedrige Eigeninduktivität (ESL) und niedrigen Serienwiderstand (ESR). Sie können hohe Stromspitzen bei Frequenzen bis in den GHz-Bereich liefern.

Elektrolyt-Kondensatoren haben zu hohe ESL und ESR für diesen Zweck. Sie werden ergänzend eingesetzt (typisch 10–100 µF), um niederfrequente Schwankungen zu filtern.

## Mehrstufige Entkopplung

| Kapazität | Typ | Funktion |
|---|---|---|
| 100 pF – 1 nF | Keramik (C0G) | Ultra-HF, direkt am Pad |
| 100 nF | Keramik (X7R) | Standard, ein pro VCC-Pin |
| 1–10 µF | Keramik oder Tantal | Mittelfrequenz, pro IC-Gruppe |
| 10–100 µF | Elektrolyt | Niedrige Frequenzen, pro Spannungsregler |

## Platzierung auf dem PCB

Die Position ist entscheidend. Der Kondensator muss so nah wie möglich am VCC-Pin des ICs sitzen.

**Richtig**: Kondensator zwischen VCC-Pin und GND-Via, direkter Anschluss ohne Umweg.

**Falsch**: Kondensator entfernt vom IC, verbunden über lange Leiterbahn. Die Leiterbahninduktivität macht die Wirkung zunichte.

:::tip
Kondensator-Via (GND) möglichst nah oder direkt unter dem IC platzieren. Auf mehrlagigen PCBs: GND-Lage direkt unter der Signallage für minimale Induktivität.
:::

## Parallel-Resonanz

Zwei parallel geschaltete Kondensatoren unterschiedlicher Grösse bilden zusammen mit deren Induktivitäten eine Parallelresonanzstelle. Dort steigt die Impedanz kurz an. Beim Design auf eine breite, lückenlose Abdeckung des Frequenzbereichs achten.

## Massefläche als Entkopplung

Eine durchgehende Massefläche auf einer inneren Lage wirkt zusammen mit der VCC-Lage wie ein flächiger Kondensator. Das ist der Grund warum mehrlagige PCBs mit Massen- und Versorgungslagen von Natur aus besser entkoppelt sind.
