---
title: FFT (Fast Fourier Transform)
kategorie: MT
tags: [FFT, spektrum, frequenzanalyse, oberschwingungen, oszilloskop, fensterung, hanning, flattop, leakage, DFT]
symbol: —
einheit: Hz, dB
---

Die FFT wandelt ein Zeitsignal in sein Frequenzspektrum um. Sie zeigt welche Frequenzanteile in einem Signal stecken und wie stark sie sind.

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen]]
- [[AD/DA Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Oberschwingungen und THD]]
:::
:::vbox
**Führt weiter zu**
- [[EMV Pre-Compliance]]
:::
:::

---

## Grundidee

Jedes periodische Signal lässt sich als Summe von Sinuswellen verschiedener Frequenzen darstellen (Fourier-Theorem). Die FFT berechnet diese Zerlegung numerisch und schnell.

Ergebnis: Ein Spektrum das zeigt welche Frequenzen vorhanden sind und wie stark.

## Was man abliest

**X-Achse**: Frequenz in Hz.
**Y-Achse**: Amplitude in dB oder Volt.

Ein reines Sinus bei 1 kHz zeigt eine einzelne Linie bei 1 kHz. Ein Rechteck bei 1 kHz zeigt Linien bei 1 kHz, 3 kHz, 5 kHz, 7 kHz... (Oberschwingungen).

## Auflösung

:::formel
f_aufloesung = f_abtast / N     # Frequenzauflösung; N = Anzahl Punkte der FFT
:::
Mehr Punkte: bessere Frequenzauflösung, längere Berechnung.

## Fensterung (Windowing)

**Das Problem (Spectral Leakage)**: Die FFT nimmt einen Signalausschnitt endlicher Länge. Wenn dieser Ausschnitt keine ganzzahlige Anzahl von Perioden enthält, entsteht am Rand des Ausschnitts ein "Sprung". Dieser Sprung fügt künstliche Frequenzanteile ins Spektrum ein (Leakage).

**Lösung: Fensterfunktionen** gewichten die Signalprobe an den Rändern auf null, in der Mitte auf eins. Das unterdrückt Leakage.

### Hanning (Hann)-Fenster
- Glatte Gewichtung zur Mitte hin
- **Gute Frequenzauflösung**: Spektrallinien sind schmal → Frequenz lässt sich genau ablesen
- **Schlechtere Amplitudengenauigkeit**: Durch das Abschneiden der Ränder wird etwas Amplitude "verschluckt"
- Einsatz: Wenn man Frequenzen präzise messen will (z.B. Oberschwingungen identifizieren)

### Flattop-Fenster
- Breitere, flache Gewichtungskurve
- **Gute Amplitudengenauigkeit**: Amplituden werden präzise dargestellt (Fehler < 0.1 dB)
- **Schlechtere Frequenzauflösung**: Spektrallinien sind breiter → Frequenz ungenauer
- Einsatz: Wenn man Amplituden präzise messen will (z.B. Kalibrierung, THD-Messung)

| Fenster | Frequenzauflösung | Amplitudengenauigkeit | Typischer Einsatz |
|---|---|---|---|
| Rechteck (kein Fenster) | Sehr gut | Schlecht (Leakage) | Nur bei exakter Synchronisation |
| Hanning | Gut | Mittel | Allgemein, Frequenzmessung |
| Blackman | Sehr gut | Mittel | Oberschwingungen suchen |
| Flattop | Schlecht | Sehr gut | Amplitudenmessung, Kalibrierung |

Im Oszilloskop voreingestellt, oft Hann als Standard.

## Anwendungen

Oberschwingungen im Netz messen (THD). Rauschquellen identifizieren. EMV-Vorprüfung: Emissionen suchen bevor das Gerät ins Labor kommt. Schwingungen in mechanischen Systemen analysieren.

:::tip
Viele moderne Oszilloskope haben eingebaute FFT. Einfach aktivieren, Kanal wählen, Zeitbasis so einstellen dass mehrere Perioden des interessanten Signals sichtbar sind.
:::
