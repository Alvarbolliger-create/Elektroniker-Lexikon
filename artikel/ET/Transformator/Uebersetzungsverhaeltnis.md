---
title: Übersetzungsverhältnis
kategorie: ET
tags: [übersetzungsverhältnis, transformator, windungszahl, spannungsübersetzung, stromübersetzung, impedanzübersetzung, kopplungsfaktor, realer transformator, streufluss, gegeninduktivität]
groessen: u|Übersetzungsverhältnis|—; N1|Windungszahl primär|—; N2|Windungszahl sekundär|—; U1|Primärspannung|V; U2|Sekundärspannung|V; I1|Primärstrom|A; I2|Sekundärstrom|A; Z1|Impedanz primär|Ohm; Z2|Impedanz sekundär|Ohm; k|Kopplungsfaktor|—
_status: PORT  # ET_alt/Transformator/Uebersetzungsverhaeltnis.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Transformator Aufbau]]
:::
:::vbox
**Führt weiter zu**
- [[Wirkungsgrad & Verluste (Transformator)]]
:::
:::

---

Das Übersetzungsverhältnis beschreibt, wie Spannung, Strom und Impedanz zwischen Primär- und Sekundärseite eines Transformators umgesetzt werden. Es ist das zentrale Designparameter bei jeder Trafodimensionierung.

## Spannungsübersetzung

:::schematic Transformator Übersetzungsverhältnis: Transformatorsymbol (zwei Spulen mit Kern); Primärseite links: N1 Windungen, Spannung U1, Strom I1; Sekundärseite rechts: N2 Windungen, Spannung U2, Strom I2, Lastwiderstand Z2; Verhältnisse U1/U2 = N1/N2 und I1/I2 = N2/N1 als Beschriftung
/schaltplaene/transformator/uebersetzungsverhaeltnis.svg
:::

Im idealen Transformator ist das Spannungsverhältnis gleich dem Windungszahlverhältnis. Mehr Windungen auf der Sekundärseite → höhere Spannung (Aufwärtstransformator).

:::formel
U2 / U1 = N2 / N1
:::

Das Übersetzungsverhältnis u = N1/N2 (primär/sekundär ist Konvention, manchmal auch umgekehrt definiert):

:::formel
u = N1 / N2
:::

| u | Typ | Wirkung |
|---|---|---|
| u > 1 | Abwärtstransformator | U2 < U1 (N2 < N1) |
| u = 1 | Trenntransformator | U2 = U1 |
| u < 1 | Aufwärtstransformator | U2 > U1 (N2 > N1) |

## Realer Transformator — Kopplungsfaktor k

Alle bisherigen Formeln gelten für den **idealen** Transformator: Der gesamte magnetische Fluss der Primärwicklung durchsetzt auch die Sekundärwicklung. In der Realität koppelt nur ein Teil — der Rest verläuft als **Streufluss** durch die Luft (→ [[Transformator Aufbau]]). Der **Kopplungsfaktor k** (0 < k ≤ 1) beschreibt, wie gut diese magnetische Kopplung ist:

:::formel
M = k * sqrt(L1 * L2)    # Gegeninduktivität M; k = 1 -> ideale (verlustfreie) Kopplung
:::

Für die im Leerlauf (kein Laststrom auf der Sekundärseite) induzierte Sekundärspannung folgt daraus eine **um den Faktor k reduzierte** Spannungsübersetzung:

:::formel
U2 = U1 * k * (N2 / N1) = U1 * k / u    # u = N1/N2 = Übersetzungsverhältnis
:::

Eine schwächere Kopplung (k < 1, z. B. durch Luftspalt, schlechten Kernschluss oder lose gekoppelte Spulen) liefert also **weniger** Sekundärspannung, als die ideale Übersetzung allein vermuten lässt — die fehlende Spannung "verschwindet" im nicht gekoppelten Streufluss.

:::monospace
Beispiel: realer Netztrafo mit k = 0.85, ü = 35, U1 = 230 V
U2_ideal = U1 / ü      = 230 / 35  = 6.57 V   (Annahme: perfekte Kopplung, k = 1)
U2_real  = U2_ideal * k = 6.57 * 0.85 = 5.59 V   (mit Kopplungsfaktor k = 0.85)
:::

:::tip
k = 1 entspricht dem idealen Transformator — alle übrigen Formeln dieser Seite gelten dann unverändert. Reale 50-Hz-Netztrafos mit gutem Kernschluss erreichen meist k > 0.95; kleine k-Werte (z. B. 0.85) treten bei deutlichem Luftspalt oder schwacher magnetischer Kopplung auf (lose gekoppelte HF-Spulen, Luftübertrager).
:::

## Stromübersetzung

Die Leistung bleibt beim idealen Trafo erhalten (P1 = P2). Da P = U · I, folgt: Was bei der Spannung "gewonnen" wird, geht beim Strom "verloren".

:::formel
I1 / I2 = N2 / N1    # Strom umgekehrt proportional zur Windungszahl
:::

Hohe Spannung → kleiner Strom (Hochspannungsübertragung: kleine Verluste). Niedrige Spannung → grosser Strom (Sekundärseite bei Schweisstransformator: hunderte Ampere).

:::monospace
Beispiel Netztrafo: N1 = 2000, N2 = 100, U1 = 230 V
U2 = 230 * 100 / 2000 = 11.5 V
Bei I2 = 2 A: I1 = 2 * 100 / 2000 = 0.1 A
P = 11.5 * 2 = 23 W = 230 * 0.1 (Probe) ✓
:::

## Impedanzübersetzung

Impedanzen werden quadratisch übersetzt. Das ist entscheidend für die [[Leistungsanpassung]]: Ein niederohmiger Lautsprecher (4 Ω) kann über einen Übertrager an einen hochohmigen Verstärkerausgang angepasst werden.

:::formel
Z1 / Z2 = (N1 / N2)^2
:::

:::monospace
Beispiel Übertrager: Verstärker Z1 = 1 kOhm, Lautsprecher Z2 = 4 Ohm
Benötigtes Windungszahlverhältnis:
N1/N2 = sqrt(Z1/Z2) = sqrt(1000/4) = sqrt(250) = 15.8
:::

:::tip
Die Impedanzübersetzung erklärt, warum Trafos in der Audiotechnik und in HF-Schaltungen eingesetzt werden: Sie ermöglichen optimale Leistungsübertragung zwischen Schaltungsstufen mit sehr unterschiedlichen Impedanzen.
:::
