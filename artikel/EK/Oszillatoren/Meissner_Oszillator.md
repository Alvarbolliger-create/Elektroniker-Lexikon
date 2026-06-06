---
title: Meissner-Oszillator
kategorie: EK
kapitel: Oszillatoren
tags: [meissner, LC-oszillator, transformatorkopplung, induktiv, resonanzfrequenz, rückkopplungsfaktor, BJT, N1, N2, wicklungsverhältnis, galvanisch-getrennt]
groessen: f_0|Resonanzfrequenz|Hz; k|Rückkopplungsfaktor|—; v_u|Spannungsverstärkung|—; L|Induktivität Schwingkreis|H; C|Kapazität|F; N1|Windungszahl Schwingkreis|—; N2|Windungszahl Rückkopplung|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[BJT Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Hartley-Oszillator]]
- [[Colpitts-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Hartley-Oszillator]]
- [[Quarzoszillator]]
:::
:::

---

Der Meissner-Oszillator ist ein LC-Oszillator mit **Transformatorkopplung**: Eine Rückkopplungswicklung (N2) am Schwingkreis-Transformator koppelt einen Teil der Ausgangsspannung phasenrichtig zurück an die Basis des Transistors.

## Schaltungsprinzip

:::schematic Meissner-Oszillator: BJT (NPN) in Emitterschaltung. Kollektor an Primärwicklung N1 des Transformators. Transformatorkern mit N1 oben und N2 unten (Wicklungsrichtung beachten für 180° Phasenumkehr). Parallelkondensator C über N1. N1+C bilden LC-Schwingkreis. Sekundärwicklung N2 vom Transformator über Koppelkondensator zurück an Basis (Rückkopplung). Basis-Spannungsteiler R1/R2. Emitter: R_E nach GND. VCC an oberes Ende von N1. Rückkopplungsfaktor k = N2/N1
/Diagramm/meissner.svg
:::

BJT in Emitterschaltung → λ = 180°. Der Schwingkreis besteht aus L (Primärwicklung N1) und C. Die Sekundärwicklung N2 ist so gewickelt und angeschlossen, dass sie nochmals 180° dreht → φ + λ = 180° + 180° = 360° ✓

Das Wicklungsverhältnis N2/N1 bestimmt, wie viel Ausgangsspannung zurückgekoppelt wird.

## Formeln aus dem Spick

:::formel
f_0 = 1 / (2 * pi * sqrt(L * C))    # Resonanzfrequenz des LC-Schwingkreises
k   = N2 / N1                         # Rückkopplungsfaktor (Wicklungsverhältnis)
v_u = 1 / k = N1 / N2               # benötigte Spannungsverstärkung
:::

## Schwingungsbedingung

Der Transistor muss mindestens v_u = N1/N2 liefern. Je kleiner N2 (weniger Rückkopplung), desto mehr Verstärkung wird benötigt.

:::info
Typisch: N2/N1 = 0.1 bis 0.3 → v_u = 3 bis 10. Das Wicklungsverhältnis bestimmt gleichzeitig die Rückkopplungsstärke und die benötigte Transistorverstärkung.
:::

## Vergleich Meissner vs. Hartley

| Eigenschaft | Meissner | Hartley |
|---|---|---|
| Rückkopplung | Transformatorwicklung N2 | Anzapfung an der Spule |
| Bauteilaufwand | höher (Trafo nötig) | geringer (1 Spule mit Tap) |
| Galvanische Trennung | ja (Trafo) | nein |
| Frequenzbereich | 100 kHz – 100 MHz | 100 kHz – 100 MHz |
| Resonanzformel | 1/(2π√LC) | 1/(2π√LC) |

## Anwendungen

- **HF-Sender:** Klassischer Mittel-/Kurzwellensender-Grundbaustein
- **Abstimmbare Generatoren:** L und C variabel für einstellbare Frequenz
- **Wenn galvanische Trennung nötig:** Transformator trennt Schwingkreis und Ausgangsstufe
