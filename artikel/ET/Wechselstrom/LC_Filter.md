---
title: LC-Filter
kategorie: ET
tags: [filter, lc, tiefpass, hochpass, resonanz, güte, bandpass, bandsperre, HF, schaltnetzteil, EMV]
symbol: —
einheit: —
---

LC-Filter verwenden Spule und Kondensator ohne ohmschen Verlust. Sie erreichen steilere Flanken als RC-Filter und werden für HF-Anwendungen und Schaltnetzteile eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
- [[Resonanz]]
- [[RC-Filter]]
:::
:::vbox
**Verwandte Artikel**
- [[RLC-Schaltungen]]
- [[Resonanz]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive Filter]]
- [[Quarz-Oszillator]]
:::
:::

---

## Prinzip

Ein idealer LC-Filter hat keine Verluste. In der Praxis begrenzt der Wicklungswiderstand der Spule (DCR) die erreichbare Güte.

Die Grenzfrequenz ergibt sich aus der Resonanzbedingung X_L = X_C:

:::formel
f_g = 1 / (2 * pi * sqrt(L * C))
:::
Unterhalb f_g: Spule niederohmig, Kondensator hochohmig → Durchlass.
Oberhalb f_g: Spule hochohmig, Kondensator niederohmig → Sperr.

## Vergleich RC vs. LC

| Eigenschaft | RC-Filter | LC-Filter |
|---|---|---|
| Flankensteilheit | −20 dB/Dekade (1. Ord.) | −40 dB/Dekade (2. Ord.) |
| Verluste | R immer vorhanden | Verlustarm möglich |
| Resonanz | keine | ja (Überschwingen möglich) |
| Frequenzbereich | DC bis HF | HF bevorzugt |
| Kosten | günstig | teurer (Spule) |

## Anwendungen

**Schaltnetzteil-Ausgangsfilter:** L und C glätten die PWM-Ausgangsspannung. Die Grenzfrequenz liegt deutlich unter der Schaltfrequenz.

**HF-Filter:** In Empfängern und Sendern zur Selektion von Frequenzbändern.

**EMV-Filter:** Netzfilter kombinieren Common Mode Choke (L) mit Y-Kondensatoren (C) zur Gleichtaktunterdrückung. Siehe [[EMV-Grundlagen]].

:::tip
LC-Filter 2. Ordnung können bei schlechter Dämpfung (hohe Güte) überschwingen. Für unkritische Anwendungen genügt ein RC-Filter. LC lohnt sich, wenn niedrige Verluste oder steile Flanken gefordert sind.
:::
