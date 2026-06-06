---
title: Aktorik Grundlagen
kategorie: EK
kapitel: Aktorik
tags: [aktorik, aktor, aktuator, stellglied, pwm, treiber, galvanische trennung, open loop, closed loop, leistungselektronik]
groessen: D|Duty Cycle|—; U_eff|Effektivspannung|V; P|Leistung|W
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[MOSFET Anwendungen]]
- [[BJT Grundlagen]]
- [[Signalverarbeitung Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Relais]]
- [[H-Brücke]]
- [[Regelkreis Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[Relais]]
- [[H-Brücke]]
- [[Heizelement & Peltier]]
- [[Piezo-Aktor]]
:::
:::

---

Ein **Aktor** (Aktuator, Stellglied) wandelt ein elektrisches Signal in eine physikalische Wirkung um: Bewegung, Wärme, Licht, Druck oder Kraft. Aktorik bezeichnet die Technik, Aktoren anzusteuern und in automatisierte Systeme einzubinden.

Im Regelkreis steht der Aktor am Ende der Signalkette:

:::schematic Aktorik Signalkette: Sensor (links) → Regler (Verarbeitung, Sollwert-Vergleich) → Treiber (Leistungsverstärker, Optokoppler) → Aktor (Motor, Heizung, Ventil) → physikalische Wirkung (Bewegung, Wärme, Druck). Rückkopplung: Sensor misst Wirkung → zurück zum Regler (geschlossener Regelkreis)
/Diagramm/aktorik_signalkette.svg
:::

## Aktortypen im Überblick

| Aktor | Wirkung | Ansteuerung |
|---|---|---|
| Relais / Schütz | Elektrisches Schalten | Digital (EIN/AUS) |
| DC-Motor | Drehbewegung | PWM + H-Brücke |
| Schrittmotor | Schrittweise Drehung | Schrittimpulse |
| Servomotor | Geregelte Winkelposition | PWM (1–2 ms Puls) |
| BLDC-Motor | Drehbewegung (bürstenlos) | 3-Phasen-Kommutierung |
| Heizelement | Wärme | PWM oder Phasenanschnitt |
| Peltier-Element | Heizen / Kühlen | PWM + H-Brücke |
| Piezo-Aktor | Feinpositionierung | Hochspannungs-Treiber |
| Magnetventil | Fluidfluss öffnen/schliessen | Digital (EIN/AUS) |
| LED | Licht | PWM (Helligkeit) |

## Steuersignale

| Signal | Beschreibung | Anwendung |
|---|---|---|
| Digital (EIN/AUS) | 0 V oder U_B | Relais, Magnetventile, Lampen |
| PWM | Pulsweitenmodulation, 0–100 % Duty Cycle | Motoren, Heizungen, LEDs |
| Analog (0–10 V) | Stufenlose Spannung | Proportionalventile, Drehzahlsteller |
| 4–20 mA | Stromschleife, störsicher | Industrieaktorik |

**PWM Effektivspannung:**

:::formel
U_eff = U_B * D        # D = Duty Cycle (0..1)
D     = t_on / T       # Einschaltzeit / Periodendauer
:::

## Schnittstelle zur Leistungselektronik

Mikrocontroller liefern 3.3 V oder 5 V bei wenigen Milliampere. Die meisten Aktoren benötigen mehr Strom oder höhere Spannung. Zwischen Logik und Aktor steht immer ein **Treiber**:

| Situation | Treiber |
|---|---|
| Kleine Last (LED, Relais-Spule) | NPN-Transistor oder N-Kanal-MOSFET |
| Motor mit Drehrichtungsumkehr | H-Brücke (4 MOSFETs) |
| Galvanische Trennung nötig | Relais oder Optokoppler |
| Hohe Spannung / Strom | Motor-Treiber-IC (L298N, DRV8833) |
| Netzspannung (230 V) | Solid-State-Relay oder Triac |

## Offener vs. Geschlossener Regelkreis

**Offener Regelkreis (Steuerung)**: Aktor führt Befehl blind aus — keine Rückmeldung ob Wirkung erreicht. Einfach, aber ungenau (Störungen wirken unkorrigiert).

**Geschlossener Regelkreis (Regelung)**: Sensor misst Ist-Wert → Vergleich mit Soll-Wert → Regler korrigiert → Aktor stellt nach. Präzise, kompensiert Störungen.

:::tip
Sobald Präzision gefragt ist (Positionierung, Temperaturhaltung, Drehzahlkonstanz), immer eine Sensorik-Rückmeldung einplanen und den geschlossenen Regelkreis realisieren.
:::
