---
title: Leiterwiderstand
kategorie: ET
tags: [leiterwiderstand, spezifischer widerstand, stromdichte, leitfähigkeit, material, temperaturkoeffizient]
groessen: R|Widerstand|Ω; ρ|spez. Widerstand|Ω*mm2/m; l|Leiterlänge|m; A|Querschnitt|mm2; J|Stromdichte|A/mm2; σ|elektr. Leitfähigkeit|S/m; α|Temperaturkoeffizient|1/K
---
 
Jeder elektrische Leiter setzt dem Stromfluss einen gewissen Widerstand entgegen. Dieser hängt von der Geometrie des Leiters und den spezifischen Materialeigenschaften ab.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektrische Leistung]]
:::
:::vbox
**Führt weiter zu**
- [[Temperaturabhängigkeit]]
- [[Leitungsschutz]]
:::
:::

---

## Geometrischer Widerstand

Der Widerstand eines Leiters wird durch seine Länge und seine Querschnittsfläche bestimmt. Ein langer, dünner Draht hat einen höheren Widerstand als ein kurzer, dicker Draht.

:::formel
R = ρ * l / A
:::

Verdoppelt man die Länge eines Leiters, verdoppelt sich der Widerstand. Verdoppelt man hingegen den Querschnitt, halbiert sich der Widerstand.

## Leitfähigkeit und Material

Das Material bestimmt, wie leicht sich Elektronen durch das Gitter bewegen können. Der spezifische Widerstand (ρ) ist eine Materialkonstante. Die elektrische Leitfähigkeit (σ) ist der Kehrwert davon.

:::formel
σ = 1 / ρ
:::

Silber und Kupfer haben die höchste Leitfähigkeit. Aluminium wird oft für Freileitungen verwendet, da es zwar schlechter leitet als Kupfer, aber wesentlich leichter und günstiger ist.

## Stromdichte

Die Stromdichte J gibt an, wie viel Strom durch eine bestimmte Querschnittsfläche fließt. Sie ist entscheidend für die Erwärmung eines Leiters.

:::formel
J = I / A
:::

In der Praxis darf eine maximale Stromdichte nicht überschritten werden, damit die Isolierung der Leitung nicht durch zu hohe Temperaturen schmilzt.

## Temperaturabhängigkeit

Bei Metallen steigt der Widerstand mit der Temperatur, da die Gitteratome stärker schwingen und den Stromfluss behindern. Man nennt sie Kaltleiter (PTC).

:::formel
R_warm = R_20 * (1 + α * Δ_T)
:::

Der Temperaturkoeffizient alpha gibt die relative Widerstandsänderung pro Kelvin an. Für Kupfer beträgt dieser Wert etwa 0,0039 1/K.

## Elektrische Leistung am Widerstand

Wenn Strom durch einen Widerstand fließt, wird elektrische Energie in Wärme umgewandelt. Dies führt zu Verlusten in Leitungen, wird aber in Heizelementen bewusst genutzt.

:::formel
P = I^2 * R
:::

Da der Strom im Quadrat in die Formel eingeht, steigen die Verluste bei einer Verdopplung der Stromstärke auf das Vierfache an. Deshalb wird Strom über weite Strecken mit Hochspannung übertragen, um die Stromstärke gering zu halten.