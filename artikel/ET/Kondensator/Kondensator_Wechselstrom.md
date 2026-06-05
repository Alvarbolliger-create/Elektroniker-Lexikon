---
title: Kondensator im Wechselstrom
kategorie: ET
tags: [kondensator, wechselstrom, blindwiderstand, kapazitiver widerstand, phasenverschiebung, xc, tiefpass]
groessen: X_C|kapazitive Reaktanz|Ohm; f|Frequenz|Hz; C|Kapazität|F; omega|Kreisfrequenz|rad/s; phi|Phasenwinkel|°
_status: PORT  # ET_alt/Kondensator/Kondensator_Wechselstrom.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kondensator (Übersicht)]]
- [[Sinuswellen & Effektivwert]]
:::
:::vbox
**Verwandte Artikel**
- [[Spule im Wechselstrom]]
:::
:::vbox
**Führt weiter zu**
- [[RC-Reihenschaltung]]
- [[RC-Parallelschaltung]]
:::
:::

---

Beim Wechselstrom blockiert der Kondensator tiefe Frequenzen und lässt hohe durch — genau umgekehrt wie die Spule. Der kapazitive Blindwiderstand X_C erklärt dieses Verhalten.

## Kapazitiver Blindwiderstand X_C

Der Kondensator "widersteht" dem Wechselstrom mit der kapazitiven Reaktanz X_C. Sie hängt von Frequenz und Kapazität ab:

:::formel
X_C = 1 / (omega * C)
:::

:::formel
X_C = 1 / (2 * pi * f * C)
:::

**Einheit:** Ohm (Ω) — genau wie ein ohmscher Widerstand, aber frequenzabhängig.

| Frequenz | Verhalten X_C | Kondensator |
|---|---|---|
| f → 0 (Gleichstrom) | X_C → ∞ | Sperrt vollständig |
| f steigt | X_C sinkt | Wird "durchlässiger" |
| f → ∞ | X_C → 0 | Kurzschluss für HF |

## Phasenverschiebung

Bei einem idealen Kondensator eilt der **Strom der Spannung um 90° vor**. Intuition: Der Kondensator muss zuerst geladen werden (Strom fliesst), bevor eine Spannung aufgebaut ist.

phi = −90° (Spannung nacheilend gegenüber Strom)

Merkhilfe: *ICE* (im ICE-Modell: bei C eilt I vor E)

:::schematic
/abbildungen/kondensator/kondensator_wechselstrom_zeiger.svg
:::

Das Zeigerdiagramm und die vollständige Behandlung im Wechselstromkreis folgen in → [[RC-Reihenschaltung]] und [[Wechselstromleistung]].

## Frequenzabhängigkeit

:::plot
var: f
range: 100, 100000
xscale: log
colors: #0284c7
xlabel: Frequenz (Hz)
ylabel: X_C (Ohm)
X_C (C=100nF):  1 / (2 * pi * f * 100e-9)
:::

:::monospace
Beispiel: C = 100 nF
bei f = 100 Hz:   X_C = 1 / (2*pi*100*100e-9) = 15.9 kOhm
bei f = 1 kHz:    X_C = 1.59 kOhm
bei f = 10 kHz:   X_C = 159 Ohm
bei f = 100 kHz:  X_C = 15.9 Ohm
:::

## Praktische Bedeutung

| Anwendung | Erklärung |
|---|---|
| Koppelkondensator | Sperrt Gleichspannungsoffset, lässt Wechselsignal durch |
| Bypass-Kondensator | X_C niedrig bei HF → Versorgungsstörungen kurzschliessen |
| RC-Tiefpass | X_C sinkt mit f → hohe Frequenzen "kurz geschlossen" |
| Netzteilfilter | Glättungskondensator sperrt Gleichspannung, leitet Brummspannung zu GND |

:::tip
Der **Bypass-Kondensator** (auch: Entkopplungskondensator) direkt am VCC-Pin von ICs ist eine der wichtigsten Massnahmen in der Digitalelektronik. Er hält die Versorgungsspannung stabil, indem er hochfrequente Lastspitzen lokal liefert — ohne weite Leitungswege zum Netzteil.
:::
