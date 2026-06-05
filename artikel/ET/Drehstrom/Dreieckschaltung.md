---
title: Dreieckschaltung
kategorie: ET
tags: [dreieckschaltung, drehstrom, strangstrom, leiterstrom, motor, kondensator]
groessen: U_str|Strangspannung|V; U_L|Leiterspannung|V; I_str|Strangstrom|A; I_L|Leiterstrom|A
_status: PORT  # ET_alt/Drehstrom/Dreieckschaltung.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Drehstrom Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Sternschaltung]]
- [[Stern-Dreieck-Transformation]]
:::
:::

---

Bei der Dreieckschaltung sind die drei Lastwiderstände (oder Wicklungen) in einem Dreieck verbunden — jede Last liegt direkt zwischen zwei Phasen. Die Dreieckschaltung wird für höhere Ströme und in Motoren für den Nennbetrieb verwendet.

## Aufbau

Jede Last ist zwischen zwei Phasenleiter geschaltet. Es gibt keinen Sternpunkt und keinen Neutralleiter. Alle drei Lasten liegen an der vollen Leiterspannung (400 V im CH-Netz).

:::schematic
/schaltplaene/drehstrom/dreieckschaltung.svg
:::

## Strom und Spannung

Die **Strangspannung ist gleich der Leiterspannung** — jede Last liegt direkt zwischen zwei Leitern:

:::formel
U_str = U_L
:::

Der **Leiterstrom** ist grösser als der Strangstrom — weil sich am Verbindungspunkt immer zwei Strangströme überlagern:

:::formel
I_L = I_str * sqrt(3)
:::

## Vergleich Stern- und Dreieckschaltung

| Grösse | Sternschaltung | Dreieckschaltung |
|---|---|---|
| Strangspannung U_str | U_L / sqrt(3) = 230 V | U_L = 400 V |
| Strangstrom I_str | I_L | I_L / sqrt(3) |
| Neutralleiter | Möglich | Nicht vorhanden |
| Leistung (sym.) | 3 · U_str · I_str · cos phi | 3 · U_str · I_str · cos phi |

Bei gleicher Last in Dreieck statt Stern liegt die dreifache Leistung an — die Strangspannung ist um sqrt(3) grösser und damit die Leistung um den Faktor 3 höher.

## Anwendungen

**Motor im Dreieck**: Nennbetrieb bei voller Spannung (400 V an jeder Wicklung). Beim Anlaufen oft zuerst in Sternschaltung (230 V pro Wicklung, reduzierter Anlaufstrom) → [[Stern-Dreieck-Transformation]].

**Kompensationskondensatoren**: Kondensatorbänke zur Blindleistungskompensation werden oft in Dreieck geschaltet, weil sie dort direkt an der Leiterspannung liegen → höhere Kompensationsleistung.

## Leistung

:::formel
P = 3 * U_str * I_str * cos(phi)    # Gesamtleistung, wie bei Stern
:::

Die Gesamtleistungsformel ist identisch mit der Sternschaltung, wenn mit Strangspannung und Strangstrom gerechnet wird. Mit Leitergrössen: P = sqrt(3) · U_L · I_L · cos(phi).

## Rechenbeispiel

:::monospace
Gegeben: Symmetrische Last, Z = 46 Ω pro Strang, cos φ = 0.85, CH-Netz (U_L = 400 V)

U_str = U_L   = 400 V               (Dreieck: Strang = Leiter)
I_str = U_str / Z = 400 / 46 = 8.70 A
I_L   = I_str * sqrt(3) = 8.70 * 1.732 = 15.06 A
P     = 3 * 400 * 8.70 * 0.85      = 8874 W ≈ 8.9 kW

Vergleich mit Stern (gleiche Last, gleiche Netzspannung):
Stern:   P ≈ 3 kW, I_L ≈ 5 A
Dreieck: P ≈ 9 kW, I_L ≈ 15 A  → 3× mehr Leistung, 3× mehr Strom
:::
