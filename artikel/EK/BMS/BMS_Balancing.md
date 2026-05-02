---
title: BMS Balancing
kategorie: EK
tags: [BMS, balancing, zellausgleich, passiv, aktiv, lithium, top-balancing, bottom-balancing, pre-balancing, zelldrift, kapazitätsverlust]
symbol: —
einheit: —
---

Balancing gleicht Spannungsunterschiede zwischen Zellen in einem Akkupack aus. Ohne Balancing wird der Pack durch die schwächste Zelle begrenzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[BMS Grundlagen]]
- [[Batterietechnik]]
:::
:::vbox
**Verwandte Artikel**
- [[BMS Grundlagen]]
:::
:::

---

## Warum driften Zellen auseinander?

Zellen sind nie identisch. Unterschiede in Kapazität, Innenwiderstand und Selbstentladung führen dazu, dass nach einigen Lade-/Entladezyklen einzelne Zellen voreilen oder nachhinken.

Beim Laden ist die vollste Zelle zuerst voll. Das BMS muss dann den Ladevorgang stoppen, obwohl andere Zellen noch nicht voll sind.

## Passives Balancing

Die überschüssige Ladung einer vorauseilenden Zelle wird in Wärme umgewandelt (Widerstand parallel zur Zelle).

Vorteile: Einfach, günstig, weit verbreitet.  
Nachteile: Energie geht verloren, Wärmeentwicklung, langsam.

Meist wird nur am Ende des Ladens balanciert (Top-Balancing), wenn alle Zellen nahe am Maximum sind.

## Aktives Balancing

Ladung wird von vollen Zellen zu leeren übertragen. Per Induktivität, Kondensator oder DC-DC-Wandler.

Vorteile: Kein Energieverlust, schneller.  
Nachteile: Komplex, teurer, mehr Bauteile.

Lohnt sich vor allem bei grossen Packs und hohen Zyklenanzahlen.

## Bottom- vs. Top-Balancing

**Top-Balancing**: Zellen werden oben (bei 100 %) ausgeglichen. Standard für die meisten Anwendungen.  
**Bottom-Balancing**: Zellen werden bei 0 % ausgeglichen. Relevant wenn die Tiefentladungsschutzfunktion des BMS die kritische Grenze ist.

:::tip
Bei selbstgebauten Packs sollten die Zellen vor dem Zusammenbau auf gleiche Spannung gebracht werden (pre-balancing). Das entlastet das Balancing-System erheblich.
:::
