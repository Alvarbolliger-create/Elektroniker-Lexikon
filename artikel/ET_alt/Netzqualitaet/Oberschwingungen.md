---
title: Oberschwingungen und THD
kategorie: ET
tags: [oberschwingungen, THD, netzqualität, harmonische, klirrfaktor, FFT, fourier, PFC, EMV, schaltnetzteil]
symbol: —
einheit: %, Hz
---

Oberschwingungen sind Vielfache der Netzfrequenz. Sie entstehen durch nichtlineare Verbraucher und verschlechtern die Netzqualität.

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen]]
- [[FFT]]
:::
:::vbox
**Verwandte Artikel**
- [[FFT]]
- [[Leistungsfaktor]]
:::
:::vbox
**Führt weiter zu**
- [[EMV Pre-Compliance]]
:::
:::

---

## Was sind Oberschwingungen?

Ein idealer Verbraucher zieht einen sinusförmigen Strom. Nichtlineare Verbraucher (Schaltnetzteile, Dimmer, Frequenzumrichter) ziehen einen verzerrten Strom.

Nach Fourier lässt sich jede periodische Kurvenform als Summe von Sinuswellen darstellen:
- Grundschwingung: 50 Hz
- 2. Harmonische: 100 Hz
- 3. Harmonische: 150 Hz
- 5. Harmonische: 250 Hz

Die 3., 5., 7. Harmonische sind meist die stärksten.

## THD (Total Harmonic Distortion)

Der THD-Wert fasst alle Oberschwingungen in einer Kennzahl zusammen:

:::formel
THD = sqrt(U2^2 + U3^2 + U4^2 + ...) / U1 * 100 %
:::
Ein reiner Sinus hat THD = 0 %. Ein Schaltnetzteils ohne Korrektur kann THD > 100 % erreichen.

## Wirkung auf das Netz

Oberschwingungen erhitzen Transformatoren und Kabel über ihr Nennmass. Sie stören empfindliche Geräte. Im Neutralleiter eines Dreiphasensystems addieren sich die 3. Harmonischen aller drei Phasen, statt sich aufzuheben. Der Neutralleiter muss dann stärker ausgelegt werden.

## Gegenmassnahmen

- **Eingangsfilter**: Passiver LC-Filter am Netzteil
- **PFC (Power Factor Correction)**: Aktive Schaltung die den Strom sinusförmig nachführt. Weit verbreitet in Schaltnetzteilen über 75 W (Pflicht nach IEC 61000-3-2)
- **Netzfilter**: Passiv, dämpft hochfrequente Anteile

## Messung

Mit einem Power Analyzer oder FFT-fähigem Multimeter. Netzqualitätsanalysatoren zeichnen über Stunden auf und zeigen Spitzen.

:::tip
Viele Multimeter mit True-RMS-Funktion messen korrekte Effektivwerte auch bei verzerrten Signalen, zeigen aber kein THD. Für THD-Messung braucht man einen Netzanalysator oder ein Oszilloskop mit FFT.
:::
