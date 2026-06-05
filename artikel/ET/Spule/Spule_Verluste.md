---
title: Verluste in der Spule (Güte, Wicklungswiderstand)
kategorie: ET
tags: [verlustfaktor, verlustwinkel, güte, wicklungsverluste, wirbelstrom, hysterese, reale spule, esr]
groessen: d|Verlustfaktor|—; Q|Güte|—; R_Cu|Wicklungswiderstand|Ohm; X_L|Reaktanz|Ohm
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Spule im Wechselstrom]]
:::
:::vbox
**Verwandte Artikel**
- [[Verluste im Kondensator (Güte, ESR)]]
:::
:::vbox
**Führt weiter zu**
- [[RL-Reihenschaltung]]
:::
:::

---

Eine reale Spule ist keine ideale Induktivität — sie hat Verluste durch den ohmschen Wicklungswiderstand, Wirbelströme und Hystereseverluste im Kern. Diese Verluste werden durch die Güte Q (oder den Verlustfaktor d) beschrieben.

## Reale vs. ideale Spule

:::schematic
/schaltplaene/spule/spule_ersatzschaltbild.svg
:::

Eine ideale Spule hat nur Induktivität L und keinen Widerstand. Das reale Ersatzschaltbild zeigt R_Cu in Reihe mit L. Parallel liegt ein Wicklungskapazität C_par (parasitäre Kapazität zwischen den Windungen), die eine Selbstresonanzfrequenz erzeugt:

| Verlustquelle | Ursache | Abhängigkeit |
|---|---|---|
| Wicklungswiderstand R_Cu | Ohmscher Widerstand des Drahtes | Unabhängig von f (bei tiefen f) |
| Skin-Effekt | Stromverdrängung in Draht bei hohem f | Steigt mit sqrt(f) |
| Wirbelstromverluste | Induzierte Kreisströme im Kern | Steigt mit f² |
| Hystereseverluste | Energieaufwand für Ummagnetisierung | Steigt linear mit f |

## Verlustfaktor d und Verlustwinkel delta

Der Verlustfaktor d ist das Verhältnis von Verlustwirkleistung zu Blindleistung — er gibt an, wie "schmutzig" die Spule ist:

:::formel
d = R_Cu / X_L    # Verlustfaktor (dimensionslos)
:::

Der Verlustwinkel delta ist der Phasenwinkel zwischen der idealen Reaktanz und dem realen Impedanzvektor. Bei einer idealen Spule ist delta = 0°.

## Güte Q

Die Güte Q ist der Kehrwert des Verlustfaktors — bei Schwingkreisen ist Q die massgebliche Kenngrösse:

:::formel
Q = X_L / R_Cu    # = 1/d
:::

| Q-Wert | Bewertung | Anwendung |
|---|---|---|
| Q < 10 | Schlecht | Netzdrosseln, Übertrager |
| Q = 10–100 | Gut | Filter, allgemeine Drosseln |
| Q > 100 | Sehr gut | Schwingkreise, HF-Anwendungen |
| Q > 10 000 | Nur mit Quarz erreichbar | Quarzoszillatoren |

## Einfluss auf den Schwingkreis

In einem Serieschwingkreis bestimmt Q direkt die Bandbreite (b = f_r / Q) und die Spannungsüberhöhung an L und C (U_L = Q · U_ein). Eine reale Spule mit kleinem Q macht den Schwingkreis breiter und schwächer.

:::tip
Bei der Spulenauswahl für Schwingkreise immer Q aus dem Datenblatt bei der gewünschten Frequenz prüfen — Q ist frequenzabhängig und sinkt bei sehr hohen Frequenzen durch Skin-Effekt und Kernverluste wieder.
:::
