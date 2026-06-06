---
title: Bandpass
kategorie: EK
kapitel: Filter
tags: [bandpass, BP, untergrenzfrequenz, obergrenzfrequenz, mittenfrequenz, güte, wienglied, T-BP, pi-BP, 20dB, 40dB, 60dB, hochpass, tiefpass]
groessen: f_u|Untergrenzfrequenz|Hz; f_o|Obergrenzfrequenz|Hz; f_m|Mittenfrequenz|Hz; Q|Güte|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Tiefpass]]
- [[Hochpass]]
:::
:::vbox
**Verwandte Artikel**
- [[Bandsperre]]
- [[Aktive Filter]]
- [[Filtercharakteristik]]
:::
:::vbox
**Führt weiter zu**
- [[Wien-Robinson-Oszillator]]
- [[Aktive Filter]]
:::
:::

---

Ein Bandpass lässt nur ein bestimmtes Frequenzband durch und dämpft oberhalb und unterhalb. Er entsteht durch Kombination von Hoch- und Tiefpass.

## Aufbau: Hochpass + Tiefpass in Serie (RC)

:::schematic RC-Bandpass (HP + TP in Serie): Eingang U_e links. Hochpassstufe: C_HP in Reihe, R_HP nach GND → Ausgang f_u. Impedanzwandler (OPV) zwischen den Stufen. Tiefpassstufe: R_TP in Reihe, C_TP nach GND → Ausgang U_aus. f_u (HP) < f_m < f_o (TP). Signal passiert nur im Band f_u … f_o
/Diagramm/bandpass_rc.svg
:::

Die einfachste Methode: Hochpass und Tiefpass hintereinander schalten. Der HP bestimmt die untere Grenzfrequenz f_u, der TP die obere f_o.

:::formel
f_u = 1 / (2 * pi * R1 * C1)    # Untergrenzfrequenz (Hochpassanteil)
f_o = 1 / (2 * pi * R2 * C2)    # Obergrenzfrequenz (Tiefpassanteil)
f_m = sqrt(f_u * f_o)           # Mittenfrequenz (geometrisches Mittel)
:::

**Voraussetzung:** f_u < f_o. Die Stufen müssen entkoppelt sein (Impedanzwandler/OPV), sonst beeinflussen sie sich gegenseitig.

Steilheit RC-Bandpass: **20 dB/Dekade** auf jeder Flanke.

## Wienglied (RC-Bandpass 1. Ordnung)

:::schematic Wienglied: Eingang U_e. Oberer Zweig (Hochpass): R1 in Reihe mit C1. Unterer Zweig (Tiefpass): C2 parallel zu R2. Beide Zweige in Serie zwischen Eingang und Ausgang U_aus. Bei f_m: minimale Dämpfung (1/3). Wird im Wien-Robinson-Oszillator als Frequenzglied eingesetzt
/Diagramm/wienglied.svg
:::

Das Wienglied kombiniert Hochpass (R1, C1) und Tiefpass (R2, C2) in einer kompakten Topologie — es wird im Wien-Robinson-Oszillator als frequenzbestimmendes Glied eingesetzt.

:::formel
f_m = 1 / (2 * pi * R * C)    # für R1 = R2 = R und C1 = C2 = C
:::

Steilheit: **20/20 dB/Dekade** auf beiden Flanken. Bei f_m beträgt die Dämpfung 1/3 (−9.5 dB).

## T-Bandpass und π-Bandpass (LC, höhere Ordnung)

LC-Glieder in T- oder π-Topologie erreichen höhere Steilheiten:

| Typ | Steilheit je Flanke | Schaltungsaufwand |
|---|---|---|
| RC-BP (HP + TP, je 1. Ord.) | 20/20 dB/Dek | 2 R + 2 C |
| LC-Bandpass (T/π) | 40/40 dB/Dek | L + C-Glieder |
| LC-Bandpass (höhere Ord.) | 60/60 dB/Dek | mehrere LC-Glieder |

:::plot
var: f
range: 0.01, 100
xlabel: f / f_m (normiert)
ylabel: Amplitude (normiert)
Bandpass HP: f / sqrt(1 + f*f)
Bandpass TP: 1 / sqrt(1 + f*f)
:::

## Güte Q

Die Güte Q beschreibt wie schmal oder breit das Durchlassband ist:

:::formel
Q = f_m / (f_o - f_u)    # Güte = Mittenfrequenz / Bandbreite
:::

| Q-Wert | Charakter | Anwendung |
|---|---|---|
| Q < 1 | Breitbandig | Audioequalisierung |
| Q = 1 | Mittel | Allgemein |
| Q > 10 | Schmalbandig | Kanalfilter, Resonanz |

## Anwendungen

- **Empfänger:** Rundfunk, Mobilfunk — bestimmten Kanal herausfiltern
- **Tonerkennung:** DTMF (Telefon) — einzelne Töne aus Gemisch erkennen
- **Wienglied im Oszillator:** Frequenzbestimmendes Netzwerk (→ [[Wien-Robinson-Oszillator]])
- **Audioequalisierung:** Bestimmtes Frequenzband anheben oder absenken
