---
title: Quarzoszillator
kategorie: EK
kapitel: Oszillatoren
tags: [quarz, quarzoszillator, piezoelektrisch, serienresonanz, parallelresonanz, güte, frequenzstabilität, ppm, ersatzschaltbild, CP, CS, L, RU, TCXO, OCXO]
groessen: f_r|Serienresonanzfrequenz|Hz; f_p|Parallelresonanzfrequenz|Hz; C_S|Serienkapazität|F; C_P|Parallelkapazität|F; L|Äquivalente Induktivität|H; Q|Güte|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[Colpitts-Oszillator]]
:::
:::vbox
**Verwandte Artikel**
- [[Pierce-Gate-Oszillator]]
- [[Colpitts-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Pierce-Gate-Oszillator]]
:::
:::

---

Ein Quarzoszillator nutzt den **piezoelektrischen Effekt** eines Quarzkristalls. Die mechanische Resonanzfrequenz ist durch die Geometrie des Kristalls extrem präzise festgelegt — typische Stabilität 10–100 ppm.

## Piezoelektrischer Effekt

Wird ein Quarzkristall elektrisch angeregt, schwingt er mechanisch. Die mechanische Schwingung erzeugt wiederum eine elektrische Spannung — ein selbstverstärkender Prozess bei der Resonanzfrequenz. Die Geometrie des Schnitts bestimmt f_r.

## Ersatzschaltbild

:::schematic Quarz-Ersatzschaltbild: Links Klemme 1, rechts Klemme 2. Oberer Zweig (Serien-Ast): R_u (Verlustwiderstand) in Reihe mit L (äquivalente Induktivität) in Reihe mit C_S (Serienkapazität). Unterer Zweig: C_P (Parallelkapazität der Elektroden) parallel über beide Klemmen. Zwischen f_r (Serienresonanz) und f_p (Parallelresonanz): Quarz wirkt induktiv — Betriebsbereich für Pierce und Colpitts
/Diagramm/quarz_ersatzschaltbild.svg
:::

Der Quarz wird elektrisch als Serienschwingkreis modelliert:

- **C_S:** Serienkapazität (mechanische Elastizität, typisch 1–50 fF)
- **L:** Serieinduktivität (mechanische Masse, typisch 1–100 mH)
- **R_u:** Serienwiderstand (Verluste, typisch 5–100 Ω)
- **C_P:** Parallelkapazität (Elektrodenkapazität, typisch 2–10 pF)

C_P liegt parallel zur gesamten Serie-Kombination (R_u + L + C_S).

## Resonanzfrequenzen (aus dem Spick)

Der Quarz hat zwei dicht beieinander liegende Resonanzfrequenzen:

:::formel
f_r = 1 / (2 * pi * sqrt(L * C_S))                       # Serienresonanz
f_p = sqrt(1 + C_S/C_P) / (2 * pi * sqrt(L * C_S))      # Parallelresonanz
:::

| Resonanz | Impedanz | Verhalten |
|---|---|---|
| Serienresonanz f_r | minimal (Kurzschluss) | rein resistiv |
| Parallelresonanz f_p | maximal (Leerlauf) | rein resistiv |
| Zwischen f_r und f_p | induktiv | Betriebsbereich Quarz-Colpitts und Pierce |

:::info
C_S ≪ C_P (typisch um Faktor 1000) → f_r und f_p liegen nur 0.1–1% auseinander. Die Güte Q des Quarzes beträgt 10'000–1'000'000. Zum Vergleich: Guter LC-Schwingkreis Q ≈ 100–200.
:::

## Frequenzstabilität

| Typ | Stabilität | Beschreibung |
|---|---|---|
| Normaler Quarz | ±10–100 ppm | Standardqualität |
| TCXO | ±1–5 ppm | Temperaturkompensiert |
| OCXO | ±0.01–0.1 ppm | Ofengesteuert (40–80 °C) |
| LC-Oszillator (Vergleich) | ±100–10'000 ppm | Stark temperaturabhängig |

## Betriebsmodi

**Serienresonanz:** Quarz als niederohmiger Pfad bei f_r — schwingt direkt in Serienresonanz.

**Parallelresonanz:** Quarz als Induktivität zwischen f_r und f_p — Basis für Pierce-Gate und Quarz-Colpitts.

:::warning
Lastkapazität einhalten: Externe Kondensatoren (C1, C2) verstimmen die Quarzfrequenz. Hersteller gibt Lastkapazität C_L im Datenblatt an — diese Angabe einhalten für spezifizierte Frequenz.
:::

## Anwendungen

- **MCU-Taktgeber:** 8–40 MHz in Pierce-Gate-Schaltung (in MCU eingebaut)
- **RTC-Quarz:** 32.768 kHz (= 2^15 Hz) für Uhrentakt
- **Kommunikation:** Trägerfrequenz-Synthese mit PLL
- **Messgeräte:** Frequenzreferenz, Zähler-Timebase
