---
title: Schaltalgebra
kategorie: SH
tags: [schaltalgebra, boolesche algebra, logik, vereinfachung, karnaughdiagramm, de-morgan, DNF, KNF, minterm, maxterm, normalform]
symbol: —
einheit: —
---

Die Schaltalgebra ist die Mathematik hinter digitalen Schaltungen. Mit ihr lassen sich Logikfunktionen vereinfachen und Gatterschaltungen optimieren.

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter]]
:::
:::vbox
**Verwandte Artikel**
- [[Binäre Arithmetik]]
:::
:::vbox
**Führt weiter zu**
- [[Flipflops]]
- [[Multiplexer & Demultiplexer]]
- [[Karnaugh-Veitch-Diagramm (KVD)]]
:::
:::

---

## Grundoperationen

Drei Grundoperationen: AND (Konjunktion), OR (Disjunktion), NOT (Negation).

Schreibweise: A AND B = A · B, A OR B = A + B, NOT A = A̅

## Wichtige Gesetze

| Gesetz | AND-Form | OR-Form |
|---|---|---|
| Identität | A · 1 = A | A + 0 = A |
| Null | A · 0 = 0 | A + 1 = 1 |
| Idempotenz | A · A = A | A + A = A |
| Komplement | A · A̅ = 0 | A + A̅ = 1 |
| De Morgan | (A · B)̅ = A̅ + B̅ | (A + B)̅ = A̅ · B̅ |

## De Morgansches Gesetz

Das wichtigste Gesetz für die Praxis. Es beschreibt, wie NAND und NOR zusammenhängen.

NAND(A, B) = NOT(A AND B) = NOT(A) OR NOT(B)

Das heisst: Ein NAND-Gatter mit invertierten Eingängen entspricht einem OR-Gatter.

## Normalformen

**DNF (Disjunktive Normalform)**: OR-Verknüpfung von AND-Termen (Minterme). Jeder AND-Term beschreibt eine Zeile mit Ausgang = 1 in der Wahrheitstabelle.

```
F = A̅·B̅·C + A̅·B·C + A·B̅·C + A·B·C = ... = C    # Beispiel DNF
```

**KNF (Konjunktive Normalform)**: AND-Verknüpfung von OR-Termen (Maxterme). Jeder OR-Term beschreibt eine Zeile mit Ausgang = 0.

**Minterm** (m_i): Ein Produktterm bei dem alle Variablen vorkommen. Er ist 1 für genau eine Eingangskombination.  
**Maxterm** (M_i): Ein Summenterm bei dem alle Variablen vorkommen. Er ist 0 für genau eine Eingangskombination.

Kurznotation: F = Σm(1,3,5,7) bedeutet: Minterme 1, 3, 5, 7 sind 1.

## Vereinfachung

Komplexe Logikfunktionen lassen sich algebraisch oder mit dem [[Karnaugh-Veitch-Diagramm (KVD)]] vereinfachen. Weniger Gatter bedeuten kleinere Schaltung, weniger Verbrauch.

Beispiel algebraisch: A · B + A · B̅ = A · (B + B̅) = A · 1 = A

:::tip
De Morgan auswendig kennen. Es ist der schnellste Weg um Gatterschaltungen umzuformen, zum Beispiel wenn man nur NAND-Gatter zur Verfügung hat.
:::
