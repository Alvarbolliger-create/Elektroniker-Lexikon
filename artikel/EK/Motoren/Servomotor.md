---
title: Servomotor
kategorie: EK
tags: [servo, positionsregelung, encoder, BLDC, servoantrieb, lageregelung, hobby-servo, PWM, industrie-servo]
symbol: M
einheit: —
---

Ein Servomotor ist kein eigener Motortyp, sondern ein geregelter Antrieb. Motor, Encoder und Regler bilden zusammen ein lagegeregeltes System.

:::hbox
:::vbox
**Voraussetzungen**
- [[BLDC Motor]]
- [[PID Regler]]
- [[Encoder]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[Frequenzumrichter]]
:::
:::

---

## Was macht einen Servo aus?

Ein Servomotor hat immer drei Komponenten:
1. Motor (meist BLDC oder DC)
2. Encoder oder Resolver für die Rückmeldung der Position
3. Regler (Lageregelung, Drehzahlregelung, Stromregelung)

Die Regelung sorgt dafür, dass der Motor genau die gewünschte Position oder Drehzahl hält, auch gegen Last.

## Hobby-Servo

Kleines Gerät mit eingebautem DC-Motor, Getriebe und Elektronik. Angesteuert über PWM-Signal:
- 1 ms Pulsbreite = eine Endlage
- 1.5 ms = Mitte
- 2 ms = andere Endlage

Typischer Drehbereich: 180 Grad. Weit verbreitet in Modellbau und einfacher Robotik.

## Industrie-Servo

AC-Servo oder BLDC-Servo mit Sinuskommutierung. Encoder mit hoher Auflösung (oft 17-23 Bit pro Umdrehung). Kommunikation über EtherCAT, Profibus, CANopen oder proprietäre Protokolle.

Eigenschaften:
- Präzise Positionierung (unter 0.01 Grad)
- Hohe Dynamik (schnelle Beschleunigung)
- Drehmomentregelung

## Servo vs. Schrittmotor

| Eigenschaft | Schrittmotor | Servo |
|---|---|---|
| Rückmeldung | keine (open loop) | Encoder (closed loop) |
| Schrittverlust | möglich | erkannt und korrigiert |
| Kosten | günstig | teurer |
| Einsatz | einfache Positionierung | hochgenaue Anwendungen |
