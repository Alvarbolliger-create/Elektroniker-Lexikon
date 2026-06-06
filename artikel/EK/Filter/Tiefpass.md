---
title: Tiefpass
kategorie: EK
kapitel: Filter
tags: [tiefpass, TP, grenzfrequenz, RC, RL, T-TP, pi-TP, glättung, rauschunterdrückung, anti-aliasing, siebung, 20dB, 60dB, bode]
groessen: f_g|Grenzfrequenz|Hz; R|Widerstand|Ω; C|Kapazität|F; L|Induktivität|H
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Filter Grundlagen]]
- [[Transit & Grenzfrequenz]]
:::
:::vbox
**Verwandte Artikel**
- [[Hochpass]]
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

Ein Tiefpass (TP) lässt tiefe Frequenzen ungehindert durch und dämpft hohe. Je höher die Frequenz über f_g, desto stärker die Dämpfung.

## Passiver RC-Tiefpass (1. Ordnung)

:::schematic RC-Tiefpass 1. Ordnung: Eingang U_e links. R in Reihe (horizontal). Mittenknoten → C nach GND. Ausgang U_aus rechts vom Mittenknoten (über C gemessen). Bei tiefen Frequenzen: X_C gross → Ausgang ≈ Eingang. Bei hohen Frequenzen: X_C klein → Spannung fällt an R
/Diagramm/rc_tiefpass.svg
:::

R in Reihe, C nach Masse. Ausgang über C abgegriffen.

- **Tiefe f:** X_C gross → Spannung fällt hauptsächlich an C ab → Signal kommt durch
- **Hohe f:** X_C klein → Spannung fällt hauptsächlich an R ab → Signal gedämpft

:::formel
f_g = 1 / (2 * pi * R * C)    # Grenzfrequenz
R   = 1 / (2 * pi * f_g * C)  # Widerstand aus f_g und C
C   = 1 / (2 * pi * f_g * R)  # Kapazität aus f_g und R
:::

| Frequenz | Amplitude | Phase |
|---|---|---|
| f ≪ f_g | ≈ 1 (0 dB) | ≈ 0° |
| f = f_g | 0.707 (−3 dB) | −45° |
| f ≫ f_g | → 0 (−20 dB/Dek) | → −90° |

## Passiver RL-Tiefpass (1. Ordnung)

L in Reihe, R nach Masse. Ausgangsspannung an R abgegriffen. Steilheit ebenfalls 20 dB/Dekade.

:::formel
f_g = R / (2 * pi * L)
:::

## T-Tiefpass und π-Tiefpass (3. Ordnung, LC)

:::hbox
:::vbox
**T-Tiefpass (LC)**
:::schematic T-Tiefpass: U_e → L/2 → Knoten → L/2 → U_aus. C vom mittleren Knoten nach GND. Beide Induktivitäten gleich L/2 (oder L1 und L2). Typische 3-Elemente T-Topologie. Steilheit 60 dB/Dekade
/Diagramm/t_tiefpass_lc.svg
:::
:::
:::vbox
**π-Tiefpass (LC)**
:::schematic Pi-Tiefpass: U_e links. C/2 nach GND (am Eingang). L in Reihe. C/2 nach GND (am Ausgang). Ausgang U_aus rechts. Typische 3-Elemente π-Topologie. Steilheit 60 dB/Dekade
/Diagramm/pi_tiefpass_lc.svg
:::
:::
:::

Durch Kombination mehrerer LC-Glieder zu T- oder π-Topologien erreicht man **60 dB/Dekade** Steilheit:

- **T-Tiefpassglied:** L1 — C (nach Masse) — L1 (oder 2L1 in der Mitte)
- **π-Tiefpassglied:** C1 (nach Masse) — L — C1 (nach Masse) (oder 2C1 in der Mitte)

:::plot
var: f
range: 0.01, 100
xlabel: f / f_g (normiert)
ylabel: Amplitude (normiert)
TP 1. Ordnung: 1 / sqrt(1 + f*f)
TP 2. Ordnung: 1 / sqrt(1 + f^4)
:::

## Steilheit nach Typ

| Typ | Steilheit | Schaltungsaufwand |
|---|---|---|
| RC-TP 1. Ordnung | 20 dB/Dek | 1 R + 1 C |
| RC-TP 2 × kaskadiert | 40 dB/Dek | 2 R + 2 C |
| T-TP / π-TP (RC) | 40 dB/Dek | mehrere R + C parallel |
| T-TP / π-TP (LC) | 60 dB/Dek | L + C-Glieder |

## Bode-Tabelle (1. Ordnung)

| f | Amplitude | Dämpfung |
|---|---|---|
| 0.1 × f_g | 0.995 | −0.04 dB |
| f_g | 0.707 | −3 dB |
| 10 × f_g | 0.100 | −20 dB |
| 100 × f_g | 0.010 | −40 dB |

## Anwendungen

- **Glättung:** Netzteil-Siebfilter — Brummspannung nach dem Gleichrichter dämpfen
- **Rauschunterdrückung:** Sensorsignal vor ADC-Eingang glätten
- **Anti-Aliasing:** Frequenzen über f_s/2 vor der Digitalisierung entfernen
- **EMV:** Netzfilter gegen hochfrequente Störungen

:::monospace
Designbeispiel: f_g = 1 kHz, R = 10 kΩ
C = 1 / (2π × 1000 × 10000) = 15.9 nF → 15 nF (E12)
Probe: f_g = 1 / (2π × 10k × 15n) = 1.06 kHz ✓
Dämpfung bei 10 kHz: −20 dB (Faktor 10 über f_g)
:::
