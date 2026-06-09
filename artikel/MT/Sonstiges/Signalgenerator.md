---
title: Signalgenerator
kategorie: MT
tags: [signalgenerator, AWG, funktionsgenerator, sweep, frequenz, DDS, burst, DC-offset, ausgangsimpedanz, 50 ohm]
symbol: —
einheit: Hz, V
---

Ein Signalgenerator erzeugt definierte elektrische Signale zum Testen von Schaltungen. Er ist das Gegenstück zum Messgerät.

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen & Effektivwert]]
- [[Oszilloskop: Aufbau & Bedienung]]
:::
:::vbox
**Verwandte Artikel**
- [[FFT (Fast Fourier Transform)]]
- [[Protokoll-Decoder]]
:::
:::

---

## Typen

**Funktionsgenerator**: Erzeugt Sinus, Rechteck, Dreieck, Sägezahn. Feste Kurvenformen. Günstig, einfach, für die meisten Laborzwecke ausreichend.

**AWG (Arbitrary Waveform Generator)**: Beliebige Kurvenform aus gespeicherten Datenpunkten. Kann z.B. reale Audiosignale, Busprotokolle oder verzerrte Netzwellen ausgeben. Teurer, aber sehr flexibel.

**HF-Signalgenerator**: Für Frequenzen im MHz- bis GHz-Bereich. Für HF-Schaltungen, Antennen, Empfänger.

## Wichtige Parameter

- **Frequenzbereich**: Was der Generator ausgeben kann
- **Amplitudenbereich**: Typisch 10 mVpp bis 20 Vpp
- **Ausgangsimpedanz**: Fast immer 50 Ohm. Relevant für Abschlusswiderstände
- **Auflösung**: Wie fein Frequenz und Amplitude einstellbar sind

## DC-Offset

Die meisten Generatoren können den Mittelwert des Signals verschieben. Nützlich um z.B. einen Sinus auf 2.5 V Mittellage zu bringen für ADC-Tests.

## Burst und Sweep

**Burst**: Eine definierte Anzahl Perioden ausgeben, dann stoppen. Nützlich für Protokolltests.

**Sweep**: Frequenz langsam von A nach B durchfahren. Zeigt Frequenzgang von Filtern oder Verstärkern.

## Einstieg

Günstige DDS-Generatoren (Direct Digital Synthesis) ab ca. 30 CHF (z.B. AD9833-basiert) sind für viele Hobby- und Lernzwecke ausreichend. Professionelle Geräte (Rigol, Siglent) bieten mehr Kanäle, bessere Spec und AWG-Funktion.
