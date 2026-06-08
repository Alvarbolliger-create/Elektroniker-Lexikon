---
title: Verluste im Kondensator (Güte, ESR)
kategorie: ET
tags: [verlustfaktor, verlustwinkel, güte, esr, realer kondensator, dissipation, ripplestrom]
groessen: d|Verlustfaktor|—; Q|Güte|—; ESR|Äquivalenter Serienwiderstand|Ohm; X_C|Reaktanz|Ohm
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kondensator im Wechselstrom]]
:::
:::vbox
**Verwandte Artikel**
- [[Verluste in der Spule (Güte, Wicklungswiderstand)]]
:::
:::vbox
**Führt weiter zu**
- [[RC-Reihenschaltung]]
:::
:::

---

Ein realer Kondensator ist keine ideale Kapazität — er hat parasitäre Widerstände und Induktivitäten, die bei Wechselstrom zu Verlusten führen. Der ESR (Equivalent Series Resistance) ist besonders bei Netzteilen und HF-Anwendungen relevant.

## Realer vs. idealer Kondensator

:::schematic
/schaltplaene/C/kondensator_ersatzschaltbild.svg
:::

Das Ersatzschaltbild zeigt die drei parasitären Elemente in Serie: ESR (Widerstand), ESL (Induktivität) und C (ideale Kapazität). Parallel zu C liegt noch ein grosser Leckwiderstand R_leck, der den sehr langsamen Selbstentladestrom beschreibt — bei hochwertigen Kondensatoren vernachlässigbar.

- **ESR** (Äquivalenter Serienwiderstand): Verluste im Dielektrikum und Zuleitungswiderstand
- **ESL** (Äquivalente Serieninduktivität): Parasitäre Induktivität durch Zuleitungen — bestimmt die Selbstresonanzfrequenz

## ESR — relevant bei DC-Ripple und AC

Der ESR ist **bei jeder Frequenz** relevant, auch bei der Netzteil-Glättung (100 Hz Ripple):

:::formel
U_ESR = I_ripple * ESR    # Spannungsabfall durch Ripplestrom
:::

Ein grosser ESR bei einem Glättelko bedeutet hohe Brummspannung am Ausgang — obwohl die Kapazität ausreicht.

:::warning
ESR steigt bei Elkos mit dem Alter und bei tiefen Temperaturen stark an. Ein defekter Elko mit hohem ESR (typisch nach 10–20 Jahren) ist oft nicht an der Kapazität erkennbar — nur am ESR-Messer. In alten Geräten sind Elkos deshalb prophylaktisch zu tauschen.
:::

## Verlustfaktor d und Verlustwinkel delta

Der Verlustfaktor d gibt an, wie "schlecht" der Kondensator ist:

:::formel
d = ESR / X_C    # = tan(delta) = 1/Q
:::

Der Verlustwinkel delta ist der Phasenwinkel, um den der reale Kondensator von der idealen Kapazität abweicht. Bei einem idealen Kondensator ist delta = 0°.

Hinweis: d, delta und Q sind **AC-Konzepte** — sie hängen von der Frequenz ab und gelten nicht bei Gleichstrom.

## Güte Q

:::formel
Q = X_C / ESR    # = 1/d
:::

| Typ | ESR (typ.) | Güte bei 1 kHz | Anwendung |
|---|---|---|---|
| Aluminiumelko | 0,1–1 Ω | < 100 | Netzteilpuffer, Kopplung |
| Tantalkondensator | 0,1–0,5 Ω | mittel | SMD-Puffer |
| Keramik (X7R) | < 0,01 Ω | sehr hoch | HF-Entkopplung, Filter |
| C0G Keramik | < 0,001 Ω | > 10 000 | Präzisionsschwingkreise |

## Selbstresonanzfrequenz

Durch die parasitäre Induktivität ESL hat jeder Kondensator eine Selbstresonanzfrequenz, oberhalb derer er induktiv wirkt:

:::formel
f_SRF = 1 / (2 * pi * sqrt(ESL * C))
:::

Oberhalb f_SRF funktioniert der Kondensator nicht mehr als Kapazität. MLCC-Kondensatoren (SMD) haben sehr kleine ESL und damit hohe f_SRF — deshalb werden sie für HF verwendet, nicht Elkos.

:::tip
Für Netzteil-Entkopplung: Grosse Elko-Kapazität (10–100 µF) für tiefe Frequenzen (< 1 MHz) mit kleinem MLCC (100 nF) parallel kombinieren. Der MLCC übernimmt die HF-Entkopplung (höhere f_SRF), der Elko die Ladungsreserve.
:::
