---
title: Schaltalgebra (Boolesche Algebra)
kategorie: SH
kapitel: Logik
tags: [boolesche algebra, schaltalgebra, kommutativgesetz, assoziativgesetz, distributivgesetz, morgansche gesetze, oder-normalform, ringlitechnik, nand-nor-umwandlung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter (UND, ODER, NICHT, NAND, NOR, EXOR)]]
:::
:::vbox
**Führt weiter zu**
- [[Karnaugh-Veitch-Diagramme]]
:::
:::

---

Die **Schaltalgebra** (auch Boolesche Algebra, nach George Boole, 1815–1864) liefert die Rechenregeln, mit denen sich digitale Schaltungen algebraisch beschreiben, umformen und vereinfachen lassen — ganz ähnlich wie die gewohnte Algebra mit Zahlen, nur dass hier ausschliesslich die Werte 0 und 1 vorkommen.

## Grundregeln (Theoreme)

Für die Verknüpfung einer Variablen mit einer Konstanten oder mit sich selbst (bzw. ihrer Negation) gelten feste Regeln:

| UND-Theorem | ODER-Theorem |
|---|---|
| A ∧ 0 = 0 | A ∨ 0 = A |
| A ∧ 1 = A | A ∨ 1 = 1 |
| A ∧ A = A | A ∨ A = A |
| A ∧ Ā = 0 | A ∨ Ā = 1 |

Zusätzlich gilt für die doppelte Negation: Ā̄ = A.

:::merke
Diese acht Regeln sind das kleine Einmaleins der Schaltalgebra — jede Vereinfachung einer Funktionsgleichung lässt sich letztlich auf wiederholte Anwendung dieser Theoreme zurückführen.
:::

## Kommutativ-, Assoziativ- und Distributivgesetz

**Kommutativgesetz**: Die Reihenfolge der Variablen in einer UND- oder ODER-Verknüpfung ist beliebig — sie hat keinen Einfluss auf das Ergebnis: A ∧ B ∧ C = C ∧ A ∧ B.

**Distributivgesetz**: Entspricht dem Ausmultiplizieren bzw. Ausklammern aus der gewohnten Algebra — und ist der wichtigste Hebel beim Vereinfachen von Gleichungen:

| Disjunktives Distributivgesetz | Konjunktives Distributivgesetz |
|---|---|
| (A ∨ B) ∧ (A ∨ C) = A ∨ (B ∧ C) | (A ∧ B) ∨ (A ∧ C) = A ∧ (B ∨ C) |

:::tip
**Trick beim Vereinfachen**: Boolesche Ausdrücke lassen sich vorübergehend in die vertraute "Algebrawelt" übersetzen — ∧ → · (Punkt/Multiplikation), ∨ → + (Plus/Addition). Dort gelten die gewohnten Rechenregeln (ausklammern, ausmultiplizieren), und am Ende rechnet man zurück. Beispiel: Z = (A ∨ B) ∧ (A ∨ C) → Z = (A+B)·(A+C) = AA+AC+BA+BC = A·(1+C)+BA+BC = A+AB+BC = A·(1+B)+BC = A+BC → Z = A ∨ (B ∧ C). Das Ergebnis stimmt mit dem Distributivgesetz überein.
:::

## Bindungsregel

Wie in der normalen Algebra "Punkt vor Strich" gilt, bindet auch in der Schaltalgebra das **UND stets stärker als das ODER**: Z = A ∨ B ∧ C ist gleichbedeutend mit Z = A ∨ (B ∧ C) — man kann sich die Klammern um jede UND-Verknüpfung gedanklich gesetzt vorstellen.

## Die Morganschen Gesetze

Die **Morganschen Gesetze** (nach Augustus De Morgan, 1806–1871) erlauben es, negierte UND-/ODER-Verknüpfungen ineinander umzuwandeln — essenziell, um Schaltungen auf eine einzige Gattersorte (NAND oder NOR) zurückzuführen:

:::formel
**1. Morgansches Gesetz**: ¬(A ∧ B) = Ā ∨ B̄ — eine NAND-Verknüpfung entspricht einer ODER-Verknüpfung der negierten Eingänge

**2. Morgansches Gesetz**: ¬(A ∨ B) = Ā ∧ B̄ — eine NOR-Verknüpfung entspricht einer UND-Verknüpfung der negierten Eingänge
:::

## NAND/NOR-Umwandlung mit der "Ringlitechnik"

In der Praxis werden digitale Schaltungen oft ausschliesslich mit NAND- *oder* NOR-Gattern aufgebaut — das vereinfacht Fertigung und Lagerhaltung. Die **Ringlitechnik** liefert dafür eine einfache, schematische Umwandlungsregel:

:::tip
**Regel der Ringlitechnik**: 
1. Invertiere alle Eingänge **und** den Ausgang des Gatters
2. "Kehre" den logischen Operator um: ∧ → ∨ und ∨ → ∧

Ein UND-Gatter mit invertierten Ein- und Ausgängen verhält sich exakt wie ein ODER-Gatter — und umgekehrt. Diese Äquivalenz folgt direkt aus den Morganschen Gesetzen.
:::

Auf dieselbe Weise lassen sich auch komplexere Funktionsgleichungen Schritt für Schritt in reine NAND- oder NOR-Schaltungen umformen — entweder zeichnerisch mit der Ringlitechnik oder algebraisch mit den Morganschen Gesetzen.

Die systematische **Vereinfachung** solcher Funktionsgleichungen — insbesondere das Erkennen, welche Terme sich zusammenfassen lassen — wird mit dem grafischen Verfahren der → [[Karnaugh-Veitch-Diagramme]] deutlich übersichtlicher als mit rein algebraischem Umformen.
