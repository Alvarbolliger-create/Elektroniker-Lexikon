---
title: DA-Wandlung mit PWM
kategorie: SH
kapitel: Wandler
tags: [pwm, pulsweitenmodulation, tiefpassfilter, mittelwert, tastverhaeltnis]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[DA-Wandler (Digital-Analog-Umsetzer)]]
:::
:::vbox
**Verwandte Artikel**
- [[Tiefpass]]
:::
:::

---

Ein vollwertiger → [[DA-Wandler (Digital-Analog-Umsetzer)|DA-Wandler]] mit → [[R-2R-Netzwerk|R-2R-Netzwerk]] und Operationsverstärker ist eine vergleichsweise aufwendige Schaltung — die meisten Mikrocontroller verzichten deshalb darauf und besitzen **keinen** integrierten DA-Wandler. Was sie aber praktisch immer mitbringen, ist ein **PWM-Ausgang** (Pulsweitenmodulation). Mit nur zwei zusätzlichen passiven Bauteilen lässt sich daraus eine erstaunlich brauchbare analoge Spannung gewinnen.

## Grundprinzip: aus Rechteckimpulsen wird Gleichspannung

:::merke
Ein **PWM-Signal** ist ein Rechtecksignal konstanter Frequenz, dessen **Tastverhältnis** (Verhältnis von High- zu Gesamtdauer) den gewünschten analogen Wert codiert: Ein Tastverhältnis von 0 % entspricht der minimalen, 100 % der maximalen Ausgangsspannung, 50 % genau dem Mittelwert. Führt man dieses Rechtecksignal auf einen **Tiefpassfilter** — die einfachste Variante besteht nur aus einem Widerstand R und einem Kondensator C —, so bildet dieser den **linearen Mittelwert** des PWM-Signals: Aus dem schnell schaltenden Rechteck entsteht eine Gleichspannung mit einem kleinen, verbleibenden Wechselanteil, dem sogenannten **Ripple** (Restwelligkeit).
:::

## Dimensionierung des Tiefpasses: ein Zielkonflikt

Wie stark dieser Ripple ausfällt, hängt direkt von der Dimensionierung des Filters ab — und hier zeigt sich ein typischer Kompromiss zwischen Reaktionsgeschwindigkeit und Glättungsgüte:

:::tip
Die Grenzfrequenz eines einfachen RC-Tiefpasses berechnet sich über → [[Tiefpass|f_c = 1 / (2π · R · C)]]. Beispiel: Bei einer PWM-Frequenz von 100 Hz, R = 100 kΩ und C = 1 µF sowie V_cc = 5 V ergibt sich ein Ripple von rund 125 mV — bei einem 8-Bit-DA-Wandler mit U_LSB ≈ 19,5 mV ist das deutlich zu viel. Senkt man die Grenzfrequenz, sinkt zwar der Ripple, doch die **Einschwingzeit** t_S ≈ 5 · R · C wächst proportional mit — bei obigem Beispiel auf bereits 500 ms. Das bedeutet: Eine Verbesserung der Glättung erkauft man sich stets mit einer trägeren Reaktion auf neue PWM-Werte. Wichtig zudem: Diese Abschätzung gilt nur, solange der Filterausgang kaum belastet wird — meist braucht es einen nachgeschalteten Spannungsfolger (→ [[OPV Grundlagen|Impedanzwandler]]), um den Tiefpass von der eigentlichen Last zu entkoppeln.
:::

## Warum ein einfacher Tiefpass an seine Grenzen stösst

:::warning
Ein RC-Tiefpass erster Ordnung dämpft Signale oberhalb seiner Grenzfrequenz nur mit **−20 dB pro Dekade** — ein Signal mit der zehnfachen Frequenz wird also lediglich um den Faktor 10 abgeschwächt. Um den Ripple auf ein vernachlässigbares Mass zu drücken, müsste das Verhältnis von PWM-Frequenz zu Grenzfrequenz entsprechend riesig sein — was wiederum eine sehr hohe PWM-Taktfrequenz voraussetzt. Bei niedrigeren PWM-Frequenzen bleibt deshalb oft nur ein unbefriedigender Kompromiss zwischen Ripple und Reaktionszeit.
:::

## Die Lösung: mehrere Tiefpässe in Serie

:::info
Schaltet man **zwei Tiefpässe in Serie**, entsteht ein Filter zweiter Ordnung mit einer Dämpfung von −40 dB pro Dekade — ein Signal mit zehnfacher Frequenz wird nun um den Faktor 100 gedämpft. Im obigen Beispiel lässt sich damit bei vergleichbarer Grenzfrequenz (rund 70 Hz) der Ripple von 125 mV auf etwa 20 mV senken — ein gewaltiger Sprung in der Filtergüte bei nur geringfügig grösserem Bauteilaufwand. Schaltet man noch mehr Filterstufen — dritter, vierter Ordnung — in Serie, meist ergänzt um Operationsverstärker als **aktive Filter**, lässt sich der Ripple weiter reduzieren; ein Ansatz, der vor allem im Audiobereich verbreitet ist. Der Grundsatz bleibt dabei immer derselbe: Der verbleibende Ripple am Kondensator muss kleiner sein als die gewünschte Auflösung des "DA-Wandlers" — bei 8 Bit und 5 V Betriebsspannung also deutlich unter U_LSB = 5 V/256 ≈ 19,5 mV.
:::

## Eine pragmatische Lösung mit klaren Grenzen

Die DA-Wandlung über PWM ist damit kein Ersatz für einen "echten" → [[R-2R-Netzwerk|R-2R-DA-Wandler]] — ihre Genauigkeit hängt stark von der Filterdimensionierung ab, und sie eignet sich vor allem für **langsame, nicht sprunghaft wechselnde** Ausgangssignale wie Helligkeitssteuerungen, Lüfterregelungen oder einfache Sollwertvorgaben. Wo schnelle Sprünge oder höchste Präzision gefragt sind, kommen integrierte DA-Wandler-Bausteine (z. B. der LTC2644) zum Einsatz. Dafür benötigt die PWM-Lösung praktisch keine zusätzliche Analogtechnik — ein einziger Mikrocontroller-Pin, ein Widerstand und ein Kondensator genügen, um aus einem rein digitalen System eine brauchbare analoge Ausgangsspannung zu gewinnen.

Damit schliesst sich der Kreis zwischen den beiden Wandlerwelten: Vom rechenintensiven, hochpräzisen → [[Sigma-Delta-Wandler|Sigma-Delta-Verfahren]] bis zur denkbar einfachsten PWM-Glättung mit zwei passiven Bauteilen — überall begegnet man demselben Grundgedanken, dass sich analoge und digitale Welt mit dem passenden Schaltungstrick elegant miteinander verbinden lassen.
