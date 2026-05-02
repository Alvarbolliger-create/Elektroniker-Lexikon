---
title: RC-Tiefpass & Hochpass
kategorie: EK
tags: [RC-filter, tiefpass, hochpass, grenzfrequenz, phasenverschiebung, bode-diagramm, übertragungsfunktion, phasengang, ADC-eingang]
symbol: f_g
einheit: Hz
---

RC-Filter sind die einfachsten passiven Filter. Ein Widerstand und ein Kondensator. Kein IC, keine Versorgung, sofort einsatzbereit.

:::hbox
:::vbox
**Voraussetzungen**
- [[Filter Grundlagen]]
- [[Auf- und Entladung]]
:::
:::vbox
**Verwandte Artikel**
- [[LC-Filter]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive Filter]]
:::
:::

---

:::plot
var: f
range: 0, 5
xlabel: Frequenz (normiert, f/f_g)
ylabel: Dämpfung
Tiefpass:  1 / sqrt(1 + f*f)
Hochpass:  f / sqrt(1 + f*f)
:::

## RC-Tiefpass

R in Reihe, C nach Masse. Ausgang über C abgegriffen.

Tiefe Frequenzen: C hat hohe Impedanz, Spannungsabfall fast nur über C. Signal kommt durch.
Hohe Frequenzen: C hat tiefe Impedanz, Spannungsabfall fast nur über R. Signal gedämpft.

```
f_g     = 1 / (2 * pi * R * C)             # −3 dB Grenzfrequenz
H(s)    = 1 / (1 + s * R * C)              # Übertragungsfunktion
|H(jω)| = 1 / sqrt(1 + (ω * R * C)^2)     # Amplitudengang
φ(ω)    = -arctan(ω * R * C)               # Phasengang
```

| Frequenz | Amplitude | Phase |
|---|---|---|
| f ≪ f_g | ≈ 1 (0 dB) | ≈ 0° |
| f = f_g | 0.707 (−3 dB) | −45° |
| f ≫ f_g | → 0 | → −90° |

## RC-Hochpass

C in Reihe, R nach Masse. Ausgang über R abgegriffen. Tiefpass umgedreht.

Tiefe Frequenzen gedämpft. Hohe Frequenzen durchgelassen.

```
f_g     = 1 / (2 * pi * R * C)
|H(jω)| = (ω * R * C) / sqrt(1 + (ω * R * C)^2)
φ(ω)    = +arctan(1 / (ω * R * C))
```

## Bode-Diagramm

Das Bode-Diagramm zeigt Amplituden- und Phasengang logarithmisch. Vereinfachte Asymptoten für den Tiefpass:

- Unterhalb f_g: 0 dB, flach
- Oberhalb f_g: −20 dB pro Dekade
- Knickpunkt genau bei f_g

```
Dämpfung [dB] = 20 * log10(|H(jω)|)
```

Bei f = 10 · f_g beträgt die Dämpfung ca. −20 dB. Bei f = 100 · f_g bereits −40 dB.

## Phasenverschiebung

Am Tiefpass eilt der Ausgang um bis zu −90° nach. An der Grenzfrequenz genau −45°.
Am Hochpass eilt der Ausgang um bis zu +90° vor. An der Grenzfrequenz genau +45°.

Das ist wichtig wenn mehrere Stufen kaskadiert werden: die Phasenverschiebungen addieren sich.

## Designbeispiel

Tiefpass für ADC-Eingang, Grenzfrequenz 1 kHz:

Wahl R = 10 kΩ. Dann: C = 1 / (2 × π × 1000 × 10000) ≈ 16 nF. Nächster E12-Wert: 15 nF.

| Ziel f_g | R | C |
|---|---|---|
| 100 Hz | 10 kΩ | 150 nF |
| 1 kHz | 10 kΩ | 15 nF |
| 10 kHz | 10 kΩ | 1.5 nF |
| 100 kHz | 1 kΩ | 1.5 nF |
