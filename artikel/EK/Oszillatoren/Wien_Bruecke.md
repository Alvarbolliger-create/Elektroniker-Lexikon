---
title: Wien-Brücken-Oszillator
kategorie: EK
tags: [wien-brücke, oszillator, OPV, sinusgenerator, RC, frequenz, amplitudenstabilisierung, NTC, klirrfaktor, THD, bandpass]
symbol: f_0
einheit: Hz
---

Der Wien-Brücken-Oszillator ist der häufigste RC-Sinusoszillator mit OPV. Er erzeugt ein sauberes Sinussignal in einem breiten Frequenzbereich.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[OPV: Aufbau & Kennwerte]]
:::
:::vbox
**Verwandte Artikel**
- [[RC-Phasenschieber-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive Filter]]
:::
:::

---

## Schaltungsprinzip

Der OPV arbeitet als nichtinvertierender Verstärker. Das frequenzselektive Netzwerk (Wien-Brücke) liegt zwischen Ausgang und dem nichtinvertierenden Eingang (+).

**Wien-Brücke**: Zwei RC-Glieder — ein Reihenschaltung und eine Parallelschaltung — hintereinandergeschaltet.

:::schematic
/Diagramm/wien_bruecke_0.svg
:::
Bei der Resonanzfrequenz f₀ beträgt die Phasendrehung des Netzwerks genau **0°** und die Dämpfung ist **1/3**. Der Verstärker muss also mindestens Verstärkung 3 haben.

---

## Formeln

:::monospace
f_0 = 1 / (2π × R × C)      # Resonanzfrequenz; R und C identisch in beiden Gliedern
A   = 1 + R_2 / R_1 = 3     # Mindest-Verstärkung; R_2 / R_1 = 2
:::
| Grösse | Symbol | Einheit | Beschreibung |
|---|---|---|---|
| Resonanzfrequenz | f_0 | Hz | Schwingfrequenz |
| RC-Glieder | R, C | Ω, F | Gleiche Werte für beide Glieder |
| Schleifenverstärkung | A × β | — | = 1 bei f₀ |

---

## Amplitudenstabilisierung

Ohne Regelung: Verstärkung leicht über 3 → Amplitude wächst → Clipping → Verzerrter Sinus.

**Lösung mit NTC-Widerstand**: R_1 im Spannungsteiler ist ein NTC. Bei grösserem Strom (höhere Amplitude) erwärmt er sich, sein Widerstand sinkt, die Verstärkung sinkt → Selbstregelung.

**Lösung mit Diodenbegrenzer**: Antiparallele Dioden begrenzen den Ausgang — einfacher aber mit mehr Verzerrung.

---

## Vertiefung

:::info
Die Wien-Brücke ist ein Bandpassfilter mit der Mittenfrequenz f₀. Bei f₀ beträgt die Ausgangsspannung genau 1/3 der Eingangsspannung und die Phase ist 0°. Nur bei dieser Frequenz ist das Barkhausen-Kriterium erfüllt.
:::

| Parameter | Typisch |
|---|---|
| Frequenzbereich | 1 Hz – 1 MHz |
| Klirrfaktor (THD) | 0.01–1 % je nach Amplitudenregelung |
| Abstimmung | R oder C tauschbar (Drehkondensator, Poti) |

:::tip
Für einen abstimmbaren Oszillator: beide R-Werte mit einem Tandem-Poti gleichzeitig ändern. So bleibt die Amplitude konstant während die Frequenz variiert.
:::
