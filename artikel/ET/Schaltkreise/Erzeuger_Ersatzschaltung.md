---
title: Erzeuger-Ersatzschaltung (Thévenin)
kategorie: ET
tags: [ersatzschaltung, thevenin, norton, innenwiderstand, leerlaufspannung, quellenmodell, klemmenspannung, kurzschlussstrom]
groessen: U0|Leerlaufspannung|V; Ri|Innenwiderstand|Ohm; I|Strom|A; U|Klemmenspannung|V; Ik|Kurzschlussstrom|A; Ra|Lastwiderstand|Ohm
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Spannungs- & Stromteiler]]
:::
:::vbox
**Verwandte Artikel**
- [[Superposition (Mehrere Quellen)]]
:::
:::vbox
**Führt weiter zu**
- [[Leistungsanpassung]]
:::
:::

---

Jede reale Quelle — Batterie, Netzteil, Signalgenerator — lässt sich durch zwei Kennwerte vollständig beschreiben: die **Leerlaufspannung U0** und den **Innenwiderstand Ri**. Diese Erzeuger-Ersatzschaltung (nach Thévenin) vereinfacht die Analyse komplexer Netzwerke erheblich.

## Modell der realen Quelle

Eine **ideale Spannungsquelle** liefert immer exakt die eingestellte Spannung — unabhängig vom Strom. In der Realität sinkt die Klemmenspannung unter Last, weil im Innenwiderstand Ri ein Spannungsfall entsteht.

Das Thévenin-Modell: ideale Spannungsquelle U0 in Reihe mit Innenwiderstand Ri.

:::schematic Erzeuger-Ersatzschaltung
/schaltplaene/schaltkreise/thevenin_ersatzschaltung.svg
:::

## Klemmenspannung unter Last

Wenn ein Lastwiderstand Ra angeschlossen wird, fliesst Strom I. Der Spannungsfall über Ri reduziert die verfügbare Klemmenspannung U.

:::formel
U = U0 - Ri * I    # Klemmenspannung unter Last
:::

:::formel
I = U0 / (Ri + Ra)    # Strom im Lastkreis
:::

Der Strom teilt die Gesamtspannung U0 auf Ri und Ra auf — klassischer [[Spannungs- & Stromteiler|Spannungsteiler]].

:::monospace
Beispiel: Batterie U0 = 12 V, Ri = 0.5 Ohm, Ra = 10 Ohm
I = 12 / (0.5 + 10) = 1.14 A
U = 12 - 0.5 * 1.14 = 11.43 V  (Spannungsfall an Ri: 0.57 V)
:::

## Leerlauf und Kurzschluss

Zwei Extremfälle definieren die Grenzen der Quelle:

**Leerlauf** (Ra → ∞, kein Strom): Die Klemmenspannung entspricht U0 — kein Spannungsfall an Ri.

**Kurzschluss** (Ra = 0): Maximaler Strom, die gesamte Spannung fällt an Ri ab. Der Kurzschlussstrom Ik = U0 / Ri (→ Norton-Abschnitt).

:::warning
Kurzschlussströme können bei kleinen Innenwiderständen sehr hoch werden. Ein Autobatterieakkumulator (Ri ≈ 5 mΩ, U0 = 12,6 V) liefert theoretisch Ik = 12,6 / 0,005 = 2520 A — genug, um Leitungen sofort zu beschädigen oder Brände zu verursachen.
:::

## Thévenin-Ersatzschaltung aus einem Netzwerk bestimmen

Jedes lineare Netzwerk mit Quellen und Widerständen lässt sich auf eine einzige Thévenin-Ersatzschaltung reduzieren — an beliebigen Klemmen A/B:

1. **U0 bestimmen**: Klemmen A/B offen lassen, Spannung zwischen A und B messen oder berechnen (Leerlaufspannung).
2. **Ri bestimmen**: Alle Quellen inaktiv schalten ([[Superposition (Mehrere Quellen)|Superposition]]), dann den Widerstand zwischen A und B messen oder berechnen.

:::monospace
Alternativ Ri aus Messung:
Ri = (U0 - U_Last) / I_Last
:::

## Norton-Ersatzschaltung

Die **Norton-Ersatzschaltung** ist das Dual zu Thévenin: ideale Stromquelle Ik **parallel** mit Ri. Beide Modelle beschreiben dasselbe Verhalten an den Klemmen A/B und sind ineinander umrechenbar.

:::schematic
/schaltplaene/schaltkreise/norton_ersatzschaltung.svg
:::

:::formel
Ik = U0 / Ri    # Kurzschlussstrom = Thévenin-Spannung / Innenwiderstand
:::

| Thévenin | Norton |
|---|---|
| Spannungsquelle U0 in Serie mit Ri | Stromquelle Ik parallel zu Ri |
| Praktisch bei Reihenschaltungen | Praktisch bei Parallelschaltungen |
| U0 = Ik · Ri | Ik = U0 / Ri |
