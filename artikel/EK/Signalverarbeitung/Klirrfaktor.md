---
title: Klirrfaktor
kategorie: EK
kapitel: Signalverarbeitung
tags: [klirrfaktor, THD, oberwellen, harmonische, nichtlinearität, verzerrung, audioqualität, effektivwert, D_k, U1, U2, klirr, sinus, spektrum]
groessen: k|Klirrfaktor|—; D_k|Klirrfaktor|dB; U_1|Grundschwingung Effektivwert|V; U_2|2. Oberwelle Effektivwert|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Verstärkung & Dämpfung]]
- [[Wien-Robinson-Oszillator]]
:::
:::vbox
**Verwandte Artikel**
- [[Verstärkung & Dämpfung]]
:::
:::vbox
**Führt weiter zu**
- [[Modulation]]
:::
:::

---

Der Klirrfaktor ist ein Qualitätskriterium für Signalquellen und Übertragungsglieder (z.B. Verstärker). Er quantifiziert das Vorhandensein von **Oberwellen** — Frequenzanteilen, die ein ganzzahliges Vielfaches der Eingangsfrequenz darstellen.

## Entstehung von Oberwellen

Übertragungsglieder bestehen aus Bauelementen mit **nichtlinearen Kennlinien**. Nicht nur Halbleiter sind nichtlinear — auch Induktivitäten (Kernsättigung), Kondensatoren und in geringem Mass Widerstände. Ein Sinus am Eingang erzeugt an nichtlinearen Gliedern Oberwellen bei 2f, 3f, 4f, ... am Ausgang.

:::info
Je nach Anwendung sind Klirrfaktoren von 0.01 % bis 1 % üblich. Im Audiobereich ist die Angabe des Klirrfaktors Standard. Der Klirrfaktor steigt mit der Ausgangsleistung — nahe an der Aussteuerungsgrenze klippt das Signal.
:::

## Berechnung (aus dem Spick)

Für alle Spannungen wird der **Effektivwert** eingesetzt:

:::formel
k   = sqrt(U_2^2 + U_3^2 + U_4^2 + ...) / sqrt(U_1^2 + U_2^2 + U_3^2 + U_4^2 + ...)
D_k = 20 * lg(k)    # Klirrfaktor in dB
:::

- **U_1:** Effektivwert der Grundschwingung (Eingangsfrequenz f)
- **U_2, U_3, U_4, ...:** Effektivwert der 2., 3., 4., ... Oberwelle (2f, 3f, 4f, ...)

:::monospace
Beispiel: U_1 = 1 V, U_2 = 0.02 V, U_3 = 0.01 V, U_4 ≈ 0
Zähler: sqrt(0.02² + 0.01²) = sqrt(0.0005) = 0.0224 V
Nenner: sqrt(1² + 0.02² + 0.01²) = sqrt(1.0005) ≈ 1.00025 V
k = 0.0224 / 1.00025 ≈ 0.0224 = 2.24 %
D_k = 20 × lg(0.0224) = −33 dB
:::

## Typische Klirrfaktoren

| Schaltung / Gerät | Typischer Klirrfaktor |
|---|---|
| Hifi-Audioverstärker | < 0.01 % |
| Guter Audioverstärker (Class AB) | < 0.1 % |
| Wien-Robinson mit NTC | < 0.1 % |
| Wien-Robinson mit Diodenbegrenzung | 1 – 5 % |
| Transformator im Betrieb | 1 – 5 % |
| Motorenwicklung | 3 – 10 % |

## Fourier-Theorem und Frequenzspektrum

Jede periodische Funktion lässt sich als Summe von Sinus- und Kosinusschwingungen darstellen (**Fourier-Theorem**). Das Frequenzspektrum zeigt, welche Frequenzanteile mit welcher Amplitude vorhanden sind.

| Signalform | Spektrum | Oberwellen |
|---|---|---|
| **Sinus** | Einzellinie bei f | keine — k = 0 % |
| **Rechteck** | f + ungerade Vielfache | 3f, 5f, 7f, ... Amplituden: 1, 1/3, 1/5, ... |
| **Dreieck** | f + ungerade Vielfache | 3f, 5f, ... Amplituden: 1, 1/9, 1/25, ... (= 1/n²) |
| **Weisses Rauschen** | alle Frequenzen gleichmässig | konstante Spektraldichte |

Das Rechteck aus der Fourier-Reihe:
```
u(t) = (4/π) × ( sin(ωt) + sin(3ωt)/3 + sin(5ωt)/5 + sin(7ωt)/7 + ... )
```
Mit mehr Oberwellen wird das Rechteck schärfer approximiert. Ein reales Rechteck (z.B. vom Funktionsgenerator) hat deshalb immer einen Klirrfaktor > 0.

## Messung

Der Klirrfaktor wird per **FFT** (Fast Fourier Transform) oder mit einem THD-Messgerät bestimmt:

1. Sinus bekannter Frequenz f anlegen (möglichst klirrarm, z.B. Wien-Robinson)
2. Ausgangsspektrum per FFT aufnehmen
3. Effektivwerte U_1, U_2, U_3, ... bei f, 2f, 3f ablesen
4. In Klirrfaktorformel einsetzen

:::tip
Zur Klirrfaktormessung braucht man eine Signalquelle mit deutlich kleinerem Klirrfaktor als das Prüfling. Wien-Robinson mit NTC-Amplitudenbegrenzung ist dafür gut geeignet (k < 0.1 %).
:::
