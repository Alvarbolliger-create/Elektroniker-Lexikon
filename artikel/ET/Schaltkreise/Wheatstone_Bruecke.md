---
title: Wheatstone-Brücke
kategorie: ET
tags: [wheatstone, messbrücke, widerstand, abgleich, sensor, dms, instrumentationsverstärker, brückenspannung, viertelbrücke, halbbrücke, vollbrücke]
symbol: —
einheit: —
---

Die Wheatstone-Brücke misst unbekannte Widerstände sehr genau. Sie ist die Grundlage vieler Sensorsignalauswertungen, zum Beispiel bei Dehnungsmessstreifen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Spannungs- & Stromteiler]]
:::
:::vbox
**Verwandte Artikel**
- [[Druck & Kraft (DMS)]]
- [[Temperatursensoren]]
:::
:::vbox
**Führt weiter zu**
- [[Sensorik]]
- [[Vierleitermessung]]
:::
:::

---

## Aufbau

Vier Widerstände in einer Raute. Eine Diagonale liegt an der Versorgungsspannung, an der anderen wird die Brückenspannung gemessen.

:::schematic Wheatstone-Brücke Grundschaltung
/schaltplaene/wheatstone.svg
:::

R1 und R2 bilden den einen Spannungsteiler, R3 und R4 den anderen. Die Ausgangsspannung ist die Differenz der beiden Mittelpunktspannungen.

## Abgeglichene Brücke

Wenn R1/R2 = R3/R4 ist die Brücke abgeglichen: U_aus = 0 V.

```
R_x = R3 * R2 / R1      # unbekannter Widerstand aus drei bekannten
```

In der Praxis wird R3 so lange eingestellt bis U_aus = 0. Dann gilt die Formel exakt.

## Verstimmte Brücke (Sensor)

Ein Widerstand im Netz ändert sich, zum Beispiel ein NTC-Temperatursensor oder ein Dehnungsmessstreifen. Die Brücke ist nicht mehr abgeglichen. Für kleine Änderungen ΔR bei gleich grossen Grundwiderständen R gilt:

```
U_aus ≈ U_vers * (ΔR / (4 * R))
```

Das Ausgangssignal ist sehr klein (mV-Bereich). Es braucht einen Verstärker, meistens einen Instrumentationsverstärker.

## Brückenkonfigurationen

Je nachdem wie viele Widerstände aktive Sensorelemente sind, unterscheidet man drei Konfigurationen:

| Konfiguration | Aktive Elemente | Signalgrösse | Typischer Einsatz |
|---|---|---|---|
| Viertelbrücke | 1 | 1× | Einzelner NTC, einfache Dehnungsmessung |
| Halbbrücke | 2 | 2× | Biegebalken mit Zug- und Druckseite |
| Vollbrücke | 4 | 4× | DMS-Wägezellen, höchste Empfindlichkeit |

:::schematic Viertelbrücke
/schaltplaene/wheatstone_viertel.svg
:::

:::schematic Halbbrücke
/schaltplaene/wheatstone_halb.svg
:::

:::schematic Vollbrücke
/schaltplaene/wheatstone_voll.svg
:::

:::tip
Bei der Vollbrücke heben sich Temperatureinflüsse weitgehend auf, weil alle vier Elemente gleich driften. Das macht sie auch bei schwankender Umgebungstemperatur stabil.
:::
