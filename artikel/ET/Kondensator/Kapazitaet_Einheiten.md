---
title: Kapazität & Einheiten
kategorie: ET
tags: [kapazität, farad, ladung, energie, kondensator, pF, nF, µF, aufdruck, code, SMD, dielektrikum]
symbol: C
einheit: F
---

Die Kapazität beschreibt, wie viel Ladung ein Kondensator bei einer bestimmten Spannung speichern kann.

:::hbox
:::vbox
**Voraussetzungen**
- [[Elektrisches Feld]]
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Verwandte Artikel**
- [[Auf- und Entladung]]
:::
:::vbox
**Führt weiter zu**
- [[Auf- und Entladung]]
:::
:::

---

## Die Grösse

```
Q = C * U       # Gespeicherte Ladung
E = 0.5 * C * U^2  # Gespeicherte Energie
```

| Grösse | Symbol | Einheit |
|---|---|---|
| Kapazität | C | F (Farad) |
| Ladung | Q | C (Coulomb) |
| Energie | E | J (Joule) |
| Spannung | U | V |

Ein Farad ist sehr gross. In der Praxis werden meist µF, nF oder pF verwendet.

## Aufdruck-Code lesen

Kondensatoren sind oft mit einem 3-stelligen Code beschriftet — analog zum Widerstandscode:

```
1. und 2. Stelle: Zahlenwert
3. Stelle:        Exponent (Basis 10, Ergebnis in pF)
```

| Aufdruck | Berechnung | Wert |
|---|---|---|
| 105 | 10 × 10⁵ pF | 1 µF |
| 104 | 10 × 10⁴ pF | 100 nF |
| 472 | 47 × 10² pF | 4.7 nF |
| 100 | 10 × 10⁰ pF | 10 pF |

Bei Buchstabennotation steht der Buchstabe für den Dezimalpunkt und die Einheit:

| Aufdruck | Wert |
|---|---|
| n47 | 0.47 nF = 470 pF |
| µ33 | 0.33 µF = 330 nF |
| 1n0 | 1.0 nF |

Steht nichts dabei, ist die Angabe meistens in nF oder pF — je nach Baugrösse entscheiden.

SMD-Kondensatoren sind oft unbeschriftet.

## Typische Werte

| Anwendung | Typische Kapazität |
|---|---|
| Bypass am IC | 100 nF |
| Siebkondensator Netzteil | 1000 µF |
| Quarz-Lastkapazität | 18 pF |
| Superkondensator | 1 F bis 100 F |

## Abhängigkeit vom Aufbau

```
C = ε * A / d
```

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Permittivität | ε | F/m | ε = εᵣ × ε₀, Materialeigenschaft des Dielektrikums |
| Plattenfläche | A | m² | grössere Fläche → mehr Kapazität |
| Plattenabstand | d | m | kleinerer Abstand → mehr Kapazität |

Elkos erreichen hohe Kapazitäten durch ein extrem dünnes Dielektrikum (oxidierte Aluminiumschicht, wenige nm) und einen grossen Folienwickel als Plattenfläche.
