---
title: DFT (Design for Testing)
kategorie: EN
tags: [DFT, testpunkte, ICT, flying probe, boundary scan, testbarkeit, JTAG, nadelbett, BGA, serienfertigung]
symbol: —
einheit: —
---

DFT bedeutet: Testpunkte und Strukturen ins Design einbauen bevor die Platine gefertigt wird. Nachträglich ist es meist zu spät.

:::hbox
:::vbox
**Voraussetzungen**
- [[PCB Aufbau & Material]]
- [[DFM (Design for Manufacturing)]]
:::
:::vbox
**Verwandte Artikel**
- [[FMEA]]
- [[IPC-Kriterien]]
:::
:::

---

## Warum DFT?

Ohne Testpunkte kann ein Fehler auf der bestückten Platine schwer lokalisiert werden. Testpunkte ermöglichen automatisierte Tests und sparen bei der Serienfertigung enorm viel Zeit.

## Testpunkte

Runde Pads (typisch 1 mm Durchmesser) an wichtigen Netzpunkten: Versorgungsspannungen, Signale, Busteilnehmer. Auf der Unterseite der Platine, damit die Testnadeln beim ICT-Test zugreifen können.

Mindestabstand zwischen Testpunkten: 2.54 mm (100 mil) für einfache Testvorrichtungen, 1.27 mm für dichte Layouts.

## ICT (In-Circuit-Test)

Ein Nadelbett (Bed of Nails) kontaktiert alle Testpunkte gleichzeitig. Ein Tester misst jeden Bauteilwert, jeden Kurzschluss, jede offene Verbindung in Sekunden.

Voraussetzungen:
- Ausreichend Testpunkte auf einer Seite
- Bekannte Testpunktpositionen im CAD

## Flying Probe

Zwei bis acht bewegliche Nadeln messen Punkt zu Punkt. Kein Nadelbett nötig, daher günstiger in der Einrichtung. Langsamer als ICT, geeignet für kleine Serien.

## Boundary Scan (JTAG)

Für dicht besetzte BGA-Bauteile die keine Testpunkte haben. Die ICs kommunizieren über die JTAG-Schnittstelle und testen ihre eigenen Verbindungen. Benötigt JTAG-fähige Bauteile.

## Was ohne DFT passiert

Fehler werden erst beim Funktionstest entdeckt. Lokalisierung braucht viel Zeit. Reparaturen ohne zugängliche Punkte sind schwierig. In der Serie erhöhen sich Fehlerkosten drastisch.
