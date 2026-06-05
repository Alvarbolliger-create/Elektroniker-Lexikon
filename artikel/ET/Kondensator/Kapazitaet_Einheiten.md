---
title: Kapazität & Einheiten
kategorie: ET
tags: [kapazität, farad, ladung, spannung, einheiten, kondensator]
groessen: C|Kapazität|F; Q|Ladung|C; U|Spannung|V
_status: PORT  # ET_alt/Kondensator/Kapazitaet_Einheiten.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektrische Ladung & Elementarladung]]
:::
:::

---

Die Kapazität ist das Mass dafür, wie viel Ladung ein Kondensator pro Volt Spannung speichern kann. Grosse Kapazität bedeutet: viel Ladung bei wenig Spannungsänderung.

## Grundformel

:::formel
C = Q / U    # Kapazität C (F) = Ladung Q (C) pro Spannung U (V)
:::

Umgestellt ergibt sich die im Artikel [[Auf- und Entladung (Kondensator)]] verwendete Form Q = C · U.

## Einheit Farad (F)

Das Farad ist eine sehr grosse Einheit — praktisch alle Kondensatoren im EFZ-Bereich liegen weit darunter.

| Vorsilbe | Symbol | Wert | Typische Bauteile |
|---|---|---|---|
| Millifarad | mF | 10⁻³ F | Grosse Elkos (Netzteilpuffer) |
| Mikrofarad | µF | 10⁻⁶ F | Elkos, Folienkondensatoren |
| Nanofarad | nF | 10⁻⁹ F | Keramik-, Folienkondensatoren |
| Pikofarad | pF | 10⁻¹² F | HF-Kondensatoren, SMD-Keramik |

:::tip
Kondensatorwerte auf Schaltplänen werden oft ohne Einheit angegeben: Werte > 1 bedeuten pF, Werte < 1 mit Dezimalpunkt können µF sein. Im Zweifel immer die Beschriftung des Bauteils prüfen.
:::

## Wichtige Grössen im Zusammenhang

Die Kapazität verbindet drei Grössen miteinander:

| Grösse | Symbol | Einheit | Zusammenhang |
|---|---|---|---|
| Kapazität | C | F | Eigenschaft des Bauteils |
| Ladung | Q | C (Coulomb = A·s) | Q = C · U |
| Spannung | U | V | U = Q / C |

Ein Kondensator mit C = 100 µF, der auf 10 V geladen ist, trägt eine Ladung von Q = 100 · 10⁻⁶ · 10 = 1 mC (1 Millicoulomb).

## Kapazität des Plattenkondensators

Geometrisch hängt die Kapazität von der Plattengeometrie und dem Dielektrikum ab — ausführlicher in [[Plattenkondensator & Influenz]]:

:::formel
C = epsilon_0 * epsilon_r * A / d
:::

Dabei ist A die Plattenfläche, d der Plattenabstand, epsilon_r die relative Permittivität des Dielektrikums und epsilon_0 = 8,854 · 10⁻¹² F/m die elektrische Feldkonstante.
