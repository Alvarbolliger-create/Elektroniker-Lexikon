---
title: Zell-Balancing
kategorie: EK
tags: [balancing, zelldrift, passiv, aktiv, ladungsausgleich]
symbol: —
einheit: —
---

Zell-Balancing ist eine Kernfunktion eines [[Batteriemanagementsystem|BMS]]. Es gleicht den Ladezustand (SOC) von in Serie geschalteten Zellen an. Da Zellen durch Fertigungstoleranzen und unterschiedliche thermische Belastungen nie exakt gleich altern, driften ihre Spannungen mit der Zeit auseinander. Ohne Balancing limitiert die schwaechste Zelle die Kapazitaet des gesamten Packs.

:::hbox
:::vbox
**Voraussetzungen**
- [[Batteriemanagementsystem]]
- [[Serienschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[Innenwiderstand]]
- [[Spannungsteiler]]
:::
:::vbox
**Fuehrt weiter zu**
- [[DC-DC-Wandler]]
:::
:::

---

## Das Problem der Zelldrift

Beim Entladen erreicht die Zelle mit der geringsten Kapazitaet zuerst die Untergrenze (UVP). Das BMS muss abschalten, obwohl andere Zellen noch Energie haben. Beim Laden verhaelt es sich umgekehrt: Die Zelle mit dem hoechsten Spannungsniveau erreicht zuerst die Obergrenze (OVP) und stoppt den Ladevorgang. Das Pack kann also weder voll geladen noch voll entladen werden. Das Balancing loest dieses Problem.

## Passive Balancing

Das passive Balancing (auch "Bleeding" genannt) ist die einfachste und am weitesten verbreitete Methode. Zellen mit einer zu hohen Spannung werden gezielt entladen, bis sie das Niveau der schwaecheren Zellen erreicht haben.

* **Funktionsweise:** Das BMS aktiviert einen Transistor, der einen Lastwiderstand parallel zur betroffenen Zelle schaltet. Ein Teil des Ladestroms fliesst nun am Akku vorbei durch den Widerstand und wird in Waerme umgewandelt.
* **Vorteile:** Sehr guenstig, geringer Platzbedarf, bewaehrte Technik.
* **Nachteile:** Energie wird vernichtet (schlechte Effizienz), langsame Ausgleichsgeschwindigkeit (typischerweise 30 bis 100 mA Ausgleichsstrom), das BMS kann sich stark erwaermen.

:::formel
I_balance = U_zelle / R_balance
:::

## Aktive Balancing

Aktives Balancing vernichtet keine Energie, sondern schiebt Ladung zwischen den Zellen hin und her.

* **Funktionsweise:** Ueber induktive (Spulen) oder kapazitive (Kondensatoren) Netzeinwerke, oft realisiert durch bidirektionale [[DC-DC-Wandler]], wird Energie aus starken Zellen entnommen und gezielt in schwache Zellen injiziert.
* **Vorteile:** Sehr hohe Effizienz (kaum Abwaerme), hohe Ausgleichsstroeme (oft 1 A bis 5 A), Balancieren ist unabhaengig vom Ladevorgang moeglich.
* **Nachteile:** Hohe Bauteilkosten, komplexes Platinenlayout, erfordert viel Platz. Wird meist nur in sehr teuren Hochleistungsakkus oder stationaeren Speichern eingesetzt.

## Trigger und Strategien

Ein BMS balanciert nicht durchgehend planlos. Es gibt klare Einschaltbedingungen (Trigger):

1. **Top-Balancing:** Dies ist der Standard bei passiven Systemen. Das Balancing startet erst am ganz am Ende des Ladevorgangs. Ein typischer Trigger fuer eine Li-Ion-Zelle koennte sein: Zellspannung > 4.10 V UND Delta-Spannung zur schwaechsten Zelle > 15 mV.
2. **Bottom-Balancing:** Die Zellen werden am unteren Ende der Entladung angeglichen. Das wird in der Praxis selten gemacht, da man meist sicherstellen moechte, dass das Pack zu 100 % voll geladen in die Nutzung startet.
3. **Continuous Balancing:** Aktive Balancer koennen permanent arbeiten, sobald sie eine Spannungsdifferenz feststellen. Dies kann jedoch irrefuehrend sein, da Spannungsunterschiede waehrend starker Last durch unterschiedliche [[Innenwiderstand|Innenwiderstaende]] entstehen koennen (dynamische Drift), obwohl die Zellen den gleichen Ladezustand haben. Daher messen smarte BMS oft nur im Ruhezustand.