---
title: Parallelschaltung
kategorie: ET
tags: [parallelschaltung, widerstand, strom, spannung, stromteiler, kirchhoff, R_ges, leitwert]
symbol: R_ges
einheit: Ω
---

Bauteile nebeneinander, alle an derselben Spannung. Der Strom teilt sich auf. Der Gesamtwiderstand ist kleiner als jeder einzelne Zweig.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Reihenschaltung]]
- [[Kirchhoffsche Gesetze]]
:::
:::vbox
**Führt weiter zu**
- [[Spannungs- & Stromteiler]]
:::
:::

---

:::info
Spannung überall gleich. Ströme addieren sich. 1/R_ges = 1/R1 + 1/R2 + 1/R3
:::

## Schaltung

:::schematic Parallelschaltung
/schaltplaene/parallelschaltung.svg
:::

Beide Enden aller Widerstände hängen an denselben zwei Knoten. Jeder Zweig ist eine unabhängige Verbindung. Fällt einer aus, fliessen die anderen weiter.

## Formeln

:::schematic
/Diagramm/parallelschaltung_0.svg
:::
Mit dem Leitwert G = 1/R in Siemens lassen sich Parallelwiderstände direkt addieren — praktischer als die Kehrwertformel.

## Beispiel

| Grösse | Berechnung | Ergebnis |
|---|---|---|
| R_ges | (100 × 200) / (100 + 200) | 66.7 Ω |
| I_ges | 12 V / 66.7 Ω | 180 mA |
| I durch R1 | 12 V / 100 Ω | 120 mA |
| I durch R2 | 12 V / 200 Ω | 60 mA |
| P_ges | 12 V × 180 mA | 2.16 W |

:::warning
Zwei Spannungsquellen mit verschiedener Spannung nie direkt parallel schalten. Der Unterschied treibt einen grossen Ausgleichsstrom.
:::
