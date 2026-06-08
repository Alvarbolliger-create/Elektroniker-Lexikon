---
title: Addierer: Ripple-Carry & Carry-Lookahead
kategorie: SH
tags: [addierer, ripple-carry, carry-lookahead, übertrag, ALU, halbaddierer, volladdierer, CLA, propagation, kogge-stone, prefix-addierer]
symbol: —
einheit: —
---

Binäre Addierer sind Grundbausteine der ALU. Die einfachste Variante (Ripple-Carry) ist langsam. Der Carry-Lookahead-Addierer berechnet alle Überträge parallel und ist wesentlich schneller.

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter]]
- [[Binäre Arithmetik]]
- [[Schaltalgebra]]
:::
:::vbox
**Verwandte Artikel**
- [[CPU Aufbau]]
- [[FPGA]]
:::
:::

---

## Halbaddierer (Half Adder)

Addiert zwei 1-Bit-Zahlen. Kein Eingangs-Carry.

:::formel
S = A XOR B     # Summenbit
C = A AND B     # Übertrag (Carry)
:::
Kann nur das unterste Bit addieren.

## Volladdierer (Full Adder)

Addiert drei Bits: A, B und Eingangs-Carry Cin.

:::formel
S = A XOR B XOR Cin
Cout = (A AND B) OR (Cin AND (A XOR B))
:::
## Ripple-Carry-Addierer

N Volladdierer in Reihe. Der Übertrag "rippt" von Bit zu Bit durch die Kette.

:::formel
Bit 0: FA → Carry0
Bit 1: FA (mit Carry0) → Carry1
Bit 2: FA (mit Carry1) → Carry2
...
Bit N: FA (mit Carry_N-1) → Summe fertig
:::
**Problem**: Die Laufzeit wächst linear mit der Bitbreite. Ein 64-Bit-Addierer muss auf 64 Carry-Propagationen warten. Bei schnellen CPUs ist das inakzeptabel.

Laufzeit: `t_gesamt = N × t_FA`

## Carry-Lookahead-Addierer (CLA)

Der CLA berechnet alle Überträge gleichzeitig (parallel), bevor die Summen berechnet werden.

**Zwei Hilfsgrössen pro Bitstelle**:
- Generate: `G_i = A_i AND B_i` — Übertrag wird erzeugt, egal was Cin ist
- Propagate: `P_i = A_i XOR B_i` — eingehender Übertrag wird weitergeleitet

**Übertragsberechnung** (alle parallel):
:::formel
C1 = G0 OR (P0 AND C0)
C2 = G1 OR (P1 AND C1) = G1 OR (P1 AND G0) OR (P1 AND P0 AND C0)
C3 = G2 OR (P2 AND G1) OR (P2 AND P1 AND G0) OR (P2 AND P1 AND P0 AND C0)
:::
Jeder Carry hängt nur von G_i, P_i und C0 ab — alles bekannt vor dem ersten Gatterdelay!

**Laufzeit**: Unabhängig von N (für den Carry). Insgesamt 2–3 Gatterdelays für jeden Carry.

## Laufzeit-Vergleich

| Addierer | Laufzeit 64 Bit |
|---|---|
| Ripple-Carry | 64 × t_FA ≈ 128 Gatterdelays |
| Carry-Lookahead (4-bit Gruppen) | ≈ 6–8 Gatterdelays |

## Gruppenstruktur

Für grosse Bitbreiten wird CLA in Gruppen aufgebaut:
- Gruppen-CLA (4-Bit-Blöcke mit CLA intern)
- Zweistufiger CLA: CLA auf Gruppenebene + CLA auf Block-Gruppenebene

Moderne CPUs nutzen Hybridstrukturen (Prefix-Addierer, Kogge-Stone, Brent-Kung) für optimale Laufzeit und Gatteranzahl.

## Anwendung

Jede ALU in Mikroprozessoren, FPGAs und DSPs enthält einen schnellen Addierer. FPGA-Carry-Chains sind hardverdrahtete Ripple-Carry-Strukturen mit sehr kurzen Delays (optimiert durch die physische Nähe der Carry-Leitungen).
