---
title: Spule (Übersicht)
kategorie: ET
tags: [spule, induktivität, bauteil, serie, parallel, energie, freilaufdiode, gegeninduktivität]
groessen: L|Induktivität|H; U|Spannung|V; I|Strom|A; E|Energie|J
_status: PORT  # ET_alt/Spule/Spule_Uebersicht.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator (Übersicht)]]
:::
:::vbox
**EK-Anwendungen**
- [[Filter Grundlagen]]
- [[DC-DC-Wandler]]
- [[Transformator Aufbau]]
:::
:::vbox
**Führt weiter zu**
- [[Spule Typen]]
- [[Induktivität & Einheiten]]
- [[Selbstinduktion & Induzierte Spannung]]
:::
:::

---

Eine Spule speichert Energie im magnetischen Feld. Sie ist nach dem Kondensator das zweite wichtige reaktive Bauteil — und in ihrem Verhalten das genaue Gegenstück: Die Spule lässt Gleichstrom durch und sperrt hohe Frequenzen.

## Was ist eine Spule?

Ein Draht, der zu einer Wicklung aufgerollt ist. Das Magnetfeld jeder Windung addiert sich — je mehr Windungen und je grösser der Kern, desto stärker das Feld und desto grösser die Induktivität. Der Kern (Luft, Ferrit, Eisen) beeinflusst die Induktivität stark.

Die entscheidende Eigenschaft: Die Spule **widersteht Stromänderungen**. Sie kann den Strom nicht sprunghaft ändern.

## Grundgrössen

**Spannung beim Stromfluss:**

:::formel
u_L = L * di / dt    # induzierte Gegenspannung (Lenzsche Regel)
:::

**Gespeicherte Energie:**

:::formel
E = L * I^2 / 2    # magnetische Energie, steigt quadratisch mit I
:::

Diese Energie muss beim Abschalten irgendwo hin — daher die gefährlichen Abschaltspannungen (→ [[Selbstinduktion & Induzierte Spannung]]).

## Reihenschaltung

:::schematic L-Reihenschaltung
/schaltplaene/L/l_reihe.svg
:::

Induktivitäten addieren sich in Reihe direkt — wie ohmsche Widerstände:

:::formel
L_ges = L1 + L2 + L3
:::

(Gilt nur ohne magnetische Kopplung zwischen den Spulen.)

## Parallelschaltung

:::schematic L-Parallelschaltung
/schaltplaene/l_parallel.svg
:::

Bei Parallelschaltung addieren sich die Kehrwerte:

:::formel
1 / L_ges = 1 / L1 + 1 / L2
:::

**Sonderfall zwei gleiche Spulen:** L_ges = L/2.

## Kopplung & Gegeninduktivität

Wenn zwei Spulen nahe beieinanderliegen, beeinflusst das Magnetfeld der einen auch die andere. Diese **Gegeninduktivität M** ist die Grundlage für Transformatoren.

:::formel
u_2 = M * di_1 / dt    # in Spule 2 induzierte Spannung durch Strom in Spule 1
:::

Der **Kopplungsfaktor k** gibt an, wie gut die Kopplung ist:

:::formel
k = M / sqrt(L1 * L2)    # 0 = keine Kopplung, 1 = perfekte Kopplung
:::

k = 1 ist nur im idealen Transformator erreichbar (alle Feldlinien koppeln). In der Praxis: Übertrager k ≈ 0,95–0,99; lose gekoppelte Spulen k < 0,1.

## Freilaufdiode

Beim Abschalten einer induktiven Last (Relais, Motor) erzeugt die Spule eine hohe Spannungsspitze (Abschaltspannung), die Halbleiter sofort zerstören kann. Eine **Freilaufdiode** parallel zur Spule (in Sperrrichtung zur Versorgung) leitet diesen Strom um und begrenzt die Spannung auf eine Diodenflussspannung.

:::schematic Freilaufdiode: Induktive Last (Spule L, z.B. Relaisspule) zwischen VCC und Transistor-Kollektor; Freilaufdiode antiparallel zur Spule geschaltet (Kathode an VCC, Anode am Kollektor); Transistor als Schalter unten nach GND; beim Öffnen des Transistors fliesst der Induktionsstrom über die Diode im Kreis
/schaltplaene/spule/freilaufdiode.svg
:::

:::warning
Jede Schaltung, die induktive Lasten (Relais, Motoren, Solenoide) mit Transistoren oder MOSFETs schaltet, **muss** eine Freilaufdiode oder andere Schutzschaltung haben. Ohne Schutz: Sofortausfall des Schaltelements.
:::
