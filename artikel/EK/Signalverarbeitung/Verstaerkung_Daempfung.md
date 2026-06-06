---
title: Verstärkung & Dämpfung
kategorie: EK
kapitel: Signalverarbeitung
tags: [verstärkung, dämpfung, dezibel, dB, verstärkungsfaktor, dämpfungsfaktor, verstärkungsmass, dämpfungsmass, spannung, strom, leistung, logarithmus, kaskade, lg, log10]
groessen: V|Verstärkungsfaktor|—; D|Dämpfungsfaktor|—; G|Verstärkungsmass|dB; A|Dämpfungsmass|dB; U_E|Eingangsspannung|V; U_A|Ausgangsspannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BJT Grundlagen]]
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Klirrfaktor]]
- [[Filter Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[Klirrfaktor]]
- [[Modulation]]
:::
:::

---

Verstärkung und Dämpfung beschreiben, wie sich ein Signal beim Durchgang durch eine Schaltung in der Amplitude verändert. Das Dezibel (dB) erlaubt den Umgang mit sehr grossen Zahlenbereichen durch Logarithmierung.

## Grundprinzip

:::schematic Verstärkung und Dämpfung Grundprinzip: Signalfluss von links nach rechts. U_E (Eingangsspannung) → Schaltungsblock (Verstärker oder Dämpfungsglied) → U_A (Ausgangsspannung). Verstärker: U_A > U_E, V > 1, G > 0 dB. Dämpfungsglied: U_A < U_E, D > 1, A > 0 dB. G in dB = 20×lg(U_A/U_E), A in dB = 20×lg(U_E/U_A)
/Diagramm/verstaerkung_daempfung.svg
:::

- **V > 1:** Ausgangssignal grösser als Eingangssignal (Verstärkung)
- **D > 1:** Ausgangssignal kleiner als Eingangssignal (Dämpfung)
- V und D sind **reziprok**: V = 1/D
- Verstärkungsmass G und Dämpfungsmass A sind **entgegengesetzt**: G = −A

:::info
**lg** = log₁₀ (dekadischer Logarithmus, Basis 10). Für Spannung und Strom gilt Faktor **20**, für Leistung Faktor **10** — weil P ∝ U² (Quadrat verdoppelt den Logarithmus).
:::

## Spannung (aus dem Spick)

:::formel
V   = U_A / U_E = 1 / D               # Verstärkungsfaktor
G   = 20 * lg(U_A / U_E) = -A         # Verstärkungsmass [dB]
U_E = U_A / V = U_A / 10^(G/20)       # Eingangsspannung aus U_A und G
U_A = U_E * V = U_E * 10^(G/20)       # Ausgangsspannung aus U_E und G

D   = U_E / U_A = 1 / V               # Dämpfungsfaktor
A   = 20 * lg(U_E / U_A) = -G         # Dämpfungsmass [dB]
U_E = U_A * D = U_A * 10^(A/20)       # Eingangsspannung aus U_A und A
U_A = U_E / D = U_E / 10^(A/20)       # Ausgangsspannung aus U_E und A
:::

## Strom (aus dem Spick)

:::formel
V   = I_A / I_E = 1 / D               # Verstärkungsfaktor
G   = 20 * lg(I_A / I_E) = -A         # Verstärkungsmass [dB]
I_E = I_A / V = I_A / 10^(G/20)       # Eingangsstrom
I_A = I_E * V = I_E * 10^(G/20)       # Ausgangsstrom

D   = I_E / I_A = 1 / V               # Dämpfungsfaktor
A   = 20 * lg(I_E / I_A) = -G         # Dämpfungsmass [dB]
I_E = I_A * D = I_A * 10^(A/20)       # Eingangsstrom aus I_A und A
I_A = I_E / D = I_E / 10^(A/20)       # Ausgangsstrom aus I_E und A
:::

## Leistung (aus dem Spick)

:::formel
V   = P_A / P_E = 1 / D               # Verstärkungsfaktor
G   = 10 * lg(P_A / P_E) = -A         # Verstärkungsmass [dB]  (Faktor 10, nicht 20!)
P_E = P_A / V = P_A / 10^(G/10)       # Eingangsleistung
P_A = P_E * V = P_E * 10^(G/10)       # Ausgangsleistung

D   = P_E / P_A = 1 / V               # Dämpfungsfaktor
A   = 10 * lg(P_E / P_A) = -G         # Dämpfungsmass [dB]
P_E = P_A * D = P_A * 10^(A/10)       # Eingangsleistung aus P_A und A
P_A = P_E / D = P_E / 10^(A/10)       # Ausgangsleistung aus P_E und A
:::

:::warning
**20 vs. 10:** Spannung und Strom → **20 · lg**. Leistung → **10 · lg**. Häufige Fehlerquelle!
:::

## Referenztabelle

| G / A | Spannungsfaktor V | Leistungsfaktor V |
|---|---|---|
| 0 dB | 1 | 1 |
| +3 dB | 1.41 (√2) | 2 |
| +6 dB | 2 | 4 |
| +10 dB | 3.16 | 10 |
| +20 dB | 10 | 100 |
| +40 dB | 100 | 10'000 |
| −3 dB | 0.707 | 0.5 |
| −6 dB | 0.5 | 0.25 |
| −20 dB | 0.1 | 0.01 |

## Kettenschaltung (Kaskade)

Bei mehreren Stufen hintereinander werden Faktoren **multipliziert**, dB-Werte **addiert**:

:::formel
V_ges = V1 * V2 * V3             # Faktoren multiplizieren
G_ges = G1 + G2 + G3             # dB-Werte addieren
:::

:::monospace
Beispiel: 3 Stufen mit +6 dB, +12 dB, −3 dB
G_ges = 6 + 12 − 3 = 15 dB
V_ges = 10^(15/20) = 5.62   (Spannungsfaktor)
:::
