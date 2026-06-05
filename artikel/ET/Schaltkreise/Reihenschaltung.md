---
title: Reihenschaltung
kategorie: ET
tags: [reihenschaltung, serie, gesamtwiderstand, teilspannung, spannungsteiler]
groessen: R|Widerstand|Ohm; U|Spannung|V; I|Strom|A
_status: PORT  # ET_alt/Schaltkreise/Reihenschaltung.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Parallelschaltung]]
- [[Kirchhoffsche Gesetze]]
:::
:::vbox
**Führt weiter zu**
- [[Spannungs- & Stromteiler]]
:::
:::

---

Bei der Reihenschaltung sind alle Widerstände hintereinander geschaltet — durch alle fliesst derselbe Strom. Die Gesamtspannung verteilt sich auf die einzelnen Teilspannungen.

:::schematic
/schaltplaene/schaltkreise/reihenschaltung.svg
:::

## Gesamtwiderstand

Die Gesamtwiderstände addieren sich direkt. Je mehr Widerstände in Reihe, desto grösser der Gesamtwiderstand.

:::formel
R_ges = R1 + R2 + R3    # beliebig viele Glieder addierbar
:::

**Merkmal**: R_ges ist immer grösser als der grösste Einzelwiderstand.

## Strom

Der gleiche Strom fliesst durch alle Glieder — die Reihe ist ein einziger Strompfad.

:::formel
I = U_ges / R_ges
:::

## Teilspannungen

Die Spannung an jedem Widerstand ist proportional zu seinem Widerstandswert. Das folgt direkt aus dem ohmschen Gesetz (U_k = I · R_k) und der Maschenregel.

:::formel
U_k = U_ges * R_k / R_ges    # Spannungsteilerregel
:::

Die Summe aller Teilspannungen ergibt die Gesamtspannung (Maschenregel):

:::formel
U_ges = U1 + U2 + U3
:::

:::monospace
Beispiel: U_ges = 12 V, R1 = 100 Ohm, R2 = 200 Ohm
R_ges = 300 Ohm
I = 12 / 300 = 40 mA
U1 = 12 * 100 / 300 = 4 V
U2 = 12 * 200 / 300 = 8 V
Probe: 4 + 8 = 12 V ✓
:::

## Besonderheiten

**Unterbrechung**: Wird ein Glied unterbrochen (unendlicher Widerstand), ist der Gesamtstrom null — alle anderen Widerstände tragen keine Spannung mehr.

**Kurzschluss**: Wird ein Glied kurzgeschlossen (R = 0), entfällt seine Teilspannung. Der Strom steigt, da R_ges kleiner wird.

:::tip
Der [[Spannungs- & Stromteiler|Spannungsteiler]] ist eine direkte Anwendung der Reihenschaltung: zwei Widerstände teilen eine Spannung im Verhältnis R1 : R2. Weit verbreitet zur Pegelanpassung und in Sensorbeschaltungen.
:::
