---
title: Zell-Balancing
kategorie: EK
kapitel: Akku
tags: [zell-balancing, zelldrift, passives-balancing, aktives-balancing, top-balancing, soc, bleeding, shuntwiderstand, dc-dc-wandler, serienschaltung, kapazitätsausgleich]
groessen: I_bal|Balancingstrom|A; R_bal|Balancingwiderstand|Ω; Delta_U|Spannungsdifferenz|mV
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Akku Grundlagen]]
- [[BMS]]
:::
:::vbox
**Verwandte Artikel**
- [[DC-DC Wandler]]
- [[NTC & PTC Thermistoren]]
:::
:::vbox
**Führt weiter zu**
- [[DC-DC Wandler]]
:::
:::

---

Zell-Balancing gleicht den Ladezustand (SOC) in Serie geschalteter Zellen an. Ohne Balancing limitiert die schwächste Zelle das gesamte Pack — nutzbare Kapazität und Lebensdauer sinken kontinuierlich.

## Das Problem: Zelldrift

Zellen altern durch Fertigungstoleranzen und unterschiedliche Temperaturen im Pack nie exakt gleich. Mit jedem Zyklus driften ihre Spannungen weiter auseinander:

:::monospace
Pack 4S (Soll: alle Zellen gleich):
  Zelle 1:  3.80 V  ← schwächste
  Zelle 2:  3.95 V
  Zelle 3:  3.92 V
  Zelle 4:  4.00 V
  → Delta_U = 200 mV
:::

**Beim Entladen**: Zelle 1 erreicht als erste die Untergrenze (z.B. 3.0 V) → BMS schaltet ab. Zellen 2–4 haben noch nutzbare Energie → verschenkte Kapazität.

**Beim Laden**: Zelle 4 erreicht als erste die Obergrenze (z.B. 4.2 V) → Ladevorgang stoppt. Zellen 1–3 sind noch nicht voll.

## Passives Balancing (Bleeding)

Einfachste und häufigste Methode. Zellen mit **zu hoher Spannung** werden über einen Widerstand gezielt entladen, bis sie das Niveau der schwächsten Zelle erreichen.

**Schaltung**: Transistor schaltet Widerstand parallel zur überspannten Zelle:

:::schematic Passives Balancing-Schaltung (eine Zelle): Zelle (Batterie-Symbol, U_Zelle). N-Kanal-MOSFET (oder NPN-Transistor) mit Drain/Kollektor an Zelle (+), Source/Emitter an Zelle (−). R_bal (Bleeding-Widerstand) in Serie mit MOSFET. BMS-IC: misst U_Zelle via ADC → wenn U_Zelle > Schwelle: Gate EIN → Balancing-Strom I_bal = ΔU/R_bal durch R_bal → Wärme. Daneben LED optional für Statusanzeige
/Diagramm/passives_balancing.svg
:::

:::formel
I_bal = Delta_U / R_bal    # Balancingstrom
P_R   = I_bal^2 * R_bal    # Verlustleistung als Wärme
:::

:::monospace
Beispiel: Delta_U = 100 mV, R_bal = 10 Ω
I_bal = 0.1 V / 10 Ω = 10 mA    → sehr langsam
:::

| Merkmal | Wert |
|---|---|
| Typischer Balancingstrom | 30–100 mA |
| Ausgleichszeit | Stunden |
| Wirkungsgrad | Schlecht (Energie wird verheizt) |
| Kosten / Aufwand | Sehr gering |
| Anwendung | Günstige Consumer-BMS, E-Bikes |

:::warning
Beim passiven Balancing erwärmt sich die BMS-Platine. Die Balancing-Widerstände müssen thermisch ausreichend dimensioniert sein. Balancing nur am Ende des Ladens starten (Top-Balancing) damit die Wärme nicht über lange Zeit produziert wird.
:::

## Aktives Balancing

Energie wird nicht vernichtet, sondern zwischen Zellen **verschoben**. DC-DC-Wandler oder Kondensator-/Spulen-Netzwerke transferieren Ladung von starken zu schwachen Zellen.

**Prinzip-Varianten**:

| Variante | Prinzip | Effizienz |
|---|---|---|
| Kapazitiver Shuttle | Kondensator wechselweise an starke/schwache Zelle | 85–90 % |
| Induktiver Transfer | Transformator oder Spule zwischen Zellen | 90–95 % |
| DC-DC-Wandler | Bidirektionaler Flyback/Buck-Boost | 85–95 % |

| Merkmal | Wert |
|---|---|
| Typischer Balancingstrom | 1–5 A |
| Ausgleichszeit | Minuten |
| Wirkungsgrad | Gut (90–95 %) |
| Kosten / Aufwand | Hoch (viele Bauteile, komplexes Layout) |
| Anwendung | Hochleistungs-EVs, stationäre Speicher |

## Balancing-Strategien (Trigger)

Das BMS balanciert nicht kontinuierlich — es gibt klare Einschaltbedingungen:

**Top-Balancing** (Standard):
- Startet am Ende des Ladevorgangs (Zellspannung nahe Ladeschluss)
- Typischer Trigger: U_Zelle > 4.1 V **UND** Delta_U > 15 mV
- Zellen mit höchster Spannung werden entladen bis alle gleich sind

**Bottom-Balancing**:
- Angleich am unteren Ende der Entladung
- In der Praxis selten — man möchte das Pack voll starten

**Continuous Balancing** (nur aktiv):
- Aktiver Balancer gleicht laufend aus sobald Delta_U > Schwelle
- Aber: Spannungsunterschiede unter Last entstehen durch verschiedene Innenwiderstände (dynamische Drift), nicht durch SOC-Unterschied → Messung besser im Ruhezustand (OCV)

:::tip
Passives Top-Balancing ist für die meisten Anwendungen (E-Bike, Power-Bank, 12-V-LFP-Pack) ausreichend. Aktives Balancing lohnt sich erst bei sehr grossen Packs (> 20 kWh) oder wenn Zyklenlebensdauer extrem wichtig ist (z.B. Industriespeicher).
:::
