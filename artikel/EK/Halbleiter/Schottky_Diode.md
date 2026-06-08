---
title: Schottky-Diode
kategorie: EK
kapitel: Halbleiter
tags: [schottky, schottky-diode, metall-halbleiter, freilaufdiode, schaltregler, durchlassspannung, reverse-recovery, majority carrier, schnell]
groessen: U_F|Durchlassspannung|V; t_rr|Sperrerholzeit|ns; I_R|Sperrstrom|µA
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[Diode]]
- [[DC-DC-Wandler]]
:::
:::vbox
**Führt weiter zu**
- [[DC-DC-Wandler]]
- [[Schaltregler Topologien]]
:::
:::

---

Die Schottky-Diode nutzt einen Metall-Halbleiter-Übergang statt eines pn-Übergangs. Dadurch ist sie erheblich schneller und hat eine tiefere Durchlassspannung — auf Kosten eines höheren Sperrstroms.

## Aufbau: Metall-Halbleiter-Übergang

Statt zweier Halbleiterschichten berühren sich ein Metall (z. B. Molybdän, Platin) und ein n-dotierter Halbleiter. An dieser Grenzfläche entsteht ebenfalls eine Potentialbarriere — aber ohne Minoritätsladungsträger im n-Gebiet.

Das ist der entscheidende Unterschied:

| Eigenschaft | PN-Diode | Schottky-Diode |
|---|---|---|
| Übergangsmaterial | p-Halbleiter / n-Halbleiter | Metall / n-Halbleiter |
| Ladungsträger | Majoritäts- und Minoritätsträger | Nur Majoritätsträger |
| Durchlassspannung U_F | 0.6–0.8 V | 0.15–0.45 V |
| Sperrerholzeit t_rr | 4 ns – 4 µs | < 1 ns |
| Sperrstrom I_R | sehr klein (nA) | grösser (µA) |
| Max. Sperrspannung | bis 1000 V | typisch 20–200 V |

## Warum so schnell?

In einer PN-Diode müssen beim Wechsel von Durchlass auf Sperr die Minoritätsladungsträger (Löcher im n-Gebiet, Elektronen im p-Gebiet) erst ausgeräumt werden. Diese **Sperrerholzeit t_rr** begrenzt die Schaltgeschwindigkeit auf einige Nanosekunden bis Mikrosekunden.

Die Schottky-Diode hat keine Minoritätsträger. Sie wechselt sofort in den Sperrzustand — t_rr < 1 ns. Das ermöglicht Betrieb bei Schaltfrequenzen von > 1 MHz.

## Schaltsymbol

:::schematic Schottky-Diode
/schaltplaene/symbole/D_S.svg
:::

Wie die normale Diode, aber die Kathoden-Linie hat beidseitig gebogene Enden (S-Form).

## Anwendungen

**Freilaufdiode in Schaltreglern**: Bei jedem Schaltvorgang fliesst der Induktivitätsstrom durch die Freilaufdiode. Bei 500 kHz Schaltfrequenz und 2 A Strom bedeutet jeder Sperrstrom-Impuls Verlustleistung. Eine Schottky spart hier erheblich gegenüber einer 1N4007.

**Gleichrichter in Netzteilen**: Weniger Verlustleistung = weniger Wärme. Bei 5 V Ausgang und 1 A: Schottky (0.35 V Abfall) statt Standard (0.7 V) spart 350 mW — das ist 7 % Effizienzgewinn.

**Ausgangsschutz bei Mikrocontrollern**: Tiefere Durchlassspannung schützt I/O-Pins effektiver.

:::info
Schottky-Dioden haben eine höhere Temperaturabhängigkeit des Sperrstroms als PN-Dioden. Bei hohen Temperaturen (> 100 °C) kann der Sperrstrom im mA-Bereich liegen und die Diode thermisch durchgehen.
:::

## Typische Bauteile

| Typ | I_F | U_R | U_F | Einsatz |
|---|---|---|---|---|
| 1N5817 | 1 A | 20 V | 0.45 V | Allgemein |
| 1N5819 | 1 A | 40 V | 0.60 V | Standard Schaltregler |
| SS34 | 3 A | 40 V | 0.40 V | SMD Schaltregler |
| MBRS360 | 3 A | 60 V | 0.42 V | Leistungsnetzteile |
