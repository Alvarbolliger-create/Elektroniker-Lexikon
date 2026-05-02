---
title: DFM (Design for Manufacturing)
kategorie: EN
tags: [DFM, fertigungsgerecht, PCB, SMD, bestückung, layout, IPC-7351, wave-löten, schablone, DRC, lötbrücke]
symbol: —
einheit: —
---

DFM bedeutet: Das Design so gestalten dass es zuverlässig und kosteneffizient gefertigt werden kann. Was auf dem Schaltplan funktioniert muss auch in der Produktion funktionieren.

:::hbox
:::vbox
**Voraussetzungen**
- [[PCB Aufbau & Material]]
- [[SMD vs. THT]]
- [[IPC-Kriterien]]
:::
:::vbox
**Verwandte Artikel**
- [[DFT (Design for Testing)]]
- [[FMEA]]
:::
:::

---

## Warum DFM?

Ein PCB kann elektrisch korrekt sein und trotzdem schlecht fertigbar sein. Zu kleine Abstände, falsche Padgeometrien, schlecht zugängliche Testpunkte erhöhen Fehlerquoten und Kosten.

DFM-Regeln kommen vom Leiterplattenhersteller und vom Bestücker. Frühzeitig anwenden spart teure Redesigns.

## Typische DFM-Regeln für PCB

**Abstände**:
- Mindestabstand Leiterbahn zu Leiterbahn: 0.1 mm (Standard), 0.075 mm (fein)
- Mindestabstand Pad zu Pad: herstellerabhängig

**Pads**:
- Korrekte Padgrössen nach IPC-7351 für SMD
- Kupferfreie Zone bei Testpunkten

**Bestückung**:
- Einheitliche Bauteilausrichtung erleichtert Schablonendruck
- Keine SMD-Bauteile nahe am Platinenrand (Vakuumhalterung)
- Grosse Bauteile nicht neben kleinen (Schablone, Lötschatten)

## Lötmaskenöffnungen

Zu kleine Stege zwischen Pads können beim Drucken die Schablone verformen. Mindestens 0.075 mm Steg, besser 0.1 mm.

## THT nach Wave-Lötung

THT-Pins die mit Wave gelötet werden:
- Bauteil auf der Oberseite, Löten von unten
- Mindestabstand zu SMD-Pads auf der Unterseite einhalten
- Lange Pinüberstände verbessern die Lötqualität, aber zu lang sind sie ein Problem beim Transportieren

## DFM-Prüfung

Viele PCB-CAD-Tools (KiCad, Altium, Eagle) haben DRC (Design Rule Check). Zusätzlich bieten viele Leiterplattenhersteller online DFM-Checks an.

:::tip
Schon bei der ersten Bauteilauswahl auf Verfügbarkeit achten. Ein perfektes DFM bringt nichts wenn das Schlüsselbauteil 52 Wochen Lieferzeit hat.
:::
