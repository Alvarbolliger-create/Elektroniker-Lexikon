---
title: Oszillatoren — Grundlagen
kategorie: EK
tags: [oszillator, schwingung, rückkopplung, barkhausen, frequenz, sinusgenerator, AGC, positive rückkopplung, schleifenverstärkung, clipping]
symbol: f
einheit: Hz
---

Ein Oszillator erzeugt ein periodisches Signal ohne externen Eingang. Er braucht eine Verstärkungsstufe und eine frequenzbestimmende Rückkopplung.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV: Aufbau & Kennwerte]]
- [[RC-Filter]]
- [[Resonanz]]
:::
:::vbox
**Verwandte Artikel**
- [[Wien-Brücken-Oszillator]]
- [[RC-Phasenschieber-Oszillator]]
- [[Colpitts-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Quarz-Oszillator]]
- [[PLL]]
:::
:::

---

## Grundprinzip

Ein Oszillator besteht aus:
1. **Verstärker** (OPV, Transistor) — ersetzt die Dämpfungsverluste
2. **Frequenzselektives Rückkopplungsnetzwerk** — bestimmt die Schwingfrequenz
3. **Positive Rückkopplung** — hält die Schwingung aufrecht

Das Ausgangssignal wird teilweise zurückgeführt und wieder verstärkt. Wenn Verstärkung und Phasenlage genau stimmen, schwingt die Schaltung.

## Schwingungsbedingung

Damit ein Oszillator stabil schwingt, müssen zwei Bedingungen gleichzeitig erfüllt sein:

```
φ = φ_V + φ_R = 0°        # Phasenbedingung: Gesamtphasendrehung im Kreis = 0
k · v_u ≥ 1               # Amplitudenbedingung: Schleifenverstärkung ≥ 1
```

- **v_u** = Spannungsverstärkung des Verstärkers
- **k** = Rückkopplungsfaktor des frequenzbestimmenden Netzwerks
- **φ_V** = Phasendrehung des Verstärkers
- **φ_R** = Phasendrehung des Rückkopplungsnetzwerks

Ist k · v_u > 1: Amplitude wächst bis zur Begrenzung (Clipping).  
Ist k · v_u < 1: Schwingung klingt ab.

:::info
In der Praxis wird der Oszillator mit k · v_u etwas grösser als 1 gestartet damit er sicher anläuft. Eine automatische Amplitudenregelung (AGC) oder nichtlineare Begrenzung hält die Amplitude dann konstant.
:::

## Klassifizierung nach Frequenznetzwerk

| Typ | Frequenznetzwerk | k | v_u min | Frequenzbereich |
|---|---|---|---|---|
| RC-Phasenschieber | RC-Kette (3 Stufen) | 1/29 | > 29 | 1 Hz – 100 kHz |
| Wien-Robinson | RC-Brücke | 1/3 | ≥ 3 | 1 Hz – 1 MHz |
| Colpitts / Hartley | LC-Schwingkreis | N₂/N₁ | — | 100 kHz – GHz |
| Quarz | Piezoelektrischer Resonator | — | — | kHz – GHz, sehr präzise |
