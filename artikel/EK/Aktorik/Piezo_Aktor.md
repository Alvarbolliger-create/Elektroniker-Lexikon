---
title: Piezo-Aktor
kategorie: EK
kapitel: Aktorik
tags: [piezo, piezoelektrisch, piezoaktor, pzt, stack-aktor, bimorph, hochspannung, hysterese, kriechen, kapazitiv, transimpedanz, treiber]
groessen: delta_L|Längenänderung|m; d_33|Piezokoeffizient|m/V; U|Steuerspannung|V; C_piezo|Kapazität|F; I|Ladestrom|A
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Aktorik Grundlagen]]
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Verwandte Artikel**
- [[H-Brücke]]
- [[Heizelement & Peltier]]
:::
:::vbox
**Führt weiter zu**
- [[Regelkreis Grundlagen]]
:::
:::

---

Ein piezoelektrischer Aktor verformt sich bei angelegter Spannung minimal, aber **exakt und schnell**. Er wird in Feinmechanik, Mikropositionierung und Mikroventilen eingesetzt, wo normale Motoren zu grob oder zu langsam sind.

## Piezoelektrischer Effekt

Piezoelektrische Materialien (typisch PZT — Bleizirkonat-Titanat, Pb[Zr,Ti]O₃) ändern ihre Abmessungen bei angelegter Spannung. Der Effekt ist **umkehrbar**: Mechanischer Druck erzeugt eine Spannung (Sensor-Modus = Piezomikrofon, Gasfeuerzünder).

**Aktor-Modus (inverser Piezoeffekt):**

:::formel
delta_L = d_33 * U    # Längenänderung durch Spannung
:::

| Grösse | Einheit | Typischer Wert |
|---|---|---|
| delta_L | m | nm–µm (je nach Aufbau) |
| d_33 | m/V | 100–600 pm/V (= 0.1–0.6 nm/V) |
| U | V | 10–1000 V (je nach Typ) |

:::info
Bei einem einzelnen PZT-Element mit d_33 = 300 pm/V und U = 100 V ergibt sich delta_L = 30 nm — das ist kleiner als eine Lichtwellenlänge.
:::

## Aufbautypen

| Typ | Hub | Kraft | Spannung | Merkmal |
|---|---|---|---|---|
| Einzelelement | < 1 µm | Sehr hoch | 500–1000 V | Kleinstste Ausdehnung |
| Stack-Aktor | bis 200 µm | 100 N – 10 kN | 100–200 V | Viele Schichten übereinander |
| Bimorph (Biegeaktor) | bis 1 mm | Gering | 10–100 V | Zwei Schichten, biegen sich |

**Stack-Aktor**: Viele dünne Keramikscheiben übereinander gestapelt — die Hübe addieren sich. Bei 100 Schichten à 10 nm/V und 150 V ergibt sich: 100 × 150 × 10 nm = 150 µm.

## Elektrische Eigenschaften

Ein Piezoaktor verhält sich elektrisch wie ein **Kondensator** — im Gleichgewicht fliesst kein Strom. Zum Verfahren muss die Kapazität umgeladen werden:

:::formel
Q = C_piezo * U          # Ladung
I = C_piezo * dU/dt      # Ladestrom (für schnelle Bewegung = hoher Strom)
:::

Typische Kapazitäten: 100 nF–100 µF. Hohe Beschleunigungen erfordern hohen Ladestrom → spezielle Hochvolt-Treiber-ICs.

:::warning
Stack-Aktoren benötigen Hochspannung (100–1000 V). Nur zugelassene Hochvolt-Treiber verwenden (z.B. Texas Instruments OPA454, MDT piezo controller). Standardlogik und 5-V-ICs sind nicht geeignet.
:::

## Hysterese und Kriechen

Piezoaktoren sind für zwei Nichtidealitäten bekannt:

**Hysterese**: Die Position hängt von der Bewegungshistorie ab. Typisch 10–15 % des maximalen Hubs. Bei Positionierung ohne Rückkopplung verursacht dies einen systematischen Fehler.

**Kriechen (Creep)**: Nach einer Spannungsänderung verformt sich das Material noch Sekunden bis Minuten weiter (logarithmische Zeitabhängigkeit). Ursache: Domänenwanderung im Kristall.

**Lösung für hohe Genauigkeit**: Rückkopplungsregelung mit Positions-Sensor (kapazitiver Abstandssensor, Dehnmessstreifen an der Keramik) und PID-Regler. Gute Piezostages haben integrierten Sensor und Regler.

## Anwendungen

| Anwendung | Details |
|---|---|
| Optik / Interferometrie | Piezo-Verschiebetische, aktive Spiegelsteuerung, Fokussierung |
| Tintenstrahldrucker | Piezo-Druckkopf drückt Tinte aus Düse (Epson) |
| Ultraschall | Schwinger für Reinigung (Ultraschallbad), Schweissen, Sonar |
| Mikrofluidik | Pumpen und Ventile in Laborautomation |
| Aktive Schwingungsdämpfung | Gegenschwingung kompensiert Vibration |
| Autofokus | Kameraobjektive mit piezoelektrischem Antrieb |

:::tip
Im Vergleich zu elektromagnetischen Aktoren (Motor, Relais) hat der Piezoaktor keinen Verschleiss, kein elektromagnetisches Streufeld, keine Geräusche und eine extrem hohe Bandbreite (kHz–MHz). Nachteil: Sehr kleiner Hub, hohe Spannung, begrenzte Kraft beim Bimorph.
:::
