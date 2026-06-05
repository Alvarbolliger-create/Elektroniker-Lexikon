---
title: Scheinleistung
kategorie: ET
tags: [scheinleistung, leistung, VA, wechselstrom, transformator, leistungsdreieck, phasenwinkel, blindleistung]
symbol: S
einheit: VA
---

Scheinleistung ist das Produkt aus Effektivwerten von Spannung und Strom. Sie beschreibt, wie stark eine Leitung oder ein Transformator belastet wird, unabhängig davon wie viel davon nutzbare Arbeit ist.

:::hbox
:::vbox
**Voraussetzungen**
- [[Wirkleistung]]
- [[Blindleistung]]
:::
:::vbox
**Verwandte Artikel**
- [[Leistungsfaktor cos φ]]
:::
:::vbox
**Führt weiter zu**
- [[Leitungsauslegung]]
:::
:::

---

## Formel

:::formel
S = U * I           # Scheinleistung; U und I als Effektivwerte
S = sqrt(P^2 + Q^2) # aus Wirk- und Blindleistung
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Scheinleistung | S | VA |
| Wirkleistung | P | W |
| Blindleistung | Q | var |

## Wozu braucht man sie?

Leitungen, Transformatoren und Generatoren werden nach Scheinleistung ausgelegt. Sie führen den vollen Strom, auch wenn ein Teil davon Blindstrom ist.

Ein Transformator mit 1 kVA kann 1000 W liefern, aber nur wenn der Leistungsfaktor 1 ist. Bei cos φ = 0.7 liefert er nur 700 W nutzbare Leistung, trägt aber trotzdem den vollen Strom.

## Leistungsdreieck

Wirk-, Blind- und Scheinleistung bilden ein rechtwinkliges Dreieck. Der Phasenwinkel φ liegt zwischen S und P.

:::formel
P = S * cos(phi)    # Wirkleistung
Q = S * sin(phi)    # Blindleistung
:::