---
title: Blindleistungskompensation
kategorie: ET
tags: [kompensation, blindleistung, kondensator, leistungsfaktor, cos phi, industrie, kostenersparnis]
groessen: Q_L|induktive Blindleistung|var; Q_C|kapazitive Blindleistung|var; C|Kompensationskondensator|F; P|Wirkleistung|W; S|Scheinleistung|VA; phi|Phasenwinkel|°
_status: PORT  # ET_alt/Leistung/Blindleistungskompensation.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Wechselstromleistung]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator (Übersicht)]]
:::
:::

---

Induktive Lasten (Motoren, Transformatoren, Drosseln) verursachen induktive Blindleistung, die den Netzstrom erhöht ohne nützliche Arbeit zu leisten. Durch Parallelschalten von Kondensatoren wird diese Blindleistung lokal kompensiert — der Netzstrom sinkt und der Leistungsfaktor verbessert sich.

## Warum kompensieren?

Induktive Blindleistung bedeutet: Strom fliesst, aber er erzeugt keine Wirkleistung. Trotzdem belasten diese Blindströme:
- **Leitungen**: höhere Ströme → höhere Kupferverluste (I² · R)
- **Transformatoren**: durch den Blindstrom höher belastet
- **Energieversorger**: müssen Scheinleistung bereitstellen, nicht nur Wirkleistung

In der Schweiz verlangen Netzanschlussbedingungen für grössere Anlagen typisch cos phi ≥ 0,9. Bei schlechterem cos phi werden Zusatzkosten für Blindleistungsbezug berechnet.

## Prinzip der Kompensation

:::schematic Blindleistungskompensation: Netzanschluss links; Motor (induktive Last, dargestellt als RL-Parallelschaltung) in der Mitte; Kompensationskondensator C parallel zum Motor geschaltet; Phasenzeiger rechts: I_Motor (nacheilend, gross), I_C (voreilend), I_Netz (kleinere Summe, näher an U); Beschriftung: U, I_Motor, I_C, I_Netz, phi_alt, phi_neu
/schaltplaene/wechselstrom/blindleistungskompensation.svg
:::

Kapazitive Blindleistung (Kondensatoren) ist entgegengesetzt zur induktiven (Motoren). Durch geziehte Parallelschaltung heben sie sich auf:

:::formel
Q_C = Q_L_kompensiert - Q_L_original    # benötigte kapazitive Blindleistung
:::

Nach der Kompensation gilt:

:::formel
Q_gesamt = Q_L - Q_C
:::

Ziel: Q_gesamt ≈ 0 → cos phi ≈ 1.

## Berechnung Kompensationskondensator

Die benötigte kapazitive Blindleistung aus dem gewünschten cos phi_neu und dem ursprünglichen cos phi_alt bei bekannter Wirkleistung P:

:::formel
Q_C = P * (tan(phi_alt) - tan(phi_neu))
:::

Die Kapazität des Kondensators (Dreieckschaltung im Drehstromnetz):

:::formel
C = Q_C / (3 * omega * U_str^2)    # für Dreieck, U_str = Strangspannung
:::

:::monospace
Beispiel: Motor P = 50 kW, cos phi_alt = 0.7 (phi = 45.6°), Ziel cos phi_neu = 0.95 (phi = 18.2°)
Q_C = 50 000 * (tan(45.6°) - tan(18.2°)) = 50 000 * (1.03 - 0.328) = 35.1 kvar

Bei U_L = 400 V (Dreieck):
C = 35100 / (3 * 2*pi*50 * 400^2 / 3) = 35100 / (2*pi*50 * 400^2) = 701 µF pro Phase
:::

## Vor und nach der Kompensation

| Grösse | Vor Kompensation | Nach Kompensation |
|---|---|---|
| Wirkleistung P | 50 kW | 50 kW (unverändert) |
| Blindleistung Q | 50 kvar | ≈ 16 kvar |
| Scheinleistung S | 70,7 kVA | 52 kVA |
| Leistungsfaktor | 0,7 | 0,95 |
| Netzstrom | 100 A | 75 A |

Der Netzstrom sinkt um 25 % — die Leitungsverluste (I²R) sinken um 44 %.

:::tip
Kompensationsanlagen werden automatisch geregelt: Ein Leistungsfaktormessgerät misst cos phi und schaltet je nach Bedarf Kondensatorstufen zu oder ab. Zu viele Kondensatoren würden zu kapazitiver Überkompensation führen — auch das ist ungünstig.
:::
