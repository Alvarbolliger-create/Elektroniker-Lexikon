---
title: Sternschaltung
kategorie: ET
tags: [sternschaltung, drehstrom, neutralleiter, strangspannung, leiterspannung, unsymmetrisch]
groessen: U_str|Strangspannung|V; U_L|Leiterspannung|V; I_str|Strangstrom|A; I_L|Leiterstrom|A
_status: PORT  # ET_alt/Drehstrom/Sternschaltung.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Drehstrom Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Dreieckschaltung]]
- [[Stern-Dreieck-Transformation]]
:::
:::

---

Bei der Sternschaltung werden alle drei Lastwiderstände (oder Wicklungen) an einem gemeinsamen Sternpunkt zusammengeführt. Sie ist die Standardschaltung im Europäischen Niederspannungsnetz — 230 V Strangspannung, 400 V Leiterspannung.

## Aufbau

Jede Phase L1, L2, L3 ist mit einem Ende der Last verbunden. Die anderen Enden treffen sich im **Sternpunkt** (Mittelpunkt). Der Neutralleiter N verbindet den Sternpunkt mit dem Neutral des Netzes.

:::schematic
/schaltplaene/drehstrom/sternschaltung.svg
:::

## Strom und Spannung

In der Sternschaltung gilt: Der **Leiterstrom ist gleich dem Strangstrom** — es gibt nur einen Strompfad pro Phase.

:::formel
I_L = I_str
:::

Die Leiterspannung (400 V) und Strangspannung (230 V) sind über sqrt(3) verknüpft:

:::formel
U_L = U_str * sqrt(3)
:::

## Symmetrische Last

Bei gleichen Impedanzen auf allen drei Phasen (symmetrische Last) fliesst im Neutralleiter kein Strom (die drei Ströme heben sich auf). Der Neutralleiter ist dann nicht nötig — er ist aber bei asymmetrischer Last unerlässlich.

## Asymmetrische Last

Wenn die Lasten ungleich sind (z. B. in einem Wohnhaus mit unterschiedlichen Verbrauchern pro Phase), fliesst ein **Ausgleichsstrom** im Neutralleiter. Fehlt der Neutralleiter bei asymmetrischer Last, verschieben sich die Strangspannungen — einzelne Phasen können zu hohe oder zu tiefe Spannung haben.

:::warning
In Niederspannungsnetzen (TN-S-System) darf der Neutralleiter nicht unterbrochen werden, solange asymmetrische Lasten angeschlossen sind. Sicherungen im Neutralleiter sind verboten (NIN-Vorschrift in der Schweiz).
:::

## Leistung

:::formel
P = 3 * U_str * I_str * cos(phi)    # Gesamtleistung (symmetrisch)
:::

Equivalent mit Leitergrössen: P = sqrt(3) · U_L · I_L · cos(phi) (→ [[Drehstrom Grundlagen]]).

## Rechenbeispiel

:::monospace
Gegeben: Symmetrische Last, Z = 46 Ω pro Strang, cos φ = 0.85, CH-Netz (U_L = 400 V)

U_str = U_L / sqrt(3) = 400 / 1.732 = 231 V
I_str = U_str / Z    = 231 / 46    = 5.02 A
I_L   = I_str        = 5.02 A       (Stern: Leiter = Strang)
P     = 3 * U_str * I_str * cos φ
      = 3 * 231 * 5.02 * 0.85      = 2960 W ≈ 3 kW

Probe: P = sqrt(3) * 400 * 5.02 * 0.85 = 2960 W ✓
:::
