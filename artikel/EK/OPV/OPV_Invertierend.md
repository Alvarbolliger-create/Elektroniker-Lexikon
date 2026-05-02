---
title: OPV Invertierend
kategorie: EK
tags: [OPV, operationsverstärker, op-amp, invertierend, verstärker, gegenkopplung, verstärkungsfaktor, phasenumkehr, virtuelle masse, summenverstärker, GBW, gain-bandwidth-product]
symbol: —
einheit: —
---

Der invertierende Verstärker dreht das Signal um und verstärkt es. Verstärkung und Eingangswiderstand werden durch zwei Widerstände definiert.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV: Aufbau & Kennwerte]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Nichtinvertierend]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive Filter]]
- [[OPV Integrierer & Differenzierer]]
:::
:::

---

## Schaltung

Eingangssignal über R1 an den invertierenden Eingang (−). Rückkoppelwiderstand R2 von Ausgang zurück auf (−). Nichtinvertierender Eingang (+) liegt auf Masse oder Referenz.

:::schematic Invertierender Verstärker
/schaltplaene/opv_invertierend.svg
:::

## Verstärkung

```
A = -R2 / R1    # negatives Vorzeichen = Phasenumkehr um 180°
```

Die Verstärkung hängt nur vom Widerstandsverhältnis ab, nicht vom OPV selbst. Das macht sie sehr präzise und stabil.

| R1 | R2 | Verstärkung |
|---|---|---|
| 10 kΩ | 10 kΩ | -1 (Inverter) |
| 10 kΩ | 100 kΩ | -10 |
| 10 kΩ | 1 kΩ | -0.1 (Abschwächer) |

## Eingangswiderstand

Der Eingangswiderstand ist R1. Bei niedrigem R1 wird die Quelle belastet. Typisch werden 10 kΩ bis 100 kΩ gewählt.

## Virtuelle Masse

Die Gegenkopplung über R2 zwingt den OPV, seinen Ausgang so nachzuregeln, dass die Differenzspannung zwischen (−) und (+) auf null bleibt. Da (+) auf Masse liegt, hält der OPV den Knoten (−) ebenfalls auf 0 V — ohne dass er direkt mit Masse verbunden ist.

Der gesamte Eingangsstrom fliesst daher durch R1 und weiter in R2. In den OPV-Eingang selbst fliesst kein Strom (idealer OPV: unendliche Eingangsimpedanz).

:::info
Virtuelle Masse gilt nur solange die Gegenkopplung aktiv ist und der Ausgang nicht sättigt. Wenn U_aus die Versorgungsgrenze erreicht, bricht die virtuelle Masse zusammen und A = −R2/R1 gilt nicht mehr.
:::

:::tip
Für Summierverstärker einfach mehrere Eingangswiderstände parallel am invertierenden Eingang anschliessen. Jedes Signal wird mit −R2 / R_n gewichtet addiert.
:::

## Bandbreite (GBW-Produkt)

Jeder OPV hat ein konstantes Gain-Bandwidth-Product (GBW):

```
GBW = |A| × f_3dB    # Konstante des OPV-Typs, aus Datenblatt
f_3dB = GBW / |A|    # Nutzbare Bandbreite bei gewählter Verstärkung
```

Beispiel: OPV mit GBW = 1 MHz, Verstärkung |A| = 10 → f_3dB = 100 kHz.

| OPV-Typ | GBW | Verstärkung 10× → Bandbreite |
|---|---|---|
| LM741 | 1 MHz | 100 kHz |
| TL071 | 3 MHz | 300 kHz |
| LM358 | 1 MHz | 100 kHz |
| OPA2134 | 8 MHz | 800 kHz |

:::warning
Je höher die Verstärkung, desto kleiner die nutzbare Bandbreite. Bei A = −100 und GBW = 1 MHz ist die Bandbreite nur noch 10 kHz. Immer GBW aus dem Datenblatt prüfen und mit der benötigten Signalfrequenz vergleichen.
:::
