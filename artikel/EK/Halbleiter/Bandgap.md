---
title: Bandgap-Referenz
kategorie: EK
tags: [Bandgap, Spannungsreferenz, temperaturstabil, PTAT, CTAT, 1.25V, Silizium]
symbol: V_BG
einheit: V
---

Eine Bandgap-Referenz erzeugt eine stabile Referenzspannung unabhängig von Temperatur und Versorgungsspannung. Das Grundprinzip nutzt zwei gegenläufige Temperaturabhängigkeiten, die sich aufheben.

:::hbox
:::vbox
**Voraussetzungen**
- [[pn-Übergang]]
- [[Bipolartransistor (BJT)]]
- [[OPV Aufbau]]
:::
:::vbox
**Verwandte Artikel**
- [[Zener-Diode]]
- [[Lineare Regler]]
:::
:::

---

## Das Problem mit anderen Referenzen

**Zener-Dioden**: Temperaturkoeffizient je nach Spannung positiv oder negativ. Bei ca. 5.6 V kompensieren sich Zener-Effekt und Lawinendurchbruch — aber trotzdem nicht stabil genug für viele Anwendungen. Zudem Rauschen.

**Dioden-Durchlassspannung**: Etwa -2 mV/K. Stark temperaturabhängig.

## Zwei gegenläufige Effekte

**CTAT (Complementary To Absolute Temperature)**: Die Basis-Emitter-Spannung VBE eines Transistors sinkt mit steigender Temperatur, ca. -2 mV/K.

**PTAT (Proportional To Absolute Temperature)**: Die Differenz der VBE zweier Transistoren, die bei unterschiedlichen Stromdichten betrieben werden, steigt proportional zur absoluten Temperatur.

:::formel
ΔVBE = (kT/q) × ln(n)    # k = Boltzmann, T = Kelvin, q = Elementarladung, n = Stromdichteverhältnis
:::
## Bandgap-Prinzip

Wenn CTAT und PTAT passend gewichtet (addiert) werden, heben sich die Temperaturkoeffizienten auf:

:::formel
V_BG = VBE + A × ΔVBE    # A = Gewichtungsfaktor
:::
Der Gewichtungsfaktor A wird so gewählt, dass die Temperaturabhängigkeit zu null wird.

Das Ergebnis ist nahezu die Bandlückenspannung von Silizium bei 0 K:

:::formel
V_BG ≈ 1.25 V    # typischer Bandgap-Referenzwert
:::
## Typische Implementierung (Widlar-Bandgap)

Zwei Transistoren Q1 und Q2, wobei Q2 aus mehreren parallel geschalteten Transistoren besteht (Emitterfläche n-fach grösser). Ein OPV hält die Emitterströme gleich. Dann gilt:

:::formel
ΔVBE = VT × ln(n)    # VT = thermische Spannung = kT/q ≈ 26 mV bei 25°C
:::
Ein Widerstandsverhältnis skaliert PTAT auf den richtigen Betrag zur Kompensation von CTAT.

## Praxis-ICs

| IC | Ausgangsspannung | Bemerkung |
|---|---|---|
| LM385-1.2 | 1.235 V | Einfache Referenz |
| TL431 | 2.5 V einstellbar | Sehr verbreitet, shunt-Referenz |
| REF02 | 5.0 V | Präzise, ±0.3 % |
| ADR4525 | 2.5 V | 3 ppm/°C, sehr niedrig |

## Anwendungen

- Referenzspannung für ADC und DAC
- Präzise Spannungsregler
- Temperaturkompensierte Messschaltungen
- Batteriespannungsüberwachung

:::info
Die Bandgap-Referenz funktioniert auch in CMOS-Technologie mit Hilfe von parasitären Bipolartransistoren (aus dem Substrat). Daher ist sie in nahezu jedem modernen Analogchip integriert.
:::
