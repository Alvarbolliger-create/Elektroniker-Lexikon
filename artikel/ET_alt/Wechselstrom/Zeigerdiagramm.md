---
title: Zeigerdiagramm (Phasor)
kategorie: ET
tags: [zeigerdiagramm, phasor, phasenverschiebung, wechselstrom, zeiger, komplexe zahl, eulerformel, impedanz, wechselstromrechnung, RLC]
symbol: —
einheit: —
---

Das Zeigerdiagramm stellt Wechselgrössen als rotierende Zeiger dar. Damit lassen sich Phasenverschiebungen und Beträge auf einen Blick erkennen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Impedanz]]
:::
:::vbox
**Führt weiter zu**
- [[Impedanz]]
:::
:::

---

:::schematic Zeigerdiagramm – Phasenverschiebung
/schaltplaene/zeigerdiagramm.svg
:::

## Grundidee

Eine Sinusgrösse lässt sich als rotierender Zeiger darstellen. Die Länge des Zeigers ist der Scheitelwert. Die aktuelle Position zeigt die Phase.

Zwei Signale mit Phasenverschiebung: ihre Zeiger stehen um diesen Winkel versetzt, drehen sich aber mit derselben Geschwindigkeit.

## Was man abliest

**Betrag**: Länge des Zeigers = Amplitude des Signals.

**Phasenwinkel**: Winkel zwischen zwei Zeigern = zeitlicher Versatz der Signale.

**Voreilung / Nacheilung**: Zeiger der voraus ist, eilt dem anderen vor. Bei einer Spule eilt die Spannung dem Strom um 90° vor. Bei einem Kondensator eilt der Strom der Spannung um 90° vor.

| Last | Strom gegenüber Spannung | Begriff |
|---|---|---|
| Induktiv (Spule) | nacheilend | Strom kommt später |
| Kapazitiv (Kondensator) | voreilend | Strom kommt früher |
| Ohmsch | in Phase | kein Versatz |

## Im RLC-Kreis

Widerstand R: Strom und Spannung zeigen in dieselbe Richtung (in Phase).

Spule X_L: Spannungszeiger 90° vor dem Stromzeiger.

Kondensator X_C: Spannungszeiger 90° hinter dem Stromzeiger.

Die Gesamtimpedanz ist der geometrische Summenpfeil aller Zeiger.

## Verbindung zur komplexen Schreibweise

Ein Zeiger ist mathematisch eine komplexe Zahl in Polarform:

:::formel
U = |U| * e^(j*φ) = |U| * (cos(φ) + j*sin(φ))
:::
Die grafische Addition von Zeigern im Diagramm entspricht der Addition komplexer Zahlen. Die Länge des resultierenden Zeigers ist der Betrag, der Winkel ist die Phase — dieselben Grössen die in [[Impedanz]] berechnet werden.

:::tip
Zeigerdiagramme von Hand zeichnen üben. Wer verstanden hat wie man Zeiger addiert, versteht automatisch warum Blindleistung entsteht und was der Phasenwinkel bedeutet.
:::
