---
title: Quarz-Oszillator
kategorie: ET
tags: [quarz, oszillator, resonanz, frequenz, takt, piezoelektrisch, TCXO, OCXO, MEMS, lastkapazität, taktgeber, güte, serienresonanz]
symbol: —
einheit: Hz
---

Ein Quarz ist ein piezoelektrischer Kristall der bei einer definierten Frequenz mechanisch resoniert. Er wird als hochpräzises Frequenzelement in Oszillatoren, Uhren und Mikrocontrollern eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Resonanz]]
- [[RLC-Schaltungen]]
:::
:::vbox
**Verwandte Artikel**
- [[LC-Filter]]
:::
:::vbox
**Führt weiter zu**
- [[Mikrocontroller]]
:::
:::

---

## Prinzip

Der Piezoeffekt bewirkt, dass mechanische Verformung eine elektrische Spannung erzeugt — und umgekehrt. Ein Quarzplättchen schwingt bei seiner mechanischen Eigenfrequenz. Diese liegt je nach Schnitt und Abmessung im kHz- bis MHz-Bereich.

Elektrisch verhält sich ein Quarz wie ein RLC-Schwingkreis mit sehr hoher Güte:

:::formel
Q_quarz ≈ 10 000 bis 100 000     # typische Güte
:::
Zum Vergleich: Ein LC-Schwingkreis erreicht Q ≈ 10–200.

## Serienresonanz und Parallelresonanz

Ein Quarz hat zwei Resonanzfrequenzen:

- **Serienresonanz f_s**: Impedanz minimal, Quarz wirkt wie ein niedriger Widerstand
- **Parallelresonanz f_p**: Impedanz maximal (durch parallele Kapazität des Gehäuses)

Der Unterschied zwischen f_s und f_p ist typisch sehr klein (0.1–1 %).

## Lastkapazität

Quarze werden mit einer bestimmten **Lastkapazität C_L** spezifiziert (typisch 12 pF oder 18 pF). Die tatsächliche Schwingfrequenz hängt von der Lastkapazität ab. Falsche C_L verschiebt die Frequenz leicht.

## Typen

| Typ | Beschreibung |
|---|---|
| Quarz (diskret) | Standardbauteil, benötigt externe Schaltung |
| XTAL + Mikrocontroller | Quarz direkt am µC-Oszillator-Pin |
| TCXO | Temperature Compensated XO — stabil über Temperatur |
| OCXO | Oven Controlled XO — im beheizten Gehäuse, sehr präzise |
| MEMS-Oszillator | Quarzfreier Ersatz, robust gegen Vibration |

## Typische Frequenzen

| Anwendung | Frequenz |
|---|---|
| Uhrenquarz | 32.768 kHz (= 2¹⁵ Hz, einfach teilbar) |
| Mikrocontroller | 4–25 MHz |
| USB | 48 MHz |
| Ethernet | 25 MHz |
| GPS | 10 MHz |
