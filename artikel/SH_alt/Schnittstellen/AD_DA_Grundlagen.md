---
title: AD/DA Grundlagen
kategorie: SH
tags: [ADC, DAC, abtastung, auflösung, nyquist, quantisierung, aliasing, sample-and-hold, anti-aliasing, LSB, INL, DNL, SNR]
symbol: —
einheit: Bit, Hz
---

ADC (Analog-Digital-Converter) wandelt analoge Spannungen in Zahlen. DAC macht das Umgekehrte. Ohne diese Bausteine können Mikrocontroller die analoge Welt nicht messen oder beeinflussen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale]]
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Sukzessive Approximation]]
- [[FFT (Fast Fourier Transform)]]
:::
:::vbox
**Führt weiter zu**
- [[Sukzessive Approximation]]
- [[R-2R Netzwerk]]
:::
:::

---

## Abtastung und Nyquist

Analoge Signale werden zu diskreten Zeitpunkten gemessen. Die Abtastfrequenz muss mindestens doppelt so hoch sein wie die höchste Signalfrequenz (Nyquist-Theorem):

:::formel
f_abtast >= 2 × f_signal
:::
Zu langsame Abtastung erzeugt Aliasing: das Signal erscheint mit falscher Frequenz. Vor dem ADC wird ein Anti-Aliasing-Filter eingesetzt.

## Auflösung

Die Auflösung in Bit bestimmt wie fein das Signal quantisiert wird:

:::formel
Anzahl Stufen = 2^n     # n = Anzahl Bits
:::
8-Bit: 256 Stufen. 12-Bit: 4096 Stufen. 16-Bit: 65536 Stufen.

Der Quantisierungsfehler beträgt maximal ±0.5 LSB (Least Significant Bit).

## Referenzspannung und LSB-Berechnung

Der ADC misst relativ zur Referenzspannung. Die Spannung pro Bit (1 LSB) berechnet sich:

:::formel
U_LSB = U_ref / 2^n     # 1 LSB Schrittweite
:::
**Beispiel 1**: 12-Bit-ADC, 3.3 V Referenz:
:::formel
U_LSB = 3.3 V / 4096 = 0.81 mV
:::
**Beispiel 2**: 10-Bit-ADC, 5 V Referenz:
:::formel
U_LSB = 5 V / 1024 ≈ 4.9 mV ≈ 5 mV pro Schritt
:::
Dieses Rechenbeispiel kommt häufig in Prüfungen vor: Ein 10-Bit-ADC mit 5 V Referenz hat einen LSB-Schritt von knapp 5 mV.

## DAC-Grundlagen

Ein DAC wandelt einen digitalen Wert in eine analoge Spannung. Verfahren:
- **R-2R-Netzwerk**: Einfach, kein externer Speicher
- **Sigma-Delta**: Hohe Auflösung durch Überabtastung
- **PWM**: Kein echter DAC, aber für viele Anwendungen ausreichend

## Wichtige Parameter

| Parameter | Bedeutung |
|---|---|
| Auflösung | Bits |
| Samplingrate | Samples/Sekunde |
| INL (Integral Non-Linearity) | Gesamtfehler |
| DNL (Differential Non-Linearity) | Sprungfehler zwischen Stufen |
| SNR | Signal-Rausch-Abstand |
