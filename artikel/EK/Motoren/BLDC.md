---
title: BLDC-Motor
kategorie: EK
tags: [BLDC, brushless, EC-Motor, hallsensor, FOC, kommutierung, sensorlos, innenläufer, aussenläufer, ESC, sinus-kommutierung]
symbol: M
einheit: —
---

BLDC (Brushless DC) ist ein permanent erregter Synchronmotor mit elektronischer Kommutierung. Kein Verschleiss durch Bürsten, hoher Wirkungsgrad, hohe Leistungsdichte.

:::hbox
:::vbox
**Voraussetzungen**
- [[DC Motor]]
- [[MOSFET]]
- [[PWM]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[Frequenzumrichter]]
:::
:::vbox
**Führt weiter zu**
- [[FOC]]
- [[Servomotor]]
:::
:::

---

## Aufbau

Der Rotor trägt Permanentmagnete. Der Stator hat Wicklungen in drei Phasen. Es gibt keine Bürsten und keinen Kommutator. Die Bestromung der Phasen übernimmt die Elektronik.

**Innenläufer**: Magnete innen, Stator aussen. Standard für hohe Drehzahlen (Lüfter, Festplatten).  
**Aussenläufer**: Magnete aussen, Stator innen. Hohes Drehmoment bei niedrigen Drehzahlen (Drohnen, Ventilatoren).

## Kommutierung

Um den Rotor anzutreiben, muss die Bestromung der Statorphasen mit der Rotorposition synchronisiert werden.

**Hallsensoren**: Drei Magnetsensoren im Stator erkennen die Rotorposition. Einfach, robust, weit verbreitet.

**Sensorlos**: Position wird aus der Gegen-EMK der nicht bestromten Phase berechnet. Kein Sensor nötig, aber schwieriger zu starten.

## Sechs-Schritt-Kommutierung

Die einfachste Methode: immer zwei von drei Phasen bestromt, sechs Zustände pro Umdrehung. Einfach zu implementieren, aber ruckartig.

## FOC (Field Oriented Control)

Sinusförmige Bestromung aller drei Phasen. Deutlich ruhigerer Lauf, bessere Ausnutzung des Drehmoments, geringere Verluste. Benötigt mehr Rechenleistung.

## Vergleich DC-Motor

| Eigenschaft | Bürstenmotor | BLDC |
|---|---|---|
| Verschleiss | Bürsten, Komm. | keiner |
| Wirkungsgrad | 75-80 % | 85-95 % |
| Ansteuerung | einfach | komplex |
| Wartung | nötig | wartungsfrei |
| Kosten | günstig | höher |

## Treiber-ICs

Fertige Gate-Treiber wie DRV8305, L6234 oder MCU-integrierte Motorcontroller (z.B. STM32 mit Timer-Komplementärausgängen) vereinfachen die Ansteuerung.

:::tip
Für Einsteiger: viele Hobby-BLDC-Regler (ESC) für Drohnen basieren auf dem BLHeli- oder KISS-Protokoll und können direkt an Mikrocontroller angeschlossen werden.
:::
