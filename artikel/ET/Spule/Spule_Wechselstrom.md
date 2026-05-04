---
title: Spule im Wechselstrom
kategorie: ET
tags: [spule, wechselstrom, impedanz, induktiver widerstand, phasenverschiebung, reaktanz, X_L, frequenzabhängigkeit, blindwiderstand]
symbol: X_L
einheit: Ω
---

Im Wechselstromkreis wirkt eine Spule wie ein frequenzabhängiger Widerstand. Je höher die Frequenz, desto höher der Widerstand.

:::hbox
:::vbox
**Voraussetzungen**
- [[Selbstinduktion]]
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Impedanz]]
- [[Kondensator im Wechselstrom]]
:::
:::vbox
**Führt weiter zu**
- [[RLC-Schaltungen]]
- [[Transformator]]
:::
:::

---

## Induktiver Widerstand

:::monospace
X_L = 2 * pi * f * L     # gilt für reine Sinusspannung
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Induktiver Widerstand | X_L | Ω |
| Frequenz | f | Hz |
| Induktivität | L | H |

Bei 0 Hz (Gleichstrom) ist X_L null: die Spule ist ein normaler Widerstand. Bei hohen Frequenzen steigt X_L stark an.

## Phasenverschiebung

:::plot
var: t
range: 0, 12.56
xlabel: Zeit
ylabel: Amplitude
Spannung U: sin(t)
Strom I (−90°): sin(t - 1.5708)
:::

Der Strom eilt der Spannung um 90° nach. Die Spannung erreicht ihr Maximum bevor der Strom nachgezogen hat.

Wie beim Kondensator gilt: Eine reine Spule (ohne ohmschen Widerstand) verbraucht keine Wirkleistung.

## Beispiel

1 mH Spule bei verschiedenen Frequenzen:

| Frequenz | X_L |
|---|---|
| 100 Hz | 0.63 Ω |
| 1 kHz | 6.3 Ω |
| 10 kHz | 63 Ω |
| 100 kHz | 628 Ω |
| 1 MHz | 6 280 Ω |

## Komplexe Impedanz

Für Phasenberechnungen und RLC-Analyse wird die Spule als komplexe Impedanz geschrieben:

:::monospace
ω   = 2 * π * f
Z_L = j * ω * L
:::
Der positive imaginäre Anteil entspricht der 90°-Phasenverschiebung (Strom eilt nach). Zusammen mit dem Kondensator `Z_C = 1 / (j * ω * C)` lassen sich RLC-Schaltungen vollständig im Komplexen berechnen.
