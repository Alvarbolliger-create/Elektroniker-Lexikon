---
title: Logikgatter (UND, ODER, NICHT, NAND, NOR, EXOR)
kategorie: SH
kapitel: Logik
tags: [und-gatter, oder-gatter, nicht-gatter, nand, nor, exor, exnor, wahrheitstabelle, funktionsgleichung, schaltzeichen]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale (Analog, Digital, Binär)]]
:::
:::vbox
**Führt weiter zu**
- [[Schaltalgebra (Boolesche Algebra)]]
- [[Logikfamilien (TTL, CMOS, BiCMOS, ECL)]]
:::
:::

---

**Logikgatter** sind die elementaren Bausteine jeder digitalen Schaltung. Jedes Gatter bildet eine binäre Eingangskombination nach einer festen Regel auf einen binären Ausgang ab. Aus diesen wenigen Grundverknüpfungen lässt sich — wie aus Buchstaben ein ganzer Text — jede beliebig komplexe digitale Schaltung aufbauen.

## Die drei logischen Grundverknüpfungen

| Verknüpfung | Schaltzeichen | Funktionsgleichung | Sprechweise |
|---|---|---|---|
| **UND (AND)** | & | Z = A ∧ B | Konjunktiv — Z = 1, wenn A **und** B = 1 |
| **ODER (OR)** | ≥1 | Z = A ∨ B | Disjunktiv — Z = 1, wenn A **oder** B = 1 |
| **NICHT (NOT)** | 1 | Z = Ā | Negation — kehrt den Eingang um |

| A | B | UND | ODER |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

:::merke
Eine **Wahrheitstabelle** listet für jede mögliche Eingangskombination den zugehörigen Ausgangswert auf. Bei n Eingängen hat sie 2ⁿ Zeilen. Die **Funktionsgleichung** beschreibt denselben Zusammenhang algebraisch.
:::

## Die negierten Verknüpfungen: NAND, NOR, EXOR, EXNOR

Aus den Grundverknüpfungen lassen sich durch Negation und Kombination weitere wichtige Gatter ableiten:

| Verknüpfung | Funktionsgleichung | Bedeutung |
|---|---|---|
| **NAND** (Not-AND) | Z = ¬(A ∧ B) | UND-Gatter mit negiertem Ausgang |
| **NOR** (Not-OR) | Z = ¬(A ∨ B) | ODER-Gatter mit negiertem Ausgang |
| **EXOR** (Exklusiv-Oder, Antivalenz) | Z = (A ∧ B̄) ∨ (Ā ∧ B) | Z = 1, wenn A und B **unterschiedlich** sind |
| **EXNOR** (Äquivalenz) | Z = (A ∧ B) ∨ (Ā ∧ B̄) | Z = 1, wenn A und B **gleich** sind |

:::tip
EXOR lässt sich auch als "Ungleichheits-Detektor" lesen, EXNOR als "Gleichheits-Detektor". Genau diese Eigenschaft macht das EXOR zum zentralen Baustein von Addierern (→ [[Addierer (Halbaddierer, Volladdierer)]]) und steuerbaren Invertern (→ [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)]]).
:::

## Schaltzeichen

In Schaltplänen begegnen je nach Norm und Herkunft unterschiedliche Symbole für dieselben Gatter:

| Funktion | Neue DIN 40900 | Amerikanisch |
|---|---|---|
| NICHT | 1 — mit Kreis am Ausgang | Dreieck mit Kreis |
| UND | & | D-Form |
| ODER | ≥1 | gewölbte Form |
| EXOR | =1 | gewölbte Form mit Doppellinie |

:::info
Integrierte Logikbausteine fassen mehrere gleichartige Gatter in einem Gehäuse zusammen — z. B. enthält ein 74LS00 (NAND) oder ein 74LS04 (NOT) jeweils vier bzw. sechs Gatter in einem 14-poligen IC. → [[Logikfamilien (TTL, CMOS, BiCMOS, ECL)]]
:::

## Signal-Zeit-Diagramm

Neben der Wahrheitstabelle lässt sich das Verhalten eines Gatters auch im **Signal-Zeit-Diagramm** darstellen: Die Eingangs- und Ausgangspegel werden über der Zeitachse aufgetragen. So wird sichtbar, *wann* sich der Ausgang ändert — wichtig, um das dynamische Verhalten realer Schaltungen (Verzögerungen, Störimpulse) zu verstehen.

Aus den drei Grundverknüpfungen UND, ODER, NICHT lässt sich **jede** beliebige digitale Funktion aufbauen — das ist die Grundaussage der → [[Schaltalgebra (Boolesche Algebra)]], mit der sich solche Funktionen systematisch beschreiben und vereinfachen lassen.
