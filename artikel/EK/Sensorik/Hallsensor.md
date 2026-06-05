---
title: Hallsensor
kategorie: EK
tags: [hallsensor, halleffekt, hallspannung, magnetfeld, strom, position]
symbol: —
einheit: V, T
---

Ein Hallsensor misst Magnetfelder ohne mechanischen Kontakt. Er basiert auf dem Halleffekt: ein stromdurchflossener Leiter in einem Magnetfeld erzeugt eine Spannung quer zur Stromrichtung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Lorentzkraft]]
:::
:::vbox
**Verwandte Artikel**
- [[DMS (Dehnmessstreifen)]]
- [[Temperatursensoren]]
:::
:::vbox
**Führt weiter zu**
- [[BLDC Motor]]
- [[DC Motor]]
:::
:::

---

## Halleffekt (Physikalische Grundlage)

Ein stromdurchflossener Leiter (oder Halbleiter) befindet sich in einem Magnetfeld senkrecht zur Stromrichtung. Die Lorentzkraft lenkt die beweglichen Ladungsträger (Elektronen) seitlich ab.

An der einen Seite des Leiters sammeln sich Elektronen (negativ), an der anderen entsteht ein Elektronenmangel (positiv). Diese Ladungstrennung erzeugt eine Spannung quer zur Stromrichtung — die **Hallspannung U_H**.

:::formel
U_H = (R_H * I * B) / d     # R_H = Hallkoeffizient (materialabhängig)
                             # I = Steuerstrom, B = Flussdichte, d = Dicke
:::
:::info
Die Hallspannung ist proportional zur magnetischen Flussdichte B. Das macht den Hallsensor zu einem linearen Magnetfeldsensor.
:::

---

## Formeln

:::formel
U_H = R_H * I * B / d       # Hallspannung; R_H = 1/(q*n) für Elektronen
B   = mu_0 * H              # magnetische Flussdichte; B in Tesla, H in A/m
:::
| Grösse | Symbol | Einheit | Beschreibung |
|---|---|---|---|
| Hallspannung | U_H | V | Messbare Ausgangsspannung |
| Steuerstrom | I | A | Konstant gehalten vom IC |
| Magnetische Flussdichte | B | T | Zu messende Grösse |
| Schichtdicke | d | m | Dünner Halbleiter → höhere U_H |
| Hallkoeffizient | R_H | m³/C | Materialkonstante |

---

## Hallsensor-ICs in der Praxis

Moderne Hallsensoren sind integrierte Schaltungen mit:
- Hall-Element (Halbleiterschicht, meist Silizium oder InAs)
- Verstärker für die sehr kleine Hallspannung (typisch µV bis mV)
- Signalaufbereitung (Analog oder Digital)

**Lineare Hallsensoren**: Ausgangsspannung proportional zu B. Für Strommessung und Positionsmessung.

**Digitale / Schaltende Hallsensoren**: Ausgang schaltet bei einem definierten Magnetfeldschwellwert. Für Drehzahlmessung, Endlagendetektierung, Zähler.

---

## Anwendungen

**Strommessung**: Strom erzeugt ein Magnetfeld. Der Hallsensor misst dieses kontaktlos — galvanische Trennung, kein Widerstand in der Leitung. Typisch: Stromzangen, Leistungsmessung.

**Drehzahl / Winkel**: Magnet auf der Welle dreht an einem Hallsensor vorbei. Jede Flanke = eine Umdrehung (oder ein Zahn). BLDC-Motoren nutzen drei Hallsensoren für die Kommutierung.

**Endlagendetektierung**: Magnet am beweglichen Teil, Sensor am festen Teil. Berührungslos, verschleissfrei.

**Brushless-DC-Motoren (BLDC)**: Drei Hallsensoren um den Rotor bestimmen die Rotorposition. Der Regler nutzt diese Information für die Kommutierung der Motorwicklungen.

---

## Vertiefung

### Typen und Empfindlichkeit

| Sensortyp | Empfindlichkeit | Einsatz |
|---|---|---|
| Linear (z.B. ACS712) | 66–185 mV/A | Strommessung |
| Linear (z.B. SS49E) | 1.4 mV/mT | Magnetfeldmessung |
| Digital schaltend (A3144) | Schwellwert einstellbar | Drehzahl, Endlage |
| 3D-Hallsensor (MLX90393) | X/Y/Z separat | Kompass, 3D-Positionierung |

### Offsetfehler und Kompensation

Das Hall-Element hat einen Offset (ohne Magnetfeld ist U_H ≠ 0). Gute ICs kompensieren diesen Offset durch Spinning-Current-Technik: Der Steuerstrom wird mehrfach gedreht und die Offsets gemittelt.

:::warning
Hallsensoren reagieren auf jedes Magnetfeld in der Nähe — auch auf Stromleitungen, Transformatoren oder Permanentmagnete in Lautsprechern. Immer auf Abstand zu Störquellen achten und die Polarität des Magnetfelds beachten: falsch gepolt liefert der Sensor das falsche Vorzeichen.
:::
