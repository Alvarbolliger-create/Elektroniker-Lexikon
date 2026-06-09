---
title: Drehstrom Grundlagen
kategorie: ET
tags: [drehstrom, dreiphasig, phasen, neutralleiter, strangspannung, leiterspannung, verkettung, leistung, pwm, frequenzumrichter, drehzahl, drehfeld]
groessen: U_str|Strangspannung|V; U_L|Leiterspannung|V; I|Strom|A; P|Leistung|W; f|Frequenz|Hz; phi|Phasenwinkel|°; n|Drehzahl|U/min; p|Polpaarzahl|—
_status: PORT  # ET_alt/Drehstrom/Drehstrom_Grundlagen.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen & Effektivwert]]
- [[Wechselstromleistung]]
:::
:::vbox
**Führt weiter zu**
- [[Sternschaltung]]
- [[Dreieckschaltung]]
- [[Verkettete Spannung]]
:::
:::vbox
**EK-Anwendungen**
- [[BLDC-Motor]]
- [[Schrittmotor]]
- [[Frequenzumrichter]]
:::
:::

---

Drehstrom (Dreiphasenwechselstrom) ist das Standardsystem für die Energieübertragung und für Antriebe. In der Schweiz liefert das Netz Drehstrom mit 400 V (zwischen Phasen) und 230 V (Phase gegen Neutral) bei 50 Hz.

## Was ist Drehstrom?

:::schematic Drehstrom-Netz (Sternschaltung): Generator links mit drei Wicklungen (L1, L2, L3) je 120° versetzt; drei Aussenleiter (L1 braun, L2 schwarz, L3 grau) führen zur Last; Neutralleiter N (blau) verbindet Sternpunkt des Generators mit Sternpunkt der Last; Strangspannung U_str = 230 V (L–N) und Leiterspannung U_L = 400 V (L–L) eingezeichnet
/schaltplaene/drehstrom/drehstrom_netz.svg
:::

Drei sinusförmige Wechselspannungen gleicher Amplitude und Frequenz, aber um je **120° zeitlich versetzt**. Sie werden in einem gemeinsamen Generator erzeugt, dessen drei Wicklungen gleichmässig um den Rotor verteilt sind.

:::hbox
:::formel
u1(t) = U_peak * sin(omega * t)
:::
:::formel
u2(t) = U_peak * sin(omega * t - 2 * pi / 3)
:::
:::formel
u3(t) = U_peak * sin(omega * t - 4 * pi / 3)
:::
:::

Die Summe aller drei Momentanwerte ist immer null: u1 + u2 + u3 = 0. Damit kann der Neutralleiter (bei symmetrischer Last) keinen Strom tragen — er kann im Prinzip weggelassen werden.

:::plot
var: t
range: 0, 12.56
xlabel: Zeit (t)
ylabel: Spannung
L1:  sin(t)
L2:  sin(t - 2.094)
L3:  sin(t - 4.189)
:::

## Leiter und Neutralleiter

| Bezeichnung | Schweiz | Bedeutung |
|---|---|---|
| Phasenleiter L1, L2, L3 | Braun, Schwarz, Grau | Drei Aussenleiter |
| Neutralleiter N | Blau | Rückleiter (bei Einphasenlast) |
| Schutzleiter PE | Grün/Gelb | Erdung (kein Betriebsstrom) |

## Strangspannung vs. Leiterspannung

| Grösse | Wert (CH-Netz) | Beschreibung |
|---|---|---|
| Strangspannung U_str | 230 V | Phase gegen Neutralleiter (L–N) |
| Leiterspannung U_L | 400 V | Zwischen zwei Phasen (L–L) |

Der Zusammenhang (→ [[Verkettete Spannung]]):

:::formel
U_L = U_str * sqrt(3)
:::

sqrt(3) ≈ 1,732 — daher 230 V · 1,732 ≈ 400 V.

## Frequenz = Drehzahl

Das umlaufende Magnetfeld im Motor dreht sich mit der elektrischen Frequenz f. Die **synchrone Drehzahl** n des Drehfeldes (in U/min) hängt von f und der Polpaarzahl p des Motors ab:

:::formel
n = f * 60 / p    # n in U/min, f in Hz, p = Anzahl Polpaare
:::

| Polpaare p | Synchrondrehzahl (50 Hz) |
|---|---|
| 1 | 3000 U/min |
| 2 | 1500 U/min |
| 3 | 1000 U/min |
| 4 | 750 U/min |

**Folgerung:** Wer die Frequenz ändert, ändert die Drehzahl. Das ist das Grundprinzip des [[Frequenzumrichter|Frequenzumrichters (VFD)]].

:::tip
Ein Motor mit p = 2 Polpaaren dreht am 50-Hz-Netz maximal 1500 U/min. Wird er mit 25 Hz betrieben, dreht er 750 U/min — bei 100 Hz wären es 3000 U/min. Frequenz und Drehzahl sind direkt proportional.
:::

## Drehstrom aus PWM — Frequenzumrichter

Das Netz liefert nur eine feste Frequenz (50 Hz). Um die Drehzahl stufenlos zu regeln, erzeugt ein **Frequenzumrichter (FU / VFD)** einen synthetischen Drehstrom beliebiger Frequenz und Amplitude.

**Prinzip in drei Schritten:**

1. **Gleichrichten**: Netz-Wechselspannung (400 V AC) → Gleichspannung (ca. 565 V DC) über Gleichrichterbrücke
2. **Zwischenkreis**: Glättkondensatoren puffern die Gleichspannung
3. **Wechselrichten (Inverter)**: Sechs Leistungsschalter (IGBTs oder MOSFETs) schalten die DC-Spannung zu drei Ausgangsphasen

Jede der drei Ausgangsphasen wird durch **Pulsweitenmodulation (PWM)** erzeugt: Der Schalter ist abwechselnd ein und aus. Das Tastverhältnis (Duty Cycle) variiert sinusförmig — bei 0° der Sinuskurve ist das Tastverhältnis 50 %, beim Scheitelwert nahe 100 %.

:::plot
var: t
range: 0, 6.28
colors: #0284c7, #16a34a
xlabel: Winkel (rad)
ylabel: Tastverhältnis / Spannung
Sollsinus L1:        sin(t)
Tastverhältnis D:    (sin(t) + 1) / 2
:::

Das Tiefpassverhalten des Motorwicklung (induktive Last, [[RL-Reihenschaltung]]) glättet das PWM-Signal automatisch — der Motor "sieht" den Mittelwert, also eine sinusförmige Spannung.

**Skalierung U/f:** Damit der Magnetfluss im Motor konstant bleibt, wird die Amplitude der Ausgangsspannung proportional zur Frequenz skaliert:

:::formel
U / f = konst.    # U/f-Kennlinie
:::

Bei halbierter Frequenz wird auch die Spannung halbiert — sonst würde der Kern übersättigen und der Motor überhitzen.

## Sensor vs. sensorlos

Um einen Motor präzise zu regeln, muss der Umrichter die aktuelle Rotorposition kennen:

| Methode | Beschreibung | Typische Anwendung |
|---|---|---|
| **Sensor (Encoder)** | Drehgeber am Motorwellenende misst Position direkt. Genau, schnell, auch im Stillstand. | CNC, Robotik, Aufzüge |
| **Sensorlos (FOC/BEMF)** | Umrichter berechnet Rotorposition aus Strom und Spannung. Kein Geber nötig, aber ungenau bei sehr tiefen Drehzahlen / Stillstand. | Pumpen, Lüfter, Haushaltsgeräte |

Bei sensorloser Regelung nutzt der Umrichter die **Gegen-EMK (Back-EMF)** — die vom sich drehenden Rotor induzierte Spannung — als Rückmeldesignal. Bei Stillstand ist keine EMK vorhanden, deshalb sind sensorlose Verfahren dort schwieriger.

## Drehstromleistung

Bei **symmetrischer Last** (gleiche Impedanz auf allen drei Phasen) gilt:

:::formel
P = sqrt(3) * U_L * I * cos(phi)    # Gesamtwirkleistung
:::

## Anwendungen

| Anwendung | Warum Drehstrom? |
|---|---|
| Asynchronmotor (Netz) | Drehendes Magnetfeld, einfache Bauweise, robust |
| BLDC / PMSM (mit FU) | Präzise Drehzahl- und Drehmomentregelung |
| Energieübertragung | Weniger Leitermaterial für gleiche Leistung als Einphasensystem |
| Schweisstrafo | Grosse Leistung ohne Spannungseinbrüche |

:::tip
Ein Drehstrommotor lässt sich durch **Tauschen zweier Phasen** in seiner Drehrichtung umkehren — dadurch dreht das magnetische Drehfeld in die andere Richtung. Beim Frequenzumrichter erfolgt die Drehrichtungsumkehr durch Software (Phasenfolge tauschen), ohne Verdrahtungsänderung.
:::
