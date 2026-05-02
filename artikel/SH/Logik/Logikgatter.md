---
title: Logikgatter
kategorie: SH
tags: [logikgatter, AND, OR, NOT, NAND, NOR, XOR, XNOR, digital, wahrheitstabelle, fanout, TTL, CMOS, universal-gatter]
symbol: —
einheit: —
---

Logikgatter sind die Grundbausteine digitaler Schaltungen. Sie verknüpfen digitale Eingänge und liefern einen digitalen Ausgang.

:::hbox
:::vbox
**Voraussetzungen**
- [[Zahlensysteme]]
:::
:::vbox
**Verwandte Artikel**
- [[Schaltalgebra]]
:::
:::vbox
**Führt weiter zu**
- [[Schaltalgebra]]
- [[Flipflops]]
:::
:::

---

## Die Grundgatter

**NOT**: Invertiert den Eingang. Aus HIGH wird LOW, aus LOW wird HIGH.

**AND**: Ausgang ist HIGH nur wenn alle Eingänge HIGH sind.

**OR**: Ausgang ist HIGH wenn mindestens ein Eingang HIGH ist.

**NAND**: Wie AND, aber invertiert. Ausgang ist LOW nur wenn alle Eingänge HIGH sind.

**NOR**: Wie OR, aber invertiert.

**XOR**: Ausgang ist HIGH wenn die Eingänge verschieden sind.

## Wahrheitstabellen (2 Eingänge)

:::truth A,B | AND,OR,NAND,NOR,XOR
0,0 | 0,0,1,1,0
0,1 | 0,1,1,0,1
1,0 | 0,1,1,0,1
1,1 | 1,1,0,0,0
:::

## NAND und NOR sind universell

Mit NAND-Gattern allein lassen sich alle anderen Gatter bauen. Dasselbe gilt für NOR. In der Praxis werden daher oft nur diese zwei Typen in einer Schaltung verwendet, um Bauelemente zu sparen.

## Logikfamilien

Gatter gibt es in verschiedenen Spannungsbereichen und Geschwindigkeiten. TTL, CMOS, LVTTL sind die häufigsten. Verschiedene Familien können nicht immer direkt miteinander verbunden werden.

:::warning
Unbenutzte Eingänge nie offen lassen. Sie schwingen zufällig und können die Schaltung stören. Auf HIGH oder LOW legen, je nach Gattertyp.
:::
