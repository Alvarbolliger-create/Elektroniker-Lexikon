---
title: Magnetfelder
kategorie: ET
tags: [magnetfeld, feldlinien, rechte-hand-regel, durchflutung, feldstärke, flussdichte, fluss, permeabilität]
groessen: H|Feldstärke|A/m; B|Flussdichte|T; Phi|Fluss|Wb; Theta|Durchflutung|A; mu_r|relative Permeabilität|—; mu_0|Feldkonstante|H/m
_status: PORT  # ET_alt/Magnetfelder/Magnetfelder.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
- [[Lorentzkraft]]
- [[Magnetisierungskurve & Hysterese]]
:::
:::vbox
**Führt weiter zu**
- [[Spule (Übersicht)]]
- [[Transformator Aufbau]]
- [[Magnetischer Widerstand (Reluktanz)]]
:::
:::

---

Magnetfelder entstehen um jeden stromdurchflossenen Leiter und um Permanentmagnete. Sie sind die Grundlage für Transformatoren, Motoren, Relais und die Selbstinduktion der Spule.

## Feldlinien & Rechte-Hand-Regel

Magnetische Feldlinien verlaufen in geschlossenen Schleifen — sie haben keinen Anfang und kein Ende. Die Richtung gibt an, von welchem Pol die Feldlinien "heraustreten" (Nord) und wo sie "eintreten" (Süd).

**Rechte-Hand-Regel** für einen geraden Leiter: Daumen in Stromrichtung, die gekrümmten Finger zeigen die Richtung des Magnetfeldes (Kreise um den Leiter).

:::schematic Rechte-Hand-Regel: Links: gerader Leiter (vertikal), Strom I nach oben (Pfeil); konzentrische Kreise als Magnetfeldlinien um den Leiter, Richtung gemäss Rechtsschraube (Uhrzeigersinn von oben gesehen); Rechts: Solenoid-Spule mit Stromrichtung in Wicklung; Magnetfeldlinien im Innern als Längslinien, aussen als geschlossene Schleifen; Daumen zeigt auf Nordpol; Beschriftung: I, B, N, S
/abbildungen/magnetfelder/rechte_hand_regel.svg
:::

**Rechte-Hand-Regel** für eine Spule: Finger in Wicklungsrichtung des Stroms, Daumen zeigt auf den Nordpol.

## Magnetische Durchflutung

Die Durchflutung Theta (auch: "magnetomotorische Kraft") gibt an, wie viel "Antrieb" für das Magnetfeld vorhanden ist. Bei einer Spule multipliziert sich der Strom mit der Windungszahl:

:::formel
Theta = N * I    # Durchflutung in Ampere (A)
:::

## Magnetische Feldstärke H

Die Feldstärke H beschreibt, wie stark das Feld im Material ist — unabhängig vom Material selbst. Bei einer langen Spule (Toroid, Solenoid) gilt:

:::formel
H = N * I / l    # l = Länge des magnetischen Pfades (m)
:::

**Einheit:** A/m (Ampere pro Meter).

## Magnetische Flussdichte B

Die Flussdichte B (auch: "magnetische Induktion") beschreibt das Feld im Material — sie hängt von H und vom Werkstoff ab:

:::formel
B = mu_0 * mu_r * H    # B in Tesla (T)
:::

| Grösse | Wert |
|---|---|
| Vakuum-Permeabilität mu_0 | 4π · 10⁻⁷ H/m ≈ 1,257 · 10⁻⁶ H/m |
| Luft, mu_r | ≈ 1 |
| Weicheisen, mu_r | 1 000 – 10 000 |
| Ferrit (Mn-Zn), mu_r | 1 000 – 15 000 |

Ein hoher mu_r-Wert bedeutet: Das Material "leitet" das Magnetfeld viel besser als Luft — deshalb werden Transformatoren und Motoren mit Eisenkern gebaut.

## Magnetischer Fluss

Der magnetische Fluss Phi beschreibt die Gesamtmenge an Feldlinien durch eine Fläche A:

:::formel
Phi = B * A    # Phi in Weber (Wb = V·s), A senkrecht zum Feld
:::

**Einheit:** Weber (Wb). 1 Wb = 1 V·s.

Der Zusammenhang mit der Selbstinduktion: Ändert sich Phi, wird in der Spule eine Spannung induziert → [[Selbstinduktion & Induzierte Spannung]].

## Zusammenhängende Berechnung

Alle Grössen sind verkettet: Strom und Wicklung bestimmen Θ, daraus folgt H, daraus B, daraus Φ. Die Reihenfolge ist immer gleich.

:::formel
Θ = N * I          # Schritt 1: Durchflutung
H = Θ / l          # Schritt 2: Feldstärke
B = mu_0 * mu_r * H    # Schritt 3: Flussdichte
Phi = B * A        # Schritt 4: Fluss
:::

:::monospace
Beispiel: N = 100, I = 2 A, l = 0.2 m, mu_r = 1000, A = 200 mm²

Θ   = 100 · 2             = 200 A
H   = 200 / 0.2           = 1000 A/m
B   = 1.257e-6 · 1000 · 1000 = 1.26 T
Φ   = 1.26 · 200e-6       = 252 µWb
:::

:::tip
Die Analogie zum elektrischen Stromkreis hilft beim Verständnis: H ↔ E-Feld, B ↔ Stromdichte, Phi ↔ Strom, Theta ↔ Spannung, magnetischer Widerstand ↔ ohmscher Widerstand → [[Magnetischer Widerstand]].
:::
