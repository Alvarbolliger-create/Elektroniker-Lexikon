---
title: Wellenwiderstand
kategorie: EK
tags: [Wellenwiderstand, Z0, 50 Ohm, 100 Ohm, Leiterbahn, Impedanz]
symbol: Z0
einheit: Ω
---

Der Wellenwiderstand einer Leiterbahn bestimmt wie sie mit hochfrequenten Signalen umgeht. Er hängt von der Geometrie und dem Material ab, nicht vom Leitungswiderstand.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signalintegrität]]
- [[Impedanz]]
:::
:::vbox
**Verwandte Artikel**
- [[Übersprechen]]
- [[PCB Aufbau]]
:::
:::

---

## Warum 50 Ohm?

50 Ohm ist ein Kompromiss zwischen maximaler Leistung (75 Ohm Koaxialkabel) und minimaler Dämpfung (33 Ohm). Weltweit standardisiert für HF-Messtechnik und die meisten digitalen Hochgeschwindigkeitsschnittstellen.

Differentielle Leitungen: oft 100 Ohm (USB, LVDS, Ethernet).

## Berechnung für Microstrip

Eine Leiterbahn auf der Aussenlage über einer Massefläche:

:::formel
Z0 = (87 / sqrt(Er + 1.41)) × ln(5.98 × h / (0.8 × w + t))
:::
- h = Substratdicke (µm)
- w = Leitungsbreite (µm)
- t = Kupferdicke (µm)
- Er = Dielektrizitätszahl des Substrats (FR4: ca. 4.4)

Für Standard-FR4 mit 100 µm Substrat und 35 µm Kupfer: etwa 0.2 mm Breite für 50 Ohm.

## Einfluss der Frequenz

Er von FR4 sinkt leicht mit der Frequenz. Die effektive Permittivität und damit Z0 ändern sich. Für präzise Anwendungen besser PTFE- oder Rogers-Material.

## Abschluss

Damit keine Reflexionen entstehen, muss die Leitung am Empfangsende mit ihrem Wellenwiderstand abgeschlossen werden.

**Serieller Abschluss**: Widerstand am Ausgang des Treibers. Einfach, kein Strom im Ruhezustand.

**Paralleler Abschluss**: Widerstand von der Leitung nach GND oder Vterm am Empfangsende. Weniger Reflexionen, aber Ruhestrom.

## Differentieller Abschluss

Bei differentiellen Paaren: Widerstand zwischen den beiden Leitungen, typisch 100 Ohm. Oder intern im IC integriert (bei LVDS, SERDES).
