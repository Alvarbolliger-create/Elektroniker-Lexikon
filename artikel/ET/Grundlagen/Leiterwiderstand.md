---
title: Leiterwiderstand
kategorie: ET
tags: [leiterwiderstand, spezifischer widerstand, stromdichte, leitfähigkeit, temperaturkoeffizient, alpha]
groessen: R|Widerstand|Ohm; rho|spez. Widerstand|Ohm·mm²/m; l|Leiterlänge|m; A|Querschnitt|mm²; J|Stromdichte|A/mm²; alpha|Temperaturkoeffizient|1/K
_status: PORT  # ET_alt/Grundlagen/Leiterwiderstand.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Elektrische Leistung]]
:::
:::vbox
**Verwandte Artikel**
- [[NTC & PTC]]
:::
:::vbox
**Führt weiter zu**
- [[Skin-Effekt]]
:::
:::

---

Jeder reale Leiter hat einen Widerstand — er hängt vom Material, der Länge, dem Querschnitt und der Temperatur ab. In der Praxis dimensioniert man Leitungsquerschnitte so, dass der Spannungsfall und die Verlustleistung im zulässigen Bereich bleiben.

## Geometrischer Widerstand

Der Widerstand eines Leiters steigt mit der Länge und sinkt mit dem Querschnitt. Das Material bestimmt den **spezifischen Widerstand** rho.

:::schematic Zylindrischer Leiter mit Länge l (Längsachse, Pfeil von links nach rechts) und kreisförmigem Querschnitt A (an der Stirnseite eingezeichnet); Strom I fliesst von links nach rechts; Material mit Kenngrösse rho beschriftet
/abbildungen/grundlagen/leiterwiderstand_geometrie.svg
:::

:::formel
R = rho * l / A
:::

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Widerstand | R | Ω | Gesuchte Grösse |
| Spez. Widerstand | rho | Ω·mm²/m | Materialkonstante |
| Länge | l | m | Leiterlänge (Hin- und Rückleiter!) |
| Querschnitt | A | mm² | Leiterquerschnitt |

**Typische Werte für rho (bei 20 °C):**

| Material | rho (Ω·mm²/m) | Anwendung |
|---|---|---|
| Kupfer (Cu) | 0,0172 | Leitungen, Wicklungen |
| Aluminium (Al) | 0,028 | Freileitungen, grosse Querschnitte |
| Eisen (Fe) | 0,1 | Konstruktionsteile |
| Konstantan | 0,49 | Präzisionswiderstände |
| Nichrom | 1,1 | Heizwiderstände |

:::tip
Bei Leitungsberechnungen ist die **Gesamtlänge** = Hinleiter + Rückleiter. Für eine 50 m lange Verbindung gilt l = 100 m.
:::

:::monospace
Beispiel: Kupferleitung, l = 100 m (50 m hin, 50 m zurück), A = 1,5 mm²
R = 0.0172 * 100 / 1.5 = 1.15 Ohm
:::

## Stromdichte

Die Stromdichte J gibt an, wie viel Strom pro mm² Querschnitt fliesst. Sie entscheidet über die thermische Belastung des Leiters.

:::formel
J = I / A    # Stromdichte J (A/mm²)
:::

**Richtwerte für Kupferleiter:**

| Anwendung | J_max (A/mm²) |
|---|---|
| Dauerbetrieb (isolierte Leitung) | 2–4 A/mm² |
| Kurzzeitbetrieb | bis 10 A/mm² |
| Wicklungen (Trafo, Motor) | 2–5 A/mm² |

:::warning
Überschreitet die Stromdichte den zulässigen Wert, erwärmt sich die Leitung übermässig. In der Schweiz legt die **NIN (Niederspannungs-Installations-Norm)** die maximalen Ströme pro Querschnitt verbindlich fest.
:::

## Temperaturabhängigkeit

Der Widerstand von Metallen steigt mit der Temperatur. Der **Temperaturkoeffizient alpha** gibt die relative Widerstandsänderung pro Kelvin an (bezogen auf 20 °C als Referenz).

:::formel
R_T = R_20 * (1 + alpha * (T - 20))    # T in °C, R_20 = Widerstand bei 20 °C
:::

| Material | alpha (1/K) |
|---|---|
| Kupfer | +0,00393 |
| Aluminium | +0,0039 |
| Konstantan | ±0,00001 (fast temperaturunabhängig) |
| Platin (Pt100) | +0,00385 (Messwiderstand) |

Ein positiver alpha-Wert bedeutet: Widerstand steigt mit der Temperatur (PTC-Verhalten). Bei [[NTC & PTC]] ist das Material dagegen so gewählt, dass der Widerstand gezielt sinkt oder stark ansteigt.

:::monospace
Beispiel: Kupferwicklung, R_20 = 2.5 Ohm, T = 80 °C
R_80 = 2.5 * (1 + 0.00393 * (80 - 20))
R_80 = 2.5 * 1.236 = 3.09 Ohm  (+24 %)
:::

## Verlustleistung am Leiter

Jeder Leitungswiderstand erzeugt Verlustleistung, die als Wärme abgegeben wird. Bei grossen Strömen ist dieser Verlust nicht vernachlässigbar.

:::formel
P_v = I^2 * R    # Verlust steigt quadratisch mit dem Strom
:::

Der quadratische Zusammenhang erklärt, warum Energieübertragung mit **hoher Spannung und kleinem Strom** effizienter ist — halbierter Strom bedeutet vierfach kleinere Leitungsverluste. Genau dafür wird der [[Transformator Aufbau|Transformator]] eingesetzt.
