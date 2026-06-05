---
title: Kirchhoffsche Gesetze
kategorie: ET
tags: [kirchhoff, knotenregel, maschenregel, netzwerk, knotenspannungsanalyse, maschenstromanalyse, superposition, schaltungsanalyse, netzwerkanalyse]
symbol: —
einheit: —
---

Zwei Regeln für die Analyse von Schaltungen. Eine gilt an Knoten, die andere in geschlossenen Maschen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[Spannungs- & Stromteiler]]
:::
:::vbox
**Führt weiter zu**
- [[Spannungs- & Stromteiler]]
- [[Wheatstone-Brücke]]
:::
:::

---

:::schematic Knotenregel und Maschenregel
/schaltplaene/kirchhoff.svg
:::

## 1. Gesetz: Knotenregel

An jedem Verzweigungspunkt ist die Summe der zufliessenden Ströme gleich der Summe der abfliessenden. Elektronen können sich nicht ansammeln.

:::formel
I_zu1 + I_zu2 = I_ab1 + I_ab2
:::
Allgemeine Schreibweise:

:::formel
ΣI = 0     # Summe aller Ströme am Knoten (Vorzeichen beachten)
:::
## 2. Gesetz: Maschenregel

Die Summe aller Spannungen in einer geschlossenen Masche ist null. Was die Quelle liefert, fällt über den Widerständen ab.

:::formel
U_quelle - U_R1 - U_R2 = 0
:::
Allgemeine Schreibweise:

:::formel
ΣU = 0     # Summe aller Spannungen in der Masche (Umlaufrichtung einhalten)
:::
:::warning
Konsequente Vorzeichen sind entscheidend. Eine Umlaufrichtung wählen und durchhalten, z.B. immer im Uhrzeigersinn. Ein Vorzeichenfehler führt zu einem falschen Ergebnis ohne Hinweis.
:::

## Beispiel

Schaltung: 12 V Quelle, R1 = 100 Ω in Reihe, danach Parallelzweig R2 = 200 Ω und R3 = 300 Ω.

| Grösse | Berechnung | Ergebnis |
|---|---|---|
| R2 \|\| R3 | (200 × 300) / (200 + 300) | 120 Ω |
| R_ges | 100 + 120 | 220 Ω |
| I_ges | 12 V / 220 Ω | 54.5 mA |
| U an R1 | 54.5 mA × 100 Ω | 5.45 V |
| U an R2/R3 | 12 V − 5.45 V | 6.55 V |
| I durch R2 | 6.55 V / 200 Ω | 32.7 mA |
| I durch R3 | 6.55 V / 300 Ω | 21.8 mA |
| Probe Knotenregel | 32.7 + 21.8 ≈ 54.5 mA | ✓ |
| Probe Maschenregel | 5.45 + 6.55 = 12 V | ✓ |

## Anwendung

Für komplexe Netzwerke stellt man ein Gleichungssystem auf. Knotenregel an jedem Knoten, Maschenregel in jeder Masche. Das System lösen liefert alle Ströme und Spannungen.

:::tip
Superposition: Mehrere Quellen einzeln berechnen, alle anderen kurzschliessen, Ergebnisse addieren.
:::
