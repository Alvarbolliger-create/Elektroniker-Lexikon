---
title: Elektrische Leistung
kategorie: ET
tags: [leistung, watt, wirkungsgrad, verlustleistung, joule, wärme]
groessen: P|Leistung|W; U|Spannung|V; I|Strom|A; R|Widerstand|Ohm; eta|Wirkungsgrad|—
_status: PORT  # ET_alt/Grundlagen/Elektrische_Leistung.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Wechselstromleistung]]
- [[Leiterwiderstand]]
:::
:::vbox
**Führt weiter zu**
- [[Elektrische Arbeit & Tarif]]
:::
:::

---

Elektrische Leistung beschreibt, wie schnell eine Schaltung Energie umsetzt. Sie ist die Grundlage für jede Dimensionierung — ob Leitungsquerschnitt, Kühlkörper oder Sicherung.

## Grundformel

Die allgemeine Leistungsformel gilt immer — für Gleich- und Wechselstrom (bei Wechselstrom mit Wirkleistungskorrektur, → [[Wechselstromleistung]]).

:::formel
P = U * I    # Leistung P (W) = Spannung (V) mal Strom (A)
:::

**Einheit:** Watt (W). 1 W = 1 V · 1 A.

## Leistung mit nur einer bekannten Grösse

Oft kennt man nur U und R oder nur I und R. Durch Einsetzen des ohmschen Gesetzes erhält man zwei weitere nützliche Formen:

::: hbox
:::formel
P = U^2 / R    # wenn U und R bekannt
:::

:::formel
P = I^2 * R    # wenn I und R bekannt
:::
:::

:::tip
P = I² · R ist die wichtigste Form für Verlustleistungen in Leitungen und Widerständen — der Strom geht quadratisch ein. Doppelter Strom → viermal die Verluste.
:::

## Wirkungsgrad

Jeder reale Wandler (Netzteil, Motor, Trafo) hat Verluste. Der Wirkungsgrad eta gibt an, welcher Anteil der zugeführten Leistung nutzbar abgegeben wird.

:::formel
eta = P_ab / P_zu
:::

| eta | Bedeutung | Beispiel |
|---|---|---|
| 1,0 (100 %) | Verlustfrei (ideal) | Nur in Theorie |
| 0,95 (95 %) | Sehr gut | Modernes Schaltnetzteil |
| 0,85 (85 %) | Gut | Trafo unter Last |
| kleiner 0,5 (50%) | Schlecht | Glühlampe (90 % Wärme) |

Die Verlustleistung ergibt sich aus:

:::formel
P_v = P_zu - P_ab    # Verluste als Differenz
:::

:::monospace
Beispiel: Netzteil P_zu = 100 W, P_ab = 85 W
eta = 85 / 100 = 0.85 (85 %)
P_v = 100 - 85 = 15 W (als Wärme abzuführen)
:::

## Wärmeleistung (Joule'sche Erwärmung)

Fliesst Strom durch einen Widerstand, wird elektrische Energie in Wärme umgewandelt. Diese **Verlustleistung** erwärmt Leiter, Widerstände und Halbleiter. Thermische Dimensionierung ist bei höheren Strömen immer zu prüfen.

:::warning
Widerstandsbauteile und Leitungen dürfen ihre maximale Verlustleistung nicht dauerhaft überschreiten. Typische Folge: Alterung, Brand. Leitungsquerschnitt und Bauteilbelastbarkeit stets aus Datenblatt oder Norm (z. B. NIN in der Schweiz) entnehmen.
:::
