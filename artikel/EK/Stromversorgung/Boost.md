---
title: Boost (Step-up)
kategorie: EK
tags: [boost, step-up, schaltregler, MOSFET, spule, hochsetzer, tastverhältnis, buck-boost, USB, batterie]
symbol: —
einheit: —
---

Der Boost-Wandler setzt eine niedrigere Spannung auf eine höhere um. Typisch für batteriebetriebene Geräte die mehr Spannung brauchen als die Batterie liefert.

:::hbox
:::vbox
**Voraussetzungen**
- [[Buck (Step-down)]]
:::
:::vbox
**Verwandte Artikel**
- [[Buck (Step-down)]]
:::
:::vbox
**Führt weiter zu**
- [[Batterietechnik]]
:::
:::

---

## Funktionsprinzip

MOSFET schaltet gegen Masse. Wenn er leitet, speichert die Spule Energie. Wenn er sperrt, muss der Strom irgendwo hin. Er fliesst über die Diode in den Ausgangskondensator, der jetzt auf höherer Spannung liegt als der Eingang.

## Tastverhältnis

```
U_aus = U_ein / (1 - D)     # D = Tastverhältnis; gilt im Idealfall
```

Bei D = 0.5: U_aus = 2 × U_ein. Bei D = 0.75: U_aus = 4 × U_ein.

In der Praxis ist D über etwa 0.9 nicht sinnvoll, weil der Wirkungsgrad stark sinkt.

## Besonderheit: Eingangsstrom

Der Boost-Wandler zieht einen kontinuierlichen Strom aus der Quelle (die Spule ist am Eingang). Das ist gut für Batterien, die kurze Stromspitzen schlecht vertragen.

Der Ausgangsstrom ist dagegen pulsierend. Der Ausgangskondensator muss das abfedern.

## Typische Anwendungen

Eine einzelne Lithium-Zelle (2.7 bis 4.2 V) auf 5 V für USB. Zwei AA-Batterien (2 bis 3 V) auf 3.3 V. LED-Treiber mit konstantem Strom und schwankender Versorgung.

| IC | U_ein | U_aus | I_max |
|---|---|---|---|
| MT3608 | 2 bis 24 V | bis 28 V | 2 A |
| TPS61023 | 0.7 bis 5.5 V | bis 5.5 V | 3 A |
| MAX1724 | 0.7 bis 5.5 V | bis 5.5 V | 0.3 A |

:::tip
Boost-Wandler können keine Spannung regeln die tiefer als die Eingangsspannung ist. Wenn die Batterie schwächer wird als die Ausgangsspannung, gibt der Regler auf. Für diesen Fall gibt es Buck-Boost-Wandler.
:::
