---
title: Sukzessive Approximation (SAR-ADC)
kategorie: SH
tags: [SAR, ADC, sukzessive approximation, bitwage, komparator, sample-and-hold, MSB, LSB, MSPS, STM32, AVR]
symbol: —
einheit: Bit
---

Der SAR-ADC (Successive Approximation Register) ist der am häufigsten verwendete ADC-Typ in Mikrocontrollern. Er ist schnell, genau und energieeffizient.

:::hbox
:::vbox
**Voraussetzungen**
- [[AD/DA Grundlagen]]
- [[OPV Komparator]]
:::
:::vbox
**Verwandte Artikel**
- [[R-2R Netzwerk]]
:::
:::

---

## Messprinzip: Bitwage

Der SAR-ADC probiert jeden Bit von MSB zu LSB aus. Bei einem 4-Bit-ADC mit 3.3 V Referenz:

1. Setze MSB (Bit 3): Vergleichsspannung = 1.65 V. Ist U_ein > 1.65 V? Ja: Bit 3 = 1. Nein: Bit 3 = 0.
2. Setze Bit 2: Vergleichsspannung = 1.65 + 0.825 V (oder - 0.825 V, je nach Bit 3). Vergleich.
3. Bit 1, Bit 0: gleich.

Nach n Schritten ist die Wandlung fertig. Braucht genau n Taktzyklen für n Bit.

## Sample-and-Hold — zwingend nötig

Der SAR-Algorithmus braucht für alle n Bit dieselbe Eingangsspannung. Ändert sich das Signal während der Wandlung, vergleicht der Komparator in Schritt 1 eine andere Spannung als in Schritt n — das Ergebnis ist falsch.

**Lösung**: Ein Sample-and-Hold-Kondensator am Eingang speichert den Momentanwert beim Abtastzeitpunkt. Er wird aufgeladen (Sample-Phase), dann von der Eingangsquelle getrennt (Hold-Phase). Der ADC wandelt den gespeicherten Wert.

:::monospace
Sample-Phase:   S (Schalter) geschlossen → C lädt auf U_ein
Hold-Phase:     S offen → C hält U_ein konstant → ADC-Wandlung startet
:::
Ohne Sample-and-Hold würde ein sich änderndes Signal während der n Taktzyklen der Bitwage zu Konversionsfehlern führen.

## Einschränkungen

Die Eingangsspannung darf sich während der Wandlung nicht ändern. Schnell wechselnde Signale können zu Fehlern führen.

Ein SAR-ADC ist nicht geeignet für sehr hohe Abtastraten (über einige MSPS). Für höhere Raten werden Flash-ADCs oder Pipelined-ADCs verwendet.

## Typische Werte in Mikrocontrollern

- 12 Bit Auflösung (oft Standard, manchmal 10 oder 16 Bit)
- 1 bis 5 MSPS Samplingrate
- Mehrere Kanäle über Multiplexer

Beispiele: STM32 (12-Bit, 1 MSPS), AVR ATmega (10-Bit, 76 kSPS).
