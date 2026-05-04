---
title: DC-Motor
kategorie: EK
tags: [DC-Motor, gleichstrommotor, drehzahl, drehmoment, PWM, kommutator, BEMF, anlaufstrom, bürste, verschleiss, H-brücke]
symbol: M
einheit: —
---

Der DC-Motor wandelt elektrische Energie in Drehbewegung um. Einfach anzusteuern, gut regelbar, weit verbreitet in der Robotik und Automatisierung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Lorentzkraft]]
- [[Relais & Schütze]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[BLDC]]
- [[H-Brücke (Motoransteuerung)]]
:::
:::vbox
**Führt weiter zu**
- [[Regelungstechnik]]
- [[Encoder & Resolver]]
:::
:::

---

## Funktionsprinzip

Spule (Anker) in einem permanenten Magnetfeld. Strom durch die Spule erzeugt eine Kraft (Lorentzkraft). Kommutator kehrt die Stromrichtung beim Drehen um, sodass die Kraft immer in dieselbe Richtung wirkt.

## Drehzahlregelung mit PWM

:::monospace
n ≈ U_motor * k     # Drehzahl proportional zur angelegten Spannung; k aus Datenblatt
:::
PWM (Pulsweitenmodulation) stellt die effektive Spannung ein. Höheres Tastverhältnis D = schnellerer Motor.

Richtungsumkehr: H-Brücke (4 Transistoren) erlaubt beide Richtungen.

## Anlaufstrom

Im Stillstand ist der Gegenstrom (BEMF) null. Der Anlaufstrom kann 5 bis 10× den Nennstrom erreichen. Strombegrenzung beim Anlauf einplanen.

## Bürsten und Verschleiss

Kommutator und Kohlebürsten verschleissen. Typisch 500 bis 3000 Betriebsstunden. Danach Austausch oder Austausch des Motors.

Bürstenloser Motor (BLDC): kein mechanischer Kommutator, kein Verschleiss, besserer Wirkungsgrad. Dafür komplexere Ansteuerung.

## Typische Kenndaten

| Grösse | Einheit | Bedeutung |
|---|---|---|
| Nennspannung | V | Betriebsspannung |
| Nennstrom | A | Strom bei Nennlast |
| Leerlaufdrehzahl | U/min | Drehzahl ohne Last |
| Haltemoment | N·cm | Max. Drehmoment im Stillstand |
| Wirkungsgrad | % | Typisch 60 bis 80 % |

:::tip
H-Brücken-ICs (z.B. L298N, DRV8833, TB6612) integrieren alle nötigen Transistoren und Schutzdioden. Einfacher als diskrete Schaltung und für die meisten Projekte ausreichend.
:::
