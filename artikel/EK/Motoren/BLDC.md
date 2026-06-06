---
title: BLDC-Motor
kategorie: EK
kapitel: Motoren
tags: [bldc, bürstenlos, brushless, hallsensor, sechs-schritt, foc, field-oriented-control, sensorlos, bemf, innenläufer, aussenläufer, esc, gate-treiber, kommutierung]
groessen: n|Drehzahl|U/min; f_el|elektrische Frequenz|Hz; p|Polpaarzahl|—; eta|Wirkungsgrad|%
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[DC Motor]]
- [[H-Brücke]]
- [[Hall-Sensor]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[Servomotor]]
- [[Frequenzumrichter]]
:::
:::vbox
**Führt weiter zu**
- [[Servomotor]]
- [[Frequenzumrichter]]
:::
:::

---

BLDC (Brushless DC) ist ein permanent erregter Synchronmotor mit **elektronischer Kommutierung**. Kein Verschleiss durch Bürsten, hoher Wirkungsgrad, hohe Leistungsdichte — dafür komplexere Ansteuerung als der klassische DC-Motor.

## Aufbau

Der **Rotor** trägt Permanentmagnete. Der **Stator** hat Wicklungen in drei Phasen (U, V, W). Es gibt keinen Kommutator und keine Bürsten — die Bestromungsreihenfolge übernimmt die Elektronik.

**Innenläufer**: Magnete innen (Rotor), Stator aussen. Kompakt, hohe Drehzahlen. Einsatz: Lüfter, Festplatten, Servomotoren.

**Aussenläufer**: Magnete aussen (Glockenläufer), Stator innen. Hohes Drehmoment bei niedrigen Drehzahlen, flache Bauform. Einsatz: Drohnen, Ventilatoren, Direktantriebe.

## Drehzahl-Polpaar-Beziehung

:::formel
n = f_el * 60 / p      # mechanische Drehzahl [U/min]
f_el = n * p / 60      # elektrische Frequenz [Hz]
:::

## KV-Zahl

Die KV-Zahl gibt an, wie viele Umdrehungen pro Minute der Motor im Leerlauf pro Volt erzeugt:

:::formel
KV  = n_leerlauf / U    # Motorkonstante [U/min/V]
n   = KV * U            # Leerlaufdrehzahl bei Spannung U
:::

:::monospace
Beispiel: Motor KV=1000, U=12V → n = 12'000 U/min
          Motor KV=400,  U=24V → n =  9'600 U/min
:::

:::info
Hoher KV-Wert = schnell, wenig Drehmoment (kleine Drohnen, Flugzeuge).
Niedriger KV-Wert = langsam, viel Drehmoment (grosse Propeller, Direktantriebe).
Die KV-Zahl gilt nur für den Leerlauf — unter Last sinkt die Drehzahl wegen des Innenwiderstands.
:::

| Grösse | Bedeutung |
|---|---|
| p | Polpaarzahl (Anzahl Magnetpolpaare am Rotor) |
| f_el | Frequenz der elektrischen Kommutierung |
| n | Mechanische Drehzahl [U/min] |

## Kommutierung: Sechs-Schritt (Trapez)

Die einfachste Methode: immer **zwei von drei Phasen** bestromt, dritte Phase offen. Pro elektrischer Umdrehung: 6 Zustände (Schritte).

Rotorposition wird mit **drei Hall-Sensoren** (je 120° versetzt) erkannt → 3 Bit = 6 eindeutige Zustände.

| Hall-Zustand (H1/H2/H3) | Aktive Phasen |
|---|---|
| 001 | U+ / V− |
| 011 | W+ / V− |
| 010 | W+ / U− |
| 110 | V+ / U− |
| 100 | V+ / W− |
| 101 | U+ / W− |

Einfach zu implementieren, aber ruckartig (Drehmomentwelligkeit ~30 %).

## Sensorlose Kommutierung (BEMF)

Ohne Hall-Sensoren: Die nicht bestromte Phase erzeugt eine Gegen-EMK (BEMF), die den Nulldurchgang der Rotorposition anzeigt. Kommutierung erfolgt 30° nach dem Nulldurchgang.

**Vorteil**: Kein Sensor → weniger Leitungen, billiger, robuster.  
**Nachteil**: Kein Anlaufmoment bei Stillstand (BEMF = 0) → Anlaufsequenz nötig (offene Schlaufe bis genug BEMF).

## FOC — Field Oriented Control (Sinus-Kommutierung)

Statt Trapezkurve werden alle drei Phasen **sinusförmig** bestromt, phasenrichtig zum Rotorwinkel. Ergebnis: gleichmässiges, welligkeitsarmes Drehmoment.

FOC benötigt:
- Hochauflösenden Encoder oder Hall-Sensor (+ Interpolation)
- Park-Transformation und inverse Park-Transformation (Koordinatentransformation Rotor ↔ Stator)
- Schnellen Mikrocontroller oder dedizierter DSP

**Vorteile FOC gegenüber 6-Schritt**:
- Wirkungsgrad um 5–15 % besser
- Drehmomentwelligkeit < 1 % vs. ~30 %
- Besseres Anlaufmoment
- Geringere Motorerwärmung

## Vergleich DC-Motor / BLDC

| Eigenschaft | DC-Motor (Bürsten) | BLDC |
|---|---|---|
| Kommutierung | Mechanisch (Bürsten) | Elektronisch |
| Verschleiss | Bürsten, Kommutator | Kein |
| Wirkungsgrad | 60–80 % | 85–95 % |
| Ansteuerung | Einfach (H-Brücke) | Komplex (3-Phasen-Treiber) |
| Kosten Motor | Günstig | Höher |
| Leistungsdichte | Mittel | Hoch |
| Wartung | Bürsten tauschen | Wartungsfrei |

## Treiber-ICs und ESC

**Gate-Treiber-ICs** (für diskrete MOSFET-H-Brücken): DRV8305, L6234, IR2110  
**Integrierte Motor-Controller**: DRV8302, MC33035  
**ESC (Electronic Speed Controller)**: Fertige Regler für Drohnen (BLHeli, KISS) — direkt an µC anschliessbar, PWM-Eingang oder DSHOT-Protokoll.

:::tip
Für erste BLDC-Projekte: fertigen ESC nehmen und mit PWM ansteuern. Eigene FOC-Implementierung erst wenn Wirkungsgrad oder Geräusch kritisch sind — dann MCPWM-fähigen Mikrocontroller (STM32, ESP32) und SimpleFOC-Library verwenden.
:::
