---
title: Early-Effekt (BJT)
kategorie: EK
tags: [Early-Effekt, BJT, Ausgangskennlinienfeld, Frühspannung, Basisbreite, Transistor]
symbol: V_A
einheit: V
---

Der Early-Effekt beschreibt die Abhängigkeit des Kollektorstroms von der Kollektor-Emitter-Spannung im Sättigungsbereich. Im idealen Transistormodell wäre IC unabhängig von UCE — in der Realität ist er es nicht.

:::hbox
:::vbox
**Voraussetzungen**
- [[Bipolartransistor (BJT)]]
- [[pn-Übergang]]
:::
:::vbox
**Verwandte Artikel**
- [[Transistor als Verstärker]]
- [[MOSFET]]
:::
:::

---

## Physikalische Ursache

Die Basisbreite eines BJT ist nicht konstant. Die Raumladungszone zwischen Basis und Kollektor wächst mit zunehmender UCE (höhere Sperrspannung = breitere Raumladungszone). Diese Raumladungszone "frisst" sich in die Basis hinein und verkleinert die effektive Basisbreite.

Eine schmalere Basis bedeutet:
- Weniger Rekombination in der Basis
- Mehr Elektronen erreichen den Kollektor
- Stromverstärkung hFE steigt
- IC steigt bei konstantem IB

## Ausgangskennlinienfeld

Im idealen Modell: Waagrechte Linien im Ausgangskennlinienfeld (IC konstant bei konstantem IB, unabhängig von UCE).

In der Realität: Die Linien steigen leicht an. Verlängert man sie nach links (negativer UCE-Bereich), schneiden sie alle (näherungsweise) in einem Punkt auf der negativen UCE-Achse.

:::monospace
Dieser Schnittpunkt ist die Early-Spannung VA
VA liegt typisch bei -50 V bis -200 V
:::
## Early-Spannung VA

Die Early-Spannung VA ist ein Kennwert des Transistors. Je grösser |VA|, desto schwächer der Early-Effekt, desto besser der Transistor als Stromquelle.

:::monospace
IC(UCE) = IC0 × (1 + UCE / VA)    # vereinfachtes Early-Modell
:::
Typische Werte: Kleine Signaltransistoren 50–150 V; Hochspannungstransistoren höher.

## Auswirkung auf Schaltungen

**Stromquellen**: Ein Transistor als Stromquelle liefert keinen perfekt konstanten Strom. Der Ausgangswiderstand ist endlich:

:::monospace
r_out = VA / IC    # Early-Widerstand (Kleinsignalmodell)
:::
Bei IC = 1 mA und VA = 100 V: r_out = 100 kΩ. Das ist viel, aber nicht unendlich.

**Differenzverstärker**: Early-Effekt beeinflusst die Gleichtaktunterdrückung (CMRR). Je höher VA, desto besser.

**Kaskodeschaltung**: Durch Überlagern zweier Transistoren (Kaskode) wird der Early-Effekt stark reduziert. Der effektive Ausgangswiderstand steigt auf r_out × β × r_be.

## Vergleich: MOSFET

Der analoge Effekt beim MOSFET heisst Channel-Length-Modulation (Kanallängenmodulation). Je kürzer der Kanal (Submikron-Technologie), desto ausgeprägter dieser Effekt. Der MOSFET-Parameter λ entspricht 1/VA.
