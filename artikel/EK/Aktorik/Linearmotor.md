---
title: Linearmotor
kategorie: EK
tags: [linearmotor, linearbewegung, linearachse, positionierung, cnc, synchronmotor, encoder]
symbol: F
einheit: N
---

Ein Linearmotor erzeugt direkt eine lineare Kraft und Bewegung, ohne Umweg über Spindel, Zahnstange oder Riemen. Er wird in Präzisions-Positioniersystemen, Linearschiebern und Fertigungsanlagen eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[DC Motor]]
- [[Servomotor]]
:::
:::vbox
**Verwandte Artikel**
- [[Magnetventil]]
- [[Aktor mit Rückmeldung]]
:::
:::vbox
**Führt weiter zu**
- [[Frequenzumrichter]]
:::
:::

---

## Wirkprinzip

Ein Linearmotor ist ein "aufgerollter" Rotationsmotor. Statt Rotor und Stator im Kreis gibt es einen linearen Primärteil (Wicklung, bewegt sich) und eine lineare Sekundärschiene (Permanentmagnete, ortsfest). Das Wechselmagnetfeld im Primärteil zieht diesen entlang der Schiene — ähnlich wie das Drehmoment im Rotationsmotor, hier als Schubkraft.

---

## Typen

| Typ | Prinzip | Einsatz |
|---|---|---|
| Synchron-Linearmotor | Permanentmagnet-Schiene | Präzisions-CNC, Halbleiterfertigung |
| Asynchron-Linearmotor | Leitfähige Reaktionsschiene | Förderanlagen, Magnetschwebebahn |
| Linearschrittmotor | Schrittweise lineare Bewegung | Einfache Positionierung |
| Tauchanker-Solenoid | Kurzer Hub, hohe Kraft | Ventile, Stempel, Verriegelungen |

---

## Vorteile gegenüber Spindelantrieb

| Eigenschaft | Linearmotor | Spindelantrieb |
|---|---|---|
| Mechanisches Spiel | Keines | Umkehrspiel möglich |
| Dynamik | Sehr hoch | Durch Massenträgheit limitiert |
| Verschleiss | Kein (berührungslos) | Spindel und Lager verschleissen |
| Positionsmessung | Linearer Encoder direkt | Drehencoder + Umrechnung |
| Preis | Hoch | Günstiger |

---

## Positionsmessung

Da keine mechanische Übersetzung vorhanden ist, muss ein Linearmassstab (linearer Encoder) direkt die Position messen. Glasmassstäbe erreichen Auflösungen im Sub-Mikrometer-Bereich.

:::tip
Ohne Positionsrückmeldung ist ein Linearmotor kaum sinnvoll einsetzbar. Er wird praktisch immer mit einem linearen Encoder als [[Aktor mit Rückmeldung]] betrieben.
:::

---

## Anwendungen

- Halbleiterfertigung (Belichtungsanlagen, nm-Genauigkeit)
- Hochgeschwindigkeits-CNC (Fräsen, Laserschneiden)
- Medizintechnik (Pipetierroboter)
- Linearsortierungen und Transfersysteme
- Magnetschwebebahn (Transrapid)
