---
title: Snubber-Netzwerk
kategorie: EK
tags: [Snubber, RC-Snubber, Schaltspitze, Überspannung, Transistorschutz, dU/dt]
symbol: —
einheit: —
---

Ein Snubber ist ein Schutzschaltung (meist RC-Glied) parallel zu einem Schalttransistor oder einer Diode. Er begrenzt Spannungsspitzen beim Schalten und dämpft Schwingungen.

:::hbox
:::vbox
**Voraussetzungen**
- [[MOSFET]]
- [[Selbstinduktion]]
- [[Kondensator Übersicht]]
:::
:::vbox
**Verwandte Artikel**
- [[Soft-Switching (ZVS/ZCS)]]
- [[Flyback & Forward Converter]]
:::
:::

---

## Das Problem: Schaltspitzen

Beim Ausschalten eines Transistors wird der Strom unterbrochen. Parasitäre Induktivitäten in Leiterbahnen und Bauelementen erzeugen dann eine Spannungsspitze:

:::monospace
U_spike = L_parasit × dI/dt    # kann Vielfaches der Betriebsspannung erreichen
:::
Beim Flyback-Converter kommt zusätzlich die Streuinduktivität des Übertragers hinzu — diese erzeugt eine hohe Spannungsspitze auf dem primärseitigen Transistor beim Ausschalten.

## RC-Snubber (RCD-Snubber)

Der einfachste Snubber: RC-Glied parallel zum Transistor (Drain–Source).

:::formel
C_s in Reihe mit R_s, parallel zu D/S
:::
**Wirkprinzip**:
- Beim Ausschalten nimmt C_s die Spannungsspitze auf (begrenzt dU/dt)
- R_s dämpft die Schwingung zwischen C_s und Streuinduktivität
- Beim Einschalten entlädt sich C_s über R_s (hier entsteht Verlust)

## Dimensionierung RC-Snubber

Faustregel für den Kondensator:

:::monospace
C_s ≈ I_off² × L_streu / U_spike²    # I_off = Strom beim Ausschalten
:::
Für den Widerstand:

:::monospace
R_s = 1 / (2π × f_osc × C_s)    # f_osc = Schwingfrequenz der Spitze
:::
Die Verlustleistung im Snubber:

:::monospace
P_snubber = 0.5 × C_s × U_peak² × f    # proportional zur Schaltfrequenz
:::
## RCD-Snubber für Flyback

Beim Flyback wird oft ein RCD-Snubber eingesetzt (Diode, Kondensator, Widerstand in einer bestimmten Anordnung):

- Diode leitet die Spannungsspitze in den Snubber-Kondensator
- Kondensator klemmt die maximale Drain-Spannung
- Widerstand entlädt den Kondensator kontinuierlich (dissipiert Verluste)

Die Klemmspannung:

:::monospace
U_clamp ≈ U_IN × n + U_spike    # n = Windungsverhältnis
:::
## Verluste vs. Schutz

Ein Snubber kostet immer Verlustleistung. Bei höheren Schaltfrequenzen steigen die Snubber-Verluste proportional.

Alternative bei hohen Frequenzen: Active Clamping (statt passivem Snubber einen Transistor zum Ableiten der Energie verwenden — Energie wird zurückgespeist statt vernichtet).

## Praktische Hinweise

- Snubber-Kondensator muss für hohe Impulsströme und Spannungen ausgelegt sein (Folienkondensator, keine Elektrolyten)
- Snubber so nah wie möglich am Schaltelement platzieren (minimale Leitungsimpedanz)
- Wert experimentell bestimmen: Spitze mit Oszilloskop messen, C und R anpassen

:::warning
Ein Snubber-Kondensator aus Elektrolyt funktioniert nicht — er hat zu hohe Eigeninduktivität und übersteht die Impulsbelastung nicht. Folienkondensatoren (MKP, MKT) oder Keramik verwenden.
:::
