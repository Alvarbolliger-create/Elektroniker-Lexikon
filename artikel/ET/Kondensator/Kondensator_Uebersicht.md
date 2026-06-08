---
title: Kondensator (Übersicht)
kategorie: ET
tags: [kondensator, kapazität, grundlagen, serie, parallel, ladung, energie]
groessen: C|Kapazität|F; Q|Ladung|C; U|Spannung|V; C_ges|Gesamtkapazität|F
_status: PORT  # ET_alt/Kondensator/Kondensator_Uebersicht.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Elektrisches Feld]]
:::
:::vbox
**Verwandte Artikel**
- [[Spule (Übersicht)]]
:::
:::vbox
**Führt weiter zu**
- [[Kondensator Typen]]
- [[Plattenkondensator & Influenz]]
- [[Kapazität & Einheiten]]
- [[Auf- und Entladung (Kondensator)]]
:::
:::

---

:::schematic
/schaltplaene/kondensator/kondensator_symbol.svg
:::

Ein Kondensator speichert elektrische Ladung zwischen zwei leitenden Flächen, die durch ein Dielektrikum getrennt sind. Er ist nach der Spule das zweite wichtige reaktive Bauteil — und er verhält sich bei Wechselstrom genau umgekehrt.

## Was ist ein Kondensator?

Zwei leitende Flächen (Elektroden) mit einem Isoliermaterial (Dielektrikum) dazwischen. Wird eine Spannung angelegt, sammeln sich Ladungen an den Elektroden und ein elektrisches Feld entsteht. Die gespeicherte Ladung ist proportional zur Spannung:

:::formel
Q = C * U
:::

Der Kondensator "merkt sich" die angelegte Spannung — er ist ein Spannungsspeicher. Im Gegensatz zur Spule (Stromspeicher) kann die Spannung am Kondensator nicht sprunghaft wechseln.

## Serieschaltung

:::schematic C-Reihenschaltung
/schaltplaene/C/c_reihe.svg
:::

Bei der Serieschaltung von Kondensatoren teilt sich die Spannung auf, aber alle tragen dieselbe Ladung (Knotenregel für Ladung). Der Gesamtkapazitätswert ist kleiner als der kleinste Einzelwert — umgekehrt wie bei Widerständen.

:::formel
1 / C_ges = 1 / C1 + 1 / C2 + 1 / C3
:::

**Sonderfall zwei gleiche Kondensatoren:** C_ges = C/2 (Kapazität halbiert sich).

### Spannungsverteilung bei Reihenschaltung

Da alle Kondensatoren dieselbe Ladung Q tragen, folgt die Spannung direkt aus Q = C · U:

:::formel
Q = C_ges * U_ges    # Gesamtladung berechnen
U_n = Q / C_n        # Spannung am einzelnen Kondensator
:::

Für zwei Kondensatoren direkt (ohne Q):

:::formel
U1 = U_ges * C2 / (C1 + C2)    # kleiner C → grössere Spannung!
U2 = U_ges * C1 / (C1 + C2)
:::

:::monospace
Beispiel: C1 = 4.7 nF, C2 = 1000 nF, U = 100 V
C_ges = (4.7 * 1000) / (4.7 + 1000) = 4.68 nF
Q = 4.68e-9 * 100 = 468 nC
U1 = 468e-9 / 4.7e-9  = 99.6 V  (fast die gesamte Spannung!)
U2 = 468e-9 / 1000e-9 = 0.47 V
Probe: 99.6 + 0.47 ≈ 100 V ✓
:::

:::warning
Der kleinere Kondensator trägt die grössere Spannung — genau umgekehrt zu Widerständen! Bei stark unterschiedlichen Kapazitäten immer die Spannungsfestigkeit des kleineren prüfen.
:::

**Anwendung:** Zwei Kondensatoren in Reihe erhöhen die effektive Spannungsfestigkeit — jeder trägt nur die halbe Spannung. Unpolarisierter Betrieb eines Elektrolytkondensators.

## Parallelschaltung

:::schematic C-Parallelschaltung
/schaltplaene/C/c_parallel.svg
:::

Bei der Parallelschaltung liegt an allen die gleiche Spannung. Die Gesamtkapazität addiert sich direkt — wie Leitwerte bei Widerständen.

:::formel
C_ges = C1 + C2 + C3
:::

**Merkmal:** C_ges ist immer grösser als der grösste Einzelwert.

**Anwendung:** Mehrere Kondensatoren parallel erhöhen die nutzbare Kapazität. Bypass-Kondensatoren (z. B. 100 µF Elko + 100 nF Keramik parallel) kombinieren grosse Kapazität mit gutem Hochfrequenzverhalten.

## Kondensator im Vergleich zur Spule

| Eigenschaft | Kondensator C | Spule L |
|---|---|---|
| Speichert | Spannung (elektrisches Feld) | Strom (magnetisches Feld) |
| Gleichstrom | Sperrt (X_C → ∞) | Lässt durch (X_L = 0) |
| Hohe Frequenz | Lässt durch (X_C → 0) | Sperrt (X_L → ∞) |
| Phasenverschiebung | Strom eilt vor (−90°) | Spannung eilt vor (+90°) |
| Serieschaltung | Kehrwerte addieren | Direkt addieren |
| Parallelschaltung | Direkt addieren | Kehrwerte addieren |

:::tip
Kondensatoren und Spulen sind in allen Formeln "dual" — was für R bei der Reihenschaltung gilt, gilt für G (Leitwert) bei der Parallelschaltung. Dasselbe Prinzip verbindet C und L.
:::
