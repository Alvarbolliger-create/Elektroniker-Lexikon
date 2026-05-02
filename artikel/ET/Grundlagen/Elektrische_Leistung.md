---
title: Elektrische Leistung
kategorie: ET
tags: [leistung, watt, energie, wirkungsgrad, ohmsches gesetz, verlustleistung, joule, P gleich U mal I]
symbol: P
einheit: W
---

Elektrische Leistung beschreibt, wie viel Energie pro Zeiteinheit umgesetzt wird. Einheit ist Watt (W).

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Wirkleistung]]
- [[Scheinleistung]]
:::
:::vbox
**Führt weiter zu**
- [[Leitungsauslegung]]
- [[Wirkungsgrad & Verluste]]
:::
:::

---

## Grundformeln

```
P = U * I           # Leistung aus Spannung und Strom
P = U^2 / R         # Leistung aus Spannung und Widerstand
P = I^2 * R         # Leistung aus Strom und Widerstand
```

Alle drei Formen folgen aus dem Ohmschen Gesetz (U = R·I). Je nach bekannten Grössen wählt man die passende Form.

| Grösse | Symbol | Einheit |
|---|---|---|
| Leistung | P | W (Watt) |
| Spannung | U | V (Volt) |
| Strom | I | A (Ampere) |
| Widerstand | R | Ω (Ohm) |

## Energie

Leistung über Zeit ergibt die verbrauchte Energie:

```
W = P * t           # Energie in Joule (J)
W = P * t / 3600    # Energie in Wh (Wattstunden)
```

1 kWh = 3 600 000 J = 3.6 MJ.

## Wärmeleistung an Widerständen

Jeder Widerstand setzt Leistung in Wärme um. Das ist bei Vorwiderständen, Shunts und Leitungen wichtig:

```
P_R = I^2 * R       # Verlustleistung am Widerstand
```

Die Bauteilbelastbarkeit (Nennleistung) darf nicht überschritten werden. Im Zweifel Derating beachten — bei erhöhter Umgebungstemperatur reduziert sich die zulässige Leistung.

## Wirkungsgrad

```
η = P_ab / P_zu     # Wirkungsgrad (dimensionslos, 0 bis 1)
η = P_ab / P_zu * 100  # in Prozent
P_verlust = P_zu - P_ab
```

Kein reales System ist verlustfrei. Transformatoren erreichen η ≈ 0.95–0.99, Schaltnetzteile η ≈ 0.85–0.95.

## Beispiele

| Verbraucher | Typische Leistung |
|---|---|
| LED | 0.1–10 W |
| Mikrocontroller | 10–500 mW |
| PC-Netzteil | 300–1000 W |
| Elektromotor (klein) | 100 W bis mehrere kW |
| Haushaltsbackofen | 2–3 kW |
