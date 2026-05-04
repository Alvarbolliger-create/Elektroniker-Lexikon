---
title: Reihenschaltung
kategorie: ET
tags: [reihenschaltung, widerstand, spannung, strom, spannungsteiler, kirchhoff, R_ges, serienschaltung]
symbol: R_ges
einheit: Ω
---

Bauteile hintereinander in einem einzigen Strompfad. Der gleiche Strom fliesst durch alle. Die Spannung verteilt sich proportional auf die Widerstände.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Parallelschaltung]]
- [[Kirchhoffsche Gesetze]]
:::
:::vbox
**Führt weiter zu**
- [[Spannungs- & Stromteiler]]
:::
:::

---

:::info
Strom überall gleich. Spannungen addieren sich. R_ges = R1 + R2 + R3
:::

## Schaltung

:::schematic Reihenschaltung
/schaltplaene/reihenschaltung.svg
:::

Quelle (+) → R1 → R2 → R3 → Quelle (−). Es gibt nur diesen einen Pfad. Fällt ein Bauteil aus, fliesst kein Strom mehr.

## Formeln

:::schematic
/Diagramm/reihenschaltung_0.svg
:::
`U_n` ist die Spannung an einem einzelnen Widerstand (Spannungsteilerformel). `P_ges` ist die Summe der Verlustleistungen aller Bauteile.

## Beispiel

12 V, R1 = 100 Ω, R2 = 200 Ω:

| Grösse | Berechnung | Ergebnis |
|---|---|---|
| R_ges | 100 + 200 | 300 Ω |
| I | 12 V / 300 Ω | 40 mA |
| U an R1 | 40 mA × 100 Ω | 4 V |
| U an R2 | 40 mA × 200 Ω | 8 V |
| P_ges | 12 V × 40 mA | 480 mW |
