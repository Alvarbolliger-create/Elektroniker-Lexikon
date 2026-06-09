---
title: Brückenschaltung (Wheatstone)
kategorie: ET
tags: [brückenschaltung, wheatstone, abgleich, brückenspannung, messtechnik, dehnmessstreifen, NTC]
groessen: U_br|Brückenspannung|V; U_e|Speisespannung|V; R1|Widerstand 1|Ohm; R2|Widerstand 2|Ohm; R3|Widerstand 3|Ohm; R4|Widerstand 4|Ohm
_status: PORT  # ET_alt/Schaltkreise/Wheatstone_Bruecke.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[Spannungs- & Stromteiler]]
- [[Innenwiderstand & Messfehler]]
- [[Vierleitermessung (Kelvin)]]
:::
:::

---

Die Wheatstone-Brücke ist eine Schaltung aus vier Widerständen, mit der sehr kleine Widerstandsänderungen präzise gemessen werden können. Sie ist die Grundlage für Dehnmessstreifen, Temperatursensoren und Drucksensoren.

## Aufbau

:::schematic
/schaltplaene/schaltkreise/wheatstone_bruecke.svg
:::

Vier Widerstände in einem Viereck (Raute). Die Speisespannung U_e liegt zwischen dem oberen und unteren Knoten. Das Messinstrument (Spannungsmesser) liegt quer zwischen den zwei Seitenknoten — U_br ist die Diagonalspannung.

## Brückenspannung

:::formel
U_br = U_e * (R1 / (R1 + R2) - R3 / (R3 + R4))
:::

Bei Abgleich (U_br = 0) gilt die Abgleichbedingung.

## Abgleichbedingung

Die Brücke ist abgeglichen (U_br = 0), wenn beide Spannungsteilerhälften dasselbe Verhältnis haben:

:::formel
R1 / R2 = R3 / R4    # Abgleichbedingung: beide Hälften gleiches Verhältnis
:::

Anschaulich: Links teilt R1/R2, rechts teilt R3/R4. Wenn beide Teiler gleich sind, liegen Ua und Ub auf demselben Potenzial → U_br = 0.

## Anwendung: Widerstandsmessung

**Abgleichverfahren**: R1, R2, R3 bekannt und fest; R4 ist der unbekannte Messwiderstand. Durch Abgleich (z. B. Verändern von R2 oder R3) auf U_br = 0 lässt sich R4 aus der Abgleichbedingung berechnen. Sehr genaue Methode, da bei U_br = 0 kein Strom durch den Messweg fliesst.

## Anwendung: Sensoren

In der Praxis wird eine Brücke aus drei festen Widerständen und einem Sensor aufgebaut:

| Sensor | Messgrösse | Funktionsprinzip |
|---|---|---|
| Dehnmessstreifen (DMS) | Dehnung, Kraft, Druck | Widerstand ändert sich mit Dehnung |
| NTC/PTC | Temperatur | Widerstand ändert sich mit Temperatur |
| Fotowiderstand (LDR) | Licht | Widerstand ändert sich mit Helligkeit |

**Vorteil gegenüber einfachem Spannungsteiler**: Kleine Widerstandsänderungen (z. B. 0,1 %) erzeugen eine messbare Brückenspannung, weil die Referenzseite exakt kompensiert. Der Offset (Grundspannung) wird herausgekürzt.

:::monospace
Beispiel: U_e = 5 V, R1 = R2 = R3 = 1 kOhm, R4 = 1 kOhm + 10 Ohm (0,1 % Änderung)
Ua = 5 * 1/(1+1) = 2.500 V (feste Seite)
Ub = 5 * 1/(1+1.01) = 2.488 V (Sensorseite)
U_br = 2.500 - 2.488 = 12.5 mV
:::

:::tip
Für noch höhere Empfindlichkeit werden alle vier Brückenwiderstände als Sensoren ausgeführt (Vollbrücke). Zwei gegenüberliegende Widerstände erhöhen ihren Wert, zwei andere erniedrigen ihn — die Ausgangsspannung verdoppelt sich und Temperatureinflüsse auf alle vier Elemente kompensieren sich gegenseitig.
:::
