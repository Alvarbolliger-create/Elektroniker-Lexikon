---
title: Oszillatoren Grundlagen
kategorie: EK
kapitel: Oszillatoren
tags: [oszillator, schwingungsbedingung, rückkopplung, phasenverschiebung, schleifenverstärkung, selbsterregung, amplitudenbegrenzung, RC-oszillator, LC-oszillator, quarzoszillator, anlaufbedingung]
groessen: φ|Phasenverschiebung Rückkopplung|°; λ|Phasenverschiebung Verstärker|°; k|Rückkopplungsfaktor|—; v_u|Spannungsverstärkung|—; f_0|Resonanzfrequenz|Hz
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Schmitt-Trigger]]
- [[Filter Grundlagen]]
- [[Bandpass]]
:::
:::vbox
**Verwandte Artikel**
- [[Wien-Robinson-Oszillator]]
- [[RC-Phasenschieber]]
- [[Quarzoszillator]]
:::
:::vbox
**Führt weiter zu**
- [[RC-Phasenschieber]]
- [[Wien-Robinson-Oszillator]]
- [[Meissner-Oszillator]]
:::
:::

---

Ein Oszillator ist eine Verstärkerschaltung, die nach dem Anlegen der Betriebsspannung **selbsttätig ein periodisches Signal** erzeugt — ohne externen Eingangsimpuls. Er braucht ein frequenzbestimmendes Rückkopplungsnetzwerk und eine Amplitudenbegrenzung.

## Grundprinzip

:::schematic Oszillator Blockschaltbild: Zwei Blöcke in einer Schleife. Verstärker (v_u, λ) oben, frequenzbestimmendes Netzwerk (k, φ) unten. Ausgang U_a vom Verstärker. Rückkopplung: Ausgang → frequenzbestimmendes Netzwerk → k × U_a zurück zum Eingang des Verstärkers. Eingang des Verstärkers = k × U_a. Schwingungsbedingungen: φ + λ = 360°, k × v_u = 1
/Diagramm/oszillator_blockschaltbild.svg
:::

Ein Oszillator besteht aus zwei Blöcken in einer Schleife:

1. **Frequenzbestimmende Baugruppe** (RC, LC oder Quarz): Gibt nur bei f_0 ein Signal mit der richtigen Phasenlage zurück
2. **Verstärker** (BJT, OPV, CMOS-Gatter): Gleicht Verluste aus und hält die Schwingung aufrecht

Eine zusätzliche **Amplitudenbegrenzung** (Dioden, NTC, AGC) hält die Amplitude konstant und verhindert die Resonanzkatastrophe — ohne sie würde die Amplitude bis zum Aussteuerungsanschlag wachsen (Clipping).

## Schwingungsbedingungen

Für eine stabile, dauerhafte Schwingung müssen **beide** Bedingungen gleichzeitig erfüllt sein:

:::formel
phi + lambda = 360°    # Phasenbedingung: Gesamtphasendrehung der Schleife = 360°
k * v_u = 1            # Amplitudenbedingung: Schleifenverstärkung genau = 1
v_u = 1 / k            # benötigte Verstärkung aus Rückkopplungsfaktor
:::

- **φ (Phi):** Phasendrehung des frequenzbestimmenden Netzwerks
- **λ (Lambda):** Phasendrehung des Verstärkers
- **k:** Rückkopplungsfaktor (Bruchteil des Ausgangssignals, der zurückgekoppelt wird)
- **v_u:** Spannungsverstärkung des Verstärkers

:::info
k · v_u > 1 → Amplitude wächst (Anlaufen). k · v_u < 1 → Schwingung klingt ab. Stabile Schwingung bei k · v_u = 1 — die Amplitudenbegrenzung regelt automatisch dahin.
:::

## Anlaufbedingung

Beim Einschalten muss k · v_u **> 1** sein, damit thermisches Rauschen sich aufschaukeln kann. Die Amplitudenbegrenzung reduziert die effektive Verstärkung im Gleichgewicht auf genau 1.

:::tip
Beim Dimensionieren: Verstärkung für Start auf 1.5× bis 3× des benötigten Werts auslegen. Zu viel Reserve → schlechte Kurvenform (Clipping). Zu wenig → Oszillator startet nicht zuverlässig bei Kältebetrieb.
:::

## Taktgenerator-ICs

Integrierte Schaltkreise erzeugen Taktfrequenzen mit wenigen externen Bauteilen — kein Schwingkreis, keine Amplitudenbegrenzung nötig.

### 555-Timer (astabil)

:::schematic NE555 Astabile Kippstufe: 555-IC. Pin 8 (VCC) und Pin 1 (GND). R1 von VCC → Pin 7 (Discharge). R2 von Pin 7 → Pin 6 (Threshold) und Pin 2 (Trigger), kurzgeschlossen. C1 von Pin 6/2 nach GND. Pin 4 (Reset) auf VCC. Pin 5 (Control) über 10 nF nach GND. Ausgang an Pin 3. Laden: C1 über R1+R2. Entladen: C1 über R2. Ausgangsfrequenz f = 1.44 / ((R1+2×R2)×C1)
/Diagramm/ne555_astabil.svg
:::

Der NE555 als astabile Kippstufe lädt C1 über R1+R2 auf und entlädt über R2. Die Formel gilt für die Standard-Beschaltung:

:::formel
T   = 0.69 * (R1 + 2 * R2) * C1    # Periodendauer (0.69 = ln 2)
f   = 1 / T                          # Frequenz
:::

:::monospace
Beispiel: R2 = 18 kΩ, C1 = 150 nF → f = 500 Hz → T = 2 ms
  T = 0.69 × (R1 + 2×18k) × 150n = 2ms  →  R1 + 36k = 19.3kΩ
  Da R1 negativ → 500 Hz mit diesen Werten nicht erreichbar; R2 oder C verkleinern.
:::

### ICL8038 Precision Waveform Generator

Erzeugt gleichzeitig Rechteck, Dreieck und Sinus. R_A und R_B steuern Puls- und Pausendauer getrennt.

:::formel
f = 1 / ((R_A * C / 0.66) * (1 + R_B / (2 * R_A - R_B)))
:::

:::monospace
Beispiel: R_A = 120 kΩ, R_B = 50 kΩ, C = 5.6 nF
  Faktor = 1 + 50k/(240k-50k) = 1.263
  T = (120k × 5.6n / 0.66) × 1.263 = 1.286 ms  →  f = 778 Hz
:::

## Oszillatortypen — Übersicht

| Typ | Frequenzbereich | Frequenzbestimmung | Stabilität | Benötigte v_u |
|---|---|---|---|---|
| RC-Phasenschieber | 10 Hz – 1 MHz | 3 × RC-Glied (je 60°) | gering | 29 |
| Wien-Robinson | 10 Hz – 1 MHz | Wienglied (HP + TP) | mittel | 3 |
| Meissner | 100 kHz – 100 MHz | LC + Transformator | gut | N1/N2 |
| Hartley | 100 kHz – 100 MHz | LC + getapte Spule | gut | (N1+N2)/N2 |
| Colpitts | 1 MHz – 1 GHz | LC + Kondensatorteiler | sehr gut | C2/C1 |
| Quarzoszillator | 10 kHz – 200 MHz | Quarz (piezo) | sehr hoch | — |
| Pierce-Gate | 1 – 40 MHz | Quarz + CMOS-Inverter | sehr hoch | in MCU eingebaut |
| 555-Timer (astabil) | 1 Hz – 500 kHz | R1, R2, C | mittel | — |
| ICL8038 | 0.001 Hz – 300 kHz | R_A, R_B, C | mittel | — |
