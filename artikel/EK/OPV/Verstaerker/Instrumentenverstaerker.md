---
title: Instrumentenverstärker (3-OPV)
kategorie: EK
kapitel: OPV
tags: [instrumentenverstärker, 3-opv, cmrr, präzisionsverstärker, messverstärker, brückenauswertung, gleichtaktunterdrückung, r_gain, ina128, ina333, hochohmig]
groessen: U_A|Ausgangsspannung|V; G|Verstärkung|—; CMRR|Gleichtaktunterdrückung|dB; R|Rückkopplungswiderstand 1. Stufe|Ω; R_gain|Gainwiderstand|Ω; R1|Eingangswiderstand 2. Stufe|Ω; R2|Gegenkopplungswiderstand 2. Stufe|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Subtrahierender Verstärker]]
- [[OPV Nichtinvertierender Verstärker]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Subtrahierender Verstärker]]
:::
:::vbox
**Führt weiter zu**
- [[Sensorik Grundlagen]]
:::
:::

---

Der Instrumentenverstärker (INA) löst die zwei grössten Schwächen des einfachen Subtrahierverstärkers: niedriger Eingangswiderstand und schlechte CMRR. Er besteht aus drei OPVs und liefert CMRR-Werte > 100 dB bei hohem Eingangswiderstand.

## Aufbau: Zwei Stufen

:::schematic Instrumentenverstärker (3-OPV, mit Verstärkungsnetzwerk R_gain)
/schaltplaene/OPV/Verstärker/opv_instrumentenverstaerker_gain.svg
:::

**Erste Stufe** — zwei nichtinvertierende Pufferverstärker (OPV A und OPV B):
- Beide Eingänge U_1 und U_2 werden von je einem OPV hochohmig gepuffert
- Zwischen den invertierenden Eingängen (–) der beiden OPVs liegt der **Gainwiderstand R_gain**, jeder OPV hat zudem einen Rückkopplungswiderstand R zu seinem eigenen Ausgang
- Die Differenz U_1 – U_2 wird verstärkt, Gleichtaktsignale werden kaum berührt

**Zweite Stufe** — ein Subtrahierverstärker (OPV C):
- Eingangswiderstände R1 und Gegenkopplungswiderstände R2 (gleiche Rollen wie beim [[OPV Subtrahierender Verstärker]]) bilden den Differenzverstärker mit der Verstärkung R2/R1
- Subtrahiert die Ausgänge der ersten Stufe und unterdrückt Reste des Gleichtaktsignals

## Ausgangsspannung und Verstärkung

:::formel
U_A = (U_2 - U_1) * (R2 / R1) * (1 + 2 * R / R_gain)
G   = (R2 / R1) * (1 + 2 * R / R_gain)
:::

In der Praxis wählt man R1 = R2, damit das Verhältnis R2/R1 = 1 wird und die zweite Stufe nicht zur Gesamtverstärkung beiträgt. Dann gilt G = 1 + 2R/R_gain, und die Verstärkung wird durch **einen einzigen Widerstand R_gain** eingestellt — alle anderen Widerstände bleiben fest. Das ist der grosse Vorteil: keine symmetrischen Widerstandspaare müssen für die Verstärkungseinstellung abgestimmt werden, R1/R2 bleiben fest und müssen nur paarweise genau übereinstimmen.

:::formel
R_gain = 2 * R / (G - 1)    # Gainwiderstand aus gewünschter Verstärkung (für R1 = R2)
:::

## Berechnungsbeispiel

:::monospace
INA128 (R intern = 40 kΩ, R1 = R2), gewünschte Verstärkung G = 100
R_gain = 2 × 40 kΩ / (100 - 1) = 80 kΩ / 99 ≈ 808 Ω → 806 Ω (Normwert E96)

Probe: G = (R2/R1) × (1 + 2×40k/806) = 1 × (1 + 99.3) ≈ 100 ✓
:::

## Vergleich: Subtrahierverstärker vs. Instrumentenverstärker

| Eigenschaft | Subtrahierverstärker | Instrumentenverstärker |
|---|---|---|
| Eingangswiderstand | R1/R3 (10–100 kΩ) | > 10 GΩ |
| CMRR | 40–80 dB | 80–130 dB |
| Verstärkungseinstellung | 2 Widerstandspaare | 1 Widerstand R_G |
| Aufwand | gering (1 OPV) | höher (3 OPV oder IC) |
| Einsatz | einfache Differenzbildung | Präzisionsmessung |

## Typische INA-ICs

| Typ | CMRR | Rauschen | Besonderheit |
|---|---|---|---|
| INA128 | 120 dB | 8 nV/√Hz | Präzision, ±18 V |
| INA333 | 100 dB | 50 nV/√Hz | 1.8–5.5 V, sehr wenig Strom |
| AD8221 | 130 dB | 7 nV/√Hz | Sehr tief Rauschen |
| INA126 | 83 dB | 35 nV/√Hz | Günstig, Single-Supply |

## Anwendungen

**Brückenauswertung**: Wheatstone-Brücke mit Dehnungsmessstreifen (DMS), NTC, Drucksensor. Die Differenzspannung ist klein (mV), Gleichtaktspannung gross (V) — hoher CMRR nötig.

**EKG / Biomedizin**: Körpersignale (µV bis mV) bei hohen Gleichtaktstörungen (50 Hz Netz).

**Thermoelement-Messung**: Thermospannung (µV/K) bei hoher Störeinstrahlung.
