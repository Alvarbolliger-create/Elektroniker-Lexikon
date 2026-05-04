---
title: Übersetzungsverhältnis
kategorie: ET
tags: [transformator, übersetzung, windungszahl, spannung, strom, impedanzanpassung, galvanische trennung, abwärtstransformator, aufwärtstransformator]
symbol: ü
einheit: —
---

Das Übersetzungsverhältnis beschreibt wie ein Transformator Spannung und Strom umwandelt. Was er an Spannung gewinnt, verliert er an Strom.

:::hbox
:::vbox
**Voraussetzungen**
- [[Transformator: Aufbau & Funktionsprinzip]]
:::
:::vbox
**Verwandte Artikel**
- [[Wirkungsgrad & Verluste]]
:::
:::vbox
**Führt weiter zu**
- [[Netzteile]]
- [[Leitungsauslegung]]
:::
:::

---

## Formel

:::monospace
ue = N1 / N2        # Übersetzungsverhältnis aus Windungszahlen
U1 / U2 = N1 / N2  # Spannungsübersetzung
I1 / I2 = N2 / N1  # Stromübersetzung (umgekehrt zur Spannung)
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Übersetzungsverhältnis | ü | — |
| Primärwindungen | N1 | — |
| Sekundärwindungen | N2 | — |

## Heruntersetzen und Hochsetzen

ü > 1: Spannung sinkt, Strom steigt (Abwärtstransformator). Typisch für Netzteile.

ü < 1: Spannung steigt, Strom sinkt (Aufwärtstransformator). Typisch für Hochspannungsanwendungen.

## Leistung bleibt (fast) gleich

:::monospace
P1 = P2     # idealer Transformator; gilt annähernd bei gutem Wirkungsgrad
U1 * I1 = U2 * I2
:::
In der Praxis entstehen Verluste durch Kupferwiderstand der Wicklungen und Ummagnetisierungsverluste im Kern.

## Impedanztransformation

Ein Transformator transformiert auch Impedanzen. Das wird genutzt um Quellen und Lasten anzupassen.

:::monospace
Z1 = ue^2 * Z2      # Impedanz von Sekundär auf Primär umgerechnet
:::
Das ist wichtig in der Audiotechnik und bei HF-Anpassnetzwerken.
