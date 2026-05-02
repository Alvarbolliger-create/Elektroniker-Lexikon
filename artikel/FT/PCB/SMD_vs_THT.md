---
title: SMD vs. THT
kategorie: FT
tags: [SMD, THT, bestückung, lötverfahren, bauform, leiterplatte, reflow, wellenlöten, 0402, 0603, 0805, footprint, mischbestückung]
symbol: —
einheit: —
---

SMD und THT sind die zwei grundlegenden Bestückungsarten für Leiterplatten. SMD ist kompakter und für automatische Fertigung geeignet, THT ist robuster und leichter von Hand zu löten.

:::hbox
:::vbox
**Voraussetzungen**
- [[PCB Aufbau & Material]]
:::
:::vbox
**Verwandte Artikel**
- [[IPC-Kriterien]]
:::
:::vbox
**Führt weiter zu**
- [[DFM (Design for Manufacturing)]]
:::
:::

---

## THT (Through Hole Technology)

Anschlussdrähte durch Bohrungen in der Leiterplatte. Lötstelle auf der Unterseite.

**Vorteile**: Robust, hohe mechanische Festigkeit, gut für Steckverbinder und Bauelemente mit grosser Kraft. Leicht von Hand zu löten und zu reparieren.

**Nachteile**: Braucht Bohrungen. Beide Seiten der Platine belegt. Grösser als SMD.

**Löten**: Wellenlöten (automatisch) oder von Hand.

## SMD (Surface Mount Device / Technology)

Bauteile direkt auf die Oberfläche gelötet, keine Bohrungen nötig.

**Vorteile**: Sehr kompakt, beide Seiten nutzbar, vollautomatisch bestückbar und lötbar (Reflow-Ofen), günstiger in der Serienproduktion.

**Nachteile**: Schwieriger von Hand zu löten (besonders kleine Bauformen). Weniger mechanisch robust.

**Löten**: Schablone aufbringen, Lotpaste sieben, Bauteile bestücken, Reflow-Ofen.

## SMD-Bauformgrössen (Widerstände, Kondensatoren)

| Bauform | Grösse (mm) | Leistung | Handlötbarkeit |
|---|---|---|---|
| 0201 | 0.6 × 0.3 | 50 mW | sehr schwer |
| 0402 | 1.0 × 0.5 | 63 mW | schwer |
| 0603 | 1.6 × 0.8 | 100 mW | möglich |
| 0805 | 2.0 × 1.25 | 125 mW | gut |
| 1206 | 3.2 × 1.6 | 250 mW | einfach |

## Mischbestückung

In vielen Produkten beide Technologien: SMD für die meisten Bauteile, THT für Steckverbinder, Leistungsbauelemente und Bauteile mit mechanischer Beanspruchung.
