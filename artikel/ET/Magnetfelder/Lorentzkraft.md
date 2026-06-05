---
title: Lorentzkraft
kategorie: ET
tags: [lorentzkraft, magnetfeld, kraft, leiter, motor, generator, linke-hand-regel, rechte-hand-regel]
groessen: F|Kraft|N; I|Strom|A; l|Leiterlänge|m; B|Flussdichte|T; v|Geschwindigkeit|m/s; q|Ladung|C
_status: PORT  # ET_alt/Magnetfelder/Lorentzkraft.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
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
