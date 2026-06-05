---
title: Aktive Filter
kategorie: EK
tags: [aktive filter, OPV, sallen-key, butterworth, chebyshev, bessel, verstärkung, filterordnung, ripple, gruppenlaufzeit]
symbol: —
einheit: —
---

Aktive Filter verwenden OPVs zusammen mit R und C. Sie können verstärken, haben niedrigen Ausgangswiderstand und brauchen keine Spulen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Filter Grundlagen]]
- [[OPV Nichtinvertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[Tiefpass (TP)]]
- [[Hochpass (HP)]]
- [[Bandpass (BP)]]
- [[Bandsperre (BS)]]
:::
:::vbox
**Führt weiter zu**
- [[Filtercharakteristik]]
:::
:::

---

## Warum aktive Filter?

Passive RC-Filter dämpfen das Signal immer. Passive LC-Filter brauchen Spulen, die gross, teuer und schwer ideal sind. Aktive Filter mit OPV und RC-Bauteilen sind kompakter, günstiger und oft genauer.

## Sallen-Key Topologie

Die häufigste Grundschaltung für aktive Tiefpässe und Hochpässe 2. Ordnung. Zwei R, zwei C, ein OPV in Spannungsfolger-Schaltung.

40 dB/Dekade Dämpfung, glatte Flanke, einfach zu berechnen.

## Filtercharakteristiken

**Butterworth**: Maximale Flachheit im Durchlassband. Kein Ripple. Sanfte Flanke. Standard für die meisten Anwendungen.

**Chebyshev**: Steilere Flanke als Butterworth, aber mit Ripple im Durchlassband. Wenn die Flanke wichtiger ist als Gleichmässigkeit.

**Bessel**: Lineare Phase, konstantste Gruppenlaufzeit. Wichtig wenn die Signalform erhalten bleiben muss (Rechtecke, Pulse).

## Höhere Ordnungen

Mehrere Filterstufen 2. Ordnung in Reihe schalten. 4. Ordnung = zwei Stufen = 80 dB/Dekade. Jede Stufe hat andere Q-Werte, zusammen ergibt sich der gewünschte Gesamtfrequenzgang.

## Grenzfrequenz einstellen

:::formel
f_g = 1 / (2 * pi * R * C)     # für Sallen-Key mit R1=R2=R und C1=C2=C
:::
## OPV-Bandbreite als Grenze

Ein realer OPV hat ein Gain-Bandwidth-Product (GBW). Je höher die gewünschte Verstärkung, desto tiefer liegt die obere nutzbare Frequenz.

Typische OPVs (LM358, TL071) verstärken nur bis ca. **1–10 MHz** korrekt. Darüber sinkt die Verstärkung und die Phase dreht — der Filter verhält sich nicht mehr wie berechnet.

:::formel
f_max ≈ GBW / V_u     # nutzbare obere Frequenz; GBW aus Datenblatt
:::
Für Filterfrequenzen über 1 MHz: schnelle OPVs (z.B. OPA657, LM7171) oder andere Schaltungstopologien verwenden.

:::tip
Online-Filter-Design-Tools (z.B. Texas Instruments Filter Design Tool) berechnen alle Bauteilwerte für den gewünschten Typ, die Ordnung und die Grenzfrequenz. Manuell ist fehleranfällig.
:::
