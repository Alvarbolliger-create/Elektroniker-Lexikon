---
title: Datenblatt-Analyse
kategorie: EN
tags: [datenblatt, bauteil, kennwerte, grenzwerte, applikation, min/max/typ, absolute maximum ratings, operating conditions, applikationshinweis, footprint]
symbol: —
einheit: —
---

Das Datenblatt ist die wichtigste Informationsquelle zu einem Bauteil. Wer es lesen kann, findet alles was er braucht, und erkennt was er nicht überschreiten darf.

:::hbox
:::vbox
**Voraussetzungen**
- —
:::
:::vbox
**Verwandte Artikel**
- [[Lifecycle & Obsolescence]]
:::
:::vbox
**Führt weiter zu**
- [[Derating]]
:::
:::

---

## Aufbau eines Datenblatts

**Beschreibung**: Kurze Zusammenfassung was das Bauteil macht und wofür es geeignet ist.

**Absolute Maximum Ratings**: Werte die nie überschritten werden dürfen. Nicht der Betriebsbereich, sondern die Zerstörungsgrenze. Kein Derating hier einkalkulieren.

**Recommended Operating Conditions**: Der sichere Betriebsbereich. Hier soll das Bauteil arbeiten.

**Electrical Characteristics**: Alle elektrischen Kennwerte, meist als Tabelle mit Min/Typ/Max.

**Application Circuit**: Typische Beschaltung. Oft der schnellste Einstieg für eigene Schaltungen.

## Was ist wichtig?

Bei passiven Bauteilen: Wert, Toleranz, Nennspannung, Nennleistung, Temperaturbereich.

Bei aktiven Bauteilen: Versorgungsspannung, Ausgangsstrom, Schutzdioden, Einschaltverhalten.

## Min/Typ/Max verstehen

**Typ**: Der Wert den das Bauteil meistens hat. Nicht für Berechnungen verwenden.

**Min / Max**: Die Grenzen über alle Exemplare, Temperaturen und Toleranzen. Schaltungen müssen mit diesen Werten funktionieren.

:::warning
Schaltungen nie auf den Typ-Wert auslegen. Das funktioniert vielleicht bei einem Prototyp, aber nicht in der Serienproduktion. Immer mit Min und Max rechnen.
:::

:::tip
Applikationshinweise (Application Notes) des Herstellers lesen. Sie erklären Fallstricke die im Datenblatt selbst nicht stehen.
:::
