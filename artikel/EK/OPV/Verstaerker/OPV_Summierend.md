---
title: OPV Summierender Verstärker
kategorie: EK
kapitel: OPV
tags: [summierender verstärker, addierer, mischer, gewichtete summe, virtuelle masse, audio-mixer, dac, entkopplung]
groessen: U_A|Ausgangsspannung|V; R_R|Gegenkopplungswiderstand|Ω; R_1..n|Eingangswiderstände|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Invertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Subtrahierend]]
- [[OPV Invertierend]]
:::
:::vbox
**Führt weiter zu**
- [[Instrumentenverstärker]]
:::
:::

---

Der summierende Verstärker addiert mehrere Eingangssignale gewichtet — jedes Eingangssignal wird mit dem Faktor –R_R/R_n multipliziert und aufsummiert. Er basiert auf dem invertierenden Verstärker.

## Schaltung und Formel

:::schematic Summierender OPV-Verstärker (3 Eingänge): OPV-Dreieck. U_1 → R_1, U_2 → R_2, U_3 → R_3 — alle drei laufen auf den invertierenden Eingang (−). Nichtinvertierender Eingang (+) auf GND. Rückkopplung R_R von Ausgang auf (−). Virtuelle Masse am (−)-Knoten. Ausgang U_A
/Diagramm/opv_summierend.svg
:::

Mehrere Eingänge über je einen Widerstand R_1, R_2, ... R_n an den invertierenden Eingang (–). Rückkopplung über R_R.

:::formel
U_A = -R_R * (U_1/R_1 + U_2/R_2 + ... + U_n/R_n)    # allgemeine Formel
:::

**Sonderfall gleiche Widerstände** (R_1 = R_2 = ... = R_n = R_R):

:::formel
U_A = -(U_1 + U_2 + ... + U_n)    # einfache Summe mit Phasenumkehr
:::

## Herleitung mit virtueller Masse

Am Knoten (–) (virtuelle Masse) gilt die Knotenregel. Alle Eingangsströme fliessen durch R_R ab:

:::formel
I_1 + I_2 + ... + I_n + I_R = 0
U_1/R_1 + U_2/R_2 + ... = -U_A/R_R    # daraus folgt die Summenformel
:::

Dank der virtuellen Masse sind die Eingänge vollständig voneinander entkoppelt — U_1 beeinflusst U_2 nicht.

## Formeln zur Dimensionierung

:::formel
R_R = -U_A / (U_1/R_1 + U_2/R_2 + ... + U_n/R_n)    # Gegenkopplungswiderstand
R_1 = -U_1 * R_R / (U_A + R_R*(U_2/R_2 + ... + U_n/R_n))  # Widerstand für Eingang 1
:::

## Berechnungsbeispiel

:::monospace
U_1 = 1 V (Gewicht 2×), U_2 = 2 V (Gewicht 1×), U_A = -4 V
→ R_R = 10 kΩ (frei gewählt)
→ R_1 = R_R / 2 = 5 kΩ  (höheres Gewicht = kleinerer Widerstand)
→ R_2 = R_R / 1 = 10 kΩ

Probe: U_A = -10k × (1V/5k + 2V/10k) = -10k × (0.2 + 0.2) mA = -10k × 0.4 mA = -4 V ✓
:::

## Anwendungen

**Audio-Mischer**: Mehrere Mikrofon-/Instrumentensignale mit einstellbaren Potentiometern als R_n mischen. Jeder Eingang hat sein eigenes Lautstärke-Poti.

**DAC (Digital-Analog-Wandler)**: R-2R-Netzwerk als gewichteter Summierverstärker — jedes Bit hat sein eigenes R mit binärer Gewichtung.

**Signaladdition**: Gleichspannungsoffset zu einem Wechselsignal addieren.

:::tip
Für gleiche Gewichtung R_1 = R_2 = ... = R_R wählen. Der Ausgangswiderstand der Signalquellen muss klein gegen R_1, R_2 etc. sein, sonst wird die Gewichtung verfälscht.
:::
