---
title: Frequenzgang und Verstärkungsfaktor
kategorie: EK
tags: [frequenzgang, verstärkung, bandbreite, -3dB, bode, OPV, GBP, slew rate, dezibel, dB, amplitudengang, phasengang]
symbol: A
einheit: dB, Hz
---

Der Frequenzgang beschreibt wie ein Verstärker oder Filter auf Signale verschiedener Frequenzen reagiert. Die Verstärkung ist oft frequenzabhängig.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV: Aufbau & Kennwerte]]
- [[RC-Tiefpass & Hochpass]]
:::
:::vbox
**Verwandte Artikel**
- [[Aktive Filter]]
- [[Stabilität und Schwingneigung]]
:::
:::

---

## Verstärkungsfaktor

Der Verstärkungsfaktor A ist das Verhältnis von Ausgangs- zu Eingangssignal:

:::formel
A = U_aus / U_ein     # Spannungsverstärkung, dimensionslos
:::
In Dezibel:
:::formel
A_dB = 20 × log10(U_aus / U_ein)    # Spannungsverstärkung
P_dB = 10 × log10(P_aus / P_ein)    # Leistungsverstärkung
:::
Faktor 10 = 20 dB (Spannung) / 10 dB (Leistung). Faktor 2 = 6 dB (U) / 3 dB (P).

| Faktor | Spannung dB | Leistung dB |
|---|---|---|
| 0.5 | –6 dB | –3 dB |
| 1 | 0 dB | 0 dB |
| 2 | +6 dB | +3 dB |
| 10 | +20 dB | +10 dB |
| 100 | +40 dB | +20 dB |

**Mehrere Stufen in Reihe**: dB-Werte addieren sich:
:::formel
A_total_dB = A1_dB + A2_dB + ... + An_dB
:::
Beispiel: Verstärker 30 dB, Filter –12 dB → Gesamtverstärkung 18 dB = Faktor 8.

## -3-dB-Grenzfrequenz

Die Frequenz bei der die Verstärkung auf 1/sqrt(2) = 0.707 des Maximalwerts abgefallen ist. Das entspricht einem Leistungsabfall auf die Hälfte (-3 dB).

Sie definiert die Bandbreite des Systems.

## GBP (Gain-Bandwidth-Product)

Bei OPVs ist das Produkt aus Verstärkung und Bandbreite näherungsweise konstant:

:::formel
GBP = A × f_-3dB
:::
Ein OPV mit GBP = 1 MHz und Verstärkung 10 hat f_-3dB ≈ 100 kHz. Mit Verstärkung 100 nur noch 10 kHz.

## Bode-Diagramm

Zwei Diagramme übereinander:
- Oben: Verstärkung in dB über log(Frequenz)
- Unten: Phasenversatz in ° über log(Frequenz)

Mit Bode-Geraden (asymptotische Näherung) können Filter und Verstärker schnell skizziert werden.

## Slew Rate

Maximale Spannungsänderungsrate am OPV-Ausgang (V/µs). Begrenzt die Amplitude bei hohen Frequenzen auch wenn die Verstärkung noch stimmt.

:::formel
f_max = Slew Rate / (2π × U_peak)
:::
Ein OPV mit 1 V/µs kann bei 10 V Amplitude maximal ca. 16 kHz unverzerrt ausgeben.
