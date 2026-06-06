---
title: Filter Grundlagen
kategorie: EK
kapitel: Filter
tags: [filter, grenzfrequenz, amplitudengang, phasengang, bode-diagramm, -3db, dämpfung, filterordnung, passiv, aktiv, tiefpass, hochpass, bandpass, bandsperre, allpass]
groessen: f_g|Grenzfrequenz|Hz; A_u|Dämpfung|dB; φ|Phasenverschiebung|°
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz & Blindwiderstand]]
- [[Verstärkung & Dämpfung]]
:::
:::vbox
**Verwandte Artikel**
- [[Tiefpass]]
- [[Hochpass]]
- [[Bandpass]]
- [[Bandsperre]]
:::
:::vbox
**Führt weiter zu**
- [[Transit & Grenzfrequenz]]
- [[Filtercharakteristik]]
- [[Aktive Filter]]
:::
:::

---

Filter lassen bestimmte Frequenzen durch und dämpfen andere. Sie trennen Nutzsignal von Störungen, entkoppeln Stufen und formen Frequenzgänge — ein Grundwerkzeug in fast jeder analogen Schaltung.

## Filtertypen

:::schematic Filter-Frequenzgänge Überblick: Vier Diagramme (Amplitude über Frequenz). Tiefpass: flach bis f_g, dann abfallend. Hochpass: ansteigend bis f_g, dann flach. Bandpass: Glocke um f_m. Bandsperre/Notch: Kerbe bei f_s, sonst flach. f_g jeweils eingezeichnet
/Diagramm/filter_typen_ueberblick.svg
:::

| Typ | Symbol | Lässt durch | Dämpft | Typische Anwendung |
|---|---|---|---|---|
| **Tiefpass** (TP) | Rechteck fallend | f < f_g | f > f_g | Langsame Sensorsignale (Temperatur, Helligkeit); Anti-Aliasing vor ADC |
| **Hochpass** (HP) | Rechteck steigend | f > f_g | f < f_g | Rundsteuersignale auf 230-V-Netz (50 Hz herausfiltern); DC-Sperre |
| **Bandpass** (BP) | Glocke | f_u … f_o | ausserhalb | Radio-Empfänger (einen Sender, z. B. 105.6 MHz, herausfiltern) |
| **Bandsperre** (BS/Notch) | Kerbe | ausserhalb | f_u … f_o | Tontechnik / Badewannen-Filter (einzelne störende Frequenz entfernen) |
| **Allpass** | flach | alle f gleichmässig | keine | Phasenkorrektur, Laufzeit |

## Grenzfrequenz (−3 dB)

Die **Grenzfrequenz f_g** ist die Frequenz, bei der die Ausgangsamplitude auf **70.7 %** des Eingangs abgefallen ist:

:::formel
A_u [dB] = 20 * log10(U_aus / U_ein)    # Dämpfung in dB
# Bei f_g: A_u = -3 dB, U_aus = 0.707 * U_ein, Phase = ±45°
:::

## Passiv vs. Aktiv

| Eigenschaft | Passiv (R, L, C) | Aktiv (R, C, OPV) |
|---|---|---|
| Versorgungsspannung | keine | nötig |
| Verstärkung | immer ≤ 1 | kann > 1 sein |
| Lasteinfluss | vorhanden | gering (OPV-Ausgang niederohmig) |
| Aufwand | gering | höher |
| Typischer Einsatz | Netzteilsiebung, HF | Audio, Messtechnik, Regelung |

## Filterordnung und Steilheit

Jede Ordnung addiert **20 dB/Dekade** (= 6 dB/Oktave) zur Flankensteilheit im Sperrbereich:

| Ordnung | Steilheit | Typische Schaltung |
|---|---|---|
| 1 | 20 dB/Dek | 1 RC- oder RL-Glied |
| 2 | 40 dB/Dek | 2 RC-Stufen oder Sallen-Key |
| 3 (T- oder π-Glied) | 60 dB/Dek | T-TP / π-TP (LC) |
| n | n × 20 dB/Dek | n Elemente |

## Bode-Diagramm

Das **Bode-Diagramm** zeigt Amplituden- und Phasengang logarithmisch über der Frequenz. Asymptoten für Tiefpass 1. Ordnung:

:::plot
var: f
range: 0.01, 100
xlabel: f / f_g (normiert)
ylabel: Amplitude (normiert)
Tiefpass: 1 / sqrt(1 + f*f)
Hochpass: f / sqrt(1 + f*f)
:::

- Unterhalb f_g: Amplitude ≈ 1 (Durchlassbereich)
- Knickpunkt bei f_g: Amplitude = 0.707, Phase = ±45°
- Oberhalb f_g: −20 dB/Dekade (Tiefpass) bzw. +20 dB/Dekade (Hochpass bis Plateau)

:::tip
Daumenregel: Jede Dekade über f_g bringt −20 dB (1. Ordnung). Bei 10·f_g: −20 dB, bei 100·f_g: −40 dB. Pro Oktave (Frequenzverdoppelung): −6 dB.
:::

## dB-Umrechnung in Spannung

Aus dem Bodediagramm lässt sich die Ausgangsspannung bei einer gegebenen Dämpfung berechnen:

:::formel
A_u_dB = 20 * log10(U_aus / U_ein)      # Verstärkung in dB (negativ = Dämpfung)
U_aus  = U_ein * 10^(A_u_dB / 20)       # Ausgangsspannung aus dB
:::

:::monospace
Beispiel: Tiefpass 2. Ordnung (40 dB/Dek), f_g = 1 Hz, U_ein = 5 V
  Bei f = 10 Hz  (10× f_g):  −40 dB → U_aus = 5 × 10^(−40/20) = 5/100   = 50 mV
  Bei f = 100 Hz (100× f_g): −80 dB → U_aus = 5 × 10^(−80/20) = 5/10000 = 500 µV
:::
