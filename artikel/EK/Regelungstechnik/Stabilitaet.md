---
title: Stabilität und Schwingneigung
kategorie: EK
tags: [stabilität, schwingneigung, phasenreserve, bode-diagramm, regelkreis, amplitudenreserve, phasengang, lead-kompensator, 45-grad-kriterium]
symbol: —
einheit: °, dB
---

Ein instabiler Regelkreis schwingt auf. Die Phasenreserve sagt wie weit ein System vom Schwingen entfernt ist.

:::hbox
:::vbox
**Voraussetzungen**
- [[Regelkreis]]
- [[PID-Regler]]
- [[Frequenzgang und Verstärkungsfaktor]]
:::
:::vbox
**Verwandte Artikel**
- [[PID Regler]]
- [[Aktive Filter]]
:::
:::

---

## Warum schwingt ein Regelkreis?

Ein Regelkreis schwingt wenn das verstärkte Signal nach dem Umlauf durch den Kreis in Phase mit dem Eingangssignal zurückkommt. Phasenversatz von 180° bei einer Verstärkung >= 1 führt zur Schwingung.

Jede reale Übertragungsstrecke verzögert das Signal frequenzabhängig.

## Bode-Diagramm

Das Bode-Diagramm zeigt:
- **Amplitudengang**: Verstärkung in dB über die Frequenz
- **Phasengang**: Phasenversatz in ° über die Frequenz

Kritischer Punkt: Frequenz bei der der Amplitudengang 0 dB (Verstärkung = 1) kreuzt.

## Phasenreserve

Die Phasenreserve ist der Abstand zwischen dem tatsächlichen Phasengang bei 0-dB-Durchgang und -180°.

:::monospace
Phasenreserve = Phasengang bei 0 dB + 180°
:::
- Phasenreserve > 45°: stabil, leicht überschwingend
- Phasenreserve > 60°: gut gedämpft, kein Überschwingen
- Phasenreserve < 30°: Gefahr, System neigt zu Schwingungen

## Amplitudenreserve

Der Abstand des Amplitudengangs von 0 dB bei -180° Phasenlage.

Typisch: mindestens 6 dB Amplitudenreserve anstreben.

## Stabilisierung

- **D-Anteil (PID)**: Schnellere Reaktion, verbessert Phasenreserve
- **Frequenzgangkorrektur**: Lead-Kompensator fügt Phase hinzu
- **Bandbreitenbegrenzung**: Tiefpass nach dem Regler vermindert Hochfrequenzverstärkung
- **Reglerverstärkung reduzieren**: Sicherster Weg, aber langsamere Reaktion

## Praktisch

Für Schaltregler: Bode-Plot mit Netzwerkanalysator oder Frequenzgangmessung mit Sinussweep und Oszilloskop messen. Phasenreserve direkt ablesen.
