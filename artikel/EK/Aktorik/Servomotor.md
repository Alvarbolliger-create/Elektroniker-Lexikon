---
title: Servomotor
kategorie: EK
tags: [servomotor, servo, encoder, pwm, rc-servo, positionsregelung, rückmeldung, potentiometer, pid]
symbol: M
einheit: —
---

Ein Servomotor ist ein Motor mit integrierter Regelung und Positionsrückmeldung. Über das Steuersignal wird ein bestimmter Drehwinkel oder eine Drehzahl angefahren und gehalten.

:::hbox
:::vbox
**Voraussetzungen**
- [[DC Motor]]
- [[PWM]]
- [[Regelkreis]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[Aktor mit Rückmeldung]]
:::
:::vbox
**Führt weiter zu**
- [[PID Regler]]
- [[Motor-Treiber-IC]]
:::
:::

---

## RC-Servo (Hobby-Servo)

RC-Servos sind günstige Stellmotoren für RC-Modelle, einfache Robotergelenke und Mechanismen. Sie integrieren Motor, Getriebe, Potentiometer und Regelungselektronik in einem kompakten Gehäuse.

Angesteuert über ein PWM-Signal mit fester Frequenz (50 Hz):

:::formel
Impulsbreite → Position
  1,0 ms     → 0°   (linker Anschlag)
  1,5 ms     → 90°  (Mitte)
  2,0 ms     → 180° (rechter Anschlag)
  Periode    → 20 ms (50 Hz)
:::

Das Potentiometer misst den aktuellen Winkel. Die interne Elektronik vergleicht Soll und Ist und steuert den Motor entsprechend.

:::tip
Mikrocontroller-Bibliotheken (z.B. Arduino Servo.h) erzeugen das PWM-Signal direkt. Nur den Winkel in Grad übergeben — die Bibliothek rechnet auf Impulsdauer um.
:::

---

## Industrieservo

Industrieservos sind für Präzision und Dynamik ausgelegt. Sie bestehen aus Motor, Präzisions-Encoder und einem separaten Servoantrieb (Verstärker), der den Regelkreis schliesst.

Der Servoantrieb vergleicht Soll-Position (vom Controller) mit Ist-Position (vom Encoder) und regelt den Motor.

Typische Regelstruktur (Kaskade):

:::formel
Positionsregler → Drehzahlregler → Stromregler → Motor
      ↑ enc             ↑ tach          ↑ I-Sensor
:::

Jeder innere Kreis ist schneller als der äussere. Der Stromregler arbeitet im µs-Bereich, der Positionsregler im ms-Bereich.

---

## Vergleich RC-Servo vs. Industrieservo

| Eigenschaft | RC-Servo | Industrieservo |
|---|---|---|
| Genauigkeit | 1–2° | < 0,01° möglich |
| Drehmoment | bis ca. 5 Nm | Beliebig skalierbar |
| Feedback | Potentiometer (analog) | Encoder (digital) |
| Steuersignal | PWM 50 Hz | Feldbus, Analog ±10 V |
| Preis | 5–50 € | 500–10 000+ € |

---

## Abgrenzung zum Schrittmotor

Ein [[Schrittmotor]] arbeitet ohne Rückmeldung (open loop). Ein Servomotor hat immer einen Rückmeldesensor. Daraus folgt:

| | Schrittmotor | Servomotor |
|---|---|---|
| Schrittverlust möglich | Ja | Nein |
| Wirkungsgrad bei Teillast | Schlecht | Gut |
| Systemkomplexität | Gering | Höher |
| Typischer Einsatz | CNC-Achsen, Drucker | Roboter, Werkzeugmaschinen |
