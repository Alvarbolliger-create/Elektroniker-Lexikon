---
title: BMS Grundlagen
kategorie: EK
tags: [BMS, batterie, lithium, schutz, SOC, SOH, überspannungsschutz, tiefentladung, thermisches-durchgehen, coulomb-counting, MOSFET-abschaltung]
symbol: —
einheit: —
---

Ein BMS (Battery Management System) schützt Lithium-Akkus vor gefährlichen Betriebszuständen und überwacht den Gesundheitszustand der Zellen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Batterietechnik]]
- [[Schutzbeschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[BMS Balancing]]
- [[BMS SOC SOH]]
:::
:::vbox
**Führt weiter zu**
- [[BMS Balancing]]
:::
:::

---

## Warum braucht man ein BMS?

Lithium-Zellen sind empfindlich. Überladen, Tiefentladen oder zu hoher Strom können die Zelle dauerhaft beschädigen oder zum Thermischen Durchgehen führen.

Ein BMS verhindert das durch Überwachung und aktives Trennen des Stromkreises.

## Schutzfunktionen

- **Überspannungsschutz**: Trenn die Ladung wenn eine Zelle über ca. 4.2 V steigt
- **Unterspannungsschutz**: Trenn die Last wenn eine Zelle unter ca. 2.5-3.0 V fällt
- **Überstromerkennung**: Schaltet bei zu hohem Entlade- oder Ladestrom ab
- **Kurzschlussschutz**: Reagiert innerhalb von Mikrosekunden
- **Temperaturschutz**: Laden und Entladen bei tiefen Temperaturen verboten

## Topologie

Das BMS misst jede Zelle einzeln. Bei einem 4S-Akku (4 Zellen in Reihe) werden 4 Zellspannungen und typisch 1-2 Temperaturen überwacht.

Die Abschaltung erfolgt über MOSFETs im Lade- und Entladepfad.

## SOC und SOH

**SOC** (State of Charge): Ladezustand in %. Wird aus Spannung und Integration des Stroms (Coulomb-Counting) berechnet.

**SOH** (State of Health): Alterungszustand. Vergleich der tatsächlichen Kapazität mit der Nennkapazität. Sinkt über die Lebensdauer.

:::warning
Ein BMS ohne Balancing-Funktion schützt zwar die Zellen, gleicht aber keine Unterschiede zwischen den Zellen aus. Bei langen Laufzeiten driften Zellen auseinander und die Gesamtkapazität sinkt.
:::
