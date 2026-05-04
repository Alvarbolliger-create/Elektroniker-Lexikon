---
title: Transistor als Verstärker
kategorie: EK
tags: [verstärker, BJT, arbeitspunkt, kleinsignal, verstärkung, steilheit, koppelkondensator, Q-punkt, basisspannungsteiler]
symbol: A
einheit: —
---

Im linearen Betrieb verstärkt ein Transistor kleine Wechselsignale. Der Arbeitspunkt legt fest wo auf der Kennlinie der Transistor arbeitet.

:::hbox
:::vbox
**Voraussetzungen**
- [[Bipolartransistor (BJT)]]
- [[Impedanz]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV: Aufbau & Kennwerte]]
:::
:::vbox
**Führt weiter zu**
- [[Grundschaltungen]]
- [[Verstärkungsfaktor]]
:::
:::

---

## Arbeitspunkt

Der Arbeitspunkt (Q-Punkt) ist der Gleichstrombetriebspunkt des Transistors. Er wird so gewählt, dass der Transistor weder sättigt noch sperrt, wenn das Wechselsignal dazu kommt.

Ein zu hoher Arbeitspunkt: der Transistor sättigt bei positiver Halbwelle. Ein zu tiefer: er sperrt bei negativer Halbwelle. Beides verzerrt das Signal.

Typisch: Arbeitspunkt in der Mitte des linearen Bereichs.

## Einstellung

:::monospace
I_C = (U_CC - U_CE) / R_C    # Kollektorstrom im Arbeitspunkt
U_CE = U_CC / 2              # optimaler Arbeitspunkt für maximale Aussteuerung
:::
Der Basisspannungsteiler (R1 und R2) stellt U_B ein. Damit folgt U_E und I_C.

## Kleinsignalverstärkung

Das Wechselsignal wird auf den Gleichstrom-Arbeitspunkt überlagert. Die Verstärkung gilt für kleine Signale um diesen Punkt.

:::monospace
A_u = -g_m * R_C    # Spannungsverstärkung; g_m = Steilheit = I_C / U_T
:::
U_T = 26 mV bei Raumtemperatur (Temperaturspannung).

## Koppelkondensatoren

Am Eingang und Ausgang trennen Kondensatoren den Gleichstromarbeitspunkt vom Signal. Nur der Wechselanteil kommt durch.

:::tip
Für Präzisionsverstärker wird heute meist ein OPV verwendet. Der Transistorverstärker ist wichtig zum Verstehen und für HF-Anwendungen wo OPVs zu langsam sind.
:::
