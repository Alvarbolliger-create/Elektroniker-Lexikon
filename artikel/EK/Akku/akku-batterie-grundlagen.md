---
title: Akku und Batterie
kategorie: ET
tags: [energiespeicher, zellchemie, zellenverbund, kapazitaet]
symbol: G
einheit: —
---

Ein Akku oder eine Batterie ist ein elektrochemischer Energiespeicher, der chemische Energie in elektrische Energie umwandelt und als Spannungsquelle fuer Verbraucher dient. Waehrend Primärbatterien nur einmalig entladen werden koennen, lassen sich Akkumulatoren (Sekundaerbatterien) durch Stromzufuhr reversibel wieder aufladen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Spannung]]
- [[Kapazitaet]]
- [[Innenwiderstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Batteriemanagementsystem]]
- [[Ladeverfahren]]
:::
:::vbox
**Fuehrt weiter zu**
- [[Zell-Balancing]]
:::
:::

---

## Elektrische Kenngroessen

Um die Leistungsfaehigkeit einer Zelle zu bewerten, zieht man verschiedene Parameter heran:
* **Nennspannung:** Die typische Spannung waehrend der Entladung. Sie haengt rein von der verwendeten Chemie ab.
* **Kapazitaet (C):** Die speicherbare Ladungsmenge in Amperestunden (Ah). 
* **Energie:** Das Produkt aus Spannung und Kapazitaet, gemessen in Wattstunden (Wh). Dies ist der eigentliche Indikator fuer den Energieinhalt.
* **C-Rate:** Beschreibt den Lade- oder Entladestrom im Verhaeltnis zur Kapazitaet. Ein Strom von 1C bei einer 3000 mAh Zelle entspricht genau 3000 mA (3 A).
* **Innenwiderstand (DCIR / ACIR):** Ein parasitärer Widerstand in der Zelle. Ein hoher Innenwiderstand fuehrt bei hohen Stroemen zu einem starken Spannungsabfall und zur Erwaermung der Zelle.

:::formel
E = U * Q
I_max = C_rate * C
:::

## Zellchemie im Vergleich

Die Materialien von Anode, Kathode und Elektrolyt bestimmen die Energiedichte, Sicherheit und Zyklenfestigkeit.

| Typ | Nennspannung | Ladeschluss | Merkmale |
|---|---|---|---|
| **Li-Ion (NMC/NCA)** | 3.6 V - 3.7 V | 4.2 V | Sehr hohe Energiedichte, empfindlich auf Uberladung, thermisches Durchgehen moeglich |
| **LiFePO4 (LFP)** | 3.2 V | 3.65 V | Extrem sicher, brennt nicht, sehr hohe Zyklenlebensdauer (oft >3000 Zyklen), etwas schwerer |
| **LTO (Lithium-Titanat)**| 2.3 V | 2.8 V | Geringe Energiedichte, aber extrem schnell ladbar (bis 10C) und extrem kälteresistent |
| **NiMH** | 1.2 V | 1.45 V | Robust, Standard fuer Haushaltsakkus (AA/AAA), Memory-Effekt stark reduziert |

## Zellenverbund (Pack-Design)

Um in realen Anwendungen die gewuenschte Spannung oder Reichweite zu erzielen, werden Einzelzellen zu einem Batteriepack verschaltet. Die physische Verbindung erfolgt meist durch Punktschweissen von Nickelbandern oder durch Laser-Schweissen.

* **Serienschaltung (S):** Mehrere Zellen werden in Reihe geschaltet. Die Spannungen addieren sich, die Kapazitaet bleibt gleich. Dies ist noetig, um die Systemspannung zu erhoehen und Kabelquerschnitte klein zu halten.
* **Parallelschaltung (P):** Zellen werden parallel verbunden. Die Gesamtkapazitaet und die maximale Strombelastbarkeit addieren sich, die Spannung entspricht der einer Einzelzelle.

:::formel
Beispiel: E-Bike Akku 10S4P aus 18650-Zellen (3.6 V / 3 Ah)
Spannung = 10 * 3.6 V = 36 V
Kapazitaet = 4 * 3 Ah = 12 Ah
Gesamtenergie = 36 V * 12 Ah = 432 Wh
:::

In einem solchen Verbund altern die Zellen jedoch nie exakt gleich. Fertigungstoleranzen und Temperaturgradienten innerhalb des Packs fuehren zur sogenannten [[Zelldrift]]. Ohne ein [[Batteriemanagementsystem]] wuerden diese Unterschiede den gesamten Pack unbrauchbar machen.