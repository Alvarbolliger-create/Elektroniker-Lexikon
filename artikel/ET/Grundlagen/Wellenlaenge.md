---
title: Wellenlänge
kategorie: ET
tags: [wellenlänge, frequenz, lichtgeschwindigkeit, ausbreitung, elektromagnetische welle, antenne]
groessen: lambda|Wellenlänge|m; f|Frequenz|Hz; c|Ausbreitungsgeschwindigkeit|m/s; T|Periodendauer|s
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen & Effektivwert]]
:::
:::

---

Jede periodische Schwingung, die sich im Raum ausbreitet, hat eine Wellenlänge — den Abstand zwischen zwei gleichen Punkten der Welle. Wellenlänge und Frequenz sind über die Ausbreitungsgeschwindigkeit verknüpft.

## Formel

:::schematic Sinusförmige Welle; X-Achse: Ort in Metern; Y-Achse: Amplitude; eine vollständige Periode dargestellt; Wellenlänge lambda als horizontaler Doppelpfeil zwischen zwei aufeinanderfolgenden Scheitelpunkten eingezeichnet; Beschriftung: lambda
/abbildungen/grundlagen/wellenlaenge.svg
:::

:::formel
lambda = c / f    # Wellenlänge lambda (m) = Geschwindigkeit c (m/s) / Frequenz f (Hz)
:::

Oder über die Periodendauer T = 1/f:

:::formel
lambda = c * T
:::

## Ausbreitungsgeschwindigkeit

Elektromagnetische Wellen breiten sich im Vakuum mit Lichtgeschwindigkeit aus:

c₀ = 3 · 10⁸ m/s = 300 000 km/s

In einem Medium (Dielektrikum) ist die Ausbreitungsgeschwindigkeit kleiner:

:::formel
c = c_0 / sqrt(epsilon_r)
:::

In Koaxialkabeln (epsilon_r ≈ 2,25) ist c ≈ 200 000 km/s, also etwa 2/3 der Lichtgeschwindigkeit.

## Typische Wellenlängen

| Bereich | Frequenz | Wellenlänge | Anwendung |
|---|---|---|---|
| Netzfrequenz | 50 Hz | 6000 km | Energie |
| Mittelwelle AM | 500 kHz–1,6 MHz | 200–600 m | Rundfunk |
| UKW FM | 88–108 MHz | 2,8–3,4 m | Rundfunk |
| WLAN 2,4 GHz | 2,4 GHz | 12,5 cm | Datenfunk |
| WLAN 5 GHz | 5 GHz | 6 cm | Datenfunk |
| Sichtbares Licht | 430–770 THz | 390–700 nm | Optik |

## Bedeutung für Antennen

Eine Antenne arbeitet optimal, wenn ihre physische Länge auf die Wellenlänge abgestimmt ist. Die häufigste Ausführung ist der **Lambda/4-Strahler** (Viertelwellen-Antenne):

:::formel
l_antenne = lambda / 4
:::

:::monospace
Beispiel: WLAN 2.4 GHz
lambda = 300e6 / 2.4e9 = 0.125 m = 12.5 cm
l_antenne = 12.5 / 4 = 3.1 cm  (typische PCB-Antenne)
:::

Bei einer Länge von genau λ/4 bildet sich eine **stehende Welle** auf dem Leiter: Strommaximum am Fusspunkt, Spannungsmaximum an der Spitze. Die Antenne befindet sich in Resonanz — der Speisepunktwiderstand ist rein reell (kein Blindanteil), was eine direkte Anpassung an den Sender ermöglicht.

Mit einer leitenden Fläche als Gegengewicht (Groundplane) wirkt der λ/4-Monopol elektrisch wie ein λ/2-Dipol — die Fläche spiegelt die fehlende Hälfte. Der Speisewiderstand beträgt dabei ca. 36 Ω (Monopol) bzw. 73 Ω (Dipol). Bei anderen Antennenlängen entsteht ein kapazitiver oder induktiver Blindanteil, der mit einem zusätzlichen Anpassnetzwerk korrigiert werden muss.

| Antennentyp | Länge | Speiswiderstand (ca.) | Anwendung |
|---|---|---|---|
| Lambda/4 Monopol + GP | λ/4 | 36 Ω | WLAN, Mobilfunk, PCB-Antennen |
| Lambda/2 Dipol | λ/2 | 73 Ω | UKW-Rundfunk, Yagi-Elemente |
| 5/8 Lambda | 5λ/8 | ~50 Ω + Induktivität | Fahrzeugantennen (höherer Gewinn) |

:::tip
Die Wellenlänge erklärt, warum höhere Frequenzen kleinere Antennen erlauben (Handys, WLAN) — aber auch warum sie schlechter durch Wände dringen: Hohe Frequenzen werden stärker absorbiert und reflektiert.
:::
