---
title: Stern-Dreieck-Transformation
kategorie: ET
tags: [stern, dreieck, transformation, netzwerkvereinfachung, Y, delta]
groessen: R_Y|Sternwiderstand|Ohm; R_D|Dreieckwiderstand|Ohm
_status: PORT  # ET_alt/Schaltkreise/Stern_Dreieck_Transformation.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[Drehstrom Grundlagen]]
:::
:::

---

Die Stern-Dreieck-Transformation erlaubt es, eine Dreieckschaltung aus drei Widerständen durch eine äquivalente Sternschaltung zu ersetzen — und umgekehrt. Damit lassen sich Netzwerke vereinfachen, die weder reine Reihen- noch Parallelschaltungen sind.

:::schematic
/schaltplaene/schaltkreise/stern_dreieck_transformation.svg
:::

## Dreieck → Stern

Ein Dreieck mit den Widerständen R12, R23, R31 (zwischen den Knoten 1-2, 2-3, 3-1) wird durch einen Stern mit R1, R2, R3 (von Knoten 1, 2, 3 zum Sternpunkt) ersetzt:

:::hbox
:::formel
R1 = R12 * R31 / (R12 + R23 + R31)
:::
:::formel
R2 = R12 * R23 / (R12 + R23 + R31)
:::
:::formel
R3 = R23 * R31 / (R12 + R23 + R31)
:::
:::

**Merkregel**: Der Sternwiderstand am Knoten n ist das Produkt der beiden angrenzenden Dreieckwiderstände geteilt durch die Summe aller drei.

## Stern → Dreieck

Ein Stern mit R1, R2, R3 wird in einen Dreieck mit R12, R23, R31 umgewandelt:

:::hbox
:::formel
R12 = R1 + R2 + R1 * R2 / R3
:::
:::formel
R23 = R2 + R3 + R2 * R3 / R1
:::
:::formel
R31 = R3 + R1 + R3 * R1 / R2
:::
:::

**Merkregel**: Dreieckwiderstand = Summe der beiden Sternwiderstände + ihr Produkt geteilt durch den dritten.

**Sonderfall: Symmetrisches Netz** (R1 = R2 = R3 = R_Y):

:::formel
R_D = 3 * R_Y    # Dreieck ist immer dreimal grösser als Stern
:::

## Wann anwenden?

Die Transformation wird angewendet, wenn ein Netzwerk weder als Reihe noch als Parallelschaltung vereinfacht werden kann:

| Situation | Vorgehen |
|---|---|
| Brückennetzwerke (z. B. Wheatstone nicht abgeglichen) | Dreieck → Stern, dann Reihe/Parallel |
| Motor-Anlaufschaltung | Stern (Anlauf) → Dreieck (Nennbetrieb) → [[Drehstrom Grundlagen]] |
| Allgemeines Dreinetz | Transformation auf Sternform, dann Analyse |

:::monospace
Beispiel Symmetrie: R_Y = 30 Ohm (Stern)
R_D = 3 * 30 = 90 Ohm (äquivalenter Dreieck)
:::

:::tip
In der Drehstromtechnik nutzt die Stern-Dreieck-Anlaufschaltung genau dieses Prinzip: Motor startet in Stern (30/sqrt(3) = niedrigere Spannung pro Wicklung → kleinerer Anlaufstrom), schaltet dann auf Dreieck (volle Leiterspannung pro Wicklung → Nennmoment).
:::
