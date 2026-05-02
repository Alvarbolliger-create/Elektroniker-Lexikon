---
title: EMV Pre-Compliance
kategorie: MT
tags: [EMV, pre-compliance, emission, störung, CISPR, messung, antenne, LISN, spektrumanalysator, dBµV, quasipeak]
symbol: —
einheit: dBµV/m, dBµV
---

EMV Pre-Compliance-Messung prüft ein Gerät auf elektromagnetische Emissionen bevor es ins akkreditierte Labor geht. Sie spart teure Nachbesserungen nach dem ersten Labortest.

:::hbox
:::vbox
**Voraussetzungen**
- [[FFT (Fast Fourier Transform)]]
- [[Oberschwingungen und THD]]
:::
:::vbox
**Verwandte Artikel**
- [[FFT (Fast Fourier Transform)]]
- [[RED (Radio Equipment Directive)]]
:::
:::

---

## Warum Pre-Compliance?

Ein EMV-Labortest kostet tausende von Franken. Wenn das Gerät durchfällt, muss es nachgebessert und erneut getestet werden. Pre-Compliance-Messungen zeigen Schwachstellen früh auf, wenn Änderungen noch günstig sind.

## Abstrahlmessung (Radiated Emissions)

Antenne (Bikonische oder Log.-per. Antenne) misst das vom Gerät abgestrahlte Feld in einem definierten Abstand. Ergebnis in dBµV/m.

Grenzwerte nach CISPR 32 (Multimedia) oder CISPR 22 (IT-Geräte):
- Klasse B (Haushaltsbereich): strenger
- Klasse A (Industriebereich): lockerer

## Leitungsgebundene Messung (Conducted Emissions)

Ein LISN (Line Impedance Stabilisation Network) wird zwischen Netz und Gerät geschaltet. Es normiert die Netzimpedanz und koppelt die Störspannungen am Netzeingang aus. Messung in dBµV.

## Messaufbau für Pre-Compliance

Minimaler Aufbau:
1. Spektrumanalysator mit Quasipeak-Detektor (oder EMI-Receiver)
2. Bikonische Antenne für 30-300 MHz
3. Log.-per. Antenne für 300 MHz bis 1 GHz
4. LISN für leitungsgebundene Messung
5. Nicht-reflektierender Untergrund (ESD-Matte oder freie Fläche)

## Was man im Spektrum sucht

Harmonische des Taktsignals (Prozessortakt, Schaltregler). Schmalbandige Peaks oberhalb der Grenzlinie. Breitbandiges Rauschen.

## Massnahmen bei Grenzwertüberschreitung

- Ferrite auf Kabeln (leitungsgebunden)
- Schirmung des Gehäuses
- Bessere Entkopplung von Schaltregler und Taktleitungen
- Spread-Spectrum-Clocking (verteilt Energie auf mehr Frequenzen)
- EMV-Filter am Netzeingang verbessern
