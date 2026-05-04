---
title: Tiefpass (TP)
kategorie: EK
tags: [tiefpass, TP, grenzfrequenz, dämpfung, RC, sallen-key, aktiv, passiv, glättung, rauschunterdrückung, filterordnung, 20dB]
symbol: —
einheit: —
---

Ein Tiefpass (TP) lässt tiefe Frequenzen ungehindert durch und dämpft hohe Frequenzen. Je höher die Frequenz über der Grenzfrequenz, desto stärker die Dämpfung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Filter Grundlagen]]
- [[RC-Filter]]
:::
:::vbox
**Verwandte Artikel**
- [[Hochpass (HP)]]
- [[Bandpass (BP)]]
- [[Aktive Filter]]
:::
:::vbox
**Führt weiter zu**
- [[Filtercharakteristik]]
:::
:::

---

## Anwendungen

- Glättung von Sensorsignalen (Temperatur, Helligkeit — langsam veränderliche Grössen)
- Rauschunterdrückung vor einem ADC
- Siebung der Versorgungsspannung nach dem Gleichrichter
- Anti-Aliasing-Filter vor der Digitalisierung

## Frequenzgang

:::plot
var: f
range: 0.01, 100
xlabel: Frequenz (normiert)
ylabel: Amplitude (normiert)
Tiefpass 1. Ordnung: 1 / sqrt(1 + f*f)
Tiefpass 2. Ordnung: 1 / sqrt(1 + f^4)
:::

Unterhalb der Grenzfrequenz f_g: volle Amplitude. Oberhalb: Dämpfung mit 20 dB/Dekade pro Ordnung.

## Grenzfrequenz

Die **Grenzfrequenz f_g** ist die Frequenz, bei der die Ausgangsamplitude auf **70.7 %** des Eingangs abgefallen ist (= −3 dB):

:::monospace
f_g = 1 / (2 · π · R · C)     # Passiver RC-Tiefpass 1. Ordnung
:::
## Passiver RC-Tiefpass (1. Ordnung)

R in Reihe, C parallel zur Last. Tiefe Frequenzen: C hat hohen Widerstand → Spannung fällt an R ab, aber kaum an C. Hohe Frequenzen: C hat niedrigen Widerstand → Spannung fällt an C ab.

- Steilheit: **20 dB/Dekade**
- Einfach, kein Versorgungsstrom
- Dämpft das Signal immer etwas

## Aktiver Tiefpass — Sallen-Key (2. Ordnung)

OPV als Spannungsfolger mit zwei R und zwei C. Steilheit: **40 dB/Dekade** bei halber Schaltungskomplexität gegenüber zwei passiven Stufen.

:::monospace
f_g = 1 / (2 · π · R · C)     # für R1 = R2 = R und C1 = C2 = C
:::
Vorteil gegenüber passivem Filter: Kein Einfluss auf die Lastimpedanz, kann leicht kaskadiert werden.

## Steilheit und Ordnung

| Ordnung | Steilheit | Schaltungsaufwand |
|---|---|---|
| 1 | 20 dB/Dek | 1 R + 1 C |
| 2 | 40 dB/Dek | Sallen-Key (2R, 2C, OPV) |
| 4 | 80 dB/Dek | 2 × Sallen-Key kaskadiert |
| 8 | 160 dB/Dek | 4 × Sallen-Key oder SC-Filter |

:::tip
Für einfache Sensorsignalglättung reicht ein RC-Tiefpass 1. Ordnung. Grenzfrequenz so wählen dass das Nutzsignal noch durchkommt, Störungen aber gedämpft werden. Faustregel: f_g = 5–10 × Nutzfrequenz.
:::
