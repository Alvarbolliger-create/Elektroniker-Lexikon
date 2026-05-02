---
title: Übersprechen (Crosstalk)
kategorie: EK
tags: [Crosstalk, Übersprechen, NEXT, FEXT, PCB, Kopplung, Signalintegrität]
symbol: —
einheit: dB
---

Übersprechen entsteht wenn ein Signal auf eine benachbarte Leitung koppelt. Bei schnellen Signalen und dichten Layouts kann das zu Bitfehlern führen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signalintegrität]]
- [[PCB Aufbau]]
:::
:::vbox
**Verwandte Artikel**
- [[Wellenwiderstand]]
:::
:::

---

## Ursache

Elektrische und magnetische Felder um eine Leiterbahn induzieren Ströme in benachbarte Leitungen. Dieser Effekt nimmt mit steigender Frequenz und steigendem Strom zu.

Kapazitive Kopplung: Das E-Feld koppelt Spannungsänderungen.  
Induktive Kopplung: Das B-Feld koppelt Stromänderungen.

## NEXT und FEXT

**NEXT (Near-End Crosstalk)**: Gemessen am gleichen Ende wie der Sender. Oft stärker.

**FEXT (Far-End Crosstalk)**: Gemessen am gegenüberliegenden Ende. Wichtig bei langen parallelen Leitungen.

## Einflussparameter

- **Abstand**: Crosstalk nimmt mit zunehmendem Abstand quadratisch ab
- **Parallele Länge**: Längerer paralleler Verlauf = mehr Crosstalk
- **Rückstromführung**: Massefläche unter der Leitung reduziert Feld
- **Frequenz**: Höhere Frequenz = mehr Kopplung

## Massnahmen

**Abstand vergrössern**: 3H-Regel: Abstand zur benachbarten Leitung mindestens 3× der Substratdicke.

**Massefläche**: Durchgehende Kupferfläche unter Hochgeschwindigkeitsleitungen. Gibt dem Strom einen definierten Rückweg direkt unter der Signalleitung.

**Differentiell**: Statt einer Leitung zwei komplementäre Leitungen eng nebeneinander. Das gemeinsame Feld ist aussen minimal.

**Leitungen orthogonal kreuzen**: Wenn Leitungen auf verschiedenen Lagen geführt werden, senkrecht kreuzen statt parallel verlaufen.

**Länge begrenzen**: Parallele Leitungsführung so kurz wie möglich halten. Bei Clock-Signalen besonders kritisch.
