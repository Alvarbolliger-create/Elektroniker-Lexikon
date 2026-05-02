---
title: Logikfamilien (TTL, CMOS, LVDS)
kategorie: SH
tags: [TTL, CMOS, LVDS, logikfamilien, pegel, fanout, propagation-delay, HCT, HC, noise-margin, level-shifter, 74HC, 74HCT, 74LVC, ESD, rauschspanne]
symbol: —
einheit: —
---

Logikfamilien definieren, wie digitale Gatter elektrisch aufgebaut sind. Sie bestimmen Spannungspegel, Stromtreibfähigkeit, Geschwindigkeit und Leistungsaufnahme.

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter]]
- [[Transistor NPN]]
- [[MOSFET]]
:::
:::vbox
**Verwandte Artikel**
- [[Pull-Up / Pull-Down]]
- [[Flipflops]]
:::
:::

---

## Pegelübersicht

Jede Logikfamilie definiert vier kritische Spannungen:

| Pegel | Bedeutung |
|---|---|
| V_OH | Minimale Ausgangsspannung für logisch 1 |
| V_OL | Maximale Ausgangsspannung für logisch 0 |
| V_IH | Minimale Eingangsspannung, die als 1 erkannt wird |
| V_IL | Maximale Eingangsspannung, die als 0 erkannt wird |

**Rauschspanne (Noise Margin)**:
```
NM_H = V_OH - V_IH    # High-Rauschspanne
NM_L = V_IL - V_OL    # Low-Rauschspanne
```

---

## TTL (Transistor-Transistor-Logik)

- Aufgebaut mit bipolaren NPN-Transistoren
- Versorgung: **5V fest**
- Hoher Ruhestrom auch ohne Last (statische Verluste)
- Schnelles Schalten, aber hoher Strombedarf

| Grösse | Typischer Wert |
|---|---|
| V_CC | 5V |
| V_OH | ≥ 2.4V |
| V_OL | ≤ 0.4V |
| V_IH | ≥ 2.0V |
| V_IL | ≤ 0.8V |
| I_OH | –400 µA (Sourceströme klein!) |
| t_pd | 10–50 ns |

:::warning
TTL kann nur wenige µA sourcen, aber mehrere mA sinken. LEDs nie direkt von TTL-Ausgang nach VCC schalten — immer gegen GND (active low).
:::

## CMOS (Complementary MOS)

- Aufgebaut mit PMOS + NMOS in Komplementärpaaren
- Statische Verluste nahezu null (Verluste nur beim Schalten)
- Vielzahl von Versorgungsspannungen möglich (1.2V–15V je nach Serie)
- Bei hohen Frequenzen: dynamische Verluste dominieren

| Grösse | HC-CMOS (5V) |
|---|---|
| V_CC | 2–6V (typisch 3.3V oder 5V) |
| V_OH | ≥ V_CC – 0.1V |
| V_OL | ≤ 0.1V |
| V_IH | ≥ 0.7 × V_CC |
| V_IL | ≤ 0.3 × V_CC |
| t_pd | 5–20 ns |

**Vorteil**: Rail-to-Rail Ausgang, hohe Rauschspanne, niedrige Leistung.  
**Nachteil**: Empfindlicher gegen statische Entladung (ESD).

---

## Vergleich der wichtigsten Familien

| Familie | V_CC | Technologie | Speed | Leistung | Kompatibilität |
|---|---|---|---|---|---|
| 74xx (TTL) | 5V | Bipolar NPN | Mittel | Hoch | — |
| 74LS (Low-power Schottky) | 5V | Schottky-TTL | Mittel | Mittel | TTL-kompatibel |
| 74HC (High-speed CMOS) | 2–6V | CMOS | Schnell | Sehr niedrig | Nicht TTL-kompatibel* |
| 74HCT (CMOS, TTL-Pegel) | 5V | CMOS | Schnell | Sehr niedrig | TTL-kompatibel |
| 74LVC (Low-Voltage CMOS) | 1.65–3.6V | CMOS | Sehr schnell | Niedrig | 5V-tolerant am Eingang |
| LVDS | 3.3V (diff.) | CMOS | Sehr schnell (GBit/s) | Niedrig | Differenziell |

*74HC mit 5V-Versorgung: V_IH = 3.5V, aber TTL-Ausgang liefert nur 2.4V min. → nicht kompatibel ohne Pull-up oder Level-Shifter.

---

## Pegel-Kompatibilität

**Problem**: Wenn verschiedene Logikfamilien oder Spannungen kombiniert werden, müssen die Pegel kompatibel sein.

**3.3V CMOS → 5V TTL/CMOS**:
- 74LVC-Ausgänge sind oft 5V-tolerant am Eingang
- 3.3V-Ausgang ≈ 3.3V, TTL benötigt V_IH ≥ 2.0V → kompatibel!
- CMOS bei 5V benötigt V_IH ≥ 3.5V → nicht kompatibel → Level-Shifter nötig

**5V → 3.3V**:
- 5V direkt an 3.3V-CMOS-Eingang: Zerstörungsgefahr (überschreitet V_CC + 0.5V)
- Lösung: Spannungsteiler, Level-Shifter IC (z.B. TXS0108), oder 5V-tolerante CMOS

---

## LVDS (Low Voltage Differential Signaling)

Für hohe Geschwindigkeiten (>100 MHz, Gbits/s):

- **Differenziell**: Zwei Leitungen, Signal = Spannungsdifferenz (typisch ±350mV)
- Sehr geringe Emission (elektromagnetisch): kleine Schwingung, hohe CMRR
- Abschlusswiderstand: 100Ω zwischen den Leitungen am Empfänger

```
Sender: D+ = 1.375V, D– = 1.025V → Diff = +350mV → logisch 1
         D+ = 1.025V, D– = 1.375V → Diff = –350mV → logisch 0
```

Anwendungen: HDMI, DisplayPort, MIPI CSI (Kamera), Hochgeschwindigkeits-ADC/DAC-Verbindungen.

---

## Fanout

Fanout gibt an, wie viele gleiche Gatter-Eingänge ein Ausgang treiben kann, ohne die Pegel zu verletzen.

```
Fanout = min(I_OH / I_IH, I_OL / I_IL)
```

| Familie | Typischer Fanout |
|---|---|
| TTL | 10 |
| HC-CMOS | 50+ (statisch, kapazitiv begrenzt) |
| LS-TTL | 20 |
