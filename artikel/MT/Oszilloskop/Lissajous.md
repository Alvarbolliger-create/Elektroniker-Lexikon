---
title: XY-Betrieb & Lissajous-Figuren
kategorie: MT
tags: [lissajous, XY-betrieb, phasenmessung, oszilloskop, phasenwinkel, frequenzvergleich, ellipse, arcsin, THD]
symbol: φ
einheit: °
---

Im XY-Betrieb zeichnet das Oszilloskop nicht Zeit auf der X-Achse, sondern die Spannung eines zweiten Kanals. Das Ergebnis sind Lissajous-Figuren — ihre Form verrät Phasenwinkel und Frequenzverhältnis.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszilloskop: Aufbau & Bedienung]]
- [[Triggerung]]
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Zeigerdiagramm (Phasor)]]
- [[Impedanz]]
:::
:::

---

## XY-Betrieb aktivieren

Statt Zeit-Basis: Kanal 1 → X-Ablenkung, Kanal 2 → Y-Ablenkung. Das Gerät zeigt die Lissajous-Figur direkt an.

Moderne Digitalspeicher-Oszilloskope: Menü → Zeitbasis → XY-Mode.

## Lissajous-Figur für gleiche Frequenz: Phasenmessung

Zwei Signale gleicher Frequenz, verschiedener Phase:

:::formel
U1 = U_peak × sin(ω × t)
U2 = U_peak × sin(ω × t + φ)
:::
Die entstehende Figur ist eine Ellipse. Aus der Ellipse kann der Phasenwinkel φ abgelesen werden.

**Messung**:
1. Ellipse aufzeichnen
2. Schnittpunkt der Ellipse mit der Y-Achse ablesen: Wert A
3. Maximale Y-Auslenkung ablesen: Wert B

:::monospace
sin(φ) = A / B    →    φ = arcsin(A / B)
:::
**Sonderfälle**:
- φ = 0°: Gerade Linie (diagonal, Steigung positiv)
- φ = 90°: Kreis (bei gleichen Amplituden)
- φ = 180°: Gerade Linie (diagonal, Steigung negativ)

## Frequenzverhältnis aus der Figur

Bei unterschiedlichen Frequenzen entstehen komplexere Figuren. Das Frequenzverhältnis lässt sich aus der Zahl der Schnittpunkte ablesen:

:::formel
f1 / f2 = Anzahl Tangentialpunkte an horizontaler Linie / an vertikaler Linie
:::
| Verhältnis f1:f2 | Figurtyp |
|---|---|
| 1:1 | Ellipse oder Gerade |
| 1:2 | 8-förmige Kurve |
| 1:3 | Kleeblatt |
| 2:3 | Komplexeres Muster |

## Praktische Anwendungen

**Phasenmessung**: Phasenverschiebung zwischen zwei Signalen messen (z.B. Eingang/Ausgang eines Filters, RLC-Schaltung, Transformator).

**Frequenzvergleich**: Ist eine unbekannte Frequenz ein ganzzahliges Vielfaches einer Referenz?

**Verzerrungsmessung**: Ein unverzerrtes Signal ergibt eine glatte Ellipse. Oberschwingungen verursachen Kräuselungen auf der Kurve.

**THD-Messung (grob)**: Ein sauberes sinusförmiges Signal → glatte Ellipse. Verzerrter Ausgang → Abweichungen sichtbar.

## Vorteil gegenüber Zeitbereichsmessung

Die direkte Phasenmessung im Zeitbereich ist fehlerträchtig (Cursors exakt auf Nulldurchgänge setzen). Die Lissajous-Methode ist geometrisch robust und oft genauer.

:::tip
Für genaue Messungen beide Kanäle auf gleiche Skalierung stellen und die Triggerstabilität nicht beachten — im XY-Betrieb ist kein Trigger nötig.
:::
