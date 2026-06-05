---
title: Piezoelektrischer Aktor
kategorie: EK
tags: [piezo, piezoelektrisch, piezoaktor, mikropositionierung, pzt, hysterese, hochspannung, kondensator]
symbol: —
einheit: m
---

Ein piezoelektrischer Aktor verformt sich bei angelegter Spannung minimal, aber exakt und schnell. Er wird in Feinmechanik, Mikropositionierung und Mikro-Ventilen eingesetzt, wo normale Motoren zu grob oder zu langsam sind.

:::hbox
:::vbox
**Voraussetzungen**
- [[Kondensator]]
- [[Elektrische Grundgrössen]]
:::
:::vbox
**Verwandte Artikel**
- [[Linearmotor]]
- [[Aktorik]]
:::
:::vbox
**Führt weiter zu**
- [[Aktor mit Rückmeldung]]
:::
:::

---

## Piezoelektrischer Effekt

Piezoelektrische Materialien (typisch PZT — Bleizirkonat-Titanat) verändern ihre Abmessungen bei angelegter Spannung. Der Effekt ist umkehrbar: Mechanischer Druck erzeugt eine Spannung (Sensor-Modus).

:::formel
delta_L = d_33 * U
:::

:::formel
delta_L = Längenänderung [m]
d_33    = Piezokoeffizient [m/V]  (typisch 100–600 pm/V)
U       = Spannung [V]
:::

Bei einem einfachen Element: wenige Nanometer Ausdehnung. Stack-Aktoren (viele Schichten übereinander) addieren die Einzelhübe.

---

## Aufbau

| Typ | Hub | Kraft | Spannung |
|---|---|---|---|
| Einfaches Element | < 1 µm | Sehr hoch | bis 1000 V |
| Stack-Aktor | bis 200 µm | 100 N – 10 kN | 100–200 V |
| Bimorph (Biegeaktor) | bis 1 mm | Gering | 10–100 V |

Stack-Aktoren schichten viele dünne Keramikscheiben übereinander. Bei 100 Schichten à 10 µm ergibt sich 1 mm Hub.

---

## Elektrische Eigenschaften

Ein Piezoaktor verhält sich elektrisch wie ein Kondensator. Im Gleichgewicht fliesst kein Strom. Zum Verfahren muss die Kapazität geladen werden:

:::formel
Q = C * U
I = C * dU/dt
:::

Hohe Beschleunigungen erfordern hohen Ladestrom. Spezielle Hochvolt-Treiber-ICs (z.B. Texas Instruments OPA454, Piezo-Controller) liefern schnelle Spannungsänderungen mit ausreichend Strom.

:::warning
Stack-Aktoren brauchen Hochspannung (100–1000 V). Nur zugelassene Hochvolt-Treiber verwenden. Standardlogik und Low-Voltage-ICs sind nicht geeignet.
:::

---

## Hysterese und Kriechen

Piezoaktoren zeigen:
- **Hysterese**: Die Position hängt von der Bewegungsgeschichte ab (typisch 10–15 % des Hubs)
- **Kriechen**: Nach einer Spannungsänderung verformt sich das Material noch Sekunden bis Minuten weiter

Für hochgenaue Positionierung ist ein Sensor zur Rückkopplung (z.B. kapazitiver Abstandssensor) und ein Regler nötig.

---

## Anwendungen

- Optik: Piezo-Verschiebetische, Interferometer, Fokussierung
- Tintenstrahldrucker: Piezo-Druckkopf
- Ultraschall: Schwinger für Reinigung, Schweissen, Sonar
- Mikrofluidik: Pumpen und Ventile in der Laborautomation
- Aktive Schwingungsdämpfung
