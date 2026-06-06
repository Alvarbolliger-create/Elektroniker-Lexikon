---
title: Regelstrecke
kategorie: EK
kapitel: Regelungstechnik
tags: [regelstrecke, RC-Glied, PT1, PT2, sprungantwort, zeitkonstante, totzeit, ordnung, verzugszeit, ausgleichszeit, streckenverhalten]
groessen: T|Zeitkonstante|s; t_u|Verzugszeit|s; t_g|Ausgleichszeit|s; K_S|Streckenverstärkung|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Regelkreis Grundlagen]]
- [[Tiefpass]]
:::
:::vbox
**Verwandte Artikel**
- [[PID-Regler]]
:::
:::vbox
**Führt weiter zu**
- [[PID-Regler]]
:::
:::

---

Die **Regelstrecke** ist das zu regelnde System — alles zwischen Stellgrösse (y) und Istwert (x), inklusive Aktor und Sensor. Ihre Ordnung und Dynamik bestimmen, welcher Regler geeignet ist.

## Regelstrecke als RC-Glieder (aus dem Spick)

Im Spick wird die Regelstrecke durch hintereinandergeschaltete RC-Glieder modelliert. Jedes Glied entspricht einer Ordnung und verlangsamt die Sprungantwort:

| Ordnung | RC-Glieder | Sprungantwort | Regelbarkeit |
|---|---|---|---|
| 1. Ordnung (PT1) | 1 RC-Glied | Exponentiell, kein Überschwingen | einfach |
| 2. Ordnung (PT2) | 2 RC-Glieder | S-Kurve, evtl. Überschwingen | schwieriger |
| 3. Ordnung | 3 RC-Glieder | S-Kurve mit scheinbarer Totzeit | schwierig |

Jedes Zeitglied addiert Phasenverzug — mit steigender Ordnung wird die Regelung anspruchsvoller.

## Zeitkonstante

:::formel
T = R * C    # Zeitkonstante eines RC-Glieds
# Nach t = T:   Ausgang bei 63.2 % des Endwerts
# Nach t = 3T:  Ausgang bei 95.0 %
# Nach t = 5T:  Ausgang bei 99.3 % (eingeschwungen)
:::

## Sprungantwort — Kennwerte

:::schematic Sprungantwort PT1 und PT2 Vergleich: Horizontale Achse = Zeit t, vertikale Achse = x/x_end in %. PT1 (1 RC-Glied): Exponentieller Anstieg, nach T = 63.2%, nach 3T = 95%, nach 5T = 99.3%. PT2 (2 RC-Glieder): S-förmige Kurve, langsamer Start, dann steilerer Anstieg, später flacher. Beide erreichen 100%. Eingezeichnet: t_u (Verzugszeit, Schnittpunkt Wendetangente/Zeitachse), t_g (Ausgleichszeit, Schnittpunkt Wendetangente/100%-Linie)
/Diagramm/sprungantwort_pt1_pt2.svg
:::

Aus der Sprungantwort der Strecke lassen sich für den Reglerentwurf ableiten:

| Kennwert | Symbol | Beschreibung |
|---|---|---|
| Verzugszeit | t_u | Zeit bis die Tangente am Wendepunkt die Zeitachse schneidet |
| Ausgleichszeit | t_g | Zeit bis die Tangente den Endwert schneidet |
| Streckenverstärkung | K_S | Verhältnis Endwert / Eingangssprung |

:::formel
K_S = Delta_x / Delta_y    # Streckenverstärkung (statisch)
:::

Das Verhältnis **t_u / t_g** beschreibt die Regelbarkeit:

| t_u / t_g | Regelbarkeit |
|---|---|
| < 0.1 | sehr gut (schnelle Strecke) |
| 0.1 – 0.3 | gut |
| 0.3 – 0.5 | schwierig |
| > 0.5 | sehr schwierig (grosse Totzeit) |

## Streckentypen in der Praxis

| Physikalisches System | Streckentyp | Typischer Regler |
|---|---|---|
| Temperaturregelung (Ofen) | PT2 / PT3 | PID |
| Motorgeschwindigkeit | PT1 | PI |
| Füllstandsregelung | Integrierende Strecke | P oder PD |
| Druckregelung | PT1 | PI |

:::tip
Für die Praxis: Die Sprungantwort der Strecke immer messen, bevor der Regler dimensioniert wird. Aus t_u, t_g und K_S lassen sich Ziegler-Nichols-Parameter direkt berechnen. → [[PID-Regler]]
:::
