---
title: H-Brücke (Motoransteuerung)
kategorie: EK
tags: [h-brücke, motor, MOSFET, PWM, richtungssteuerung, shoot-through, totzeit]
symbol: —
einheit: —
---

Die H-Brücke erlaubt die Drehrichtungssteuerung eines Gleichstrommotors durch vier Schalter, die so angeordnet sind, dass der Strom in beiden Richtungen durch den Motor fliessen kann.

:::hbox
:::vbox
**Voraussetzungen**
- [[MOSFET]]
- [[Transistor als Schalter]]
- [[PWM]]
:::
:::vbox
**Verwandte Artikel**
- [[Relais & Schütze]]
- [[LED-Ansteuerung]]
:::
:::vbox
**Führt weiter zu**
- [[BLDC Motor]]
- [[Stepper Motor]]
:::
:::

---

## Aufbau

Vier Schalter (typisch N-Kanal-MOSFETs oder NPN-Transistoren) bilden eine H-Form:

```
       +VCC
        |
   [S1]   [S2]
    |         |
    +---[M]---+    ← Motor zwischen den Mittelknoten
    |         |
   [S3]   [S4]
        |
       GND
```

| S1 | S2 | S3 | S4 | Motorverhalten |
|---|---|---|---|---|
| EIN | AUS | AUS | EIN | Vorwärts |
| AUS | EIN | EIN | AUS | Rückwärts |
| EIN | AUS | EIN | AUS | Bremsen (Kurzschluss über GND) |
| AUS | EIN | AUS | EIN | Bremsen (Kurzschluss über VCC) |
| AUS | AUS | AUS | AUS | Freilauf (Motor dreht aus) |

---

## Shoot-Through

:::warning
**Shoot-Through** (Querstrom): Wenn S1 und S3 gleichzeitig leitend sind, entsteht ein direkter Kurzschluss von VCC nach GND. Die Schalter und die Versorgung werden sofort zerstört.
:::

**Ursache**: Beim Umschalten hat der abschaltende MOSFET eine Ausschaltzeit. Wenn der andere MOSFET schon einschaltet, leiten beide kurz gleichzeitig.

**Lösung: Totzeit (Dead Time)**

Zwischen Ausschalten eines High-Side-FETs und Einschalten des Low-Side-FETs eine kurze Pause einfügen (typisch 100ns–5µs). Beide Seiten sind kurz gesperrt.

```
S1: ___/‾‾‾‾‾‾\___
                    ← Totzeit (z.B. 500ns)
S3: ______________/‾‾‾‾‾‾\_
```

---

## PWM-Drehzahlregelung

Durch Pulsweitenmodulation (PWM) eines Schalterpaares lässt sich die effektive Motorspannung und damit die Drehzahl steuern:

```
U_motor_eff = U_VCC × D    # D = Duty Cycle 0...1
n ≈ U_motor_eff             # Drehzahl proportional zur effektiven Spannung
```

Typisch: PWM-Frequenz 10–50 kHz (über Hörbereich, verhindert Motorpfeifen).

---

## MOSFET-Auswahl

| Parameter | Anforderung |
|---|---|
| U_DS | > U_VCC × 1.5 (Sicherheitsmarge) |
| I_D | > I_Motor_max |
| R_DS(on) | So klein wie möglich (Verluste) |
| Schaltzeit | Klein für hohe PWM-Frequenz |

**High-Side-Problem**: Ein N-Kanal-MOSFET schaltet durch, wenn U_GS > U_th. Bei High-Side (Source auf VCC) muss U_GS > VCC + U_th sein. Dafür wird ein **Bootstrap-Kondensator** oder ein spezieller Gate-Treiber benötigt. Alternativ: P-Kanal-MOSFET für High-Side.

---

## Fertige IC-Lösungen

| IC | Spannung | Strom | Besonderheit |
|---|---|---|---|
| L298N | 5–46V | 2A (4A peak) | Älterer H-Brücken-IC, bipolar |
| DRV8833 | 2.7–10.8V | 1.5A | Klein, integrierte Freilaufdioden |
| TB6612FNG | 2.5–13.5V | 1.2A | Häufig bei Arduino-Projekten |
| IFX9201SG | 6–36V | 6A | Automotive, SPI-Ansteuerung |

:::tip
Für schnelle Prototypen immer einen fertigen H-Brücken-IC verwenden. Diskret aufgebaute H-Brücken erfordern genaue Totzeit-Steuerung und sind fehleranfälliger.
:::
