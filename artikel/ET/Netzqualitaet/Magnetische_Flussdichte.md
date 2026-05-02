---
title: Magnetische Flussdichte
kategorie: ET
tags: [magnetfeld, flussdichte, tesla, gauss, permeabilität, induktion, hallsensor, sättigung, elektroblech, ferrit]
symbol: B
einheit: T
---

Die magnetische Flussdichte B beschreibt die Stärke und Richtung eines Magnetfelds. Sie bestimmt wie stark eine Kraft auf bewegte Ladungsträger wirkt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Lorentzkraft]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
- [[Induktivität & Einheiten]]
:::
:::

---

## Definition

Die Flussdichte B ist das Verhältnis des magnetischen Flusses zur durchströmten Fläche:

```
B = Φ / A     # Φ = magnetischer Fluss in Wb, A = Fläche in m²
```

Einheit: Tesla (T) = Wb/m² = V·s/m².

Praktische Umrechnung: 1 T = 10.000 Gauss (Gauss = ältere, noch gebräuchliche Einheit).

## Typische Werte

| Quelle | Flussdichte |
|---|---|
| Erdmagnetfeld | 25-65 µT |
| Kühlschrankmagnet | ca. 5 mT |
| Lautsprecher-Dauermagnet | 1-1.5 T |
| MRT (medizinisch) | 1.5-3 T |
| Supraleitende Magnete | 10-20 T |

## Materialeigenschaften: Permeabilität

Die relative Permeabilität µr beschreibt wie stark ein Material das Magnetfeld verstärkt oder schwächt:
- Vakuum, Luft: µr = 1
- Aluminium: µr ≈ 1 (paramagnetisch, schwach)
- Ferrit: µr = 100-10.000
- Elektroblech (Si-Stahl): µr = 5.000-100.000

```
B = µ0 × µr × H     # H = magnetische Feldstärke in A/m
```

## Sättigung

Weichmagnetische Materialien sättigen bei einem bestimmten B-Wert. Dann kann keine weitere Feldverstärkung durch den Kern erfolgen, und die Induktivität sinkt.

Ferrit: Sättigung ca. 200-500 mT. Elektroblech: ca. 1.5-2 T.

Im Transformator- und Drosseldesign muss die Flussdichte unter der Sättigungsgrenze bleiben. Das vollständige B-H-Kurvenverhalten ist unter [[Sättigung und Hysterese]] beschrieben.

## Messung

Hallsensoren messen B direkt. Preiswerte Hallsensoren (A1302, SS49E) liefern eine analoge Spannung proportional zu B. Für präzise Messungen: Teslameter mit kalibrierter Hallsonde.
