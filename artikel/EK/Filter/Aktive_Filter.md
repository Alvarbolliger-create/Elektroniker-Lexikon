---
title: Aktive Filter
kategorie: EK
kapitel: Filter
tags: [aktive filter, OPV, sallen-key, tiefpass, hochpass, bandpass, bandsperre, impedanz, blindwiderstand, 40dB, butterworth, 2. ordnung, invertierend, frequenzabhängig]
groessen: f_g|Grenzfrequenz|Hz; v_u|Spannungsverstärkung|—; Z|Impedanz|Ω; X_C|kapazitiver Blindwiderstand|Ω; x_p|kapazitiver Blindwiderstand (parallel)|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
- [[OPV Invertierend]]
- [[Filter Grundlagen]]
- [[Tiefpass]]
- [[Hochpass]]
:::
:::vbox
**Verwandte Artikel**
- [[Filtercharakteristik]]
- [[Bandpass]]
- [[Bandsperre]]
:::
:::vbox
**Führt weiter zu**
- [[Filtercharakteristik]]
- [[Oszillatoren Grundlagen]]
:::
:::

---

Aktive Filter kombinieren OPV mit passiven RC-Elementen. Der OPV-Ausgang ist **sehr niederohmig** und darf deshalb als "mit Masse verbunden" betrachtet werden — die Lastimpedanz beeinflusst den Frequenzgang nicht.

## Vorteil gegenüber passiven Filtern

| Eigenschaft | Passiv (RC) | Aktiv (RC + OPV) |
|---|---|---|
| Verstärkung | ≤ 1 (dämpft immer) | > 1 möglich |
| Lasteinfluss | vorhanden | vernachlässigbar |
| Kaskadierbarkeit | schwierig (Impedanzanpassung nötig) | einfach |
| Steilheit 2. Ord. | 40 dB/Dek mit 2 RC-Stufen | 40 dB/Dek (Sallen-Key) |
| Versorgung | keine | nötig |

## Aktiver Tiefpass (invertierend)

:::schematic Aktiver Tiefpass (invertierend): OPV-Dreieck. Eingang U_e → R_e → invertierender Eingang (−). Nichtinvertierender Eingang (+) auf GND. Rückkopplung: R_p parallel zu C_p von Ausgang auf (−). Bei tiefen Frequenzen: X_Cp gross → Z_Rückkopplung ≈ R_p → Verstärkung −R_p/R_e. Bei hohen Frequenzen: X_Cp klein → Z → 0 → Ausgang 0 (Tiefpass)
/Diagramm/aktiv_tiefpass_inv.svg
:::

Rückkopplungszweig: R_p parallel zu C_p. Eingangswiderstand: R_e.

Die Impedanz des Rückkopplungszweigs ist frequenzabhängig — bei tiefen Frequenzen dominiert R_p, bei hohen C_p.

:::formel
x_p = 1 / (2 * pi * f * C)                      # kapazitiver Blindwiderstand C_p
Z   = (R_p * x_p) / sqrt(R_p^2 + x_p^2)         # Parallelimpedanz R_p || C_p
v_u = -Z / R_e                                   # Spannungsverstärkung (invertierend)
:::

**Frequenzgang:**
- Tiefe f: x_p gross → Z ≈ R_p → v_u = −R_p/R_e (konstante Verstärkung)
- Hohe f: x_p klein → Z → 0 → v_u → 0 (Dämpfung, Tiefpassverhalten)

## Aktiver Hochpass (invertierend)

:::schematic Aktiver Hochpass (invertierend): OPV-Dreieck. Eingang U_e → C → R_C (Serienimpedanz) → invertierender Eingang (−). Nichtinvertierender Eingang (+) auf GND. Rückkopplung: R_k von Ausgang auf (−). Bei tiefen Frequenzen: X_C gross → Z gross → Verstärkung ≈ 0. Bei hohen Frequenzen: X_C klein → Z ≈ R_C → Verstärkung −R_k/R_C (Hochpass)
/Diagramm/aktiv_hochpass_inv.svg
:::

Eingangszweig: R_C in Reihe mit C (Impedanz Z). Rückkopplungswiderstand: R_k.

:::formel
X_C = 1 / (2 * pi * f * C)     # kapazitiver Blindwiderstand C
Z   = sqrt(R_C^2 + X_C^2)      # Serienimpedanz R_C + C
v_u = -R_k / Z                  # Spannungsverstärkung (invertierend)
:::

**Frequenzgang:**
- Tiefe f: X_C gross → Z gross → v_u ≈ 0 (Dämpfung)
- Hohe f: X_C klein → Z ≈ R_C → v_u = −R_k/R_C (konstante Verstärkung, Hochpassverhalten)

:::info
Der aktive Hochpass ist zugleich ein Bandpass: Bei sehr hohen Frequenzen begrenzt das GBW des OPV die Verstärkung. Die obere Grenzfrequenz wird durch f_t des OPV bestimmt (→ [[OPV Grundlagen]]).
:::

## Sallen-Key Filter (2. Ordnung, 40 dB/Dek)

:::hbox
:::vbox
**Sallen-Key Tiefpass**
:::schematic Sallen-Key Tiefpass 2. Ordnung: Eingang U_e → R1 → Knoten A → R2 → (+) des OPV. C1 von Knoten A nach Ausgang (Rückkopplungskondensator). C2 von (+) nach GND. OPV als Spannungsfolger (Ausgang → −). Ausgang U_aus. Butterworth: R1 = R2 = R, C1 = 2C, C2 = C/2 → Q = 0.707
/Diagramm/sallen_key_tp.svg
:::
:::
:::vbox
**Sallen-Key Hochpass**
:::schematic Sallen-Key Hochpass 2. Ordnung: Eingang U_e → C1 → Knoten A → C2 → (+) des OPV. R1 von Knoten A nach Ausgang. R2 von (+) nach GND. OPV als Spannungsfolger (Ausgang → −). Ausgang U_aus. Dual zum Tiefpass: Widerstände und Kondensatoren vertauscht
/Diagramm/sallen_key_hp.svg
:::
:::

Die Sallen-Key-Topologie realisiert aktive Filter 2. Ordnung mit einem OPV als Spannungsfolger (v_u = 1). Zwei R und zwei C um den OPV. Für gleiche Bauteile (R1 = R2 = R, C1 = C2 = C):

:::formel
f_g = 1 / (2 * pi * R * C)    # Grenzfrequenz Sallen-Key (TP und HP)
:::

Durch Wahl der Bauteilwertverhältnisse wird die **Filtercharakteristik** (Butterworth, Chebyshev, Bessel) bestimmt. Butterworth: Q = 1/√2 ≈ 0.707 (maximale Flachheit, kein Überschwingen).

## Aktiver Bandpass und Bandsperre (2. Ordnung)

| Typ | Ordnung | Steilheit |
|---|---|---|
| Aktiver TP (Sallen-Key) | 2 | 40 dB/Dek |
| Aktiver HP (Sallen-Key) | 2 | 40 dB/Dek |
| Aktiver BP | 2 | 20/20 dB/Dek |
| Aktive BS (Notch) | 2 | 20/20 dB/Dek |

Aktive BP und BS 2. Ordnung werden mit mehreren OPVs und RC-Netzwerken realisiert (z.B. State-Variable-Filter für gleichzeitigen TP/HP/BP-Ausgang).

:::tip
Für Butterworth-Charakteristik Sallen-Key TP 2. Ordnung: C1 = C2 = C, dann R1 = √2/(2π·f_g·C) und R2 = 1/(√2·2π·f_g·C). Das ergibt Q = 0.707 — maximale Flachheit ohne Welligkeit.
:::

## SC-Filter (Switched-Capacitor)

Ein OPV-Filter höherer Ordnung (z. B. 8. Ordnung = 160 dB/Dek) erfordert viele Stufen und ist aufwändig. Als Alternative existieren integrierte **SC-Filter (Switched-Capacitor-Filter)**: Sie emulieren analoge RC-Widerstände durch einen getakteten Kondensator (CLK-Signal), der mit einer Frequenz f_CLK hin und her geschaltet wird.

- **Vorteil**: Hohe Ordnungen auf einem Chip, f_g programmierbar über CLK-Frequenz
- **Nachteil**: Der Taktvorgang erzeugt Störfrequenzen (Spiegelfrequenzen) im Ausgang

Deshalb wird dem SC-Filter typisch ein **aktiver Tiefpass nachgeschaltet**, der diese Takt-Störanteile herausfiltert.

:::monospace
Beispiel: MAX293 (8. Ordnung SC-Tiefpass)
  Steilheit = 8 × 20 dB/Dek = 160 dB/Dek
  f_g = f_CLK / 100 (einstellbar)
  Nachgeschalteter TP: eliminiert Störungen durch die CLK-Taktung
:::
