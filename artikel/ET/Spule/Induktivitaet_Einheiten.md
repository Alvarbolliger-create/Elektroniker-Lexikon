---
title: Induktivität & Einheiten
kategorie: ET
tags: [induktivität, henry, windungszahl, spulenkonstante, al-wert, berechnung]
groessen: L|Induktivität|H; N|Windungszahl|—; A_L|Spulenkonstante|H; mu_r|relative Permeabilität|—; l|Kernlänge|m; A|Kernfläche|m²
_status: PORT  # ET_alt/Spule/Induktivitaet_Einheiten.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Spule (Übersicht)]]
:::
:::

---

Die Induktivität ist das Mass für die Fähigkeit einer Spule, magnetische Energie zu speichern. Grosse Induktivität bedeutet: viel Energie bei kleiner Stromänderung.

## Einheit Henry (H)

Das Henry (H) ist die SI-Einheit der Induktivität. 1 H = 1 Vs/A — eine Induktivität von 1 H erzeugt bei einer Stromänderung von 1 A/s eine Gegenspannung von 1 V.

| Vorsilbe | Symbol | Wert | Typische Bauteile |
|---|---|---|---|
| Millihenry | mH | 10⁻³ H | Drosseln, NF-Übertrager |
| Mikrohenry | µH | 10⁻⁶ H | HF-Drosseln, SMD-Spulen |
| Nanohenry | nH | 10⁻⁹ H | Leitungsinduktivität, Chip-Induktor |

## Berechnung (Solenoid/Ringkern)

Für eine zylindrische Spule (Solenoid) mit Länge l, Querschnitt A, Windungszahl N und Kernmaterial mu_r:

:::formel
L = mu_0 * mu_r * N^2 * A / l
:::

Die Induktivität wächst:
- Quadratisch mit der Windungszahl N
- Linear mit mu_r (Kernmaterial entscheidend)
- Linear mit der Kernfläche A
- Umgekehrt mit der Kernlänge l

## AL-Wert (Spulenkonstante)

Hersteller von Kernmaterialien geben den **AL-Wert** (Spulenkonstante) an. Er beschreibt, wie viel Induktivität pro Windung² der Kern liefert:

:::formel
L = A_L * N^2    # L in Henry, wenn A_L in H angegeben
:::

Der AL-Wert wird oft in nH/N² oder µH/N² angegeben.

:::monospace
Beispiel: Ferritkern AL = 250 nH, N = 20 Windungen
L = 250e-9 * 20^2 = 250e-9 * 400 = 100 µH

Benötigte Windungszahl für L = 470 µH:
N = sqrt(L / AL) = sqrt(470e-6 / 250e-9) = sqrt(1880) = 43 Windungen
:::

:::tip
Der AL-Wert ist eine praktische Grösse für die Spulenentwicklung: Kern wählen (nach AL-Wert aus Datenblatt), Windungszahl berechnen, wickeln. Keine komplizierte Geometrieberechnung nötig.
:::
