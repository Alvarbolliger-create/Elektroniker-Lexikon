---
title: Transit & Grenzfrequenz
kategorie: EK
kapitel: Filter
tags: [transitfrequenz, grenzfrequenz, RC-Glied, RL-Glied, bode-diagramm, -3db, 20dB, 6dB, dekade, oktave, phasenverschiebung, 45grad]
groessen: f_g|Grenzfrequenz|Hz; f_t|Transitfrequenz|Hz; R|Widerstand|Ω; C|Kapazität|F; L|Induktivität|H
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Filter Grundlagen]]
- [[Impedanz & Blindwiderstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Tiefpass]]
- [[Hochpass]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive Filter]]
- [[OPV Grundlagen]]
:::
:::

---

Grenz- und Transitfrequenz beschreiben, wo ein Filter oder Verstärker seine Funktion beginnt zu ändern. Beide lassen sich aus R, C und L direkt berechnen.

## Grenzfrequenz

Bei der Grenzfrequenz f_g tritt zwischen Ein- und Ausgangssignal eine **Phasenverschiebung von 45°** auf (Filter 1. Ordnung). Die Ausgangsamplitude beträgt −3 dB (70.7 %).

### RC-Glieder (Tiefpass und Hochpass)

:::formel
f_g = 1 / (2 * pi * R * C)    # Grenzfrequenz RC
R   = 1 / (2 * pi * f_g * C)  # Widerstand aus f_g und C
C   = 1 / (2 * pi * f_g * R)  # Kapazität aus f_g und R
:::

### RL-Glieder (Tiefpass und Hochpass)

:::formel
f_g = R / (2 * pi * L)        # Grenzfrequenz RL
R   = 2 * pi * f_g * L        # Widerstand aus f_g und L
L   = R / (2 * pi * f_g)      # Induktivität aus f_g und R
:::

## Transitfrequenz

Die **Transitfrequenz f_t** ist der Punkt, wo die Verstärkung eines Verstärkers auf **1 (= 0 dB)** gesunken ist. Unterhalb f_t verstärkt die Schaltung; oberhalb dämpft sie.

:::info
Bei OPVs gilt: f_t = GBW (Gain-Bandwidth-Product). Bei Transistoren ist f_T die Frequenz, bei der die Stromverstärkung B auf 1 gesunken ist (typisch 100–300 MHz für BC547).
:::

## Dämpfungsmaß im Bode-Diagramm

:::schematic Bode-Diagramm RC-Tiefpass 1. Ordnung: Horizontale Achse = Frequenz f (logarithmisch, Dekaden). Oberes Diagramm (Amplitudengang): 0 dB bis f_g (flach), dann Abfall mit −20 dB/Dekade. Bei f_g: Punkt bei −3 dB markiert. Asymptoten: horizontal bei 0 dB und schräg mit −20 dB/Dek ab f_g. Unteres Diagramm (Phasengang): 0° weit unter f_g, −45° bei f_g, −90° weit über f_g
/Diagramm/bode_tiefpass_1.svg
:::

Die Steilheit eines RC-Filters 1. Ordnung im Sperrbereich:

:::formel
Steilheit = 20 dB / Dekade = 6 dB / Oktave
:::

| Frequenz | Dämpfung (TP 1. Ordnung) |
|---|---|
| f = f_g | −3 dB |
| f = 2 × f_g (1 Oktave) | ≈ −7 dB |
| f = 10 × f_g (1 Dekade) | −20 dB |
| f = 100 × f_g (2 Dekaden) | −40 dB |
| f = 1000 × f_g (3 Dekaden) | −60 dB |

Die Tabelle gilt für 1. Ordnung. Jede weitere Ordnung multipliziert die Steilheit.

:::monospace
Berechnungsbeispiel RC:
f_g = 1 kHz, C = 10 nF → R

R = 1 / (2π × 1000 × 10e-9) = 15.9 kΩ → nächster E12-Wert: 15 kΩ
Probe: f_g = 1 / (2π × 15000 × 10e-9) = 1.06 kHz ✓

Berechnungsbeispiel RL:
f_g = 10 kHz, L = 1 mH → R
R = 2π × 10000 × 0.001 = 62.8 Ω → 68 Ω (E12)
Probe: f_g = 68 / (2π × 0.001) = 10.8 kHz ✓
:::
