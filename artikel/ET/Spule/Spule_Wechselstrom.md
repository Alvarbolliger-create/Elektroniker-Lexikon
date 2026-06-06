---
title: Spule im Wechselstrom
kategorie: ET
tags: [spule, wechselstrom, induktiver widerstand, phasenverschiebung, x_l, blindwiderstand, hochpass]
groessen: X_L|induktive Reaktanz|Ohm; f|Frequenz|Hz; L|Induktivität|H; omega|Kreisfrequenz|rad/s; phi|Phasenwinkel|°
_status: PORT  # ET_alt/Spule/Spule_Wechselstrom.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Selbstinduktion & Induzierte Spannung]]
- [[Sinuswellen & Effektivwert]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator im Wechselstrom]]
:::
:::vbox
**Führt weiter zu**
- [[RL-Reihenschaltung]]
- [[RL-Parallelschaltung]]
:::
:::

---

Beim Wechselstrom widersteht die Spule dem Stromfluss mit einem frequenzabhängigen Blindwiderstand. Tiefe Frequenzen lässt sie durch — hohe blockiert sie. Das ist genau umgekehrt wie beim Kondensator.

## Induktiver Blindwiderstand X_L

Die Spule erzeugt eine Gegenspannung proportional zur Stromänderungsgeschwindigkeit. Je schneller der Strom wechselt (hohe Frequenz) und je grösser L, desto stärker die Gegenwirkung:

:::formel
X_L = omega * L
:::

:::formel
X_L = 2 * pi * f * L
:::

**Einheit:** Ohm (Ω) — frequenzabhängig, steigt linear mit f.

| Frequenz | Verhalten X_L | Spule |
|---|---|---|
| f = 0 (Gleichstrom) | X_L = 0 | Reiner Draht |
| f steigt | X_L steigt | Wird "sperriger" |
| f → ∞ | X_L → ∞ | Offener Schalter für HF |

## Phasenverschiebung

Bei einer idealen Spule eilt die **Spannung dem Strom um 90° vor**. Die Spule bremst Stromänderungen — der Strom hinkt hinterher.

phi = +90° (Spannung voreilend gegenüber Strom)

:::schematic Zeigerdiagramm Spule: Zeiger U_L zeigt senkrecht nach oben (positive imaginäre Achse); Zeiger I liegt horizontal nach rechts (reale Achse); Winkel phi = +90° zwischen U_L und I eingezeichnet; Beschriftung: U_L oben, I rechts, phi = +90°
/abbildungen/spule/spule_wechselstrom_zeiger.svg
:::

Merkhilfe: *ELI* (im ELI-Modell: bei L eilt E vor I)

## Frequenzabhängigkeit

:::monospace
Beispiel: L = 10 mH
bei f = 100 Hz:   X_L = 2*pi*100*0.01 = 6.3 Ohm
bei f = 1 kHz:    X_L = 62.8 Ohm
bei f = 10 kHz:   X_L = 628 Ohm
bei f = 100 kHz:  X_L = 6.28 kOhm
:::

## Komplexe Impedanz

In der komplexen Darstellung (→ [[Impedanz]]):

Z_L = j · omega · L

Das j zeigt: 90° Phasenvoreilung der Spannung. Der Betrag |Z_L| = X_L = omega · L.

## Praktische Bedeutung

| Anwendung | Erklärung |
|---|---|
| Drosselspule | Sperrt HF-Störungen, lässt Gleichstrom durch |
| Tiefpassfilter (Induktiv) | X_L steigt mit f → HF wird blockiert |
| Transformator-Kern | Induktivität konzentriert Energie im Kern |
| Ferritkern auf Kabel | Sperrt hochfrequente Störströme (EMV) |

:::warning
Beim Abschalten einer Spule entsteht eine Induktionsspannung (Gegenspannung), die sehr hoch sein kann. Diese gefährdet angeschlossene Halbleiter. Immer [[Spule (Übersicht)|Freilaufdiode]] vorsehen!
:::
