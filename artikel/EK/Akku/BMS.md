---
title: BMS — Batteriemanagementsystem
kategorie: EK
kapitel: Akku
tags: [bms, batteriemanagementsystem, ovp, uvp, ocp, otp, soc, soh, coulomb-counting, thermal-runaway, mosfet-schalter, can-bus, shunt, hall-sensor, schutzfunktion]
groessen: SOC|State of Charge|%; SOH|State of Health|%; U_Zelle|Einzelzellspannung|V; I_Pack|Packstrom|A; T|Temperatur|°C
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Akku Grundlagen]]
- [[MOSFET Anwendungen]]
- [[Hall-Sensor]]
:::
:::vbox
**Verwandte Artikel**
- [[Zell-Balancing]]
- [[NTC & PTC Thermistoren]]
:::
:::vbox
**Führt weiter zu**
- [[Zell-Balancing]]
- [[Regelkreis Grundlagen]]
:::
:::

---

Ein Batteriemanagementsystem (BMS) ist die elektronische Steuereinheit eines Akkupacks. Es überwacht alle Einzelzellen, schützt den Akku vor schädlichen Betriebszuständen und kommuniziert mit Ladegerät und Verbraucher.

## Messgrößen

Das BMS erfasst in Echtzeit:

| Messgrösse | Sensor | Genauigkeit |
|---|---|---|
| Einzelzellspannungen | Differenz-ADC, dedizierter IC (z.B. BQ76940) | ±1–5 mV |
| Gesamtstrom (Laden + Entladen) | Shunt-Widerstand oder Hall-Sensor | ±0.5–2 % |
| Temperatur (Zellen + MOSFETs) | NTC-Thermistoren | ±1–2 °C |

## Zustandsgrößen: SOC und SOH

Aus den Rohmesswerten berechnet der Mikrocontroller:

**SOC (State of Charge)** — aktueller Ladezustand in %:

:::formel
SOC = SOC_initial + (1 / C_Ah) * integral(I, dt)    # Coulomb Counting
:::

Coulomb Counting integriert den Strom über Zeit. Regelmässige Kalibrierung über die Ruhespannung (OCV — Open Circuit Voltage) korrigiert den Drift.

**SOH (State of Health)** — Alterungszustand in %:

:::formel
SOH = C_aktuell / C_nenn * 100 %    # aktuelle Kapazität vs. Nennkapazität
:::

Ein SOH < 80 % gilt als Ende der Nutzungszeit für Fahrzeugbatterien (Garantiegrenze).

## Schutzfunktionen

Die wichtigste Aufgabe des BMS ist die Prävention von Zellzerstörung. Überschreitet ein Wert die Limits, trennt das BMS den Akku über Leistungs-MOSFETs oder Schütze vom System:

| Funktion | Kürzel | Auslöser | Gefahr bei Ausfall |
|---|---|---|---|
| Überspannungsschutz | OVP | Zellspannung > U_max | Thermal Runaway, Brand, Explosion |
| Unterspannungsschutz | UVP | Zellspannung < U_min | Irreversible Zellzerstörung, Kupferbrücken |
| Überstromschutz Entladen | OCD | I > I_max_entladen | Zellbrand, Kabelschmelze |
| Überstromschutz Laden | OCC | I > I_max_laden | Lithium-Plating, Dendritenbildung |
| Kurzschlussschutz | SCP | I >> I_max (sofort) | Zellbrand, Platinenschaden |
| Übertemperaturschutz | OTP | T > T_max | Rapide Alterung, interner Kurzschluss |
| Untertemperaturschutz | UTP | T < T_min_laden | Lithium-Plating beim Laden bei Frost |

:::warning
Fällt OVP bei Li-Ion-Zellen (NMC/NCA) aus, kann **Thermal Runaway** eintreten: unkontrollierbare exotherme Reaktion, die sich selbst beschleunigt. Ein dadurch entstandener Brand liefert seinen eigenen Sauerstoff — er ist kaum zu löschen. LFP-Chemie ist davon weitgehend frei.
:::

## Leistungs-MOSFETs als Schalter

Das BMS unterbricht den Strom mit N-Kanal-MOSFETs in Serie zum Strompfad:

:::schematic BMS MOSFET-Schalter im Strompfad: Akku (+) → MOSFET_Entladen (N-Kanal, Gate via BMS-IC gesteuert) → MOSFET_Laden (N-Kanal, Gate via BMS-IC) → Last / Ladegerät. Shunt-Widerstand R_sense in Serie für Strommessung. BMS-Mikrocontroller misst: Einzelzellspannungen, Packstrom (über Shunt), NTC-Temperaturen. Gate-Signale steuern Lade-/Entlade-MOSFET unabhängig
/Diagramm/bms_mosfet_schalter.svg
:::

Zwei MOSFETs in Reihe (einer für Laden, einer für Entladen) ermöglichen:
- **Nur entladen**: Lade-MOSFET sperrt → kein Rückstrom ins Ladegerät
- **Nur laden**: Entlade-MOSFET sperrt → kein Strom zur Last
- **Beides gesperrt**: Vollständige Trennung (Kurzschluss, Übertemperatur)

## BMS-Kommunikation

| Schnittstelle | Einsatz |
|---|---|
| CAN-Bus | Fahrzeuge, Industriespeicher: BMS teilt Ladegrenzen mit Wechselrichter/Motorcontroller |
| RS485 / Modbus | Heimspeicher (PV), lange Kabelstrecken |
| SMBus / I²C | Laptop-Akkus, kleine Geräte |
| Bluetooth / UART | Parametrierung, Diagnose per Smartphone-App |

:::tip
Ein "Smart BMS" mit CAN-Kommunikation kann dem Ladegerät dynamisch sagen, wie viel Strom gerade aufgenommen werden darf (z.B. bei hoher Temperatur: Ladestrom reduzieren). Das schont die Zellen deutlich besser als ein einfaches Ein/Aus-BMS.
:::
