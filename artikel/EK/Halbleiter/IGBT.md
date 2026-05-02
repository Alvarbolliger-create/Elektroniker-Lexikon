---
title: IGBT
kategorie: EK
tags: [IGBT, leistungshalbleiter, schalten, frequenzumrichter, kollektor, emitter, current-tail, U_CE_sat, gate-treiber, solarwechselrichter]
symbol: Q
einheit: —
---

Der IGBT verbindet die Vorteile von MOSFET und Bipolartransistor. Spannungsgesteuert wie der MOSFET, aber mit den Niederspannungseigenschaften eines Bipolartransistors. Standard in Frequenzumrichtern und Stromrichtern.

:::hbox
:::vbox
**Voraussetzungen**
- [[FET / MOSFET]]
- [[Bipolartransistor (BJT)]]
:::
:::vbox
**Verwandte Artikel**
- [[Frequenzumrichter]]
:::
:::vbox
**Führt weiter zu**
- [[Frequenzumrichter]]
- [[Buck (Step-down)]]
:::
:::

---

## Aufbau

Gate, Kollektor, Emitter. Das Gate wird wie beim MOSFET spannungsgesteuert. Der Laststrom fliesst wie beim BJT durch Kollektor und Emitter.

## Vorteile gegenüber MOSFET

Bei hohen Spannungen (über 600 V) hat der MOSFET einen sehr hohen R_DS_on. Der IGBT hat dort eine niedrigere Durchlassspannung (U_CE_sat ≈ 1.5 bis 3 V) und damit weniger Verluste.

## Vorteile gegenüber BJT

Spannungsgesteuert, kein Basisstrom nötig. Einfachere Ansteuerung, höhere Schaltfrequenz möglich.

## Nachteile

Beim Ausschalten entsteht ein Schweif (Current Tail): Der Bipolartransistorteil räumt seine Ladungsträger langsamer aus als ein MOSFET. Das begrenzt die maximale Schaltfrequenz (typisch bis 50 kHz).

## Ansteuerung

Gate-Treiber-IC nötig. Gate-Spannung typisch 15 V für Ein, -8 bis 0 V für Aus. Negative Sperrspannung verhindert parasitäres Einschalten.

## Typische Anwendungen

Frequenzumrichter (Drehstromantriebe), Schaltnetzteil-Brücken bei hohen Leistungen, Solarwechselrichter, Induktionsheizung.

| Typ | U_CE max | I_C max | Schaltfrequenz |
|---|---|---|---|
| IKW40N120H3 | 1200 V | 40 A | bis 30 kHz |
| IRGP50B60PD1 | 600 V | 50 A | bis 40 kHz |
| FGH40T65SQD | 650 V | 40 A | bis 60 kHz |
