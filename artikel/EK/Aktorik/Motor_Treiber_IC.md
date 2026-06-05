---
title: Motor-Treiber-IC
kategorie: EK
tags: [motor-treiber, l298n, tb6612, drv8833, drv8825, h-brücke, ic, treiber, pwm, schutzschaltung, chopper]
symbol: —
einheit: —
---

Ein Motor-Treiber-IC ist ein integrierter Schaltkreis, der einen oder mehrere Motoren direkt ansteuert. Er enthält die nötige Leistungselektronik, Schutzschaltungen und PWM-Logik — fertig für die direkte Verwendung mit Mikrocontrollern.

:::hbox
:::vbox
**Voraussetzungen**
- [[H-Brücke]]
- [[PWM]]
- [[DC Motor]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[Aktorik]]
:::
:::vbox
**Führt weiter zu**
- [[Frequenzumrichter]]
:::
:::

---

## Aufbau

Ein Motor-Treiber-IC enthält typisch:

- Eine oder zwei [[H-Brücke|H-Brücken]] (für einen oder zwei DC-Motoren / eine Schrittmotorphase)
- Logikpegel-Eingang (3,3 V oder 5 V kompatibel)
- Integrierte Freilaufdioden
- Überstromschutz (Kurzschlussabschaltung)
- Thermische Abschaltung
- Optionale Strommesspins

Die Logikseite und die Motorspannungsseite sind intern getrennt. Beide brauchen eigene Versorgung.

---

## Vergleich gängiger ICs

| IC | U_mot | I_max | Phasen | Besonderheit |
|---|---|---|---|---|
| L298N | 5–46 V | 2 A (4 A peak) | 2 DC | Alt, hohe Verluste (~2 V Abfall pro Seite), kein PWM-Chopper |
| TB6612FNG | 2,5–13,5 V | 1,2 A | 2 DC | Kompakt, niedrige Verluste, weit verbreitet |
| DRV8833 | 2,7–10,8 V | 1,5 A | 2 DC | Integrierte Freilaufdioden, günstig |
| DRV8825 | 8,2–45 V | 2,5 A | 1 Stepper | Mikroschritt bis 1/32, einstellbares Current Limiting |
| A4988 | 8–35 V | 2 A | 1 Stepper | Günstig, Standard in vielen CNC-Projekten |
| TMC2209 | 4,75–29 V | 2 A | 1 Stepper | Sehr leise, StallGuard-Diagnose, UART-Konfiguration |

---

## Ansteuerung TB6612FNG (Beispiel)

| Pin | Funktion |
|---|---|
| AIN1, AIN2 | Richtungssteuerung Motor A |
| PWMA | PWM-Signal für Drehzahl Motor A |
| BIN1, BIN2 | Richtungssteuerung Motor B |
| PWMB | PWM-Signal für Drehzahl Motor B |
| STBY | Standby (LOW = Treiber abschalten) |

:::formel
Vorwärts:  AIN1=1, AIN2=0, PWMA=PWM-Signal
Rückwärts: AIN1=0, AIN2=1, PWMA=PWM-Signal
Bremsen:   AIN1=1, AIN2=1  (Kurzschluss-Bremse)
Freilauf:  AIN1=0, AIN2=0
:::

---

## Verlustleistung und Kühlung

Die Verlustleistung entsteht am R_DS(on) der internen FETs:

:::formel
P_V = I^2 * R_DS_on * 2
:::

Bei Strömen über 1 A ist eine ausreichende Kupferfläche auf der Platine (Wärmeableitung durch PCB) oder ein Kühlkörper nötig.

:::warning
Der L298N hat einen Spannungsabfall von ca. 2 V pro H-Brücken-Seite (Gesamtverlust 4 V). Bei 12 V und 2 A: P_V = 4 V × 2 A = 8 W. Ohne Kühlung überhitzt der IC sofort.
:::

---

## Auswahl

:::tip
Für neue Designs L298N meiden. TB6612FNG oder DRV8833 sind effizienter, kompakter und haben integrierte Schutzfunktionen. Für Schrittmotoren TMC2209 wählen, wenn leiser Betrieb oder Diagnose wichtig ist.
:::
