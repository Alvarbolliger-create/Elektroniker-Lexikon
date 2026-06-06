---
title: LC-Filter
kategorie: ET
tags: [lc-filter, tiefpass, hochpass, bandpass, saugkreis, sperrkreis, filterordnung]
groessen: f_r|Resonanzfrequenz|Hz; L|Induktivität|H; C|Kapazität|F; omega_0|Resonanzkreisfrequenz|rad/s
_status: PORT  # ET_alt/Wechselstrom/LC_Filter.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Resonanz & Schwingkreise]]
:::
:::vbox
**Führt weiter zu**
- [[Quarz-Oszillator]]
:::
:::

---

LC-Filter nutzen den Resonanzeffekt von Spule und Kondensator, um bestimmte Frequenzen durchzulassen oder zu sperren. Sie erreichen steilere Filterkurven als einfache RC-Filter und finden Anwendung in HF-Technik, Netzfiltern und Audioverstärkern.

## Tiefpass (L + C)

:::schematic LC-Tiefpass und LC-Hochpass: Links oben: Tiefpass — Eingang links, Spule L in Reihe, dann Knoten, Kondensator C nach GND, Ausgang U_a rechts; Links unten: Hochpass — Eingang links, Kondensator C in Reihe, dann Knoten, Spule L nach GND, Ausgang U_a rechts; Beschriftung: U_e, L, C, U_a
/schaltplaene/wechselstrom/lc_filter_topologien.svg
:::

Ein Tiefpass lässt tiefe Frequenzen durch und sperrt hohe. Die einfachste LC-Tiefpassstruktur: L in Reihe, C parallel zur Last.

Bei tiefen Frequenzen: X_L klein → Signaldurchgang; X_C gross → kein Kurzschluss.
Bei hohen Frequenzen: X_L gross → Signal wird geblockt; X_C klein → Kurzschluss zur Masse.

**Grenzfrequenz** (Resonanzfrequenz des LC-Glieds):

:::formel
f_r = 1 / (2 * pi * sqrt(L * C))
:::

Oberhalb f_r fällt die Ausgangsspannung mit −40 dB/Dekade (2. Ordnung) — steiler als RC (−20 dB/Dekade).

## Hochpass (C + L)

Spiegelbildlich: C in Reihe, L parallel zur Last. Tiefe Frequenzen werden geblockt, hohe passieren.

Gleiche Resonanzfrequenzformel. Unterhalb f_r: −40 dB/Dekade.

## Bandpassfilter

Kombination: Serienresonanzkreis (LC-Reihe) als Bandpass, oder Parallelresonanzkreis als Bandsperre.

**Serienresonanzkreis als Bandpass**: Bei f = f_r ist Z minimal → maximaler Strom zur Last.

**Parallelresonanzkreis als Sperrkreis (Saugkreis)**: Bei f = f_r ist Z maximal → minimaler Strom zur Last. Dieser "Saugkreis" wird in Netzfiltern verwendet, um Oberschwingungen (z. B. 150 Hz, 250 Hz) zu unterdrücken.

## Frequenzgang

Die Amplitude im Verhältnis zur Eingangsfrequenz (normiert auf die Resonanzfrequenz f_r = 1):

:::plot
var: x
range: 0.1, 10
xscale: log
colors: #0284c7, #16a34a, #9333ea
xlabel: Frequenz (normiert, f_r = 1)
ylabel: Amplitude (normiert)
LC-TP (Q=0.7, Butterworth):  1 / sqrt((1 - x^2)^2 + (x/0.7)^2)
LC-TP (Q=2, Resonanzüberhöhung): 1 / sqrt((1 - x^2)^2 + (x/2)^2)
RC-TP 1. Ordnung (Vergleich): 1 / sqrt(1 + x^2)
:::

Unterhalb f_r: alle Filter auf voller Amplitude. Ab f_r fällt LC mit −40 dB/Dekade (2. Ordnung), RC nur mit −20 dB/Dekade. Bei Q > 0.707 entsteht eine Resonanzüberhöhung direkt bei f_r.

## Filterordnung

Jedes LC-Glied erhöht die Filterordnung um 2 (weil L und C zusammen wirken):

| Ordnung | Flankensteilheit | Bauteile |
|---|---|---|
| 1. Ordnung | −20 dB/Dekade | 1× R oder L oder C |
| 2. Ordnung | −40 dB/Dekade | 1× L + 1× C |
| 4. Ordnung | −80 dB/Dekade | 2× L + 2× C |

**Anwendungsbeispiel**: Netzfilter in Schaltnetzteilen verwenden LC-Filter hoher Ordnung, um die hochfrequenten Schaltstörungen vom Netz fernzuhalten (EMV-Norm).

:::tip
LC-Filter werden gegenüber RC-Filtern bevorzugt, wenn kein Leistungsverlust toleriert wird — eine Induktivität erzeugt im Idealfall keine Wärmeverluste (nur Blindwiderstand). In der Praxis hat L aber immer einen Wicklungswiderstand, der kleine Verluste verursacht.
:::
