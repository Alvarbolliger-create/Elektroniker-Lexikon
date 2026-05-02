---
title: Magnetfelder
kategorie: ET
tags: [magnetfeld, feldlinien, rechte-hand-regel, elektromagnet, induktion, fluss]
symbol: B
einheit: T
---

Jeder stromdurchflossene Leiter erzeugt ein Magnetfeld um sich herum. Das ist die Grundlage von Spulen, Transformatoren und Elektromotoren.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
- [[Lorentzkraft]]
- [[Sättigung und Hysterese]]
:::
:::vbox
**Führt weiter zu**
- [[Transformator]]
- [[Spule (Übersicht)]]
:::
:::

---

## Feldlinien

Das Magnetfeld wird durch Feldlinien dargestellt. Sie verlaufen in Kreisen um den Leiter herum. Wo die Linien dichter sind, ist das Feld stärker.

Die Richtung der Feldlinien hängt von der Stromrichtung ab.

## Rechte-Hand-Regel (Korkenzieherregel)

Zeigt der Daumen der rechten Hand in die technische Stromrichtung, zeigen die gekrümmten Finger die Richtung des Magnetfelds.

Bei einer Spule: Finger zeigen in die Stromrichtung der Windungen, Daumen zeigt zum Nordpol.

In Schnittzeichnungen wird die Stromrichtung im Leiterquerschnitt so dargestellt:

| Symbol | Bedeutung |
|---|---|
| ⊗ (Kreuz) | Strom fliesst weg vom Betrachter (Pfeilende) |
| ⊙ (Punkt) | Strom fliesst zum Betrachter hin (Pfeilspitze) |

## Magnetische Feldstärke H

Die magnetische Feldstärke H beschreibt die Erregung unabhängig vom Material (Einheit: A/m).

**Gerader Leiter** (im Abstand r):
```
H = I / (2 * π * r)
```

**Zylinderspule** (N Windungen, Länge l):
```
H = I * N / l
Θ = I * N              # Magnetische Durchflutung in A
H = Θ / l
```

**Ringspule (Toroid)** (mittlere Feldlinienlänge l_m):
```
H = I * N / l_m
```

## Magnetische Grössen

```
Φ = B * A              # Magnetischer Fluss
B = µ * H              # Flussdichte aus Feldstärke und Permeabilität
µ = µr * µ0            # Permeabilität des Materials (µ0 = 4π × 10⁻⁷ H/m)
```

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Magnetischer Fluss | Φ | Wb (Weber) | Gesamtfluss durch eine Fläche |
| Magnetische Flussdichte | B | T (Tesla) | Fluss pro Flächeneinheit |
| Magnetische Feldstärke | H | A/m | Erregung unabhängig vom Material |
| Permeabilität | µ | H/m | Wie gut ein Material das Feld leitet |

Die Permeabilität beschreibt, wie gut ein Material das Magnetfeld leitet. Eisen hat eine viel höhere Permeabilität als Luft — deshalb konzentrieren Eisenkerne das Feld in Transformatoren und Spulen. Wird der Kern gesättigt, bricht µ ein. Mehr dazu unter [[Sättigung und Hysterese]].

## Faradaysches Induktionsgesetz

Eine Änderung des magnetischen Flusses induziert eine Spannung. Das ist die Grundlage jeder Spule, jedes Transformators und jedes Generators:

```
U_ind = -N * dΦ/dt
```

Das Minuszeichen steht für die Lenz'sche Regel: Die induzierte Spannung wirkt der Flussänderung entgegen. Bei N Windungen addiert sich der Beitrag jeder Windung.

## Typische Flussdichten

| Quelle | Flussdichte |
|---|---|
| Erdmagnetfeld | ca. 50 µT |
| Kühlschrankmagnet | ca. 5 mT |
| Transformatorkern | 1 bis 1.5 T |
| MRT (Kernspin) | 1.5 bis 7 T |
