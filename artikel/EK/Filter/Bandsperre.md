---
title: Bandsperre (BS)
kategorie: EK
tags: [bandsperre, BS, notch, kerbfilter, sperrfrequenz, güte, Q-faktor, wien-robinson, doppel-T-glied, brumm, 50Hz, tontechnik]
symbol: —
einheit: —
---

Eine Bandsperre (BS), auch Notch- oder Kerbfilter genannt, dämpft ein schmales Frequenzband und lässt alle anderen Frequenzen ungehindert durch. Das Gegenteil des Bandpasses.

:::hbox
:::vbox
**Voraussetzungen**
- [[Tiefpass (TP)]]
- [[Hochpass (HP)]]
- [[Bandpass (BP)]]
:::
:::vbox
**Verwandte Artikel**
- [[Aktive Filter]]
- [[Wien-Brücken-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Filtercharakteristik]]
:::
:::

---

## Anwendungen

- **Tontechnik (Badewannenfilter)**: Zu starke Signale einer bestimmten Frequenz unterdrücken
- **50-Hz-Brumm-Unterdrückung**: Netzbrumm aus Audiosignalen entfernen
- **Medizintechnik**: 50/60-Hz-Netzstörungen aus EKG- oder EEG-Messungen entfernen
- **Audioequalizer**: Einzelne Frequenz präzise absenken

## Frequenzgang

:::plot
var: f
range: 0.01, 100
xlabel: Frequenz (normiert, f_0 = 1)
ylabel: Amplitude (normiert)
Bandsperre (Q=1):  sqrt((1-f*f)^2) / sqrt((1-f*f)^2 + f*f)
Bandsperre (Q=5):  sqrt((1-f*f)^2) / sqrt((1-f*f)^2 + (f/5)^2 * 25)
:::

Bei der Sperrfrequenz f_0 ist die Dämpfung maximal (theoretisch unendlich). Links und rechts davon volle Amplitude.

## Schaltungen

### Passiv: Doppel-T-Glied

Passive Schaltung aus R und C in T-Anordnung (zwei T-Glieder). Einfach, aber geringe Güte (Q ≈ 0.25). Für einfache 50-Hz-Sperrung ausreichend.

Sperrfrequenz:
```
f_0 = 1 / (2 · π · R · C)
```

### Aktiv: Wien-Robinson-Brücke

OPV mit Wien-Robinson-Gegenkopplung. Höhere Güte als das passive Doppel-T-Glied, abstimmbar. Wird auch in Oszillatoren verwendet (der Frequenzpunkt wo die Phasendrehung 0° ist).

## Güte und Sperrtiefe

| Güte Q | Bandbreite | Typische Schaltung |
|---|---|---|
| ~0.25 | sehr breit | Passives Doppel-T-Glied |
| 1–5 | mittel | Aktive Schaltung mit OPV |
| > 10 | schmal | LC-Schwingkreis |

:::info
Eine ideale Bandsperre hat bei f_0 eine Dämpfung von −∞ dB. In der Praxis sind −40 bis −60 dB gut erreichbar, was einer Spannungsunterdrückung von 1:100 bis 1:1000 entspricht.
:::
