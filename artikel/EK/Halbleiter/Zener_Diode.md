---
title: Zener-Diode
kategorie: EK
tags: [zenerdiode, spannungsreferenz, sperrspannung, regler, überspannungsschutz, vorwiderstand, U_Z, BZX, TVS, crowbar]
symbol: D_Z
einheit: —
---

Die Zener-Diode hält in Sperrrichtung eine definierte Spannung aufrecht. Sie wird als einfache Spannungsreferenz oder zum Schutz vor Überspannung eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[Lineare Regler]]
:::
:::vbox
**Führt weiter zu**
- [[Lineare Regler]]
- [[Schutzbeschaltung]]
:::
:::

---

## Schaltsymbol

Wie eine normale Diode, aber die Linie am Ende hat gebogene Enden (wie ein Z).

:::hbox
:::schematic Diode
/schaltplaene/symbole/D.svg
:::
:::schematic Zener-Diode
/schaltplaene/symbole/D_Z.svg
:::
:::

## Funktionsprinzip

In Durchlassrichtung verhält sich die Zener wie eine normale Diode (0.7 V Abfall). In Sperrrichtung bricht sie bei der Zener-Spannung U_Z kontrolliert durch und hält diese Spannung aufrecht.

:::info
Die Zener wird absichtlich in Sperrrichtung betrieben. Das ist der normale Betriebszustand.
:::

## Grundschaltung: Spannungsreferenz

Vorwiderstand in Reihe mit der Zener, Zener nach GND.

:::formel
R_V = (U_ein - U_Z) / I_Z    # Vorwiderstand; I_Z = Zenerstrom (aus Datenblatt, typisch 5-20 mA)
:::
Die Ausgangsspannung bleibt auf U_Z, solange genug Strom durch die Zener fliesst.

## Einsatzgebiete

**Spannungsreferenz**: Stabile Spannung für ADC-Referenz oder Komparator.

**Überspannungsschutz**: Parallelschalten zum Eingang, begrenzt Spannungsspitzen.

**Pegelverschiebung**: Versatz einer Spannung um U_Z.

:::warning
Eine Zener ohne Vorwiderstand direkt an einer Spannungsquelle zieht unbegrenzten Strom und verbrennt sofort. Immer R_V berechnen und einbauen.
:::

## Kenndaten

Zener-Spannungen sind normiert: 2.4 V, 3.3 V, 3.9 V, 4.7 V, 5.1 V, 6.2 V, 7.5 V, 8.2 V, 9.1 V, 10 V, 12 V, 15 V, ...

| Typ | U_Z | P_max | Genauigkeit |
|---|---|---|---|
| BZX55C5V1 | 5.1 V | 500 mW | ±5 % |
| BZX84C3V3 | 3.3 V | 300 mW | ±5 % |
| LM4040-5.0 | 5.0 V | 150 mW | ±0.1 % |
