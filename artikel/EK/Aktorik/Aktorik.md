---
title: Aktorik
kategorie: EK
tags: [aktorik, aktor, aktuator, stellglied, antrieb, wandler, steuerung]
symbol: —
einheit: —
---

Ein Aktor (auch Aktuator oder Stellglied) ist eine Komponente, die ein elektrisches Signal in eine physikalische Wirkung umwandelt: Bewegung, Wärme, Licht, Druck oder Kraft. Aktorik bezeichnet die Technik, Aktoren anzusteuern und in automatisierte Systeme einzubinden.

:::hbox
:::vbox
**Voraussetzungen**
- [[Transistor als Schalter]]
- [[PWM]]
:::
:::vbox
**Verwandte Artikel**
- [[Sensorik]]
- [[Regelkreis]]
:::
:::vbox
**Führt weiter zu**
- [[Aktor mit Rückmeldung]]
- [[Bussystem-Aktor]]
:::
:::

---

## Begriff

Im Regelkreis steht der Aktor am Ende der Signalkette: Sensor erfasst, Steuerung entscheidet, Aktor wirkt. Der Begriff kommt vom lateinischen "agere" (handeln).

---

## Wichtige Aktortypen

| Typ | Wirkung | Beispiele |
|---|---|---|
| [[DC Motor\|Gleichstrommotor]] | Drehbewegung | Lüfter, Pumpen, Antriebe |
| [[Schrittmotor]] | Schrittweise Drehbewegung | CNC, Drucker |
| [[Servomotor]] | Geregelte Drehbewegung | RC-Modelle, Roboter |
| [[Linearmotor]] | Lineare Bewegung | Linearachsen, Positionierung |
| [[Relais]] | Elektrisches Schalten | Steuer-/Leistungskreistrennung |
| [[Magnetventil]] | Fluidfluss öffnen/schliessen | Pneumatik, Hydraulik |
| [[Piezoelektrischer Aktor]] | Feinpositionierung | Mikropositionierung |
| [[Heizelement / Peltier-Element\|Heizelement]] | Wärme | Thermostat, Heizung |
| [[LED-Ansteuerung\|Licht-Aktor]] | Licht | Beleuchtung, Anzeigen |

---

## Steuersignale

| Signal | Einsatz |
|---|---|
| Digital (EIN/AUS) | Relais, Magnetventile, Lampen |
| [[PWM]] | DC-Motoren (Drehzahl), LEDs (Helligkeit), Heizungen |
| Analog (0–10 V, 4–20 mA) | Proportionalventile, Drehzahlsteller |
| Feldbus (KNX, CAN, Modbus) | Gebäude- und Industrieautomation |

---

## Schnittstelle zur Leistungselektronik

Mikrocontroller liefern 3,3 V oder 5 V mit wenigen Milliampere. Die meisten Aktoren brauchen mehr Strom oder eine andere Spannung. Zwischen Logik und Aktor steht immer ein Treiber:

- [[Transistor als Schalter]] für einfache Lasten
- [[H-Brücke]] für Motoren mit Drehrichtungsumkehr
- [[Motor-Treiber-IC]] für fertige integrierte Lösungen
- [[Relais]] für galvanische Trennung

---

## Offener und geschlossener Regelkreis

Ohne Rückmeldung arbeitet der Aktor "blind" — er führt Befehle aus, ohne zu wissen, ob die gewünschte Wirkung erreicht wurde. Mit einem [[Aktor mit Rückmeldung|Sensor als Rückmeldung]] entsteht ein geschlossener Regelkreis und damit die Grundlage für präzise Automatisierung.
