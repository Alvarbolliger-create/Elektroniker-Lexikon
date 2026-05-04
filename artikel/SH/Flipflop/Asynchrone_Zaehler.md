---
title: Asynchrone Zähler
kategorie: SH
tags: [zähler, asynchron, ripple-counter, flipflop, binärzähler, frequenzteiler, modulo, glitch, T-flipflop, propagation-delay]
symbol: —
einheit: —
---

Asynchrone Zähler verketten mehrere Flipflops. Der Ausgang jedes Flipflops taktet das nächste. Einfach aufgebaut, aber mit zunehmendem Takt wird er ungenauer.

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops]]
:::
:::vbox
**Verwandte Artikel**
- [[Synchrone Zähler]]
:::
:::vbox
**Führt weiter zu**
- [[Synchrone Zähler]]
:::
:::

---

## Vorwärtszähler

Vier T-Flipflops in Reihe. Jeder dividiert den Takt durch zwei. Zusammen: 4-Bit Binärzähler von 0 bis 15.

Q0 (LSB) schaltet bei jedem Taktimpuls. Q1 bei jedem zweiten. Q2 bei jedem vierten. Q3 (MSB) bei jedem achten.

## Rückwärtszähler

Wie Vorwärtszähler, aber die invertierten Ausgänge (Q_quer) takten das nächste Flipflop. Der Zähler zählt von 15 nach 0.

## Das Ripple-Problem

Die Bits schalten nicht gleichzeitig. Q0 schaltet zuerst, dann mit etwas Verzögerung Q1, dann Q2 und Q3. Bei 4 Flipflops addieren sich vier Laufzeiten.

Bei hohen Frequenzen kann dieser Versatz zu Glitches führen: kurze falsche Zwischenzustände. Für einfache Anwendungen unkritisch, für präzise Schaltungen problematisch.

## Modulo-N Zähler

Durch Rücksetzen beim gewünschten Endwert lässt sich ein Zähler auf jede Zahl begrenzen. Beispiel: Dezimalzähler (0 bis 9) setzt sich bei 10 zurück auf 0.

## Frequenzteiler

Jedes Flipflop im Zähler teilt die Taktfrequenz durch 2:

:::formel
f_Q0 = f_CLK / 2
f_Q1 = f_CLK / 4
f_Q2 = f_CLK / 8
f_Q3 = f_CLK / 16
:::
Ein 4-Bit-Zähler erzeugt vier Teilfrequenzen. Das ist der einfachste Frequenzteiler.

**Modulo-N Teiler**: Mit Rücksetzlogik lässt sich auf beliebiges N teilen.

Beispiel: 10 MHz durch 10 teilen → Modulo-10-Zähler → 1 MHz am Ausgang.

:::tip
Für zeitkritische Anwendungen synchrone Zähler verwenden. Alle Flipflops schalten gleichzeitig, kein Ripple, keine Glitches. Der asynchrone Zähler ist gut wenn Einfachheit wichtiger ist als Präzision.
:::
