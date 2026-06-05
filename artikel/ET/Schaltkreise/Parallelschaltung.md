---
title: Parallelschaltung
kategorie: ET
tags: [parallelschaltung, gesamtwiderstand, teilstrom, leitwert, stromteiler]
groessen: R|Widerstand|Ohm; G|Leitwert|S; U|Spannung|V; I|Strom|A
_status: PORT  # ET_alt/Schaltkreise/Parallelschaltung.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Reihenschaltung]]
- [[Kirchhoffsche Gesetze]]
:::
:::vbox
**Führt weiter zu**
- [[Spannungs- & Stromteiler]]
:::
:::

---

Bei der Parallelschaltung liegen alle Widerstände an derselben Spannung. Der Gesamtstrom teilt sich auf die Zweige auf — je kleiner der Widerstand eines Zweigs, desto grösser sein Anteil am Strom.

:::schematic
/schaltplaene/schaltkreise/parallelschaltung.svg
:::

## Spannung

An allen parallel geschalteten Widerständen liegt dieselbe Spannung.

:::formel
U = U1 = U2 = U3
:::

## Gesamtwiderstand

Die Kehrwerte der Widerstände addieren sich:

:::formel
1 / R_ges = 1 / R1 + 1 / R2 + 1 / R3
:::

**Merkmal**: R_ges ist immer kleiner als der kleinste Einzelwiderstand.

:::monospace
Beispiel: R1 = 100 Ohm, R2 = 200 Ohm, U = 12 V
1/R_ges = 1/100 + 1/200 = 0.010 + 0.005 = 0.015
R_ges = 1 / 0.015 = 66.7 Ohm
I_ges = 12 / 66.7 = 180 mA
:::

## Teilströme

Jeder Zweig zieht einen Strom entsprechend seinem Widerstand. Der Gesamtstrom ist die Summe aller Teilströme (Knotenregel).

:::formel
I_ges = I1 + I2 + I3
:::

:::formel
I_k = U / R_k    # Strom im Zweig k
:::

:::monospace
Fortsetzung Beispiel:
I1 = 12 / 100 = 120 mA
I2 = 12 / 200 = 60 mA
I_ges = 120 + 60 = 180 mA ✓
:::

## Besonderheiten

**Kurzschluss in einem Zweig**: R_ges = 0, Gesamtstrom → sehr gross. Alle anderen Zweige sind wirkungslos, da die Spannung an ihnen auf 0 V zusammenbricht — wichtig für Sicherungsauslegung.

**Unterbrechung in einem Zweig**: Dieser Zweig trägt keinen Strom, die anderen arbeiten normal weiter. R_ges steigt etwas.

:::tip
Parallelschaltungen sind die Grundlage jedes Netzteil-Busses: Alle Verbraucher liegen parallel an derselben Versorgungsspannung und ziehen ihren Strom unabhängig voneinander.
:::

## Gemischte Schaltung (Reihe + Parallel)

Reale Schaltungen kombinieren beide Typen. Die Lösungsmethode ist immer dieselbe: schrittweise Gruppen zu einem Ersatzwiderstand zusammenfassen, bis eine einfache Reihenschaltung übrig bleibt.

**Vorgehen:**
1. Innerste Parallel- oder Reihengruppe identifizieren
2. Ersatzwiderstand R_ers berechnen
3. R_ers an Stelle der Gruppe einsetzen
4. Wiederholen bis nur noch ein Gesamtwiderstand R_ges übrig ist
5. Gesamtstrom berechnen: I = U / R_ges
6. Rückwärts alle Teilspannungen und Teilströme bestimmen

:::monospace
Beispiel: U = 12 V, R1 = 2 kΩ und R2 = 2 kΩ in Reihe, parallel dazu R3 = 1 kΩ

Schritt 1: R1 + R2 in Reihe → R_12 = 2 + 2 = 4 kΩ
Schritt 2: R_12 parallel R3 → R_ges = (4 * 1) / (4 + 1) = 0.8 kΩ = 800 Ω
Schritt 3: I_ges = 12 / 800 = 15 mA
Schritt 4: U_R3 = 12 V (liegt direkt parallel zur Quelle)
           I_R3  = 12 / 1000 = 12 mA
           I_R12 = 12 / 4000 = 3 mA
           U_R1  = 3e-3 * 2000 = 6 V,  U_R2 = 6 V
Probe: I_R3 + I_R12 = 12 + 3 = 15 mA = I_ges ✓
:::

:::tip
**Strategie für unübersichtliche Schaltungen**: Schaltung neu zeichnen mit allen Knoten markiert. Bauteile zwischen denselben zwei Knoten liegen parallel, Bauteile in einem einzigen Strompfad liegen in Reihe.
:::
