---
title: Blindleistung
kategorie: ET
tags: [blindleistung, reaktiv, var, leistungsfaktor, kondensator, spule, kompensation, phasenwinkel, blindstrom]
symbol: Q
einheit: var
---

Blindleistung entsteht bei reaktiven Lasten. Sie pendelt zwischen Quelle und Verbraucher hin und her, ohne Arbeit zu leisten. Trotzdem belastet sie die Leitung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
- [[Wirkleistung]]
:::
:::vbox
**Verwandte Artikel**
- [[Scheinleistung]]
- [[Leistungsfaktor cos φ]]
:::
:::vbox
**Führt weiter zu**
- [[Leistungsfaktor cos φ]]
:::
:::

---

## Warum entsteht sie?

Eine Spule speichert Energie im Magnetfeld und gibt sie zurück. Ein Kondensator dasselbe im elektrischen Feld. Diese Energie fliesst vor und zurück, erzeugt aber keine nutzbare Arbeit.

Der Strom fliesst trotzdem durch die Leitung. Das heisst: die Leitung wird belastet, obwohl keine Arbeit geleistet wird.

```
Q = U * I * sin(phi)    # Blindleistung; phi = Phasenwinkel
```

| Grösse | Symbol | Einheit |
|---|---|---|
| Blindleistung | Q | var (Voltampere reaktiv) |
| Phasenwinkel | phi | ° |

## Induktiv vs. kapazitiv

Spulen verursachen induktive Blindleistung (positives Q). Kondensatoren kapazitive (negatives Q). Die beiden heben sich auf, wenn sie gleich gross sind. Das ist das Prinzip der Kompensation.

## Kompensation

Industriebetriebe mit grossen Motoren (induktive Last) schalten Kondensatorbatterien parallel. Die kapazitive Blindleistung der Kondensatoren hebt die induktive der Motoren auf. Der Leitungsstrom sinkt, der Leistungsfaktor steigt.

:::tip
Schlechter Leistungsfaktor kostet Geld. Energieversorger verrechnen Blindleistung bei Industriekunden. Deshalb lohnt sich Kompensation schon bei mittleren Anlagen.
:::
