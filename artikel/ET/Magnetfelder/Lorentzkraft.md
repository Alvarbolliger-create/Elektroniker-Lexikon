---
title: Lorentzkraft
kategorie: ET
tags: [lorentzkraft, magnetfeld, kraft, motor, elektromagnet, linke-hand-regel, ampere, flussdichte]
symbol: F
einheit: N
---

Ein stromdurchflossener Leiter im Magnetfeld erfährt eine Kraft. Das ist die Lorentzkraft. Sie ist das Grundprinzip hinter Elektromotoren.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
:::
:::vbox
**Führt weiter zu**
- [[DC-Motor]]
- [[Schrittmotor]]
:::
:::

---

## Die Kraft

```
F = I * l * B * sin(θ)    # allgemeine Form
F = I * l * B             # vereinfacht wenn Strom senkrecht zu B (θ = 90°)
```

| Grösse | Symbol | Einheit |
|---|---|---|
| Kraft | F | N |
| Strom | I | A |
| Leiterlänge im Feld | l | m |
| Magnetische Flussdichte | B | T |
| Winkel zwischen Strom und B | θ | ° |

Bei θ = 90° (Strom senkrecht zum Feld) ist die Kraft maximal. Bei θ = 0° (Strom parallel zum Feld) ist die Kraft null. Grösserer Strom, stärkeres Feld oder längerer Leiter: mehr Kraft.

## Richtung: Drei-Finger-Regel

Rechte Hand: Daumen zeigt in Stromrichtung, Zeigefinger in Feldrichtung (Nord nach Süd). Mittelfinger zeigt die Kraftrichtung.

Oder: Zeigefinger = Feld (B), Mittelfinger = Strom (I), Daumen = Kraft (F).

## Im Motor

Eine Spule im Magnetfeld. Strom durch die Spule erzeugt eine Kraft auf die Leiter. Diese Kraft dreht die Spule. Das ist ein Elektromotor.

Die Kraft wechselt die Richtung wenn der Strom wechselt. Deshalb braucht ein Gleichstrommotor einen Kommutator um den Strom im richtigen Moment umzupolen.

## Auf bewegte Ladungen

Die Lorentzkraft wirkt auch auf einzelne Ladungsträger in einem Magnetfeld:

```
F = q * v * B * sin(θ)
```

Das ist die Grundlage von Kathodenstrahlröhren und Massenspektrometern.

## Halleffekt

Fliessen Ladungsträger durch einen Leiter in einem senkrechten Magnetfeld, werden sie seitlich abgelenkt. Dadurch entsteht eine messbare Querspannung — die Hallspannung. Sie ist proportional zur Flussdichte B und zum Strom I.

In der Praxis steckt dieses Prinzip in **Hallsensoren**: Sie messen kontaktlos Magnetfelder, Ströme und Positionen. Mehr dazu unter [[Hallsensor]].
