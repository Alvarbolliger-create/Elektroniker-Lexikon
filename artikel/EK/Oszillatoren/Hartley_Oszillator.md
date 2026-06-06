---
title: Hartley-Oszillator
kategorie: EK
kapitel: Oszillatoren
tags: [hartley, LC-oszillator, induktiv, getapte-spule, N1, N2, resonanzfrequenz, rückkopplungsfaktor, BJT, anzapfung, abstimmbar]
groessen: f_0|Resonanzfrequenz|Hz; k|Rückkopplungsfaktor|—; v_u|Spannungsverstärkung|—; L|Gesamtinduktivität|H; C|Kapazität|F; N1|Windungen unterer Teil|—; N2|Windungen oberer Teil|—
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
- [[Meissner-Oszillator]]
- [[Colpitts-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Colpitts-Oszillator]]
:::
:::

---

Der Hartley-Oszillator ist ein LC-Oszillator mit einer **induktiv geteilten Spule**: Die Gesamtinduktivität L = N1 + N2 hat eine Anzapfung, die als induktiver Spannungsteiler für die Rückkopplung dient.

## Schaltungsprinzip

:::schematic Hartley-Oszillator: BJT (NPN) in Emitterschaltung. LC-Schwingkreis: Parallelkondensator C zwischen Kollektor und GND (über VCC-Bypass). Getapte Spule: N1 (oberer Teil) von VCC/Kollektor, Anzapfung (Mittelpunkt) nach GND (Emitter), N2 (unterer Teil) von Anzapfung nach Rückkopplungspunkt. Rückkopplungspunkt über Koppelkondensator an Basis. Basis-Spannungsteiler R1/R2. Emitter: R_E nach GND. L_gesamt = N1 + N2. Rückkopplungsfaktor k = N2/(N1+N2)
/Diagramm/hartley.svg
:::

BJT in Emitterschaltung → λ = 180°. Der Schwingkreis schwingt bei f_0 mit L (gesamt) und C. Die Spulenanzapfung zwischen N1 und N2 teilt die Schwingkreisspannung induktiv auf. Der Abgriff koppelt den Bruchteil N2/(N1+N2) zurück an die Basis mit 180° Phasendrehung → φ + λ = 360° ✓

## Formeln aus dem Spick

:::formel
f_0 = 1 / (2 * pi * sqrt(L * C))        # Resonanzfrequenz (L = N1 + N2 gesamt)
k   = N2 / (N1 + N2)                     # Rückkopplungsfaktor
v_u = 1 / k = (N1 + N2) / N2           # benötigte Spannungsverstärkung
:::

## Frequenzabstimmung

Durch eine **variable Kapazität** C (Drehkondensator, Varaktordiode) lässt sich f_0 abstimmen, ohne die Rückkopplung zu verändern. Das macht den Hartley-Oszillator gut geeignet für abstimmbare HF-Generatoren.

## Vergleich Hartley vs. Colpitts

| Eigenschaft | Hartley | Colpitts |
|---|---|---|
| Spannungsteiler | induktiv (Spulenanzapfung N1/N2) | kapazitiv (C1 und C2) |
| Frequenzbereich | 100 kHz – 100 MHz | 1 MHz – 1 GHz |
| HF-Eignung | gut | sehr gut |
| Quarz-Version | selten | ja (Quarz-Colpitts) |
| Abstimmung | variable C (einfach) | variable C (einfach) |
| Oberwellenunterdrückung | gut | besser |

## Anwendungen

- **Abstimmbare HF-Generatoren:** AM-/FM-Testsender, Signalgeneratoren
- **Radioempfänger:** Ortoszillator im Superheterodyne-Prinzip
- **Überall wo inductiv getapte Spulen einfacher realisierbar sind als 2 separate Kondensatoren**
