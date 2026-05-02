---
title: Widerstand
kategorie: ET
tags: [widerstand, bauteil, passiv, farbcode, smd, e-reihen, leistung]
symbol: R
einheit: Ω
---

Das häufigste passive Bauelement. Begrenzt Ströme, teilt Spannungen, wandelt Energie in Wärme um.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[Leitungsauslegung]]
:::
:::

---

## Schaltsymbol

In Europa (IEC): Rechteck mit zwei Anschlüssen.

:::schematic Widerstand (IEC)
/schaltplaene/symbole/R.svg
:::

In Amerika (ANSI): Zickzack-Linie. In Schweizer Schaltplänen wird meistens das IEC-Symbol verwendet.

## Bauformen

**THT (Through Hole)**: Drahtanschlüsse, wird durch die Leiterplatte gesteckt. Einfach zu löten, gut für Prototypen.

**SMD (Surface Mount)**: Flaches Keramikgehäuse, direkt auf die Leiterplatte gelötet. Grösse als Code: 0402, 0603, 0805, 1206 (Zoll × 100).

**Drahtwiderstände**: Widerstandsdraht auf Keramik gewickelt. Für hohe Leistungen bis mehrere hundert Watt.

**Potentiometer**: Einstellbarer Widerstand mit Schleifer. Dient als einstellbarer Spannungsteiler.

## Farbcode (THT)

<!-- TODO: Farben in der Tabelle einfärben sobald der Renderer das unterstützt -->

| Farbe | Ziffer | Multiplikator | Toleranz | TK (ppm/K) |
|---|---|---|---|---|
| Schwarz | 0 | ×1 | — | 250 |
| Braun | 1 | ×10 | ±1 % | 100 |
| Rot | 2 | ×100 | ±2 % | 50 |
| Orange | 3 | ×1 k | — | 15 |
| Gelb | 4 | ×10 k | — | 25 |
| Grün | 5 | ×100 k | ±0.5 % | — |
| Blau | 6 | ×1 M | ±0.25 % | 10 |
| Violett | 7 | ×10 M | ±0.1 % | 5 |
| Grau | 8 | — | ±0.05 % | — |
| Weiss | 9 | — | — | — |
| Gold | — | ×0.1 | ±5 % | — |
| Silber | — | ×0.01 | ±10 % | — |

**4 Ringe**: Ziffer 1 — Ziffer 2 — Multiplikator — Toleranz
Beispiel: Braun-Schwarz-Rot-Gold = 1-0 × 100 = 1 kΩ ±5 %

**5 Ringe**: Ziffer 1 — Ziffer 2 — Ziffer 3 — Multiplikator — Toleranz
Beispiel: Braun-Schwarz-Schwarz-Braun-Braun = 1-0-0 × 10 = 1 kΩ ±1 %

**6 Ringe**: wie 5-Ring, zusätzlich Ring 6 = Temperaturkoeffizient (ppm/K)
Wird bei Präzisionswiderständen eingesetzt, wo Temperaturstabilität wichtig ist.

**0-Ω-Widerstand (THT)**: Ein einzelner schwarzer Ring oder alle Ringe schwarz. Wird als bestückbarer Drahtbrücke verwendet um Leiterbahnen bei der Fertigung flexibel verbinden zu können.

## SMD-Kennzeichnung

**3-stellig** (Standard, E24): Erste zwei Ziffern = Wert, dritte Ziffer = Anzahl Nullen.
Beispiel: `103` = 10 × 10³ = 10 kΩ

**4-stellig** (Präzision, E96): Erste drei Ziffern = Wert, vierte Ziffer = Anzahl Nullen.
Beispiel: `1002` = 100 × 10² = 10 kΩ

**R-Notation**: R steht für das Dezimalkomma.
Beispiel: `R47` = 0.47 Ω, `4R7` = 4.7 Ω, `47R` = 47 Ω

**0-Ω-Widerstand (SMD)**: Aufschrift `000` oder `0`. Funktioniert als bestückbare Drahtbrücke — praktisch für Layoutvarianten oder um Fertigungslinien zu vereinfachen.

## E-Reihen

Widerstände werden nicht in jedem beliebigen Wert gefertigt, sondern in normierten Reihen. Die Abstufungen sind logarithmisch gleichmässig verteilt, sodass sich benachbarte Werte um einen konstanten Faktor unterscheiden.

Der k-te Wert einer E-Reihe mit N Stufen pro Dekade ergibt sich aus:

```
R_k = 10^(k / N)     # k = 0, 1, 2, ... , N-1
```

Die tatsächlichen Normwerte sind auf sinnvolle Stellen gerundet. Die Formel liefert den theoretischen Idealwert.

| Reihe | Werte pro Dekade | Toleranz | Typischer Einsatz |
|---|---|---|---|
| E12 | 12 | ±10 % | Einfache Schaltungen |
| E24 | 24 | ±5 % | Allgemein, am häufigsten |
| E48 | 48 | ±2 % | Präzision |
| E96 | 96 | ±1 % | Messtechnik, Präzision |
| E192 | 192 | ±0.5 % | Höchste Präzision |

**E12-Werte** (Grundwerte, skalierbar mit ×10ⁿ):
1.0 — 1.2 — 1.5 — 1.8 — 2.2 — 2.7 — 3.3 — 3.9 — 4.7 — 5.6 — 6.8 — 8.2

**E24-Werte**:
1.0 — 1.1 — 1.2 — 1.3 — 1.5 — 1.6 — 1.8 — 2.0 — 2.2 — 2.4 — 2.7 — 3.0
3.3 — 3.6 — 3.9 — 4.3 — 4.7 — 5.1 — 5.6 — 6.2 — 6.8 — 7.5 — 8.2 — 9.1

:::tip
Wenn ein berechneter Wert nicht in der E-Reihe existiert, den nächsten verfügbaren Wert wählen und die Auswirkung auf die Schaltung prüfen.
:::

## Verlustleistung

```
P = I^2 * R
P = U^2 / R
P = U * I
```

Die Leistung steigt quadratisch mit dem Strom. Der doppelte Strom bedeutet viermal mehr Wärme.

:::warning
Die Nennleistung ist ein Maximum. Bei hoher Umgebungstemperatur nur 50 bis 70 % davon nutzen (Derating).
:::

## Kenndaten

| Typ | Widerstandsbereich | Toleranz | Nennleistung |
|---|---|---|---|
| Kohleschicht THT | 1 Ω bis 10 MΩ | ±5 % | 0.25 W |
| Metallfilm THT | 1 Ω bis 1 MΩ | ±1 % | 0.25 W |
| SMD 0402 | 1 Ω bis 10 MΩ | ±1 % | 0.063 W |
| SMD 1206 | 1 Ω bis 10 MΩ | ±1 % | 0.25 W |
| Drahtwiderstand | 0.1 Ω bis 100 kΩ | ±5 % | 5 bis 100 W |
