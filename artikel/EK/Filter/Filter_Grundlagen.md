---
title: Filter Grundlagen
kategorie: EK
tags: [filter, tiefpass, hochpass, bandpass, grenzfrequenz, dämpfung, notch, bandsperre, filterordnung, aktiv, passiv, -3dB]
symbol: f_g
einheit: Hz
---

Filter lassen bestimmte Frequenzen durch und dämpfen andere. Sie sind in fast jeder Schaltung: in Netzteilen, Audioverstärkern, Kommunikationssystemen und Sensorsignalaufbereitungen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
- [[RLC-Schaltungen]]
:::
:::vbox
**Verwandte Artikel**
- [[RC-Tiefpass & Hochpass]]
:::
:::vbox
**Führt weiter zu**
- [[RC-Tiefpass & Hochpass]]
- [[Aktive Filter]]
:::
:::

---

## Filtertypen

**Tiefpass**: Lässt tiefe Frequenzen durch, dämpft hohe. Typisch für Glättung und Rauschunterdrückung.

**Hochpass**: Lässt hohe Frequenzen durch, dämpft tiefe. Typisch für Wechselstromkopplung und Entfernung von Gleichanteilen.

**Bandpass**: Lässt ein Frequenzband durch, dämpft ausserhalb. Typisch für Empfänger und Signalauswahl.

**Bandsperre (Notch)**: Dämpft ein schmales Band, lässt ausserhalb durch. Typisch für 50-Hz-Brumm-Unterdrückung.

## Grenzfrequenz

Die -3 dB Frequenz (Grenzfrequenz f_g) ist die Frequenz bei der die Ausgangsamplitude auf 70.7 % des Eingangs gesunken ist.

```
f_g = 1 / (2 * pi * R * C)     # RC-Tiefpass und Hochpass
```

## Filterordnung

Jede Ordnung fügt 20 dB/Dekade Dämpfung hinzu. Ein Filter 1. Ordnung: 20 dB/Dek. 2. Ordnung: 40 dB/Dek. Mehr Ordnungen: steilere Flanke, aber komplexere Schaltung.

## Passiv vs. Aktiv

**Passive Filter** (R, L, C): Kein Verstärker, kein Versorgungsstrom. Einfach, aber dämpfen das Signal immer.

**Aktive Filter** (R, C, OPV): Können verstärken, kein Einfluss auf Lastimpedanz. Besser geeignet für Audio und Signalaufbereitung.

:::tip
Für einfache Signalglättung (Sensorsignal, ADC-Eingang) reicht meist ein RC-Tiefpass 1. Ordnung. Grenzfrequenz so wählen dass das Nutzsignal noch durchkommt, Störungen aber gedämpft werden.
:::
