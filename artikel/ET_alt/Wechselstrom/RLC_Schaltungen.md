---
title: RLC-Schaltungen
kategorie: ET
tags: [RLC, resonanz, wechselstrom, impedanz, reihenschwingkreis, parallelschwingkreis, schwingkreis, güte, bandbreite]
symbol: —
einheit: —
---

RLC-Schaltungen kombinieren Widerstand, Spule und Kondensator. Bei der Resonanzfrequenz heben sich die reaktiven Anteile auf. Das ist die Grundlage von Filtern und Oszillatoren.

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
- [[Kondensator im Wechselstrom]]
- [[Spule im Wechselstrom]]
:::
:::vbox
**Verwandte Artikel**
- [[Resonanz]]
- [[Filter Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[Filter Grundlagen]]
- [[Resonanz]]
:::
:::

---

## Resonanzfrequenz

Bei der Resonanzfrequenz ist X_L = X_C. Die reaktiven Anteile heben sich auf.

:::formel
f_0 = 1 / (2 * pi * sqrt(L * C))   # Resonanzfrequenz
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Resonanzfrequenz | f_0 | Hz |
| Induktivität | L | H |
| Kapazität | C | F |

## Reihenschwingkreis

R, L und C in Reihe. Bei Resonanz ist die Impedanz minimal (nur R übrig). Der Strom ist maximal.

:::formel
Z = R + j * (X_L - X_C) = R + j * (ω*L - 1/(ω*C))
:::
Bei Resonanz gilt X_L = X_C, der imaginäre Anteil verschwindet und Z = R.

:::warning
**Spannungsüberhöhung**: Bei Serienresonanz liegt an L und C jeweils das Q-fache der Quellspannung an. Bei Q = 10 und U_ein = 10 V entstehen 100 V an den Bauteilen — auch wenn die Versorgung nur 10 V liefert.
:::

Wird als Serienresonanzfilter eingesetzt: Bei f_0 durchgelassen, sonst gedämpft.

## Parallelschwingkreis

R, L und C parallel. Bei Resonanz ist die Impedanz maximal. Der Strom aus der Quelle ist minimal.

Wird als Parallelresonanzfilter eingesetzt: Bei f_0 gesperrt, sonst durchgelassen.

## Güte Q

Die Güte beschreibt wie scharf die Resonanz ist.

:::formel
Q = (ω_0 * L) / R      # aus Bauteilwerten (Reihenschwingkreis)
Q = f_0 / B            # aus Resonanzfrequenz und 3dB-Bandbreite
B = f_0 / Q            # Bandbreite in Hz
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Güte | Q | — |
| Bandbreite (−3 dB) | B | Hz |
| Resonanzfrequenz | f_0 | Hz |

Hohe Güte: scharfe, hohe Resonanzspitze, kleine Bandbreite. Niedrige Güte: breite, flache Resonanz, grosse Bandbreite.

:::tip
LC-Filter haben eine steilere Flanke als RC-Filter. Für scharfe Frequenztrennung (z.B. Empfänger, HF-Filter) werden LC-Kreise verwendet. Für einfache Anwendungen reicht meist ein RC-Filter.
:::
