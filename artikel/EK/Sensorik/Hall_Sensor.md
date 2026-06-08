---
title: Hall-Sensor
kategorie: EK
kapitel: Sensorik
tags: [hallsensor, halleffekt, hallspannung, magnetfeld, magnetische flussdichte, lorentzkraft, strommessung, drehzahl, bldc, kommutierung, acs712, linear, digital]
groessen: U_H|Hallspannung|V; B|Magnetische Flussdichte|T; I|Steuerstrom|A; d|Schichtdicke|m; R_H|Hallkoeffizient|m³/C
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sensorik Grundlagen]]
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Lichtsensor]]
- [[NTC & PTC Thermistoren]]
:::
:::vbox
**Führt weiter zu**
- [[BLDC-Motor]]
- [[DC-Motor]]
- [[Regelkreis Grundlagen]]
:::
:::

---

Ein Hall-Sensor misst **Magnetfelder ohne mechanischen Kontakt**. Basis ist der Halleffekt: ein stromdurchflossener Halbleiter in einem Magnetfeld erzeugt eine Querspannung — die Hallspannung U_H.

## Physikalisches Prinzip (Halleffekt)

:::schematic Hall-Effekt Grundprinzip: Rechteckiger Halbleiter-Plättchen (Seitenansicht). Steuerstrom I fliesst von links nach rechts (horizontale Richtung). Magnetfeld B steht senkrecht nach oben aus dem Plättchen. Lorentzkraft drängt Elektronen an die untere Kante. Oben: Elektronenmangel (positiv), Unten: Elektronenüberschuss (negativ). Hallspannung U_H = R_H × I × B / d quer zum Strom messbar
/Diagramm/hall_effekt.svg
:::

Ein Steuerstrom I fliesst durch einen dünnen Halbleiter. Ein Magnetfeld B steht senkrecht zur Stromrichtung. Die **Lorentzkraft** drängt die beweglichen Ladungsträger (Elektronen) seitlich ab. Auf der einen Seite sammeln sich Elektronen (negativ), auf der anderen entsteht ein Mangel (positiv). Diese Ladungstrennung erzeugt die **Hallspannung** quer zum Strom.

## Formeln

:::formel
U_H = (R_H * I * B) / d    # Hallspannung
B   = mu_0 * H             # magnetische Flussdichte (µ_0 = 4π × 10⁻⁷ H/m)
:::

| Grösse | Einheit | Bedeutung |
|---|---|---|
| U_H | V | Messbare Ausgangsspannung (typisch µV–mV am Element) |
| R_H | m³/C | Hallkoeffizient (Materialkonstante) |
| I | A | Steuerstrom (konstant gehalten vom IC) |
| B | T | Magnetische Flussdichte (Messgrösse) |
| d | m | Schichtdicke des Halbleiters (dünn → grosses U_H) |

:::info
Die Hallspannung ist sehr klein (µV–mV). Moderne Hall-ICs enthalten Verstärker, Offset-Kompensation (Spinning-Current) und Signalaufbereitung auf dem gleichen Chip.
:::

## Lineare vs. Digitale Hall-Sensoren

**Lineare Hall-Sensoren**: Ausgangsspannung proportional zu B. Für kontinuierliche Messung von Magnetfeld, Strom oder Position.

**Digitale/Schaltende Hall-Sensoren**: Ausgang schaltet bei einem definierten Magnetfeldschwellwert (Operate-Point). Für Drehzahl, Zählen, Endlagen. Intern ist oft ein Schmitt-Trigger mit Hysterese verbaut.

| Typ | Beispiel-IC | Empfindlichkeit | Anwendung |
|---|---|---|---|
| Linear (Strom) | ACS712 | 66–185 mV/A | Strommessung 5–30 A |
| Linear (Feld) | SS49E | 1.4 mV/mT | Magnetfeldmessung |
| Digital schaltend | A3144 | Schwellwert ca. 17 mT | Drehzahl, Endlage |
| 3D-Hallsensor | MLX90393 | X/Y/Z separat | Kompass, 3D-Position |

## Anwendungen

**Galvanisch getrennte Strommessung**: Strom erzeugt ein Magnetfeld um den Leiter. Hall-Sensor misst dieses Feld — kein Widerstand im Stromkreis, kein Energieverlust, galvanische Trennung. Typisch: ACS712 in Serie im Strompfad.

**Drehzahlmessung**: Magnet auf der Welle dreht an einem schaltenden Hall-Sensor vorbei. Jede Flanke entspricht einer Umdrehung (oder einem Zahn bei Zahnrad). Frequenz → Drehzahl.

:::formel
n = f_Pulse / Z_Magnete    # Drehzahl [U/s] = Pulsfrequenz / Anzahl Magnete
:::

**BLDC-Kommutierung**: Drei Hall-Sensoren (je 120° versetzt) um den Rotor detektieren die Rotorposition. Der Motorcontroller nutzt diese 3-Bit-Information um die richtige Wicklungsphase zu aktivieren.

**Endlagendetektierung**: Magnet am beweglichen Teil, Sensor am festen Teil — berührungslos und verschleissfrei.

**Winkelgeber**: Hallsensor unter einem Diametralmagneten liefert Sinus/Kosinus der Winkelposition (Rotationsencoder ohne Schleifringe).

## Praktische Hinweise

:::warning
Hall-Sensoren reagieren auf jedes Magnetfeld in der Umgebung — Stromleitungen, Transformatoren, Lautsprecher. Abstand zu Störquellen einhalten und die Polarität des Magnetfelds beachten: falsch gepolt kehrt der lineare Sensor das Vorzeichen um, der schaltende Sensor spricht nicht an.
:::

**Offsetfehler**: Ohne Magnetfeld ist U_H ≠ 0 (Temperatur- und Fertigungsstreuung). Gute ICs kompensieren dies mit Spinning-Current-Technik: Steuerstrom wird mehrfach gedreht, Offsets gemittelt.

**Schaltbild ACS712 (Strommessung):**

:::schematic ACS712 Strommessung: Strompfad (zu messendes Signal) fliesst durch den ACS712 IC (Pins IP+ und IP−). Innen: Kupferschiene + Hall-Element, galvanisch getrennt von der Ausgangsseite. ACS712 VCC (+5V) und GND. Ausgang OUT (Analogspannung): 0 A → 2.5 V Mitte. +1 A → 2.5 V + 185 mV. −1 A → 2.5 V − 185 mV. Filterkondensator 100 nF an OUT nach GND. Vorteil: Galvanische Trennung zum Messkreis
/Diagramm/acs712_strommessung.svg
:::
