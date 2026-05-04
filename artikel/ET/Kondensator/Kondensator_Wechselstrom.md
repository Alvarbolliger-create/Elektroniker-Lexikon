---
title: Kondensator im Wechselstrom
kategorie: ET
tags: [kondensator, wechselstrom, impedanz, kapazitiver widerstand, phasenverschiebung, reaktanz, X_C, frequenzabhängigkeit, blindwiderstand]
symbol: X_C
einheit: Ω
---

Im Wechselstromkreis wirkt ein Kondensator wie ein frequenzabhängiger Widerstand. Je höher die Frequenz, desto tiefer der Widerstand.

:::hbox
:::vbox
**Voraussetzungen**
- [[Auf- und Entladung]]
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Impedanz]]
- [[Spule im Wechselstrom]]
:::
:::vbox
**Führt weiter zu**
- [[RLC-Schaltungen]]
:::
:::

---

## Kapazitiver Widerstand

:::monospace
X_C = 1 / (2 * pi * f * C)     # gilt für reine Sinusspannung
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Kapazitiver Widerstand | X_C | Ω |
| Frequenz | f | Hz |
| Kapazität | C | F |

Bei 0 Hz (Gleichstrom) ist X_C unendlich: kein Strom fliesst. Bei sehr hohen Frequenzen geht X_C gegen null: fast kein Widerstand.

## Phasenverschiebung

:::plot
var: t
range: 0, 12.56
xlabel: Zeit
ylabel: Amplitude
Spannung U: sin(t)
Strom I (+90°): sin(t + 1.5708)
:::

Der Strom eilt der Spannung um 90° voraus. Der Kondensator lädt sich auf, bevor die Spannung ihr Maximum erreicht.

Das ist wichtig bei Leistungsberechnungen: Ein reiner Kondensator verbraucht keine Wirkleistung. Energie wird nur zwischengespeichert.

## Beispiel

100 nF Kondensator bei verschiedenen Frequenzen:

| Frequenz | X_C |
|---|---|
| 100 Hz | 15 920 Ω |
| 1 kHz | 1 592 Ω |
| 10 kHz | 159 Ω |
| 100 kHz | 15.9 Ω |
| 1 MHz | 1.6 Ω |

## Komplexe Impedanz

Für Phasenberechnungen und RLC-Analyse wird der Kondensator als komplexe Impedanz geschrieben:

:::monospace
ω   = 2 * π * f
Z_C = 1 / (j * ω * C) = -j / (ω * C)
:::
Der negative imaginäre Anteil entspricht der 90°-Phasenverschiebung (Strom eilt vor). In Simulationen und Filterberechnungen wird ausschliesslich diese Schreibweise verwendet.
