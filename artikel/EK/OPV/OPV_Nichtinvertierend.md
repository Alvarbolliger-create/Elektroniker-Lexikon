---
title: OPV Nichtinvertierend
kategorie: EK
tags: [OPV, nichtinvertierend, verstärker, impedanzwandler, puffer, voltage-follower, eingangswiderstand, ADC-puffer]
symbol: —
einheit: —
---

Der nichtinvertierende Verstärker gibt das Signal in gleicher Phase aus. Der Eingang belastet die Quelle kaum. Minimale Verstärkung ist 1.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV: Aufbau & Kennwerte]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Invertierend]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive Filter]]
:::
:::

---

## Schaltung

Eingangssignal direkt auf den nichtinvertierenden Eingang (+). Spannungsteiler R1/R2 vom Ausgang zurück auf (-).

## Verstärkung

:::monospace
A = 1 + R2 / R1     # immer grösser oder gleich 1
:::
| R1 | R2 | Verstärkung |
|---|---|---|
| — | — | 1 (Impedanzwandler, R2 = 0, R1 = offen) |
| 10 kΩ | 10 kΩ | 2 |
| 10 kΩ | 90 kΩ | 10 |

## Impedanzwandler (Voltage Follower)

Spezialfall: R2 = 0, R1 entfällt. Ausgang direkt auf (-). Verstärkung = 1, Signal unverändert.

Zweck: Sehr hoher Eingangswiderstand, sehr tiefer Ausgangswiderstand. Schützt eine hochohmige Quelle (z.B. Spannungsteiler, Sensor) vor Belastung durch nachfolgende Stufen.

:::info
Spannungsteiler als Referenz für ADC: Der Teiler wird belastet wenn direkt angeschlossen. Mit Impedanzwandler dahinter: die Spannung bleibt stabil, der ADC sieht einen niederohmigen Treiber.
:::

## Unterschied zum invertierenden

Gleiche Verstärkung möglich, aber Eingangswiderstand ist nahezu unendlich (OPV-Eingang direkt). Nachteil: Verstärkung beginnt bei 1, kann nicht unter 1 gehen.
