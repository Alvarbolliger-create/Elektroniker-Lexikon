---
title: Wien-Robinson-Oszillator
kategorie: EK
kapitel: Oszillatoren
tags: [wien-robinson, wienglied, RC-oszillator, sinusgenerator, amplitudenbegrenzung, NTC, abstimmbar, klirrfaktor, audiogenerator, k=1/3, v_u=3, 0-grad, tandempoti]
groessen: f_0|Resonanzfrequenz|Hz; k|Rückkopplungsfaktor|—; v_u|Spannungsverstärkung|—; R1|Widerstand 1|Ω; C1|Kapazität 1|F; R2|Widerstand 2|Ω; C2|Kapazität 2|F
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[Bandpass]]
- [[OPV Nichtinvertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[RC-Phasenschieber]]
:::
:::vbox
**Führt weiter zu**
- [[Meissner-Oszillator]]
- [[Klirrfaktor]]
:::
:::

---

Der Wien-Robinson-Oszillator ist der Standard-Sinusgenerator für den Audiobereich. Er verwendet das **Wienglied** als frequenzbestimmendes Netzwerk und benötigt nur eine Verstärkung von 3.

## Das Wienglied als Bandpass

:::schematic Wien-Robinson-Oszillator: OPV-Dreieck (nichtinvertierend). Wienglied als frequenzbestimmendes Netzwerk am (+)-Eingang: R1 in Reihe mit C1 (Hochpasszweig), C2 parallel zu R2 (Tiefpasszweig). Verstärker: R_E von (−) nach GND, R_R von Ausgang nach (−) mit NTC parallel (Amplitudenbegrenzung). Ausgang U_a. Bei f_0: φ = 0°, k = 1/3, v_u = 3
/Diagramm/wien_robinson.svg
:::

Das Wienglied kombiniert einen Hochpass (R1, C1) mit einem Tiefpass (R2, C2). Bei der Resonanzfrequenz beträgt die Phasenverschiebung beider Pässe je 45° — mit **entgegengesetztem Vorzeichen**. Die Gesamtphasendrehung hebt sich auf (φ = 0°).

Der **nichtinvertierende Verstärker** (λ = 0°) erfüllt damit die Phasenbedingung: φ + λ = 0° + 0° = 0° = 360°.

## Formeln aus dem Spick

:::formel
f_0 = 1 / (2 * pi * sqrt(R1 * C1 * R2 * C2))    # Resonanzfrequenz (allgemein)
f_0 = 1 / (2 * pi * R * C)                        # Sonderfall: R1=R2=R, C1=C2=C
k   = 1 / 3                                        # Rückkopplungsfaktor des Wienglieds bei f_0
v_u = 3                                            # benötigte Spannungsverstärkung
:::

## Verstärkerdimensionierung (OPV nichtinvertierend)

:::formel
v_u = 1 + R_R / R_E = 3    → R_R = 2 * R_E
:::

Typisch: R_E = 10 kΩ, R_R = 20 kΩ. Für sicheres Anlaufen leicht grösser: R_R = 22 kΩ → v_u = 3.2. Die Amplitudenbegrenzung regelt auf v_u = 3.

## Amplitudenbegrenzung

Ohne Regelung clippt die Ausgangsspannung → hoher Klirrfaktor. Zwei Methoden:

**Mit Dioden (antiparallel im R_R):** Begrenzt direkt. Einfach, THD höher (typisch 1–5 %).

**Mit NTC im Gegenkopplungszweig:** Bei steigender Amplitude erwärmt sich der NTC → sein Widerstand steigt → v_u sinkt automatisch auf 3. Sehr gute Kurvenqualität (THD < 0.1 %), aber langsame Amplitude-Regelung.

:::monospace
Designbeispiel: f_0 = 1 kHz, R1 = R2 = 10 kΩ
C = 1 / (2π × 1000 × 10000) = 15.9 nF → 15 nF (E12)
Probe: f_0 = 1 / (2π × 10k × 15n) = 1.06 kHz ✓

Verstärker: R_E = 10 kΩ, R_R = 22 kΩ → v_u = 3.2 (Anlauf)
NTC parallel zu R_R → bei Amplitude 3 Vpp: NTC ≈ 20 kΩ → v_u = 3
:::

## Frequenzabstimmung

Bei R1 = R2 = R und C1 = C2 = C kann f_0 mit einem **Tandempotentiometer** (beide Widerstände gemeinsam) stufenlos verstellt werden. Bereichswechsel durch Umschalten von C1 und C2 (Stufenschalter).

:::tip
Der Wien-Robinson ist der bevorzugte Sinusgenerator für den Audiobereich (20 Hz – 20 kHz). Mit NTC-Amplitudenbegrenzung sind Klirrfaktoren unter 0.1 % erreichbar. Für HF-Anwendungen (> 1 MHz) → LC-Oszillatoren.
:::
