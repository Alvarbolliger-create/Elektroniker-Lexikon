---
title: H-Brücke
kategorie: EK
tags: [h-brücke, motor, mosfet, pwm, drehrichtung, shoot-through, totzeit, freilaufdiode, bootstrap]
symbol: —
einheit: —
---

Die H-Brücke ist eine Schaltung aus vier Schaltern (typisch [[MOSFET|MOSFETs]]), die eine Last mit umkehrbarer Polarität betreiben kann. Sie ist die Standardschaltung für Drehrichtungssteuerung und Drehzahlregelung von [[DC Motor|Gleichstrommotoren]].

:::hbox
:::vbox
**Voraussetzungen**
- [[MOSFET]]
- [[Transistor als Schalter]]
- [[PWM]]
:::
:::vbox
**Verwandte Artikel**
- [[DC Motor]]
- [[Schrittmotor]]
:::
:::vbox
**Führt weiter zu**
- [[Motor-Treiber-IC]]
- [[Frequenzumrichter]]
:::
:::

---

## Aufbau

Vier Schalter sind paarweise zwischen Versorgungsspannung und GND angeordnet. Der Motor liegt als Last in der Mitte — das ergibt im Schaltplan die charakteristische H-Form.

:::schematic H-Brücke Grundschaltung
/Diagramm/h_bruecke_0.svg
:::

| S1 | S2 | S3 | S4 | Motorverhalten |
|---|---|---|---|---|
| EIN | AUS | AUS | EIN | Vorwärts |
| AUS | EIN | EIN | AUS | Rückwärts |
| EIN | AUS | EIN | AUS | Bremsen (Kurzschluss über GND) |
| AUS | AUS | AUS | AUS | Freilauf (Motor dreht aus) |

S1 und S4 sind High-Side-Schalter (zwischen VCC und Motor), S2 und S3 Low-Side-Schalter (zwischen Motor und GND).

---

## Drehzahlsteuerung per PWM

[[PWM|Pulsweitenmodulation (PWM)]] auf einem Schalterpaar regelt die effektive Motorspannung und damit die Drehzahl:

:::formel
U_eff = U_VCC * D
:::

:::monospace
D     = Duty Cycle  0 ... 1
n     ≈ U_eff       (Drehzahl proportional)
:::

Typische PWM-Frequenz: 10–50 kHz — oberhalb des Hörbereichs, damit der Motor nicht pfeift.

---

## Freilaufdioden

Ein Motor ist induktiv. Beim Abschalten entsteht eine Spannungsspitze. Freilauf- (Flyback-) Dioden parallel zu jedem Schalter leiten diesen Strom ab.

:::warning
Ohne Freilaufdioden zerstören induktive Spannungsspitzen die Transistoren. Viele fertige [[Motor-Treiber-IC|IC-Lösungen]] integrieren diese Dioden bereits.
:::

Bei N-Kanal-MOSFETs ist die Body-Diode oft ausreichend, wenn sie schnell genug ist. Bei bipolaren Transistoren müssen externe Schottky-Dioden hinzugefügt werden.

---

## Shoot-Through

:::danger
**Shoot-Through** (Querstrom): Leiten S1 und S2 (oder S3 und S4) gleichzeitig, entsteht ein direkter Kurzschluss von VCC nach GND. Die Schalter und die Versorgung werden sofort zerstört.
:::

**Ursache**: MOSFETs haben eine endliche Schaltzeit. Beim Umschalten kann der noch leitende Transistor kurz gleichzeitig mit dem einschaltenden leiten.

**Lösung: Totzeit (Dead Time)**

Zwischen Ausschalten eines High-Side-FETs und Einschalten des Low-Side-FETs eine Pause einfügen (typisch 100 ns bis 5 µs). Viele Gate-Treiber-ICs erzeugen die Totzeit automatisch.

:::monospace
S1 (High): ___/‾‾‾‾‾\___________
                    ← Totzeit →
S2 (Low):  ___________/‾‾‾‾‾\___
:::

---

## MOSFET-Auswahl

| Parameter | Anforderung |
|---|---|
| U_DS | > U_VCC × 1,5 (Sicherheitsmarge) |
| I_D | > I_Motor_max |
| R_DS(on) | So klein wie möglich (niedrige Verluste) |
| Schaltzeit (t_r, t_f) | Klein genug für die gewählte PWM-Frequenz |

**High-Side-Problem**: Ein N-Kanal-MOSFET auf der High-Side braucht eine Gate-Spannung, die höher als VCC ist. Dafür wird ein Bootstrap-Kondensator oder ein dedizierter Gate-Treiber-IC benötigt. Alternativ: P-Kanal-MOSFET für High-Side (einfachere Ansteuerung, aber höherer R_DS(on)).

---

## Integrierte Lösungen

Für die meisten Anwendungen sind fertige [[Motor-Treiber-IC|Motor-Treiber-ICs]] die bessere Wahl:

| IC | Spannung | Strom | Besonderheit |
|---|---|---|---|
| L298N | 5–46 V | 2 A | Alt, hohe Verluste |
| DRV8833 | 2,7–10,8 V | 1,5 A | Integrierte Freilaufdioden |
| TB6612FNG | 2,5–13,5 V | 1,2 A | Kompakt, effizient |

:::tip
Für Prototypen immer einen fertigen H-Brücken-IC einsetzen. Diskrete Aufbauten lohnen sich erst bei hohen Strömen oder besonderen Spannungsbereichen.
:::
