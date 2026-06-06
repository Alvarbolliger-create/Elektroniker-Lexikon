---
title: Instrumentenverstärker (3-OPV)
kategorie: EK
kapitel: OPV
tags: [instrumentenverstärker, 3-opv, cmrr, präzisionsverstärker, messverstärker, brückenauswertung, gleichtaktunterdrückung, r_g, ina128, ina333, hochohmig]
groessen: G|Verstärkung|—; CMRR|Gleichtaktunterdrückung|dB; R_G|Gainwiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Subtrahierend]]
- [[OPV Nichtinvertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Subtrahierend]]
:::
:::vbox
**Führt weiter zu**
- [[Sensorik Grundlagen]]
:::
:::

---

Der Instrumentenverstärker (INA) löst die zwei grössten Schwächen des einfachen Subtrahierverstärkers: niedriger Eingangswiderstand und schlechte CMRR. Er besteht aus drei OPVs und liefert CMRR-Werte > 100 dB bei hohem Eingangswiderstand.

## Aufbau: Zwei Stufen

:::schematic Instrumentenverstärker 3-OPV: Erste Stufe: OPV A (nichtinvertierend, Eingang U_1) und OPV B (nichtinvertierend, Eingang U_2). Zwischen den (−)-Eingängen beider OPVs liegt R_G (Gainwiderstand). Ausgänge OPV A und B führen zur zweiten Stufe. Zweite Stufe: OPV C als Subtrahierverstärker mit 4 gleichen Widerständen R. Ausgang U_out. Verstärkung G = 1 + 2R/R_G
/Diagramm/instrumentenverstaerker.svg
:::

**Erste Stufe** — zwei nichtinvertierende Pufferverstärker (OPV A und OPV B):
- Beide Eingänge U_1 und U_2 werden von je einem OPV hochohmig gepuffert
- Zwischen den invertierenden Eingängen (–) der beiden OPVs liegt der **Gainwiderstand R_G**
- Die Differenz U_1 – U_2 wird verstärkt, Gleichtaktsignale werden kaum berührt

**Zweite Stufe** — ein Subtrahierverstärker (OPV C):
- Vier gleiche Widerstände R bilden den Differenzverstärker
- Subtrahiert die Ausgänge der ersten Stufe und unterdrückt Reste des Gleichtaktsignals

## Verstärkungsformel

:::formel
G = (1 + 2 * R / R_G)    # Gesamtverstärkung; R = Widerstände der zweiten Stufe
R_G = 2 * R / (G - 1)    # Gainwiderstand aus gewünschter Verstärkung
:::

Die Verstärkung wird durch **einen einzigen Widerstand R_G** eingestellt — alle anderen Widerstände bleiben fest. Das ist der grosse Vorteil: keine symmetrischen Widerstandspaare müssen abgestimmt werden.

## Berechnungsbeispiel

:::monospace
INA128 (R intern = 40 kΩ), gewünschte Verstärkung G = 100
R_G = 2 × 40 kΩ / (100 - 1) = 80 kΩ / 99 ≈ 808 Ω → 806 Ω (Normwert E96)

Probe: G = 1 + 2×40k/806 = 1 + 99.3 ≈ 100 ✓
:::

## Vergleich: Subtrahierverstärker vs. Instrumentenverstärker

| Eigenschaft | Subtrahierverstärker | Instrumentenverstärker |
|---|---|---|
| Eingangswiderstand | R_E (10–100 kΩ) | > 10 GΩ |
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
