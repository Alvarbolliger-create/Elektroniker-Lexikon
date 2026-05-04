---
title: Strom, Spannung, Widerstand
kategorie: ET
tags: [strom, spannung, widerstand, ohm, leitwert, grundlagen, ohmsches gesetz, uri, elektrisches gesetz, lineare bauelemente, ampere, volt]
symbol: I, U, R, G
einheit: A, V, Ω, S
---

Spannung treibt elektrischen Strom durch einen Leiter. Wie stark er fliesst, hängt vom Widerstand ab. Der Zusammenhang zwischen allen drei Grössen ist das Ohmsche Gesetz — die Grundlage aller Schaltungsanalyse.

:::hbox
:::vbox
**Voraussetzungen**
- —
:::
:::vbox
**Verwandte Artikel**
- [[Kirchhoffsche Gesetze]]
:::
:::vbox
**Führt weiter zu**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
- [[Spannungs- & Stromteiler]]
:::
:::

---

**Spannung U** in Volt (V) ist der Unterschied im elektrischen Potential zwischen zwei Punkten. Ohne Spannung fliesst kein Strom. Eine Batterie erzeugt Spannung durch chemische Energie.

**Strom I** in Ampere (A) beschreibt wie viele Elektronen pro Sekunde durch einen Leiter fliessen. Die technische Stromrichtung geht von Plus nach Minus, Elektronen fliessen physikalisch in die andere Richtung.

**Widerstand R** in Ohm (Ω) beschreibt wie stark ein Material den Stromfluss behindert. Metalle haben einen tiefen Widerstand, Kunststoffe einen sehr hohen.

## Ohmsches Gesetz

Spannung, Strom und Widerstand hängen linear zusammen — verdoppelt sich die Spannung, fliesst doppelt so viel Strom.

:::schematic URI-Dreieck
schaltplaene/uri_dreieck.svg
:::

:::formel
U = R * I
R = U / I
I = U / R
:::
Das Gesetz gilt nur für lineare Bauteile: Widerstände, Heizdrähte, Leitungen. Dioden und Transistoren folgen ihm nicht.

## Leitwert

:::formel
G = 1 / R
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Leitwert | G | S (Siemens) |
| Widerstand | R | Ω (Ohm) |

Bei Parallelschaltungen addieren sich die Leitwerte direkt — praktischer als mit Widerständen zu rechnen.

## Beispiele

| Spannung | Widerstand | Strom |
|---|---|---|
| 5 V | 100 Ω | 50 mA |
| 12 V | 1 kΩ | 12 mA |
| 3.3 V | 330 Ω | 10 mA |

## Wann gilt es nicht?

Bei Dioden und Transistoren ist der Zusammenhang nicht linear. R = U / I ergibt dort zwar einen Zahlenwert, aber er gilt nur für diesen einen Arbeitspunkt, nicht für die Schaltung allgemein.

Für nichtlineare Bauteile verwendet man den **differenziellen Widerstand** am Arbeitspunkt:

:::formel
r = ΔU / ΔI
:::
Er beschreibt die Steigung der Kennlinie an einem bestimmten Punkt — wie stark sich der Strom bei einer kleinen Spannungsänderung verändert.

Im Wechselstromkreis erweitert die Impedanz Z den Widerstand R um Kondensatoren und Spulen. Die Formel bleibt gleich: U = Z * I.
