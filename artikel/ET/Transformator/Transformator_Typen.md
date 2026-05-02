---
title: Transformator Typen
kategorie: ET
tags: [transformator, ringkern, EI-kern, spartransformator, HF-transformator, netztransformator, ferrit, balun, galvanische trennung, variac, übertrager, strommesswandler]
symbol: —
einheit: —
---

Transformatoren gibt es in vielen Bauformen für verschiedene Frequenzen, Leistungen und Anwendungen. Die Kernform bestimmt die Eigenschaften.

:::hbox
:::vbox
**Voraussetzungen**
- [[Transformator Aufbau]]
- [[Übersetzungsverhältnis]]
:::
:::vbox
**Verwandte Artikel**
- [[Wirkungsgrad & Verluste]]
- [[Buck (Step-down)]]
:::
:::vbox
**Führt weiter zu**
- [[Schaltnetzteile]]
- [[EMV-Grundlagen]]
:::
:::

---

## EI-Kern (Netztransformatoren)

Gestapelte Bleche in E- und I-Form. Der klassische 50-Hz-Netztransformator. Günstig, robust, bewährt.

Nachteil: Schwer, gross, brummt bei Sättigung. Streufeld relativ hoch.

## Ringkern

Toroidaler Kern aus gewickeltem Band. Geringes Streufeld (gut für Audiogeräte). Hoher Wirkungsgrad. Teurer als EI, schwieriger zu wickeln.

Im Audiobereich bevorzugt wegen niedrigem 50-Hz-Brummen in der Nähe von empfindlichen Schaltungen.

## Spartransformator

Primär- und Sekundärwicklung sind elektrisch verbunden (nicht galvanisch getrennt). Günstiger bei kleinen Übersetzungsverhältnissen.

Ein Variac ist ein regelbarer Spartransformator. Kein Schutz gegen Körperschluss: der Ausgang steht nicht galvanisch getrennt.

## HF-Transformatoren (Schaltnetzteile)

Ferrit- oder Eisenpulverkerne für Frequenzen von kHz bis MHz. Viel kleiner als 50-Hz-Transformatoren bei gleicher Leistung. Das ist der Grund warum Schaltnetzteile kompakt sind.

Kernmaterialien: Ferrit (MnZn für <1 MHz, NiZn für >1 MHz), Pulverkerne (Eisenpulver, MPP, Kool Mu) für glatte Drosselkennlinien.

## Übertrager

Sehr breitbandige Transformatoren für Audio oder HF. Kein DC-Anteil. Für Impedanzanpassung und Signalkopplung.

Baluns (Balanced/Unbalanced) sind Übertrager zwischen symmetrischen und unsymmetrischen Leitungen. In der Antennentechnik und bei RS485/Ethernet.

## Strommesswandler

Toroidkern mit einer Primärwindung (der zu messende Leiter) und vielen Sekundärwindungen. Misst den Strom über die transformierte Spannung. Galvanisch getrennt.

Prinzip der Strommesszange.
