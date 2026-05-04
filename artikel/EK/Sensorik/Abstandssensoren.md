---
title: Abstandssensoren
kategorie: EK
tags: [abstandssensor, ultraschall, IR, TOF, LIDAR, näherungsschalter, HC-SR04, VL53L0X, induktiv, kapazitiv, triangulation]
symbol: —
einheit: m, mm
---

Abstandssensoren messen den Abstand zu einem Objekt ohne Berührung. Das Messprinzip bestimmt Reichweite, Genauigkeit und welche Objekte erkannt werden.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale]]
- [[Mikrocontroller]]
:::
:::vbox
**Verwandte Artikel**
- [[Temperatursensoren]]
- [[DMS]]
:::
:::

---

## Ultraschall (HC-SR04)

Sendet einen Ultraschallimpuls aus und misst die Laufzeit des Echos.

:::formel
Abstand = Laufzeit × Schallgeschwindigkeit / 2
:::
Reichweite: 2 cm bis 4 m. Günstig (unter 2 CHF). Funktioniert mit den meisten Oberflächen. Problem: schräge Flächen reflektieren am Sensor vorbei.

## IR-Distanz (Sharp GP2Y)

Triangulationsverfahren: IR-LED sendet Strahl, der auf ein Objekt trifft. Rückgestreutes Licht trifft abhängig vom Abstand auf verschiedene Stellen eines Positionssensors.

Reichweite: 10-80 cm. Ausgabe: analoge Spannung. Nicht linear, Kennlinie aus Datenblatt verwenden.

## Time of Flight (TOF)

Misst Laufzeit von Lichtpulsen (Laser oder IR). Sehr genau, kompakt.

VL53L0X/VL53L1X (STMicroelectronics): I2C-Sensor, 2 mm Genauigkeit bis 2 m. Weit verbreitet in Smartphones (Autofokus).

## LiDAR

Rotierende oder phased-array Laserscanner mit TOF. 2D- oder 3D-Abstandskarte. Teuer aber sehr präzise. In autonomen Fahrzeugen, Robotern, Industrie.

Einstieg: RPLIDAR A1 (unter 100 CHF), 2D, 12 m Reichweite.

## Induktive Näherungsschalter

Erkennen metallische Objekte durch Wirbelstromverluste in einer Spule. Kein Messwert, nur Schaltausgang. Sehr robust, für Industrie. Keine Glasscheiben oder Kunststoff dazwischen.

## Kapazitive Näherungsschalter

Erkennen jedes Material durch Kapazitätsänderung. Auch durch nichtleitende Materialien. Sensibel für Feuchtigkeit.
