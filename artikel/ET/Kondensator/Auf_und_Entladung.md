---
title: Auf- und Entladung
kategorie: ET
tags: [kondensator, RC, zeitkonstante, tau, laden, entladen, exponentialkurve, RC-glied, zeitverhalten, transient]
symbol: τ
einheit: s
---

Wenn ein Kondensator über einen Widerstand geladen oder entladen wird, geschieht das nicht sofort. Die Spannung steigt und sinkt nach einer Exponentialkurve.

:::hbox
:::vbox
**Voraussetzungen**
- [[Kapazität & Einheiten]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator Typen]]
:::
:::

---

## Die Zeitkonstante

```
tau = R * C     # Zeitkonstante in Sekunden
```

Nach einer Zeitkonstante ist der Kondensator auf 63 % der Zielspannung geladen. Nach fünf Zeitkonstanten gilt er als vollständig geladen (99 %).

| Zeit | Ladezustand |
|---|---|
| 1 × tau | 63 % |
| 2 × tau | 86 % |
| 3 × tau | 95 % |
| 5 × tau | 99 % |

## Formeln

```
U_laden(t)    = U₀ * (1 - e^(-t / τ))
U_entladen(t) = U₀ * e^(-t / τ)
I(t)          = (U₀ / R) * e^(-t / τ)
```

Der Strom ist beim Einschalten am grössten und nimmt exponentiell ab. Die Spannung verhält sich umgekehrt.

## Aufladen

Spannung steigt langsam, weil der Kondensator dem Strom immer mehr Widerstand entgegensetzt. Am Anfang fliesst der grösste Strom.

:::plot
var: t
range: 0, 5
Laden:    1 - exp(-t)
Entladen: exp(-t)
xlabel: Zeit (τ)
ylabel: U / U₀
:::

:::tip
tau = R × C ist die wichtigste Formel dieses Artikels. R in Ohm, C in Farad ergibt tau in Sekunden. Beispiel: 10 kΩ und 100 µF ergeben tau = 1 s.
:::

:::warning
Grosse Kondensatoren mit tiefer Kapazität können auch nach dem Ausschalten der Schaltung noch lange gefährliche Spannung tragen. Vor Arbeiten immer entladen und prüfen.
:::
