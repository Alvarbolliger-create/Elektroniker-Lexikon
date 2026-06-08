---
title: Pierce-Gate-Oszillator
kategorie: EK
kapitel: Oszillatoren
tags: [pierce-gate, quarz, CMOS-inverter, MCU, mikrocontroller, 180-grad, schleifenverstärkung, gm, RS, C1, C2, RF, taktgeber, eingebaut, lastkapazität, PCB-layout]
groessen: f_0|Betriebsfrequenz|Hz; g_m|Transkonduktanz|A/V; R_f|Rückkopplungswiderstand|Ω; R_S|Serienwiderstand|Ω; C1|Lastkapazität 1|F; C2|Lastkapazität 2|F; C_L|Lastkapazität Quarz|F
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Quarzoszillator]]
- [[FET Grundlagen]]
- [[Oszillatoren Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Quarzoszillator]]
- [[Colpitts-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Regelkreis Grundlagen]]
:::
:::

---

Der Pierce-Gate-Oszillator ist das weltweit am häufigsten verwendete Quarzoszillator-Prinzip. Der CMOS-Inverter (U1) ist in nahezu jedem Mikrocontroller eingebaut — der Entwickler muss nur Quarz, C1, C2 und R_S extern anschliessen.

## Schaltungsprinzip

:::schematic Pierce-Gate-Oszillator: CMOS-Inverter U1 (Dreieck mit Kreis am Ausgang). R_f (1–10 MΩ) von Ausgang U1 nach Eingang U1 (Arbeitspunkteinstellung). Quarz X zwischen Ausgang U1 und Knoten A. R_S (0–470 Ω) in Reihe mit Quarz (Schleifenverstärkungsbegrenzung). C1 von Knoten A nach GND. C2 von Ausgang U1 nach GND (oder hinter R_S). Taktausgang XTAL_OUT vom Ausgang des Inverters (oft über zweiten Pufferivertier). Phasendrehung: −180° (Inverter) + −180° (Quarz + C1 + C2) = −360° ✓
/Diagramm/pierce_gate.svg
:::

**Bauteile und ihre Funktion:**

| Bauteil | Funktion |
|---|---|
| U1 (CMOS-Inverter) | Verstärker, liefert −180° Phasendrehung (λ) |
| R_f (1–10 MΩ) | Stellt Arbeitspunkt ein (Inverter in linearer Region) |
| Quarz (X_s) | Schwingt zwischen f_r und f_p (wirkt induktiv) |
| R_S (0–1 kΩ) | Begrenzt Schleifenverstärkung, schützt Quarz |
| C1, C2 | Erzeugen mit Quarz nochmals −180° Phasendrehung |

Phasenbedingung: −180° (Inverter) + −180° (R_S, C1, C2, Quarz) = −360° = 0° ✓

## Schleifenverstärkung

:::formel
G_schleife = g_m * X_C1 * X_C2 / R_S    # vereinfachte Formel
# g_m: Transkonduktanz des CMOS-Inverters (aus Datenblatt MCU)
# X_C = 1/(2π·f·C): kapazitiver Blindwiderstand
:::

Für sicheres Anlaufen: **G_schleife ≥ 5** (Sicherheitsfaktor gegenüber Temperatur und Alterung).

## Dimensionierung der Lastkapazitäten

Der Quarzhersteller gibt eine **Lastkapazität C_L** an (typisch 12–18 pF). Die externen C1 und C2 müssen diese erfüllen:

:::formel
C_L = (C1 * C2) / (C1 + C2) + C_streu    # Lastkapazität (C1, C2 seriell + Streukapazität PCB)
:::

Typische Wahl: C1 = C2 → C1 = C2 = 2 × (C_L − C_streu). Streukapazität PCB schätzen: 2–5 pF.

:::monospace
Beispiel: 16 MHz Quarz, C_L = 18 pF (Datenblatt)
C_streu ≈ 3 pF (PCB-Schätzung)
C_L_ext = C_L − C_streu = 15 pF
C1 = C2 = 2 × 15 pF = 30 pF → 33 pF (E12) wählen
R_f = 10 MΩ (meist in MCU eingebaut, kein externes Bauteil)
R_S = 0 bis 470 Ω (je nach gm des Inverters im Datenblatt prüfen)
:::

## PCB-Layout-Hinweise

:::warning
Layout ist kritisch: Quarz, C1 und C2 so kurz wie möglich an die MCU-Pins legen. Lange Leiterbahnen erhöhen C_streu und verstimmen die Frequenz.

Massefläche unter dem Quarz weglassen — sie würde kapazitiv zwischen den beiden Oszillator-Pins koppeln und die Phasenbedingung stören.
:::

## Vergleich Pierce-Gate vs. Colpitts-Quarz

| Eigenschaft | Pierce-Gate | Colpitts-Quarz |
|---|---|---|
| Verstärker | CMOS-Inverter (in MCU) | BJT oder FET |
| Externer Aufwand | minimal (C1, C2, R_S) | mehr Bauteile |
| Frequenzbereich | 1 – 40 MHz | 1 – 200 MHz |
| Typischer Einsatz | MCU, FPGA, ASIC | diskrete HF-Schaltungen |
| Quarz-Betriebsmodus | Parallelresonanz (induktiv) | Parallelresonanz |
