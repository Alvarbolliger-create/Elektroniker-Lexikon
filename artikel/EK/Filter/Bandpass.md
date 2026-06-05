---
title: Bandpass (BP)
kategorie: EK
tags: [bandpass, BP, mittenfrequenz, bandbreite, güte, Q-faktor, sallen-key, aktiv, passiv, radio, signalauswahl, resonanz]
symbol: —
einheit: —
---

Ein Bandpass (BP) lässt nur ein bestimmtes Frequenzband durch. Frequenzen unterhalb der unteren Grenzfrequenz und oberhalb der oberen Grenzfrequenz werden gedämpft.

:::hbox
:::vbox
**Voraussetzungen**
- [[Tiefpass (TP)]]
- [[Hochpass (HP)]]
:::
:::vbox
**Verwandte Artikel**
- [[Bandsperre (BS)]]
- [[Aktive Filter]]
:::
:::vbox
**Führt weiter zu**
- [[Filtercharakteristik]]
:::
:::

---

## Anwendungen

- **Radio/Empfänger**: Einen bestimmten Sender herausfiltern (z.B. 105.6 MHz)
- **Audioequalizer**: Bestimmten Frequenzbereich anheben oder absenken
- **Messsysteme**: Nur relevante Signalfrequenz durchlassen
- **Schwingkreisfilter**: Schmalbandige Selektion eines Signals

## Frequenzgang

:::plot
var: f
range: 0.01, 100
xlabel: Frequenz (normiert, f_0 = 1)
ylabel: Amplitude (normiert)
Bandpass (Q=1):  f / sqrt((1 - f*f)^2 + f*f)
Bandpass (Q=5):  5*f / sqrt((1 - f*f)^2 + 25*f*f)
:::

## Kenngrössen

:::formel
f_0 = sqrt(f_u · f_o)         # Mittenfrequenz (geometrisches Mittel)
B   = f_o - f_u               # Bandbreite (obere minus untere Grenzfrequenz)
Q   = f_0 / B                 # Gütefaktor (schmal = hoher Q)
:::
- **f_0**: Mittenfrequenz — hier ist die Verstärkung am grössten
- **B**: Bandbreite — Frequenzbereich zwischen den −3 dB Punkten
- **Q**: Gütefaktor — hoher Q = schmales, selektives Band

## Aufbau

Ein Bandpass entsteht durch **Kombination von Tiefpass und Hochpass**:
- Tiefpass: definiert die obere Grenzfrequenz f_o
- Hochpass: definiert die untere Grenzfrequenz f_u
- Beide hintereinander geschaltet → nur das Band f_u bis f_o kommt durch

Für schmalbandige Anwendungen: LC-Schwingkreis oder Multi-Feedback-Topologie mit OPV.

## Steilheit

Ein Bandpass 2. Ordnung hat:
- **+40 dB/Dekade** unterhalb f_u (Hochpass-Anteil)
- **−40 dB/Dekade** oberhalb f_o (Tiefpass-Anteil)

:::tip
Je höher der Q-Faktor, desto selektiver der Filter — aber desto schwieriger auch die genaue Abstimmung. Bei Q > 10 empfiehlt sich ein LC-Schwingkreis oder ein Quarz statt eines aktiven RC-Filters.
:::
