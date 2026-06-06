---
title: Bandsperre
kategorie: EK
kapitel: Filter
tags: [bandsperre, notch, doppel-T-filter, allpass, 50Hz, brumm, parallel, hochpass, tiefpass, sperrfrequenz, 20dB, 40dB, bauteiltoleranz]
groessen: f_s|Sperrfrequenz|Hz; f_u|Untergrenzfrequenz|Hz; f_o|Obergrenzfrequenz|Hz
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Tiefpass]]
- [[Hochpass]]
- [[Bandpass]]
:::
:::vbox
**Verwandte Artikel**
- [[Bandpass]]
- [[Aktive Filter]]
:::
:::vbox
**Führt weiter zu**
- [[Filtercharakteristik]]
- [[Aktive Filter]]
:::
:::

---

Eine Bandsperre (Notch-Filter) dämpft ein schmales Frequenzband und lässt ausserhalb ungehindert durch. Klassische Anwendung: 50-Hz-Netzbrumm aus Messsignalen entfernen.

## Aufbau: Hochpass + Tiefpass parallel (RC)

:::schematic RC-Bandsperre (HP + TP parallel): Eingang U_e zu beiden Zweigen. Oberer Zweig (TP): R in Reihe, C nach GND → Ausgang. Unterer Zweig (HP): C in Reihe, R nach GND → Ausgang. Beide Ausgänge zusammengeführt (addiert). Im Sperrband löschen sich HP und TP-Anteile gegenseitig aus. Ausgang U_aus
/Diagramm/bandsperre_rc.svg
:::

Im Gegensatz zum Bandpass (Hintereinanderschaltung) werden HP und TP **parallel** betrieben. Der TP lässt tiefe Frequenzen durch, der HP hohe — im gesperrten Band löschen sich die Anteile aus.

:::formel
f_u = 1 / (2 * pi * R1 * C1)    # Untere Grenzfrequenz (TP-Anteil)
f_o = 1 / (2 * pi * R2 * C2)    # Obere Grenzfrequenz (HP-Anteil)
f_s = sqrt(f_u * f_o)           # Sperrfrequenz (geometrisches Mittel)
:::

Steilheit RC-Bandsperre: **20/20 dB/Dekade** auf beiden Seiten.

## Doppel-T-Filter

:::schematic Doppel-T-Filter: Eingang U_e links, Ausgang U_aus rechts. Oberer T-Zweig (TP): U_e → R → Knoten A → R → U_aus, mit C von Knoten A nach GND. Unterer T-Zweig (HP): U_e → C → Knoten B → C → U_aus, mit 2R von Knoten B nach GND. Bei f_s = 1/(2πRC): vollständige Auslöschung (theoretisch −∞ dB). Aktive Variante: OPV-Rückkopplung erhöht Kerbtiefe
/Diagramm/doppel_t_filter.svg
:::

Das Doppel-T-Filter ist eine passive RC-Schaltung mit sehr scharfer Kerbwirkung. Es besteht aus zwei T-Gliedern — einem Tiefpass-T und einem Hochpass-T — deren Ausgänge zusammengeführt werden.

**Dimensionierung** (symmetrisch: alle R gleich, alle C gleich):

:::formel
f_s = 1 / (2 * pi * R * C)    # Sperrfrequenz Doppel-T
:::

Spick-Beispiel: 100 Ω / 200 Ω, 100 nF / 200 nF → f_s ≈ 10 kHz. Bei f_s beträgt die Dämpfung theoretisch −∞ dB (vollständige Auslöschung bei idealen Bauteilen).

:::warning
Das Doppel-T-Filter ist sehr empfindlich auf Bauteiltoleranzen. Bereits 1 % Abweichung reduziert die Kerbtiefe erheblich. Immer 1%-Widerstände und Folienkondensatoren verwenden.
:::

## Allpass

:::schematic Aktiver Allpass (1. Ordnung): OPV-Dreieck. Eingang U_e → nichtinvertierender Eingang (+) direkt. Gleichzeitig U_e → R → invertierender Eingang (−) mit C nach GND (RC-Tiefpass zum (−)-Eingang). Rückkopplung R von Ausgang auf (−). Amplitudengang flach, Phasengang dreht von 0° bis −180° mit f_g = 1/(2πRC)
/Diagramm/allpass.svg
:::

Der **Allpass** dämpft keine Frequenz — er lässt alle durch mit gleicher Amplitude. Er verschiebt jedoch die **Phase** frequenzabhängig (bis −180°). Anwendung: Phasenkorrektur, Laufzeitanpassung zwischen Signalpfaden.

| Eigenschaft | Allpass |
|---|---|
| Amplitudengang | flach (0 dB über alle f) |
| Phasengang | dreht Phase 0° bis −180° |
| Steilheit | 0 dB/Dek |

## Steilheiten-Übersicht

| Typ | Steilheit RC | Steilheit LC (T/π) |
|---|---|---|
| Bandsperre (HP+TP parallel) | 20/20 dB/Dek | 40/40 dB/Dek |
| T-BP + π-BP als Bandsperre | — | 60/60 dB/Dek |
| Doppel-T (Kerbe) | sehr steil (schmal) | — |

## Anwendungen

- **50-Hz-Unterdrückung:** EKG-Messung, Audiotechnik — Netzbrumm entfernen
- **Audionotch:** Störfrequenz aus Aufnahme entfernen (z.B. Feedback beim Gitarrenverstärker)
- **Messgeräte:** Störfrequenz des Netzes vor der Digitalisierung dämpfen
- **Aktive Variante:** Doppel-T mit OPV-Rückkopplung für höhere Kerbtiefe und einstellbare f_s
