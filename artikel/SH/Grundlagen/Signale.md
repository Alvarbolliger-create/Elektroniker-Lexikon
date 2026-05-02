---
title: Signale
kategorie: SH
tags: [signal, analog, digital, pegel, spannung, rauschen, ADC, DAC, signalintegrität, TTL, CMOS, sampling, HIGH, LOW]
symbol: —
einheit: —
---

Ein Signal überträgt Information. In der Elektronik ist das meistens eine Spannung die sich über die Zeit verändert. Signale sind entweder analog oder digital.

:::hbox
:::vbox
**Voraussetzungen**
- —
:::
:::vbox
**Verwandte Artikel**
- [[Zahlensysteme]]
- [[Logikgatter]]
:::
:::vbox
**Führt weiter zu**
- [[Zahlensysteme]]
- [[AD/DA Grundlagen]]
:::
:::

---

## Analoges Signal

Kann jeden beliebigen Wert annehmen. Ein Mikrofon gibt eine analoge Spannung aus, die dem Schalldruck folgt. Ein Temperatursensor gibt eine analoge Spannung proportional zur Temperatur.

Analogsignale sind empfindlich gegenüber Rauschen. Jede Störung verändert den Wert.

## Digitales Signal

Kennt nur zwei Zustände: HIGH und LOW. In der Praxis sind das Spannungsbereiche, nicht exakte Werte.

| Logikfamilie | LOW | HIGH |
|---|---|---|
| 5V TTL | unter 0.8 V | über 2.0 V |
| 3.3V CMOS | unter 1.0 V | über 2.3 V |
| 1.8V LVTTL | unter 0.6 V | über 1.2 V |

Digitale Signale sind robuster. Ein Pegel von 3.0 V wird als HIGH interpretiert, unabhängig ob er eigentlich 3.0 oder 3.2 V ist.

## Analog zu Digital

Analoge Signale werden mit einem Analog-Digital-Wandler (ADC) in digitale Zahlen umgewandelt. Digital zu Analog geht mit einem DAC.

Mehr dazu unter [[AD/DA Grundlagen]].

## Signalintegrität

Lange Leitungen, hohe Frequenzen und schlechtes Layout können digitale Signale verfälschen. Was als scharfe Rechteckflanke losgeht, kommt verundet oder mit Über- und Unterschwingern an.
