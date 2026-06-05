---
title: Kirchhoffsche Gesetze
kategorie: ET
tags: [kirchhoff, knotenregel, maschenregel, KCL, KVL, netzwerkanalyse]
groessen: I|Strom|A; U|Spannung|V
_status: PORT  # ET_alt/Schaltkreise/Kirchhoffsche_Gesetze.md
---

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
- [[Knotenpotenzialanalyse]]
- [[Superposition (Mehrere Quellen)]]
:::
:::

---

Die Kirchhoffschen Gesetze sind die Grundlage jeder Schaltungsanalyse. Sie folgen direkt aus der Ladungserhaltung und der Energieerhaltung — und gelten für jede elektrische Schaltung.

:::schematic
/schaltplaene/schaltkreise/kirchhoff_gesetze.svg
:::

## Knotenregel (KCL — Kirchhoff's Current Law)

An jedem Knoten (Verbindungspunkt) einer Schaltung ist die Summe aller zuflies­senden Ströme gleich der Summe aller abfliessenden Ströme. Ladung kann sich nicht ansammeln.

:::formel
sum(I_k, k, 1, n) = 0    # Summe aller Ströme am Knoten = 0
:::

**Vorzeichenregel:** Zuflies­sende Ströme positiv, abfliessende negativ (oder umgekehrt — Hauptsache konsequent).

:::monospace
Beispiel Knoten A:
I1 = 3 A zufliessend
I2 = 1 A abfliessend
I3 = ?
KCL: I1 - I2 - I3 = 0  →  I3 = 2 A
:::

## Maschenregel (KVL — Kirchhoff's Voltage Law)

Die Summe aller Spannungen entlang einer geschlossenen Masche ist null. Was "hinaufgeht", muss auch wieder "herunterkommen" — Energieerhaltung.

:::formel
sum(U_k, k, 1, n) = 0    # Summe aller Spannungen in der Masche = 0
:::

**Vorzeichenregel:** Man legt eine Umlaufrichtung fest. Fällt die Spannung in Umlaufrichtung ab (Verbraucher), ist sie positiv. Steigt sie (Quelle), ist sie negativ — oder umgekehrt, solange es konsequent durchgehalten wird.

:::monospace
Beispiel Masche:
U_Q = 12 V (Quelle)
U_R1 = 4 V, U_R2 = 8 V (Verbraucher)
KVL: -12 + 4 + 8 = 0  ✓
:::

## Anwendung

Die Kirchhoffschen Gesetze bilden zusammen mit dem ohmschen Gesetz ein Gleichungssystem, das jede Schaltung lösbar macht:

1. **Ströme benennen**: An jedem Zweig einen Pfeil mit Namen festlegen (Richtung frei wählbar, falsches Vorzeichen im Ergebnis korrigiert sich selbst).
2. **KCL an n − 1 Knoten** anwenden (der letzte Knoten ist abhängig).
3. **KVL in unabhängigen Maschen** anwenden.
4. Gleichungssystem lösen.

:::tip
Bei grösseren Netzwerken (mehr als 3 Maschen) ist die [[Knotenpotenzialanalyse]] systematischer — sie braucht weniger Gleichungen.
:::

**Gedächtnishilfe:**
- **KCL (Knoten)**: Strom — fliess rein, fliess raus, alles muss aufgehen.
- **KVL (Masche)**: Spannung — was raufgeht, muss wieder runter.
