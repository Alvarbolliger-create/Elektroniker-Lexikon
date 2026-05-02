---
title: Verkettete Spannung
kategorie: ET
tags: [verkettete spannung, drehstrom, 400V, wurzel 3, strangspannung, leistungsformel, schweizer netz, 230V]
symbol: U_v
einheit: V
---

Die verkettete Spannung ist die Spannung zwischen zwei Aussenleitern im Drehstromnetz. Sie ist um den Faktor √3 grösser als die Strangspannung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Sternschaltung]]
- [[Dreieckschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[Wirkleistung]]
:::
:::vbox
**Führt weiter zu**
- [[Frequenzumrichter]]
:::
:::

---

## Herkunft des Faktors √3

Die drei Phasenspannungen sind um 120° versetzt. Die Differenz zwischen zwei Phasenvektoren ergibt geometrisch den Faktor √3 = 1.732.

```
U_verkettet = sqrt(3) * U_strang    # 400 V = sqrt(3) * 230 V
```

## Im Schweizer Netz

| Spannung | Wert | Zwischen |
|---|---|---|
| Strangspannung | 230 V | Aussenleiter und Neutralleiter |
| Verkettete Spannung | 400 V | Aussenleiter und Aussenleiter |

230 V für Steckdosen und Leuchten. 400 V für Motoren, Herde und Industrieanlagen.

## Leistung im Drehstromnetz

```
P = sqrt(3) * U_verkettet * I * cos_phi    # Wirkleistung symmetrische Last
```

Der Faktor √3 erscheint auch in der Leistungsformel, weil drei Phasen je einen Beitrag leisten.

:::tip
Schnelle Abschätzung: 1 kW bei 400 V und cos φ = 1 entspricht etwa 1.44 A pro Aussenleiter. Bei cos φ = 0.8 sind es 1.8 A. Das hilft bei der Leitungsauslegung.
:::
