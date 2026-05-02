---
title: Wirkleistung
kategorie: ET
tags: [wirkleistung, leistung, leistungsfaktor, cos phi, watt, phasenwinkel, PFC, wechselstrom]
symbol: P
einheit: W
---

Wirkleistung ist die Leistung, die tatsächlich in Arbeit oder Wärme umgesetzt wird. Bei Gleichstrom einfach U × I. Bei Wechselstrom kommt der Phasenwinkel dazu.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Blindleistung]]
- [[Scheinleistung]]
:::
:::vbox
**Führt weiter zu**
- [[Leistungsfaktor cos φ]]
:::
:::

---

## Phasenverschiebung

:::plot
var: t
range: 0, 6.28
xlabel: Zeit
ylabel: Amplitude
U (Spannung): sin(t)
I (Strom):    sin(t - 1.05)
:::

## Gleichstrom

```
P = U * I
P = U^2 / R
P = I^2 * R
```

Alle drei Formen sind gleichwertig und über das Ohmsche Gesetz ineinander umrechenbar. `P = I²*R` ist besonders nützlich für Verlustberechnungen in Leitungen und Widerständen.

## Wechselstrom

Bei Wechselstrom mit induktiven oder kapazitiven Lasten ist Strom und Spannung nicht mehr gleichzeitig am Maximum. Der Phasenwinkel phi entsteht.

```
P = U * I * cos(phi)    # phi = Phasenwinkel zwischen Strom und Spannung
```

cos(phi) heisst Leistungsfaktor. Bei rein ohmschen Lasten ist phi = 0, cos(phi) = 1. Bei rein induktiven oder kapazitiven Lasten ist phi = 90°, cos(phi) = 0, keine Wirkleistung.

## Was ist der Unterschied zu Scheinleistung?

Scheinleistung S = U × I (ohne cos phi) ist das, was durch die Leitung fliesst. Wirkleistung ist der nutzbare Anteil davon.

```
P = S * cos(phi)
```

Mehr dazu unter [[Scheinleistung]] und [[Leistungsfaktor cos φ]].

:::tip
Glühbirnen, Heizungen und reine Widerstände: cos(phi) = 1, Schein- und Wirkleistung sind gleich. Motoren und Schaltnetzteile: cos(phi) oft 0.7 bis 0.9. Das ist der Grund warum Industriebetriebe Blindleistung kompensieren.
:::

## Kenndaten

| Last | Typischer cos φ | Bemerkung |
|---|---|---|
| Glühbirne, Heizung | 1.0 | Rein ohmsch |
| Leuchtstofflampe | 0.5 bis 0.9 | Je nach Vorschaltgerät |
| Elektromotor | 0.7 bis 0.9 | Lastabhängig |
| Schaltnetzteil | 0.6 bis 0.99 | Mit oder ohne PFC |
