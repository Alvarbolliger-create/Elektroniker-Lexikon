---
title: Colpitts-Oszillator
kategorie: EK
kapitel: Oszillatoren
tags: [colpitts, LC-oszillator, kapazitiv, C1, C2, kondensatorteiler, resonanzfrequenz, rückkopplungsfaktor, BJT, HF, quarz-colpitts, serienkapazität]
groessen: f_0|Resonanzfrequenz|Hz; k|Rückkopplungsfaktor|—; v_u|Spannungsverstärkung|—; L|Induktivität|H; C1|Kapazität 1|F; C2|Kapazität 2|F; C_ser|Serienkapazität|F
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[BJT Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Hartley-Oszillator]]
- [[Meissner-Oszillator]]
- [[Quarzoszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Quarzoszillator]]
- [[Pierce-Gate-Oszillator]]
:::
:::

---

Der Colpitts-Oszillator ist ein LC-Oszillator mit **kapazitiv geteiltem Schwingkreis**: Zwei Kondensatoren C1 und C2 bilden den kapazitiven Spannungsteiler für die Rückkopplung. Er eignet sich besonders für hohe Frequenzen und ist die Basis des Pierce-Gate-Oszillators.

## Schaltungsprinzip

:::schematic Colpitts-Oszillator: BJT (NPN) in Emitterschaltung. Kollektor über R_K an VCC, Emitter über R_E nach GND. LC-Schwingkreis: L von Kollektor nach VCC (oder über Drossel). C1 von Kollektor nach Basis-Rückkopplungspunkt. C2 von Rückkopplungspunkt nach GND (Emitter). Basis-Rückkopplung: Verbindung C1/C2 (Mittelabgriff) über Koppelkondensator an Basis. Schwingkreis schwingt mit L und C_ser = C1×C2/(C1+C2). k = C1/C2, Phasendrehung Rückkopplung: 180°
/Diagramm/colpitts.svg
:::

BJT in Emitterschaltung → λ = 180°. Der Schwingkreis besteht aus L und der Serienschaltung von C1 und C2. Die Verbindung zwischen C1 und C2 ist der Rückkopplungsabgriff — er koppelt den Bruchteil C1/C2 zurück und dreht 180° → φ + λ = 360° ✓

## Formeln aus dem Spick

:::formel
C_ser = C1 * C2 / (C1 + C2)                       # effektive Serienkapazität im Schwingkreis
f_0   = 1 / (2 * pi * sqrt(L * C_ser))             # Resonanzfrequenz
f_0   = 1 / (2 * pi * sqrt(L * C1*C2/(C1+C2)))    # kompakt
k     = C1 / C2                                     # Rückkopplungsfaktor
v_u   = 1 / k = C2 / C1                            # benötigte Spannungsverstärkung
:::

:::monospace
Beispiel: f_0 = 10 MHz, L = 1 µH, Verhältnis C2 = 10 × C1
ω = 2π × 10e6 = 62.83e6 rad/s
C_ser = 1 / (L × ω²) = 1 / (1e-6 × 3948e9) = 253 pF

C2 = 10 × C1, C_ser = 10C1²/11C1 = 10C1/11 = 253 pF
→ C1 = 278 pF → 270 pF (E12), C2 = 2700 pF (E12)

k = 270/2700 = 0.1 → v_u = 10 ✓
:::

## Quartz-Colpitts

Wenn der Quarz **statt der Spule L** eingesetzt wird, arbeitet er in seiner Parallelresonanz (zwischen f_r und f_p) als hochselektive Induktivität. Das ergibt einen hochstabilen Quarzoszillator in Colpitts-Topologie. → [[Quarzoszillator]]

## Vergleich mit Hartley

| Eigenschaft | Colpitts | Hartley |
|---|---|---|
| Spannungsteiler | kapazitiv (C1 und C2) | induktiv (N1 und N2) |
| Frequenzbereich | 1 MHz – 1 GHz | 100 kHz – 100 MHz |
| HF-Stabilität | sehr gut | gut |
| Quarz-Version | ja (Quarz-Colpitts) | selten |

## Anwendungen

- **HF-Signalgeneratoren:** Stabile Frequenzerzeugung im MHz-Bereich
- **Mobilfunk-Frontends:** VCO (spannungsgesteuerter Oszillator mit Varaktordiode als C1)
- **Basis des Pierce-Gate:** CMOS-Quarzoszillator in MCUs ist ein Colpitts-Derivat
