---
title: Hochpass
kategorie: EK
kapitel: Filter
tags: [hochpass, HP, grenzfrequenz, RC, RL, T-HP, pi-HP, wechselstromkopplung, DC-sperre, brumm, einschwingvorgang, 20dB, 40dB, 60dB]
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
- [[Tiefpass]]
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

Ein Hochpass (HP) lässt hohe Frequenzen durch und dämpft tiefe. Gleichspannung (0 Hz) wird vollständig gesperrt — der Hochpass ist die DC-Sperre.

## Passiver RC-Hochpass (1. Ordnung)

:::schematic RC-Hochpass 1. Ordnung: Eingang U_e links. C in Reihe (horizontal). Mittenknoten → R nach GND. Ausgang U_aus rechts vom Mittenknoten (über R gemessen). Bei tiefen Frequenzen: X_C gross → Spannung fällt an C → Ausgang ≈ 0. Bei hohen Frequenzen: X_C klein → Ausgang ≈ Eingang. Vergleich: Tiefpass mit vertauschten Bauteilen
/Diagramm/rc_hochpass.svg
:::

C in Reihe, R nach Masse. Ausgang über R abgegriffen — Tiefpass mit vertauschten Bauteilen.

- **Tiefe f:** X_C gross → fast keine Spannung an R → Signal gesperrt
- **Hohe f:** X_C klein → Spannung fällt hauptsächlich an R ab → Signal kommt durch

:::formel
f_g = 1 / (2 * pi * R * C)    # Grenzfrequenz (identisch zum Tiefpass)
R   = 1 / (2 * pi * f_g * C)
C   = 1 / (2 * pi * f_g * R)
:::

| Frequenz | Amplitude | Phase |
|---|---|---|
| f ≪ f_g | → 0 (−20 dB/Dek) | → +90° |
| f = f_g | 0.707 (−3 dB) | +45° |
| f ≫ f_g | ≈ 1 (0 dB) | ≈ 0° |

## Passiver RL-Hochpass (1. Ordnung)

R in Reihe, L nach Masse. Ausgangsspannung an L abgegriffen.

:::formel
f_g = R / (2 * pi * L)
:::

## T-Hochpass und π-Hochpass (höhere Ordnung)

Mehrere Glieder kaskadiert erhöhen die Steilheit:

| Typ | Steilheit | Schaltungsaufwand |
|---|---|---|
| RC-HP 1. Ordnung | 20 dB/Dek | 1 C + 1 R |
| T-HP / π-HP (RC) | 40 dB/Dek | mehrere C + R parallel |
| T-HP / π-HP (LC) | 60 dB/Dek | C + L-Glieder |

:::plot
var: f
range: 0.01, 100
xlabel: f / f_g (normiert)
ylabel: Amplitude (normiert)
HP 1. Ordnung: f / sqrt(1 + f*f)
HP 2. Ordnung: f*f / sqrt(1 + f^4)
:::

:::warning
Beim Einschalten erzeugt der Hochpass einen **Einschwingvorgang**: Der Ausgang springt kurz auf und klingt dann ab. Bei Audioverstärkern kann das zu einem Knackgeräusch führen. Abhilfe: Soft-Start-Schaltung oder den Koppelkondensator nach dem Verstärker anordnen.
:::

## Anwendungen

- **Wechselstromkopplung:** DC-Offset aus Sensorsignal entfernen (z.B. vor BJT-Verstärker)
- **Brummunterdrückung:** Audio — tieffrequentes Netzbrummen (50/100 Hz) dämpfen
- **Windgeräuschfilter:** Mikrofon — Windgeräusche unter 100 Hz entfernen
- **Koppelkondensator:** Gleichspannungsanteil zwischen Verstärkerstufen blockieren

:::monospace
Designbeispiel: DC-Sperre für Audio, f_g = 20 Hz, C = 10 µF
R = 1 / (2π × 20 × 10e-6) = 796 Ω → 820 Ω (E12)
Probe: f_g = 1 / (2π × 820 × 10e-6) = 19.4 Hz ✓
Bei 20 Hz: −3 dB — darunter wird Signal gedämpft
:::
