---
title: Superposition (Mehrere Quellen)
kategorie: ET
tags: [superposition, überlagerung, mehrere quellen, spannungsquelle, stromquelle, netzwerkanalyse]
groessen: U|Spannung|V; I|Strom|A; R|Widerstand|Ohm
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kirchhoffsche Gesetze]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Erzeuger-Ersatzschaltung (Thévenin)]]
:::
:::vbox
**Führt weiter zu**
- [[Knotenpotenzialanalyse]]
:::
:::

---

Das Superpositionsprinzip erlaubt es, eine Schaltung mit mehreren Quellen in mehrere einfachere Teilprobleme zu zerlegen — jede Quelle wird einzeln betrachtet, die Ergebnisse am Schluss addiert.

## Prinzip

In einem **linearen** Netzwerk ist der Gesamteffekt aller Quellen gleich der Summe der Einzeleffekte. Statt eine komplizierte Schaltung mit mehreren Quellen auf einmal zu lösen, löst man sie mehrfach — aber jedes Mal mit nur einer aktiven Quelle.

Das Superpositionsprinzip gilt nur für **lineare** Netzwerke (Widerstände, lineare Quellen). Bei nichtlinearen Bauteilen wie Dioden oder Transistoren funktioniert es nicht direkt.

## Inaktive Quellen

Um eine Quelle "abzuschalten", wird sie durch ihren **Innenwiderstand** ersetzt — bei einer idealen Quelle:

| Quellentyp | Inaktiv schalten | Warum |
|---|---|---|
| Ideale Spannungsquelle | Kurzschluss (0 V, 0 Ω) | Eine ideale Spannungsquelle hat Ri = 0 Ω |
| Ideale Stromquelle | Leerlauf (0 A, ∞ Ω) | Eine ideale Stromquelle hat Ri = ∞ Ω |
| Reale Quelle | Innenwiderstand Ri bleibt im Kreis | Ri ≠ 0, also nicht einfach kurzschliessen |

:::warning
Eine Spannungsquelle kurzschliessen heisst: die Klemmen direkt verbinden. Nicht das Gerät kurzschliessen — das gilt nur für die Berechnung mit der idealen Quelle.
:::

## Vorgehen Schritt für Schritt

1. **Quelle 1 aktiv**, alle anderen Quellen inaktiv schalten (kurzschliessen / unterbrechen)
2. Strom oder Spannung am gesuchten Element berechnen → Teilergebnis I' oder U'
3. **Quelle 2 aktiv**, alle anderen inaktiv
4. Erneut berechnen → I'' oder U''
5. **Gesamtergebnis addieren**: I = I' + I'' (mit Vorzeichen!)

Das Vorzeichen ist entscheidend: Eine Teilstrom-Komponente, die entgegen der definierten Richtung fliesst, geht mit negativem Vorzeichen in die Summe ein.

## Beispiel

:::schematic
/schaltplaene/schaltkreise/superposition_beispiel.svg
:::

Schaltung: R1 = 100 Ω zwischen A und B, R2 = 200 Ω von B nach GND, Spannungsquelle U1 = 12 V an A, Stromquelle I_Q = 50 mA von B nach GND.

**Schritt 1 — Nur U1 aktiv** (Stromquelle unterbrochen):

R1 und R2 liegen in Reihe: R_ges = 300 Ω.

:::monospace
I' = U1 / (R1 + R2) = 12 / 300 = 40 mA
U'_B = I' * R2 = 40e-3 * 200 = 8 V
:::

**Schritt 2 — Nur I_Q aktiv** (Spannungsquelle kurzgeschlossen):

R1 liegt jetzt parallel zu GND (da A kurzgeschlossen). I_Q teilt sich auf R2 und R1 auf.

:::monospace
U''_B = I_Q * (R1 || R2) = 50e-3 * (100*200 / 300) = 50e-3 * 66.7 = 3.33 V
:::

**Superposition:**

:::monospace
U_B = U'_B + U''_B = 8 + 3.33 = 11.33 V
:::

:::tip
Superposition ist besonders nützlich, wenn eine Quelle eine Gleichspannung (Bias) und eine weitere eine Signalspannung liefert — klassisch in der Verstärkertechnik. Die Gleichanteile und Signalanteile lassen sich getrennt analysieren.
:::
