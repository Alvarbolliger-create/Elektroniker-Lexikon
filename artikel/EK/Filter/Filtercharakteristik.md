---
title: Filtercharakteristik
kategorie: EK
kapitel: Filter
tags: [filtercharakteristik, butterworth, chebyshev, bessel, elliptic, cauer, thompson, phasenlinearität, welligkeit, flankensteilheit, approximation, durchlassband, sperrband]
groessen: —
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Filter Grundlagen]]
- [[Tiefpass]]
- [[Hochpass]]
:::
:::vbox
**Verwandte Artikel**
- [[Aktive Filter]]
- [[Bandpass]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive Filter]]
:::
:::

---

Verschiedene mathematische Filterapproximationen bieten unterschiedliche Kompromisse zwischen flacher Durchlasskurve, Flankensteilheit und Phasenlinearität. In der Praxis werden meist Butterworth oder Chebyshev gewählt.

## Überblick

:::schematic Filtercharakteristiken Vergleich (Amplitudengang): Normierter Frequenzgang (f/f_g horizontal, dB vertikal). Butterworth: flach bis f_g, monoton fallend. Chebyshev: Welligkeit (Ripple) im Durchlassband, dann steilerer Abfall. Bessel: sanft abfallend schon vor f_g, dafür linearstes Phasenverhalten. Elliptisch: steilste Flanke, Welligkeit in beiden Bändern. Alle Kurven kreuzen sich bei f_g
/Diagramm/filtercharakteristik_vergleich.svg
:::

| Charakteristik | Durchlassband | Sperrband | Phase | Impulsantwort |
|---|---|---|---|---|
| **Butterworth** | maximal flach | monoton fallend | mittel | mittel |
| **Chebyshev** | Welligkeit | steiler als Butterworth | schlechter | Überschwingen |
| **Inverse Chebyshev** | flach | Welligkeit (Einbrüche) | besser als Cheby | mittel |
| **Elliptisch (Cauer)** | Welligkeit | Welligkeit | schlecht | stark überschwingend |
| **Bessel (Thompson)** | flach (sanft abfallend) | weich | maximal linear | minimal |

## Butterworth — maximal flach

Keine Welligkeit im Durchlassband — maximale Flachheit ("maximally flat magnitude"). Amplitude bei f_g: immer genau −3 dB. Steifheit steigt mit der Ordnung n.

- Beste Wahl für allgemeine Anwendungen
- Amplitude bei f_g: genau −3 dB
- Monoton fallend im Sperrbereich — keine Einbrüche

**Typischer Einsatz:** Audio, allgemeine Signalaufbereitung, ADC-Eingang.

## Chebyshev — steile Flanke

Steifere Flanke als Butterworth gleicher Ordnung, erkauft durch **Welligkeit (Ripple)** im Durchlassband. Typische Welligkeit: 0.5 dB, 1 dB oder 3 dB wählbar.

- Je grösser die Welligkeit, desto steiler die Flanke
- Bei hoher Güte Q > 0.707: **Resonanzüberhöhung bei f_g** — die Amplitude steigt kurz über 0 dB bevor sie abfällt. Das ist der typische "Buckel" im Bodediagramm
- Schlechtere Phaseneigenschaften als Butterworth

**Typischer Einsatz:** Kanaltrennung, wenn Durchlasskurve etwas schwanken darf; wenn eine Verstärkung nahe f_g gewünscht wird.

## Inverse Chebyshev — flacher Durchlass, Sperrband-Welligkeit

Welligkeit liegt im **Sperrband** (nicht im Durchlassband). Durchlassband bleibt flach, Sperrband hat Einbrüche (Nullstellen).

**Typischer Einsatz:** Wenn Durchlasskurve flach sein muss, aber Sperrband-Welligkeit tolerierbar ist.

## Elliptisch (Cauer) — steilste Flanke

Welligkeit sowohl im Durchlass- als auch im Sperrband. Dafür die **steilste Flanke** aller Charakteristiken bei gleicher Ordnung.

- Maximale Effizienz: höchste Steilheit bei gegebener Ordnung
- Komplexeste Berechnung und Realisierung
- Stark überschwingende Impulsantwort

**Typischer Einsatz:** Kritische Kanaltrennung, HF-Filter, wenn Bauteilanzahl minimiert werden muss.

## Bessel (Thompson) — lineares Phasenverhalten

Maximale Linearität der **Phasenverschiebung** über der Frequenz — alle Frequenzanteile werden gleich verzögert. Signalform bleibt erhalten (kein Überschwingen).

- Flachste Flanke aller Charakteristiken (dafür linearstes Phasenverhalten)
- Impulsantwort ohne Überschwingen — ideal für Rechteck- und Impulssignale

**Typischer Einsatz:** Datenübertragung, Impulsmessung, Videofilter, überall wo die Signalform erhalten bleiben muss.

## Entscheidungshilfe

:::tip
Für die Praxis gilt: **Butterworth zuerst probieren.** Wenn Flankensteilheit nicht reicht → Chebyshev. Wenn Signalform (Impuls, Rechteck) wichtig → Bessel. Elliptisch nur wenn wirklich die steilste mögliche Flanke gebraucht wird und Welligkeit tolerierbar ist.
:::

| Priorität | Wahl |
|---|---|
| Einfach, allgemein | Butterworth |
| Steilste Flanke | Elliptisch (Cauer) |
| Linearstes Phasenverhalten | Bessel |
| Kompromiss Steilheit/Flachheit | Chebyshev |
