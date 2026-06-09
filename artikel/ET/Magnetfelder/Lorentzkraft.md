---
title: Lorentzkraft
kategorie: ET
tags: [lorentzkraft, magnetfeld, kraft, leiter, motor, generator, linke-hand-regel, rechte-hand-regel, parallele-leiter, anziehung, abstossung, feldlinienverdichtung, ampere-definition]
groessen: F|Kraft|N; I|Strom|A; l|Leiterlänge|m; B|Flussdichte|T; v|Geschwindigkeit|m/s; q|Ladung|C; a|Leiterabstand|m; mu_0|magnetische Feldkonstante|H/m
_status: PORT  # ET_alt/Magnetfelder/Lorentzkraft.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Führt weiter zu**
- [[DC-Motor]]
:::
:::

---

Die Lorentzkraft ist die Kraft, die ein Magnetfeld auf einen stromdurchflossenen Leiter oder eine bewegte Ladung ausübt. Sie ist die Ursache für die Drehbewegung in Elektromotoren und die Grundlage für die Geschwindigkeitsinduktion in Generatoren.

## Kraft auf einen stromdurchflossenen Leiter

:::schematic
/abbildungen/magnetfelder/lorentzkraft_leiter.svg
:::

:::formel
F = I * l * B * sin(alpha)    # alpha = Winkel zwischen Leiter und Feldlinien
:::

**Was bedeutet sin(alpha)?** Der Sinus kommt daher, dass nur der Teil des Leiters Kraft erfährt, der tatsächlich Feldlinien "schneidet" — also senkrecht zu B liegt. Stellt man sich den Leiter in Bezug auf die Feldlinien vor, kann man den Leiter in zwei Komponenten zerlegen:

- Komponente **quer** zu B (Länge l · sin(alpha)): diese schneidet Feldlinien → erzeugt Kraft
- Komponente **parallel** zu B (Länge l · cos(alpha)): diese liegt in Richtung der Feldlinien → erzeugt keine Kraft

| Winkel alpha | sin(alpha) | Kraft |
|---|---|---|
| 0° (Leiter parallel zu B) | 0 | keine Kraft |
| 45° | 0,707 | 71 % der Maximalkraft |
| 90° (Leiter senkrecht zu B) | 1 | maximale Kraft |

Im Elektromotor werden die Leiter deshalb so eingebaut, dass sie möglichst senkrecht zum Magnetfeld liegen (alpha = 90°).

## Richtungsregel

**Linke-Hand-Regel** (UVW-Regel für Motorbetrieb):
- **Zeigefinger** → Feldrichtung B (Nord nach Süd)
- **Mittelfinger** → Technische Stromrichtung I
- **Daumen** → Kraftrichtung F (Bewegung)

**Rechte-Hand-Regel** gilt für den Generatorbetrieb: Daumen = Bewegungsrichtung, Zeigefinger = B, Mittelfinger = induzierter Strom.

## Kraft zwischen parallelen Leitern

Zwei stromdurchflossene Leiter erzeugen jeweils ihr eigenes kreisförmiges Magnetfeld (Richtung nach der Rechte-Hand-Regel, siehe [[Magnetfelder]]). Liegt ein Leiter im Feld des anderen, wirkt auf ihn eine Lorentzkraft — die Leiter beeinflussen sich also gegenseitig:

:::schematic Kraft zwischen parallelen Leitern: Zwei vertikale Leiter nebeneinander im Abstand a. Links: gleichsinnige Ströme (beide Pfeile nach oben) — Feldlinien zwischen den Leitern heben sich auf (verdünnt), aussen verstärken sie sich (verdichtet) → Kraftpfeile F zeigen aufeinander zu (Anziehung). Rechts: gegensinnige Ströme (Pfeile entgegengesetzt) — Feldlinien zwischen den Leitern verdichten sich, aussen verdünnen sie sich → Kraftpfeile F zeigen voneinander weg (Abstossung). Beschriftung: I1, I2, a, F
/abbildungen/magnetfelder/parallele_leiter.svg
:::

**Anschauliche Erklärung über die Feldliniendichte:** Wo sich die Felder zweier Leiter überlagern, addieren oder subtrahieren sich die Feldlinien. Auf der Seite mit *verdichteten* Feldlinien ist das Feld stärker (wie ein gespanntes Gummiband), auf der Seite mit *verdünnten* Feldlinien schwächer. Die Kraft wirkt immer von der dichten zur dünnen Seite — die Leiter "wollen" in den Bereich mit dem schwächeren Feld ausweichen:

| Stromrichtungen | Feld zwischen den Leitern | Kraft F |
|---|---|---|
| **Gleichsinnig** (parallel, gleiche Richtung) | hebt sich auf (verdünnt) → aussen verdichtet | Leiter werden **angezogen** |
| **Gegensinnig** (antiparallel, entgegengesetzt) | verstärkt sich (verdichtet) → aussen verdünnt | Leiter **stossen sich ab** |

:::tip
Eselsbrücke: Bei parallelen **Leitern** verhält es sich umgekehrt zur Erfahrung mit Magnetpolen — dort stossen sich Gleichnamiges ab. Bei stromdurchflossenen Leitern gilt: **"Gleichsinnig zieht an, gegensinnig stösst ab."**

Diese Kontrolle lässt sich auch direkt mit der **Linken-Hand-Regel** nachvollziehen: Das Feld B des einen Leiters (Zeigefinger, kreisförmig nach Rechte-Hand-Regel bestimmt) zusammen mit der Stromrichtung I des anderen Leiters (Mittelfinger) ergibt über den Daumen die Kraftrichtung F auf diesen Leiter.
:::

:::formel
F / l = mu_0 * I1 * I2 / (2 * pi * a)    # Kraft pro Leiterlänge zwischen zwei parallelen Leitern im Abstand a
:::

Diese Formel ist auch die historische Definition der Einheit **Ampere**: Bei a = 1 m und I1 = I2 = 1 A wirkt zwischen den Leitern eine Kraft von genau 2 · 10⁻⁷ N pro Meter Leiterlänge.

## Kraft auf eine bewegte Ladung

Eine einzelne Ladung q, die sich mit Geschwindigkeit v senkrecht zu B bewegt, erfährt ebenfalls eine Kraft:

:::formel
F = q * v * B    # Lorentzkraft auf Einzelladung
:::

Dieser Effekt erklärt die Hall-Spannung: Fliesst Strom durch ein Halbleiterelement im Magnetfeld, werden die Ladungsträger zur Seite abgelenkt — es entsteht quer eine messbare Spannung (Hall-Effekt, Grundlage für Stromsensoren und Drehgeber).

## Anwendungen

| Anwendung | Prinzip |
|---|---|
| Elektromotor | Lorentzkraft auf Leiter im Magnetfeld → Drehmoment |
| Generator | Bewegung im Feld → induzierte Spannung (Umkehrung) |
| Lautsprecher | Schwingspule im Dauermagnetfeld → mechanische Schwingung |
| Magnetbremse | Wirbelströme im leitenden Material → Bremskraft |
| Hall-Sensor | Ablenkung von Ladungsträgern → Spannungsmessung |

:::tip
Beim Elektromotor und Generator handelt es sich um dasselbe Prinzip — nur die Richtung der Energieumwandlung ist umgekehrt. Ein Motor kann als Generator betrieben werden und umgekehrt. Das ist die Grundlage für **regeneratives Bremsen** in Elektrofahrzeugen.
:::
