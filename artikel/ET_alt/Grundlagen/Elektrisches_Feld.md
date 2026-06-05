---
title: Elektrisches Feld
kategorie: ET
tags: [elektrisches feld, feldlinien, potential, ladung, coulomb, permittivität]
groessen: F|Kraft|N; Q|Ladung|C; r&d|Abstand|m; ε|Permittivität|F/m; E|elektrische Feldstärke|N/C
---

Jede elektrische Ladung erzeugt ein Kraftfeld um sich herum. Dieses Feld wirkt auf andere Ladungen, auch ohne direkten Kontakt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Führt weiter zu**
- [[Kondensator (Übersicht)]]
:::
:::

---

## Feldlinien

Feldlinien zeigen die Richtung der Kraft auf eine positive Ladung. Sie verlaufen von Plus nach Minus. Wo die Linien dichter sind, ist das Feld stärker.

Zwischen zwei parallelen Platten (wie im Kondensator) verlaufen die Feldlinien gleichmässig und parallel. Das nennt man ein homogenes Feld.

## Coulombsches Gesetz

Zwei Ladungen ziehen sich an oder stossen sich ab. Die Kraft hängt vom Produkt der Ladungen und vom Abstand ab:

:::formel
F = (1 / (4 * π * ε)) * (Q1 * Q2) / r²
:::

Verdoppelt sich der Abstand, sinkt die Kraft auf ein Viertel. Das ist das gleiche Abstandsgesetz wie bei der Gravitation.

## Feldstärke

Die elektrische Feldstärke E gibt an, wie stark das Feld an einem Punkt ist.

:::formel
E = U / d          # homogenes Feld zwischen zwei parallelen Platten
E = F / Q          # Kraft pro Ladung an einem Punkt
:::
## Permittivität

Im Vakuum gilt ε₀ = 8.854 × 10⁻¹² F/m. In Materialien wird das Feld durch die relative Permittivität εᵣ abgeschwächt:

:::formel
ε = εᵣ * ε₀
:::
Luft hat εᵣ ≈ 1, Glas etwa 4–10, spezielle Keramiken bis über 10 000. Das ist der Grund warum Kondensatoren mit Dielektrikum viel mehr Kapazität erreichen als ohne.

## Durchschlag

Jedes Material hält nur eine begrenzte Feldstärke aus. Wird sie überschritten, entlädt sich das Feld schlagartig. In Luft liegt dieser Wert bei etwa 3 MV/m das ist der physikalische Ursprung des Blitzes.

Bei Kondensatoren nennt man diesen Wert die Durchbruchspannung. Sie hängt direkt von d und εᵣ des Dielektrikums ab.

## Wirkung auf geladene Teilchen

Ein elektrisches Feld übt auf jede geladene Teilchen eine Kraft aus:

:::formel
F = Q * E
:::
In der Elektronik erscheint dieses Prinzip im MOSFET: Das Gatefeld steuert die Ladungsträger im Kanal. In älteren CRT-Bildschirmen lenkte es den Elektronenstrahl.
