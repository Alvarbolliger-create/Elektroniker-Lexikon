---
title: OPV Invertierender Verstärker
kategorie: EK
kapitel: OPV
tags: [invertierend, invertierender verstärker, opv, phasenumkehr, 180 grad, virtuelle masse, gegenkopplung, gbw, gain-bandwidth-product]
groessen: v_u|Verstärkung|—; U_A|Ausgangsspannung|V; U_E|Eingangsspannung|V; R_R|Gegenkopplungswiderstand|Ω; R_E|Eingangswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Nichtinvertierend]]
- [[OPV Summierend]]
:::
:::vbox
**Führt weiter zu**
- [[OPV Summierend]]
- [[OPV Integrierer]]
- [[OPV Differenzierer]]
:::
:::

---

Der invertierende Verstärker dreht das Signal um 180° und verstärkt es. Verstärkung und Eingangswiderstand werden durch zwei Widerstände exakt definiert — unabhängig vom OPV-Typ.

## Schaltung

:::schematic Invertierender OPV-Verstärker: OPV-Dreieck. U_E links → R_E → invertierender Eingang (−). Nichtinvertierender Eingang (+) auf GND. R_R von Ausgang zurück auf (−) (Gegenkopplung). Ausgang U_A rechts. Stromfluss: I_E durch R_E → virtuelle Masse → I_R durch R_R → Ausgang. Phasenumkehr 180°
/Diagramm/opv_invertierend.svg
:::

Signal über R_E an den invertierenden Eingang (–). R_R von Ausgang zurück auf (–). Nichtinvertierender Eingang (+) liegt auf GND (oder Referenz).

## Formeln

:::formel
U_A = -U_E * R_R / R_E      # Ausgangsspannung; Minuszeichen = 180° Phasenumkehr
U_E = -U_A * R_E / R_R      # Eingangsspannung
R_R = -(U_A / U_E) * R_E    # Gegenkopplungswiderstand
R_E = -(U_E / U_A) * R_R    # Eingangswiderstand
:::

Die Verstärkung:

:::formel
v_u = -R_R / R_E    # negativ = Phasenumkehr
:::

## Virtuelle Masse

Die Gegenkopplung zwingt den OPV seinen Ausgang nachzuregeln bis U_– = U_+ = 0 V (da + auf GND). Der Knoten am invertierenden Eingang (–) bleibt auf 0 V — die **virtuelle Masse**.

Der gesamte Strom aus U_E fliesst durch R_E in die virtuelle Masse, dann weiter durch R_R in den Ausgang. Nichts davon geht in den OPV-Eingang.

:::info
Virtuelle Masse gilt nur solange der Ausgang nicht sättigt. Wenn U_A die Versorgungsgrenze erreicht, bricht die virtuelle Masse zusammen.
:::

## Berechnungsbeispiel

:::monospace
Gesucht: U_A = -5 V aus U_E = 0.5 V (Verstärkung -10)
R_E = 10 kΩ (frei wählbar)
R_R = |v_u| × R_E = 10 × 10 kΩ = 100 kΩ

Probe: U_A = -0.5 × 100k/10k = -5 V ✓
:::

## GBW und Bandbreite

Das Gain-Bandwidth-Product begrenzt die nutzbare Bandbreite:

:::formel
f_3dB = GBW / |v_u|    # bei LM741 (GBW = 1 MHz) und v_u = 10: f_3dB = 100 kHz
:::

| OPV | GBW | v_u = 1 | v_u = 10 | v_u = 100 |
|---|---|---|---|---|
| LM741 | 1 MHz | 1 MHz | 100 kHz | 10 kHz |
| TL071 | 3 MHz | 3 MHz | 300 kHz | 30 kHz |
| OPA2134 | 8 MHz | 8 MHz | 800 kHz | 80 kHz |

:::warning
Hohe Verstärkung = kleine Bandbreite. Bei A = –100 und GBW = 1 MHz ist die Bandbreite nur 10 kHz. Immer GBW prüfen bevor ein OPV-Typ gewählt wird.
:::
