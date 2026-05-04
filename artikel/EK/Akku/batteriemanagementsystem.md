---
title: Batteriemanagementsystem
kategorie: EK
tags: [bms, schutzschaltung, ueberwachung, telemetrie]
symbol: —
einheit: —
---

Ein Batteriemanagementsystem (BMS) ist die elektronische Steuereinheit eines [[Zellenverbund|Batteriepacks]]. Es ueberwacht die physikalischen Zustaende jeder Einzelzelle, schuetzt den Akku vor schaedlichen Betriebszustaenden und kommuniziert mit externen Systemen wie Ladegeraeten oder Motorsteuerungen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Akku und Batterie]]
- [[Mikrocontroller]]
:::
:::vbox
**Verwandte Artikel**
- [[Shunt-Widerstand]]
- [[Zell-Balancing]]
:::
:::vbox
**Fuehrt weiter zu**
- [[CAN-Bus]]
- [[RS485]]
:::
:::

---

## Messgroessen und Zustandserfassung

Das BMS fungiert als Sensor-Hub und misst in Echtzeit:
* **Einzelzellspannungen:** Die Genauigkeit muss oft im Bereich von Millivolt liegen.
* **Gesamtstrom:** Gemessen ueber einen [[Shunt-Widerstand]] oder einen Hall-Sensor, sowohl beim Laden als auch beim Entladen.
* **Temperatur:** Mehrere NTC-Thermistoren ueberwachen die Zelltemperatur und die Temperatur der Leistungselektronik (MOSFETs) auf der BMS-Platine.

Aus diesen Rohdaten berechnet ein [[Mikrocontroller]] zwei entscheidende Kennwerte:
1. **State of Charge (SOC):** Der aktuelle Ladezustand (0 bis 100 %). Die Berechnung erfolgt meist durch "Coulomb Counting" (Stromintegration ueber Zeit), gestuetzt durch Spannungsabgleich im Ruhezuastand.
2. **State of Health (SOH):** Der Alterungszustand. Er vergleicht die aktuell maximal nutzbare Kapazitaet mit der werksseitigen Nennkapazitaet.

## Sicherheit und Schutzfunktionen

Die wichtigste Aufgabe des BMS ist die Praevention von Zellzerstoerung und Braenden. Ueberschreitet ein Wert die Limits, trennt das BMS den Akku ueber Leistungs-MOSFETs oder Schuetze vom restlichen System.

| Schutzfunktion | Beschreibung | Gefahr bei Ausfall |
|---|---|---|
| **OVP (Over-Voltage Protection)** | Abschaltung bei Ueberschreiten der Ladeschlussspannung. | Thermisches Durchgehen (Brand), Explosion. |
| **UVP (Under-Voltage Protection)** | Abschaltung bei Unterschreiten der Entladeschlussspannung. | Irreversible Zerstoerung der Zellchemie, Kupferbruecken. |
| **OCP (Over-Current Protection)** | Schutz vor zu hohen Entlade- (OCD) oder Ladestroemen (OCC) sowie Kurzschluessen. | Schmelzende Kabel, Zellbrand, Platinenschaeden. |
| **OTP/UTP (Temperature Protection)**| Verhindert Laden bei Frost (Gefahr von Lithium-Plating) oder Betrieb bei Ueberhitzung. | Rapide Alterung, interner Kurzschluss, Brand. |

:::danger
Fallen diese Schutzmechanismen (insbesondere OVP) bei Lithium-Ionen-Akkus aus, kann es zum unkontrollierbaren "Thermal Runaway" kommen. Ein dadurch entstandener Brand liefert seinen eigenen Sauerstoff und ist kaum zu loeschen.
:::

## BMS-Kommunikation

Moderne "Smart BMS" agieren nicht isoliert, sondern teilen ihre Daten mit der Applikation.
* **CAN-Bus:** Industriestandard. Das BMS teilt dem Wechselrichter oder Motorcontroller beispielsweise mit, wie viel Strom aktuell maximal aufgenommen oder abgegeben werden darf (Charge/Discharge Current Limits).
* **RS485 / Modbus:** Sehr verbreitet in stationaeren Heimspeichersystemen (Photovoltaik) fuer die Kommunikation ueber laengere Kabelstrecken.
* **Bluetooth / UART:** Dient hauptsaechlich der Parametrierung durch den Hersteller oder der Diagnose durch den Endanwender per Smartphone-App.