---
title: Schrittmotor
kategorie: EK
tags: [schrittmotor, stepper, schritt, mikroschrittbetrieb, positionierung, A4988, DRV8825, TMC, halbschritt, vollschritt, schrittverlust, resonanz]
symbol: M
einheit: °/Schritt
---

Der Schrittmotor dreht sich in definierten Schritten. Jeder Impuls dreht ihn um einen festen Winkel. Keine Rückmeldung nötig für einfache Positionierungsaufgaben.

:::hbox
:::vbox
**Voraussetzungen**
- [[DC-Motor]]
:::
:::vbox
**Verwandte Artikel**
- [[Servomotor]]
:::
:::vbox
**Führt weiter zu**
- [[CNC]]
- [[Positionierung]]
:::
:::

---

## Funktionsprinzip

Mehrere Statorwicklungen werden der Reihe nach bestromt. Das Magnetfeld dreht sich. Der Rotor (Permanentmagnet oder gezahntes Eisen) folgt dem Feld in Schritten.

Typischer Schrittwinkel: 1.8° pro Schritt = 200 Schritte pro Umdrehung.

## Vollschritt vs. Halbschritt vs. Mikroschritt

**Vollschritt**: Immer eine oder zwei Phasen aktiv. 200 Schritte/Umdr. Weniger fein.

**Halbschritt**: Abwechselnd eine und zwei Phasen. 400 Schritte/Umdr. Sanfterer Lauf.

**Mikroschritt**: Ströme sinusförmig moduliert. 1600, 3200, 6400 Schritte/Umdr. oder mehr. Sehr ruhiger Lauf, höhere Auflösung.

## Typen

**Unipolarer Schrittmotor**: Sechs oder acht Leitungen. Einfachere Ansteuerung, weniger Drehmoment.

**Bipolarer Schrittmotor**: Vier Leitungen. Mehr Drehmoment, braucht H-Brücke pro Phase.

## Drehmoment

Schrittmotoren verlieren Drehmoment bei hohen Drehzahlen. Zu schnelle Schrittfolge: der Motor springt aus dem Schritt und verliert die Position (Schrittverlust).

Resonanzfrequenzen beachten: Bei bestimmten Drehzahlen vibriert der Motor stark. Durch Beschleunigungs-Rampen umgehen.

## Treiberchips

A4988, DRV8825, TMC2208 (leise), TMC2209 (mit Diagnosefunktion). Alle integrieren H-Brücken und Mikroschrittteilung.

:::tip
TMC-Treiber verwenden wenn leiser Betrieb wichtig ist. Sie modulieren den Strom so, dass kaum hörbare Frequenzen entstehen (StealthChop). Standard in modernen 3D-Druckern.
:::
