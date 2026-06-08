---
title: Addierer (Halbaddierer, Volladdierer)
kategorie: SH
kapitel: Digitaltechnik
tags: [halbaddierer, volladdierer, summe, uebertrag, addierwerk, alu]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)]]
- [[Logikgatter (UND, ODER, NICHT, NAND, NOR, EXOR)]]
:::
:::vbox
**Führt weiter zu**
- [[Rechnerarchitekturen (CISC, RISC, DSP)]]
:::
:::

---

Jede → [[Rechnerarchitekturen (CISC, RISC, DSP)|Recheneinheit]] eines Prozessors muss im Kern eine einzige Grundoperation beherrschen: die binäre Addition. Aus zwei elementaren Bausteinen — dem **Halbaddierer** und dem **Volladdierer** — lässt sich jedes beliebig breite Addierwerk aufbauen.

## Der Halbaddierer

Ein **Halbaddierer (HA)** addiert zwei einzelne Bits A und B und liefert dabei zwei Ausgänge: die **Summe** S und den **Übertrag** (Carry) C in die nächsthöhere Stelle:

| A | B | S (Summe) | C (Übertrag) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

:::merke
Aus der Wahrheitstabelle lassen sich die beiden Verknüpfungsgleichungen direkt ablesen: Die Summe entspricht einer **EXOR-Verknüpfung** (S = A ⊻ B — "1, wenn die Eingänge unterschiedlich sind"), der Übertrag entspricht einer **UND-Verknüpfung** (C = A ∧ B — "1, nur wenn beide Eingänge gesetzt sind"). Ein Halbaddierer besteht damit aus genau zwei Gattern: einem EXOR und einem UND.
:::

Der Name "Halb"-Addierer verrät bereits seine Einschränkung: Er kann keinen von einer vorherigen Stelle kommenden Übertrag mit verarbeiten — für eine mehrstellige Addition reicht er deshalb nicht aus.

## Der Volladdierer

Der **Volladdierer (VA)** schliesst genau diese Lücke: Er verarbeitet zusätzlich zu den beiden Operandenbits A und B auch einen **Übertragseingang** Cᵢₙ (Carry-In) aus der vorherigen Stelle und liefert wiederum Summe S und Übertragsausgang Cₒᵤₜ (Carry-Out):

| A | B | Cᵢₙ | S | Cₒᵤₜ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

:::tip
Ein Volladdierer lässt sich elegant aus **zwei Halbaddierern und einem ODER-Gatter** zusammensetzen: Der erste Halbaddierer addiert A und B, der zweite addiert dieses Zwischenergebnis mit Cᵢₙ — die Summe S ergibt sich am Ausgang des zweiten Halbaddierers. Die beiden Übertragsausgänge der Halbaddierer werden mit einem ODER-Gatter zu Cₒᵤₜ zusammengeführt (es kann ja niemals in beiden Halbaddierern gleichzeitig ein Übertrag entstehen). So entsteht aus zwei einfachen Bausteinen ein vollwertiger 1-Bit-Volladdierer mit Übertragsverarbeitung in beide Richtungen.
:::

## Mehrstellige Addierwerke: Carry-Ripple-Addierer

Reiht man mehrere Volladdierer aneinander und verbindet jeweils den Übertragsausgang Cₒᵤₜ einer Stelle mit dem Übertragseingang Cᵢₙ der nächsthöheren Stelle, entsteht ein **paralleles Addierwerk**, das ganze Binärwörter auf einen Schlag addiert. Ein bekannter integrierter Vertreter ist der **74283** — ein fertiger 4-Bit-Volladdierer, der zwei 4-Bit-Operanden plus einen Übertrag addiert und Summe sowie Übertragsausgang liefert.

:::warning
Bei diesem sogenannten **Carry-Ripple-Prinzip** muss sich der Übertrag von Stufe zu Stufe "durchwellen" (engl. *to ripple*), bevor das Endergebnis feststeht — die letzte Stelle kann ihre Summe erst dann sicher ausgeben, wenn der Übertrag durch alle vorangehenden Stufen hindurchgelaufen ist. Bei breiten Addierwerken (32 Bit, 64 Bit) summiert sich diese Durchlaufzeit zu einer spürbaren Verzögerung — ein Grund, weshalb moderne Prozessoren auf schnellere Verfahren wie den **Carry-Look-Ahead-Addierer** setzen, der den Übertrag für alle Stufen gleichzeitig vorausberechnet.
:::

## Subtraktion mit demselben Baustein

Ein praktischer Vorteil des Volladdierers: Mit Hilfe des → [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)|Zweierkomplements]] lässt sich auch die **Subtraktion** auf eine Addition zurückführen — der Subtrahend wird dazu bitweise invertiert und über den anfänglichen Übertragseingang (Cᵢₙ = 1) automatisch um 1 erhöht. Dasselbe Addierwerk kann so — je nach Steuersignal — sowohl addieren als auch subtrahieren, was den Schaltungsaufwand einer → [[Rechnerarchitekturen (CISC, RISC, DSP)|arithmetisch-logischen Einheit (ALU)]] erheblich reduziert.
