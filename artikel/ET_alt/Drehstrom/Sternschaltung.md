---
title: Sternschaltung
kategorie: ET
tags: [sternschaltung, drehstrom, neutralleiter, strangspannung, Y-schaltung, stern-dreieck-anlauf, 400V, 230V]
symbol: Y
einheit: —
---

Bei der Sternschaltung sind alle drei Wicklungen oder Lasten an einem gemeinsamen Sternpunkt verbunden. Der Sternpunkt kann mit dem Neutralleiter verbunden sein.

:::hbox
:::vbox
**Voraussetzungen**
- [[Drehstrom: Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Dreieckschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[Verkettete Spannung]]
:::
:::

---

## Aufbau

:::schematic Sternschaltung
/schaltplaene/drehstrom_stern.svg
:::

Drei Wicklungen oder Lasten. Ein Ende jeder Wicklung am Aussenleiter (L1, L2, L3). Das andere Ende aller drei am gemeinsamen Sternpunkt N.

Symbol: Y

## Spannungsverhältnisse

:::formel
U_verkettet = sqrt(3) * U_strang     # verkettete Spannung aus Strangspannung
:::
Im Netz: U_strang = 230 V, U_verkettet = 400 V.

Strangspannung ist die Spannung von einem Aussenleiter zum Neutralleiter.
Verkettete Spannung ist die Spannung zwischen zwei Aussenleitern.

## Neutralleiter

Im symmetrischen Betrieb (gleiche Last an allen drei Phasen) fliesst kein Strom im Neutralleiter. Bei unsymmetrischer Last gleicht der Neutralleiter die Differenz aus.

Ohne Neutralleiter können bei Unsymmetrie gefährliche Spannungsverschiebungen am Sternpunkt entstehen.

## Motorwicklung in Stern

Niedrigere Spannung über jeder Wicklung. Bei Sternanlauf: Motor startet in Stern (tieferer Strom), wird nach dem Anlauf auf Dreieck umgeschaltet (volle Leistung).

:::info
Stern-Dreieck-Anlauf ist das klassische Verfahren um den Anlaufstrom grosser Motoren zu begrenzen. Ohne Anlaufhilfe können Motoren bis zu 6-fachen Nennstrom beim Einschalten ziehen.
:::
