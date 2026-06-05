---
title: DMS (Dehnungsmessstreifen)
kategorie: EK
tags: [DMS, dehnungsmessstreifen, wheatstone, kraft, druck, wägezelle, gauge-factor, instrumentenverstärker, INA128, HX711, temperaturkompensation]
symbol: —
einheit: —
---

Ein DMS misst Dehnung oder Stauchung eines Körpers. Dünne Metallfolienbahnen ändern ihren Widerstand wenn sie verformt werden.

:::hbox
:::vbox
**Voraussetzungen**
- [[Wheatstone Brücke]]
- [[Vierleitermessung]]
:::
:::vbox
**Verwandte Artikel**
- [[Abstandssensoren]]
- [[Temperatursensoren]]
:::
:::

---

## Messprinzip

Der Widerstand einer metallischen Leitung ändert sich mit ihrer Länge:

:::formel
ΔR/R = GF × ε     # GF = Gauge Factor (ca. 2 für Metallfolie), ε = Dehnung
:::
Typische Dehnung: wenige Mikrometer pro Meter. Die Widerstandsänderung ist deshalb sehr klein (mΩ-Bereich).

## Wheatstone-Brücke

DMS werden immer in einer Wheatstone-Brücke betrieben. Dabei werden 1, 2 oder 4 DMS in die Brücke eingebaut.

- **Viertelbrücke (1 DMS)**: Einfachste Variante, Temperaturkompensation über Brückenwiderstand
- **Halbbrücke (2 DMS)**: Besser: Biege-DMS oben und unten verdoppeln das Signal
- **Vollbrücke (4 DMS)**: Maximale Empfindlichkeit, beste Temperaturkompensation

## Temperaturkompensation

DMS ändern ihren Widerstand auch mit der Temperatur. Durch den symmetrischen Aufbau der Brücke heben sich Temperatureffekte auf.

## Verstärkung

Das Brückensignal ist im µV-Bereich. Ein Instrumentenverstärker (INA128, INA122, AD8422) mit einstellbarer Verstärkung von 1-1000 bringt das Signal auf auswertbare Bereiche.

## Wägezellen

Eine Wägezelle ist ein mechanisches Bauteil mit aufgeklebten DMS und Vollbrücke. Genormt auf einen Nennwert (z.B. 2 mV/V bei Nennlast). Ausgangssignal direkt an ADC oder Wägezellenverstärker (HX711).

## Einsatz

Kraftmessung, Druckmessung, Drehmoment, Beschleunigung, Wägen. Fast jede Waage, jeder Drucksensor und jeder Kraftsensor enthält DMS.
