---
title: Temperatursensoren
kategorie: EK
tags: [temperatursensor, NTC, PTC, PT100, thermoelement, temperaturmessung, seebeck-effekt, kaltstellenkompensation, vierleitermessung, LM35, IC-sensor]
symbol: T
einheit: °C
---

Temperatursensoren wandeln Temperatur in ein elektrisches Signal um. Jeder Typ hat andere Eigenschaften, Genauigkeiten und Einsatzbereiche.

:::hbox
:::vbox
**Voraussetzungen**
- [[Widerstand]]
- [[Wheatstone-Brücke]]
:::
:::vbox
**Verwandte Artikel**
- [[Druck & Kraft (DMS)]]
:::
:::vbox
**Führt weiter zu**
- [[Regelungstechnik]]
:::
:::

---

## NTC (Negative Temperature Coefficient)

Widerstand sinkt mit steigender Temperatur. Günstig, weit verbreitet, aber nichtlineare Kennlinie.

Typisch für Temperaturüberwachung in Netzteilen, Akkus und einfachen Regelungen. Braucht Linearisierung (Spannungsteiler + Kalibrierung) für genaue Messungen.

## PTC (Positive Temperature Coefficient)

Widerstand steigt mit Temperatur. Wird oft als selbstregulierende Sicherung eingesetzt: Bei Überhitzung steigt R, Strom sinkt, Bauteil kühlt ab.

## PT100 / PT1000

Platinwiderstand mit definiertem Wert bei 0 °C (100 Ω bzw. 1000 Ω). Sehr genaue und stabile Kennlinie. Standard in der Industrie.

PT100 hat 0.385 Ω/°C. Kleines Signal, braucht Verstärker.

PT1000 hat 3.85 Ω/°C. Einfacher auszuwerten, weniger empfindlich gegen Leitungswiderstand.

Messung mit Vierleiterschaltung für beste Genauigkeit.

## Thermoelemente

Zwei verschiedene Metalle verbunden. An der Verbindungsstelle entsteht eine temperaturabhängige Spannung (Seebeck-Effekt). Sehr grosser Temperaturbereich, bis über 1000 °C.

Signal sehr klein (Mikrovolt pro Kelvin). Braucht Kaltstellenkompensation und Verstärker.

## Vergleich

| Typ | Bereich | Genauigkeit | Signal | Aufwand |
|---|---|---|---|---|
| NTC | -50 bis 150 °C | ±1 bis 5 °C | R nichtlinear | niedrig |
| PT100 | -200 bis 850 °C | ±0.1 °C | R linear | mittel |
| Thermoelement (Typ K) | -200 bis 1260 °C | ±2 °C | µV | hoch |
| IC-Sensor (z.B. LM35) | -55 bis 150 °C | ±1 °C | Spannung linear | sehr niedrig |
