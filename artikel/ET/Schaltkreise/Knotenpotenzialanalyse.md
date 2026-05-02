---
title: Knotenpotenzialanalyse
kategorie: ET
tags: [knotenpotenzial, knotenspannungsverfahren, netzwerkanalyse, kirchhoff, leitwert, KCL, SPICE, MNA, supernode, maschenstromverfahren]
symbol: U_n
einheit: V
---

Die Knotenpotenzialanalyse ist eine systematische Methode zur Berechnung komplexer Netzwerke mit vielen Quellen und Widerständen. Sie liefert alle Knotenspannungen durch Lösen eines Gleichungssystems.

:::hbox
:::vbox
**Voraussetzungen**
- [[Kirchhoffsche Gesetze]]
- [[Strom, Spannung, Widerstand]]
- [[Reihenschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[Wheatstone-Brücke]]
- [[Stern-Dreieck-Transformation]]
:::
:::

---

## Grundidee

Anstatt Maschengleichungen zu schreiben (Maschenstromverfahren), werden Knotengleichungen aufgestellt. An jedem Knoten gilt: Summe aller zufliessenden Ströme = 0 (Kirchhoff 1. Gesetz).

Alle Ströme werden durch Leitwerte (G = 1/R) und Knotenspannungen ausgedrückt.

## Vorgehen Schritt für Schritt

**1. Bezugsknoten (Masse) festlegen**: Einen Knoten als Referenz wählen (Potential = 0 V). Meist der Knoten mit den meisten Verbindungen oder GND.

**2. Unbekannte Knotenspannungen benennen**: Alle anderen Knoten erhalten Variablen U1, U2, U3, ...

**3. KCL an jedem Knoten**: Summe aller Ströme = 0. Strom von Knoten 1 zu Knoten 2 ist (U1 - U2) × G12.

**4. Gleichungssystem lösen**: N-1 Gleichungen für N-1 unbekannte Knotenspannungen (der Bezugsknoten braucht keine Gleichung).

## Beispiel: Drei Knoten, zwei Quellen

Netzwerk: Knoten 1 (U1), Knoten 2 (U2), Bezugsknoten (0 V).
- Spannungsquelle U_Q1 von Bezug zu Knoten 1 → U1 = U_Q1 (bekannt)
- Widerstand R12 zwischen Knoten 1 und 2
- Widerstand R2 von Knoten 2 zu Bezug
- Stromquelle I_Q von Bezug zu Knoten 2

KCL an Knoten 2:
```
(U1 - U2) × G12 + I_Q - U2 × G2 = 0
U2 × (G12 + G2) = U1 × G12 + I_Q
U2 = (U1 × G12 + I_Q) / (G12 + G2)
```

## Matrix-Form (für grössere Netze)

Bei n unbekannten Knoten entsteht ein n×n-Gleichungssystem in Matrix-Form:

```
[G] × [U] = [I]
```

- [G]: Leitwertmatrix (Diagonalelemente: Summe aller Leitwerte am Knoten; Off-Diagonal: negativer Leitwert zwischen den Knoten)
- [U]: Vektor der unbekannten Knotenspannungen
- [I]: Vektor der eingespeisten Ströme (von Quellen)

Lösung durch Gauss-Elimination oder Cramersche Regel.

## Umgang mit Spannungsquellen

**Spannungsquelle zwischen Knoten und Bezug**: Knotenspannung direkt bekannt, Knoten aus den Unbekannten streichen.

**Spannungsquelle zwischen zwei unbekannten Knoten**: Supernode-Methode. Die beiden Knoten werden als ein Superknoten behandelt, die KCL wird um ihn herum aufgestellt.

## Vergleich: Knotenpotenzial vs. Maschenstrom

| Methode | Gleichungen | Gut für |
|---|---|---|
| Knotenpotenzial | N-1 (N = Knoten) | Netze mit vielen Parallelzweigen, Stromquellen |
| Maschenstrom | M (M = unabhängige Maschen) | Netze mit vielen Reihenzweigen, Spannungsquellen |

Beide liefern dasselbe Ergebnis. Die Wahl hängt davon ab, welches System weniger Gleichungen ergibt.

:::tip
Für computergestützte Schaltungssimulation (SPICE) wird intern die Knotenpotenzialanalyse (Modified Nodal Analysis, MNA) verwendet. Das ist der Grund, warum SPICE mit beliebig grossen Netzen umgehen kann.
:::
