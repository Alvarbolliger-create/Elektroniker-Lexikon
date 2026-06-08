---
title: Servomotor
kategorie: EK
kapitel: Motoren
tags: [servo, servomotor, positionsregelung, encoder, pid, lageregelung, drehzahlregelung, stromregelung, hobby-servo, pwm, industrie-servo, kaskadenregelung]
groessen: phi|Winkelposition|°; t_puls|Pulsbreite PWM|ms; n|Drehzahl|U/min; M|Drehmoment|N·m
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Schrittmotor]]
- [[BLDC-Motor]]
- [[PID-Regler]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[BLDC-Motor]]
- [[Frequenzumrichter]]
:::
:::vbox
**Führt weiter zu**
- [[Regelkreis Grundlagen]]
- [[Frequenzumrichter]]
:::
:::

---

Ein Servomotor ist kein eigener Motortyp, sondern ein **geregelter Antrieb**: Motor + Encoder + Regler bilden ein System, das eine Lage oder Drehzahl exakt hält — auch gegen äussere Störungen.

## Was macht einen Servo aus?

1. **Motor** (meist BLDC oder DC für Hobby; BLDC für Industrie)
2. **Encoder** oder Resolver für die Positionsrückmeldung
3. **Regler** (Lageregelung, Drehzahlregelung, Stromregelung — oft als Kaskade)

Die Regelung korrigiert kontinuierlich die Abweichung zwischen Soll- und Ist-Position.

## Hobby-Servo

Kompaktes Gerät mit eingebautem DC-Motor, Getriebe, Potenziometer (Positionssensor) und einfacher Elektronik. Ansteuerung über **PWM-Signal**:

:::formel
t_puls = 1.0 ms  → eine Endlage (z.B.   0°)
t_puls = 1.5 ms  → Mittelstellung         (90°)
t_puls = 2.0 ms  → andere Endlage       (180°)
f_PWM  = 50 Hz   → Periode T = 20 ms
:::

Typischer Drehbereich: **180°**. Weit verbreitet in Modellbau, einfacher Robotik.

:::info
Das Potenziometer im Hobby-Servo ist kein Encoder — es hat nur begrenzte Auflösung und Lebensdauer. Für genaue Positionierung oder Dauerbetrieb: Industrie-Servo.
:::

## Industrie-Servo: Regelkaskade

:::schematic Dreistufige Kaskadenregelung Servo: Sollposition (links) → Lageregler (P/PD) → Solldrehzahl → Drehzahlregler (PI) → Sollstrom → Stromregler (PI) → PWM → Motor → Encoder (Rückkopplung). Encoder-Signal zurück zu allen drei Reglern (Lage, Drehzahl, Strom). Innerster Kreis (Strom) am schnellsten, äusserster (Lage) am langsamsten
/Diagramm/servo_kaskadenregelung.svg
:::

| Regelkreis | Regler | Messgrösse | Stellgrösse |
|---|---|---|---|
| Lageregelung (äusserer) | P oder PD | Winkelposition (Encoder) | Solldrehzahl |
| Drehzahlregelung (mittlerer) | PI | Drehzahl (Encoder) | Sollstrom |
| Stromregelung (innerer) | PI | Phasenstrom (Shunt) | PWM-Duty |

Der innerste Regelkreis (Strom) ist am schnellsten, der äusserste (Lage) am langsamsten.

## Encoder-Auflösung

| Typ | Auflösung | Einsatz |
|---|---|---|
| Inkremental-Encoder | 256–65536 Pulse/Umdr. | Drehzahl + Relativposition |
| Absolutwert-Encoder (Single-Turn) | 12–23 Bit (4096–8 Mio. Schritte) | Absolute Position einer Umdrehung |
| Absolutwert-Encoder (Multi-Turn) | + Umdrehungszähler | Position über mehrere Umdrehungen |

Hochauflösende Encoder: 23 Bit = 8'388'608 Schritte/Umdrehung → Positionsauflösung << 0.001°.

## Kommunikation

Industrie-Servos kommunizieren über Feldbusse:

| Bus | Typischer Einsatz |
|---|---|
| EtherCAT | Hochdynamische Achsen, synchronisiert |
| CANopen | Maschinenautomation, Robotik |
| PROFIBUS / PROFINET | Siemens-Umgebungen |
| Analoge 0–10 V / ±10 V | Ältere Maschinen |

## Vergleich Schrittmotor / Servo

| Eigenschaft | Schrittmotor | Industrie-Servo |
|---|---|---|
| Positionsrückmeldung | Keine (Open-Loop) | Encoder (Closed-Loop) |
| Schrittverlust | Möglich (unbemerkt) | Erkannt + korrigiert |
| Dynamik | Mittel | Sehr hoch |
| Positionsgenauigkeit | Abhängig von Mikroschritt | << 0.01° |
| Kosten | Günstig | Deutlich höher |
| Komplexität | Mittel | Hoch (Regler, Verdrahtung) |
| Typischer Einsatz | 3D-Drucker, CNC hobby | Roboter, Werkzeugmaschinen |

:::tip
Für einfache Positionieraufgaben (CNC-Fräse, 3D-Drucker, Plotter): Schrittmotor. Sobald hohe Dynamik, genaue Positionierung unter wechselnder Last oder Schrittverlust ein Problem ist: Industrie-Servo.
:::
