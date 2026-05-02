---
title: RC-Phasenschieber-Oszillator
kategorie: EK
tags: [rc-phasenschieber, oszillator, OPV, transistor, phasendrehung, 180-grad, mindest-verstärkung, abgleich, klirrfaktor]
symbol: f_0
einheit: Hz
---

Der RC-Phasenschieber-Oszillator nutzt drei RC-Glieder, die zusammen 180° Phasendrehung liefern. Mit einem invertierenden Verstärker (weitere 180°) ergibt das 360° — die Bedingung für Schwingung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[RC-Filter]]
:::
:::vbox
**Verwandte Artikel**
- [[Wien-Brücken-Oszillator]]
:::
:::

---

## Schaltungsprinzip

Drei identische RC-Hochpassglieder in Reihe, jedes dreht die Phase um ca. 60°. Zusammen: 180° Phasendrehung.

```
Ausgang → [RC] → [RC] → [RC] → (−)-Eingang
(invertierender Verstärker: weitere 180°)
Gesamtphasendrehung: 180° + 180° = 360° → Schwingbedingung
```

Das Rückkopplungsnetzwerk dämpft das Signal stark. Der Verstärker braucht daher eine Verstärkung von mindestens **29**, um die Dämpfung zu kompensieren.

---

## Formeln

```
f_0 = 1 / (2π × R × C × √6)    # Resonanzfrequenz bei identischen R und C
A_min = 29                       # Mindestverstärkung für stabile Schwingung
```

| Grösse | Symbol | Einheit | Beschreibung |
|---|---|---|---|
| Resonanzfrequenz | f₀ | Hz | Schwingfrequenz |
| RC-Glieder | R, C | Ω, F | Alle drei identisch |
| Mindestverstärkung | A_min | — | 29 bei drei gleichen RC-Stufen |

---

## Vertiefung

**Nachteil**: Die benötigte Verstärkung von 29 macht den Abgleich schwierig. Kleine Toleranzen in R und C verschieben die Frequenz und die Phasenbedingung gleichzeitig.

**Vorteil**: Sehr einfache Schaltung, kein Induktor nötig, kann auch mit einem einzigen Transistor (NPN) realisiert werden.

:::warning
Mit einem Transistor statt OPV: Der Transistor invertiert selbst um 180°. Die drei RC-Glieder müssen dann als Tiefpass-Kette geschaltet werden (statt Hochpass), damit sie die restlichen 180° liefern.
:::

| Vergleich | Wien-Brücke | RC-Phasenschieber |
|---|---|---|
| Mindest-Verstärkung | 3 | 29 |
| Abgleich | Einfach | Aufwändig |
| Klirrfaktor | Gering | Mittel |
| Implementierung | OPV typisch | OPV oder Transistor |
