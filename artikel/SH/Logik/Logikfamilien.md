---
title: Logikfamilien (TTL, CMOS, BiCMOS, ECL)
kategorie: SH
kapitel: Logik
tags: [ttl, cmos, bicmos, ecl, logikfamilie, verlustleistung, schaltgeschwindigkeit, treiberfaehigkeit, integrationsdichte]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter (UND, ODER, NICHT, NAND, NOR, EXOR)]]
:::
:::vbox
**Führt weiter zu**
- [[Schaltpegel & Störabstand]]
- [[Fan-Out & Fan-In]]
:::
:::

---

Nicht jedes Logikgatter ist intern gleich aufgebaut. Je nachdem, mit welcher Halbleitertechnologie ein Gatter realisiert wird, unterscheiden sich Schaltgeschwindigkeit, Verlustleistung, Treiberfähigkeit und Betriebsspannung erheblich. Man fasst Bausteine mit gleicher zugrunde liegender Schaltungstechnik zu **Logikfamilien** zusammen — die wichtigsten sind TTL, CMOS, BiCMOS und ECL.

## TTL — Transistor-Transistor-Logik

Bei der **TTL-Logik** kennen die Transistoren nur zwei Zustände: gesperrt oder leitend (daher auch "Zweizustandslogik" bzw. bipolare Logik). Ein TTL-NAND vom Typ 7400 zieht den Ausgang über eine feste Transistorstruktur auf High oder Low. TTL ist seit etwa 1975 auf dem Markt und bot der ersten Generation hohe Schaltgeschwindigkeit und hohe Treiberfähigkeit — allerdings auf Kosten einer hohen Verlustleistung. Mit Schottky-Dioden liess sich die Verlustleistung später um das Fünffache senken (→ **LS-TTL**, 74LS00).

:::merke
Grundeigenschaften der TTL-Familie: hohe Schaltgeschwindigkeit, hohe Treiberfähigkeit, guter ESD-Schutz — aber hohe Verlustleistung und vergleichsweise geringe Integrationsdichte. Die Betriebsspannung beträgt fest 5 Volt. Bekannte Varianten sind LS-TTL, ALS-TTL und AS-TTL — für Neuentwicklungen wird TTL heute kaum mehr eingesetzt.
:::

## CMOS — Complementary Metal Oxide Semiconductor

**CMOS**-Logikfamilien verwenden anstelle bipolarer Transistoren **Feldeffekttransistoren (FET)**. Das bringt zwei entscheidende Vorteile: FETs sind sehr hochohmig, wodurch die Verlustleistung im statischen Zustand praktisch null ist (sie steigt allerdings mit der Arbeitsfrequenz spürbar an — die Verlustleistung von CMOS ist also **frequenzabhängig**). Ausserdem sind FETs geometrisch sehr klein, was eine hohe Integrationsdichte ermöglicht — hochintegrierte Bausteine wie DRAMs und CPUs werden praktisch ausschliesslich in CMOS-Technologie gefertigt.

Die ersten CMOS-Familien hatten gegenüber TTL noch langsamere Durchlaufzeiten und eine geringere Treiberfähigkeit; durch optimierte Fertigungsprozesse wurden diese Nachteile inzwischen ausgemerzt. Moderne CMOS-Familien arbeiten mit unterschiedlichen Betriebsspannungen — gängig sind 5 V, 3.3 V, 2.5 V und sogar 1.8 V. Die schnellsten CMOS-Familien (CBT, CBTLV) erreichen heute Durchlaufzeiten unter 1.5 ns.

:::info
Bekannte CMOS-Vertreter sind HC/HCT (High Speed CMOS), AC/ACT (Advanced CMOS), LV/LVC (Low Voltage CMOS) sowie ALVC und AVC für besonders niedrige Versorgungsspannungen.
:::

## BiCMOS — das Beste aus beiden Welten

**BiCMOS**-Familien (z. B. BCT, ABT, LVT) kombinieren die CMOS-Technik mit der TTL-Technik: Eine **CMOS-Eingangsstufe** sorgt für eine kleine Verlustleistung, während eine **TTL-Ausgangsstufe** den nötigen Treiberstrom liefert. So vereint BiCMOS die Vorteile der TTL-Schaltungen (kurze Durchlaufzeit, hohe Treiberfähigkeit) mit denjenigen der CMOS-Schaltungen (kleine Verlustleistung).

## ECL — Emitter Coupled Logic

Steht die Geschwindigkeit absolut im Vordergrund und spielt die Verlustleistung nur eine untergeordnete Rolle, kommt die **ECL-Logik** zum Einsatz. Sie zeichnet sich durch extrem kurze Durchlaufzeiten aus (die schnellste ECL-Familie 100E100 erreicht ca. 0.4 ns!). Erreicht wird dies, indem die Transistoren im ungesättigten Zustand betrieben werden und kleinere Signalpegel als bei "normaler" TTL-Logik verwendet werden.

:::warning
Die ECL-Logik wird **negativ gespeist** (z. B. −5.2 V) — ein wichtiger Unterschied zu TTL und CMOS, der bei der Schaltungsplanung unbedingt zu beachten ist. Typische Einsatzgebiete sind Superrechner für Wissenschaft und Militär, bei denen die hohe Verlustleistung (rund 55 mW pro NOR-Gatter bei der Standard-ECL-Serie) eine untergeordnete Rolle spielt — solche Anlagen werden oft aktiv gekühlt. Im Gegensatz zu CMOS ist die Verlustleistung von ECL **frequenzunabhängig**.
:::

## Vergleich: Durchlaufzeit, Verlustleistung und Betriebsspannung

| Familie | Gatter | Spannung | Verlustleistung Pᵥ | Laufzeit t_PD |
|---|---|---|---|---|
| TTL | 7400 | 5 V | 10 mW | 10 ns |
| LS-TTL | 74LS00 | 5 V | 2 mW | 10 ns |
| ALS-TTL | 74ALS00 | 5 V | 1 mW | 4 ns |
| CMOS HC | 74HC00 | 5 V | 0.5 mW/MHz | 10 ns |
| CMOS AC | 74AC00 | 5 V | 0.8 mW/MHz | 3 ns |
| CMOS LV | 74LV00 | 3.3 V | 0.6 mW/MHz | 14 ns |
| ECL standard | 10.100 | −5.2 V | 35 mW | 2 ns |
| ECL high Speed | 100E100 | −4.5 V | 40 mW | 0.4 ns |

![Marktübersicht der Logikfamilien über die Zeit: Bipolare Familien (TTL) dominierten in der Frühphase, wurden dann durch CMOS-Familien abgelöst und schliesslich durch BiCMOS ergänzt — der Lebenszyklus zeigt Einführung, Akzeptanz, Höhepunkt, Marktabnahme und Auslauf](abbildungen/logikfamilien_marktuebersicht.png)

:::tip
Die Wahl der richtigen Logikfamilie ist eine Abwägung zwischen technischen Kriterien (Durchlaufzeit, Verlustleistung, Betriebsspannung, **Treiberfähigkeit**, **Schaltpegel**, Störsicherheit) und wirtschaftlichen Kriterien (Preis, Lieferbarkeit, Second Source). Wie sich Schaltpegel und Treiberfähigkeit konkret auswirken — und was beim Zusammenschalten verschiedener Familien zu beachten ist — zeigen die Artikel → [[Schaltpegel & Störabstand]] und → [[Fan-Out & Fan-In]].
:::
