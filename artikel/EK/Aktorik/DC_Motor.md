---
title: Elektromotor (Gleichstrommotor)
kategorie: EK
tags: [dc-motor, gleichstrommotor, pwm, drehzahl, drehmoment, kommutator, anlaufstrom, bürstenmotor, h-brücke]
symbol: M
einheit: —
---

Der Gleichstrommotor (DC-Motor) wandelt elektrische Energie in mechanische Drehbewegung um. Spannung bestimmt die Drehzahl, Strom das Drehmoment; die Drehrichtung folgt der Polarität.

:::hbox
:::vbox
**Voraussetzungen**
- [[PWM]]
- [[Transistor als Schalter]]
:::
:::vbox
**Verwandte Artikel**
- [[H-Brücke]]
- [[Motor-Treiber-IC]]
- [[Schrittmotor]]
:::
:::vbox
**Führt weiter zu**
- [[Aktor mit Rückmeldung]]
- [[Frequenzumrichter]]
:::
:::

---

## Aufbau

Ein DC-Motor besteht aus Stator (Feldmagnet, aussen) und Rotor (Anker, innen). Kommutator und Kohlebürsten sorgen dafür, dass der Ankerstrom immer so umgekehrt wird, dass das Drehmoment konstant in dieselbe Richtung wirkt.

Bürsten und Kommutator sind Verschleissteile (typisch 500–3000 h). Bürstenlose Motoren ([[BLDC]]) haben keine mechanischen Verschleissteile, brauchen aber eine komplexere elektronische Kommutierung.

---

## Drehzahlregelung mit PWM

Pulsweitenmodulation (PWM) stellt die effektive Motorspannung ein:

:::formel
U_eff = U_VCC * D
n ≈ U_eff * k
:::

:::formel
D    = Duty Cycle  0 ... 1
k    = Motorkonstante [U/min per V]  (aus Datenblatt)
:::

Typische PWM-Frequenz: 10–50 kHz. Die Motorinduktivität glättet den Strom.

---

## Drehmoment und Anlaufstrom

Das Drehmoment ist proportional zum Strom. Im Stillstand ist die Gegen-EMF null — der Anlaufstrom ist maximal:

:::formel
M = k_t * I
I_anlauf = U / R_A
:::

:::formel
k_t   = Drehmomentkonstante [Nm/A]
R_A   = Ankerwiderstand [Ω]
:::

Der Anlaufstrom kann 5–10× den Nennstrom erreichen. Treiberelektronik muss diesen kurzzeitig liefern können.

:::warning
Blockierten Motor sofort abschalten: Im Stillstand fliesst dauerhaft der volle Ankerstrom, der Motor überhitzt schnell.
:::

---

## Drehrichtungsumkehr

Für Drehrichtungsumkehr muss die Polarität am Motor gewechselt werden. Dazu ist eine [[H-Brücke]] nötig. Ein einzelner Transistor erlaubt nur einen Drehsinn.

---

## Wichtige Kenngrössen

| Parameter | Bedeutung |
|---|---|
| Nennspannung | Betriebsspannung für Nennbetrieb |
| Leerlaufdrehzahl | Drehzahl ohne Last bei Nennspannung |
| Anlaufstrom | Strom beim Start (typisch 5–10× Nennstrom) |
| Nenndrehmoment | Dauerhaft zulässiges Drehmoment |
| Wirkungsgrad | Typisch 60–80 % |

---

## Treiberelektronik

- Einfacher Transistor: Nur eine Drehrichtung, kein Bremsen
- [[H-Brücke]]: Beide Richtungen, Bremsen möglich
- [[Motor-Treiber-IC]]: Fertige Lösung mit integrierten Schutzschaltungen

:::tip
Für die meisten Projekte reicht ein fertiger Motor-Treiber-IC (z.B. TB6612FNG, DRV8833). Freilaufdioden, Schutzschaltungen und PWM-Logik sind bereits integriert.
:::
