---
title: Buck-Boost Converter
kategorie: EK
tags: [Buck-Boost, Tief-Hochsetzsteller, inverting, Schaltregler, CCM, DCM]
symbol: —
einheit: —
---

Ein Buck-Boost-Converter kann die Ausgangsspannung sowohl unter als auch über die Eingangsspannung setzen. Je nach Topologie ist die Ausgangsspannung invertiert oder nicht.

:::hbox
:::vbox
**Voraussetzungen**
- [[Buck (Step-down)]]
- [[Boost (Step-up)]]
- [[PWM Arten]]
:::
:::vbox
**Verwandte Artikel**
- [[Flyback & Forward Converter]]
- [[Lineare Regler]]
:::
:::

---

## Warum Buck-Boost?

Batteriebetriebene Geräte: Die Batteriespannung sinkt von 4.2 V (voll) auf 3.0 V (leer). Wenn die gewünschte Ausgangsspannung 3.3 V ist, braucht man manchmal einen Hochsetzsteller (Boost) und manchmal einen Tiefsetzsteller (Buck). Der Buck-Boost deckt den gesamten Bereich ab.

## Invertierende Topologie (klassisch)

Die einfachste Buck-Boost-Topologie invertiert die Ausgangsspannung:

**Einschaltphase** (Transistor leitet):
- Eingang lädt die Drossel
- Ausgang wird von C_out gespeist
- Diode sperrt

**Ausschaltphase** (Transistor sperrt):
- Drossel gibt Energie über Diode an Ausgang ab
- Ausgang liegt zwischen GND und Diodenkatode → negativer Ausgang

:::formel
UOUT = -UIN × D / (1 - D)    # D = Tastverhältnis (Duty Cycle)
:::
Nachteil: Ausgang ist invertiert. Für viele Anwendungen unpraktisch.

## Nicht-invertierende Topologie (SEPIC, Ćuk, 4-Schalter)

### SEPIC (Single-Ended Primary Inductance Converter)

Zwei Drosseln und ein Kopplungskondensator. Ausgang nicht invertiert, galvanisch nicht getrennt.

:::formel
UOUT = UIN × D / (1 - D)    # nicht-invertierend
:::
### Ćuk-Converter

Ähnlich wie SEPIC aber invertierend. Vorteile: beide Ströme (Ein und Aus) werden gefiltert.

### 4-Schalter Buck-Boost

Vier Transistoren (zwei H-Brücke am Eingang, zwei am Ausgang mit gemeinsamer Drossel). Jeder moderne Lithium-Laderegulator (z.B. in Smartphones) verwendet diese Topologie. Geringer Ripple, guter Wirkungsgrad.

## CCM (Continuous Conduction Mode)

Der Spulenstrom fliesst immer, bricht nie auf null ab. Gültig bei mittleren bis hohen Lasten.

:::formel
UOUT/UIN = D / (1 - D)    # CCM, invertierend
:::
Im CCM: Rückkopplungsregelung stabiler, Ausgangsstrom kontinuierlich.

## DCM (Discontinuous Conduction Mode)

Bei kleinen Lasten fällt der Spulenstrom auf null, bevor der nächste Einschaltzyklus beginnt. Ausgangsspannung steigt stärker mit sinkendem Laststrom — anderes Regelverhalten.

## Typische Controller-ICs

| IC | Topologie | Bemerkung |
|---|---|---|
| LM2577 | Boost / inverting | Einfach, bis 3 A |
| TPS63000 | 4-Schalter | Bis 1 A, ideal für Akkubetrieb |
| LTC3780 | 4-Schalter | Bis 20 A, hohe Effizienz |
| MAX17222 | Boost | Ultra-Low-Power |

:::tip
Für Akkubetrieb mit variabler Spannung ist der 4-Schalter Buck-Boost die beste Wahl. Für einfache Anwendungen mit invertiertem Ausgang genügt die klassische Topologie.
:::
