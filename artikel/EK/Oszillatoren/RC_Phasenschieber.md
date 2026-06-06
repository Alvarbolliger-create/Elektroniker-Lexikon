---
title: RC-Phasenschieber-Oszillator
kategorie: EK
kapitel: Oszillatoren
tags: [RC-phasenschieber, phasenschieber, RC-oszillator, 180-grad, invertierend, resonanzfrequenz, rückkopplungsfaktor, sinusgenerator, 60-grad, v_u=29, k=1/29]
groessen: f_0|Resonanzfrequenz|Hz; k|Rückkopplungsfaktor|—; v_u|Spannungsverstärkung|—; R|Widerstand|Ω; C|Kapazität|F
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[Filter Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Wien-Robinson-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Wien-Robinson-Oszillator]]
:::
:::

---

Der RC-Phasenschieber-Oszillator verwendet drei RC-Glieder, die zusammen **180° Phasendrehung** erzeugen. Ein invertierender Verstärker dreht nochmals 180° → Summe = 360° (Schwingungsbedingung erfüllt).

## Funktionsprinzip

:::schematic RC-Phasenschieber-Oszillator (Hochpass-Variante): Invertierender OPV-Verstärker rechts (Eingang an −, R_E und R_R). Drei RC-Hochpassglieder links: je C in Reihe, R nach GND — hintereinander. Ausgang OPV → erstes RC-Glied → zweites → drittes → zurück an den (−)-Eingang des OPV. Jedes RC-Glied dreht 60° bei f_0. Drei × 60° + 180° (OPV invertierend) = 360° ✓
/Diagramm/rc_phasenschieber_osz.svg
:::

Jedes RC-Glied dreht die Phase um bis zu 90°. Genau bei der Resonanzfrequenz f_0 dreht jedes Glied **60°** — drei Glieder zusammen ergeben 180°. Der invertierende Verstärker (OPV oder BJT Emitterschaltung) liefert die restlichen 180°.

## Vektordiagramm eines RC-Gliedes

Bei f_0 dreht jedes RC-Glied genau 60°. Das Vektordiagramm zeigt: U_gesamt setzt sich aus U_R (phasengleich mit Strom) und U_C (90° nacheilend) zusammen.

:::formel
tan(60°) = U_R / U_C = R / X_C      # 60°-Bedingung pro Stufe
R = X_C * sqrt(3)                    # Widerstandsbedingung bei 60°
X_C = 1 / (2 * pi * f * C)          # kapazitiver Blindwiderstand
:::

Drei Stufen à 60° liefern 180° Gesamtphasendrehung. Der invertierende Verstärker addiert weitere 180° → Schwingungsbedingung erfüllt.

Es gibt zwei Varianten je nach Anordnung von R und C:

## Variante 1 — Hochpass-RC-Kette (C in Reihe, R nach Masse)

:::formel
f_0 = 1 / (sqrt(6) * 2 * pi * R * C)    # Resonanzfrequenz
k   = 1 / 29                              # Rückkopplungsfaktor
v_u = 29                                  # benötigte Spannungsverstärkung
:::

## Variante 2 — Tiefpass-RC-Kette (R in Reihe, C nach Masse)

:::formel
f_0 = sqrt(6) / (2 * pi * R * C)         # Resonanzfrequenz
k   = 1 / 29                              # Rückkopplungsfaktor (gleich wie Variante 1)
v_u = 29                                  # benötigte Spannungsverstärkung (gleich)
:::

:::info
In beiden Varianten sind k und v_u identisch — nur f_0 unterscheidet sich. Variante 2 (TP) schwingt um den **Faktor 6** höher als Variante 1 (HP): f_TP = sqrt(6)/(2π×R×C) = 6 × f_HP. Umbau TP→HP: Frequenz sinkt auf 1/6.
:::

## Verstärkerdimensionierung (OPV invertierend)

:::formel
v_u = R_R / R_E = 29    → R_R = 29 * R_E
:::

Für sicheres Anlaufen R_R leicht grösser wählen (z.B. R_R = 33 × R_E). Die Amplitudenbegrenzung (antiparallele Dioden im Gegenkopplungszweig) reduziert v_u auf 29 im Gleichgewicht.

:::monospace
Beispiel Variante 1: f_0 = 1 kHz, C = 10 nF
R = 1 / (√6 × 2π × 1000 × 10e-9) = 6.5 kΩ → 6.8 kΩ (E12)
Probe: f_0 = 1 / (√6 × 2π × 6800 × 10e-9) = 955 Hz ✓

Verstärker: R_E = 10 kΩ, R_R = 33 × 10 kΩ = 330 kΩ (E12)
→ v_u = 33, Anlaufverstärkung OK (> 29)
:::

## Vergleich mit Wien-Robinson

| Eigenschaft | RC-Phasenschieber | Wien-Robinson |
|---|---|---|
| Benötigte v_u | 29 | 3 |
| Frequenzabstimmung | schwierig (3 Elemente gleichzeitig) | einfach (Tandempoti) |
| Kurvenqualität (THD) | schlechter | besser |
| Schaltungsaufwand | gering | mittel |
| Typischer Einsatz | einfacher Sinusgenerator | Audiogenerator |
