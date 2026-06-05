---
title: Spannungs- & Stromteiler
kategorie: ET
tags: [spannungsteiler, stromteiler, belastet, unbelastet, pegelanpassung]
groessen: U|Spannung|V; I|Strom|A; R|Widerstand|Ohm
_status: PORT  # ET_alt/Schaltkreise/Spannungs_Stromteiler.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
:::
:::vbox
**Verwandte Artikel**
- [[Erzeuger-Ersatzschaltung (Thévenin)]]
:::
:::vbox
**Führt weiter zu**
- [[Leistungsanpassung]]
- [[Brückenschaltung (Wheatstone)]]
:::
:::

---

Spannungs- und Stromteiler sind die einfachsten Schaltungen zur Signalanpassung. Sie stecken in fast jedem Gerät — als Pegel-Anpassung, Referenzspannung oder Sensorauswertung.

## Unbelasteter Spannungsteiler

:::schematic
/schaltplaene/schaltkreise/spannungsteiler.svg
:::

Zwei Widerstände R1 und R2 in Reihe teilen die Eingangsspannung U_e im Verhältnis ihrer Widerstandswerte. Der Ausgang U_a wird zwischen R2 und GND abgegriffen.

:::formel
U_a = U_e * R2 / (R1 + R2)
:::

"Unbelastet" bedeutet: kein Strom fliesst aus dem Ausgang heraus — der Abnehmer hat unendlich hohen Eingangswiderstand.

:::monospace
Beispiel: U_e = 10 V, R1 = 30 kOhm, R2 = 10 kOhm
U_a = 10 * 10 / (30 + 10) = 2.5 V
:::

## Belasteter Spannungsteiler

Wird ein Lastwiderstand R_L an den Ausgang angeschlossen, liegt er **parallel** zu R2. Der effektive Widerstand R2 || R_L ist kleiner als R2 — die Ausgangsspannung sinkt.

:::formel
U_a = U_e * (R2 * R_L / (R2 + R_L)) / (R1 + R2 * R_L / (R2 + R_L))
:::

**Faustregel**: Damit der Belastungseffekt klein bleibt, sollte R_L mindestens **10× grösser** sein als R2. In der Praxis werden Spannungsteiler deshalb so dimensioniert, dass der Ruhestrom durch R1/R2 deutlich grösser ist als der Laststrom.

:::monospace
Belastungseffekt: R1 = 30 kOhm, R2 = 10 kOhm, R_L = 10 kOhm
R2 || R_L = 5 kOhm
U_a = 10 * 5 / (30 + 5) = 1.43 V  (statt 2.5 V)
:::

:::warning
Operationsverstärker, Mikrocontroller-Eingänge und andere hochohmige Abnehmer belasten den Teiler kaum. Niederohmige Lasten (Relais, direkte Verdrahtung) können die Ausgangsspannung stark verfälschen.
:::

## Stromteiler

:::schematic
/schaltplaene/schaltkreise/stromteiler.svg
:::

Beim Stromteiler liegen R1 und R2 **parallel** an einer gemeinsamen Spannung U. Der Gesamtstrom I_ges teilt sich im umgekehrten Verhältnis der Widerstände auf.

:::formel
I1 = I_ges * R2 / (R1 + R2)
:::

:::formel
I2 = I_ges * R1 / (R1 + R2)
:::

Merkhilfe: Der Strom im Zweig R1 bestimmt sich mit R2 im Zähler — weil R2 den anderen Pfad beschreibt. Der kleinere Widerstand zieht den grösseren Strom.

:::monospace
Beispiel: I_ges = 100 mA, R1 = 100 Ohm, R2 = 400 Ohm
I1 = 100 * 400 / (100 + 400) = 80 mA  (kleinerer R, grösserer I)
I2 = 100 * 100 / (100 + 400) = 20 mA
Probe: 80 + 20 = 100 mA ✓
:::

:::tip
Stromteiler werden z. B. zur Messbereichserweiterung von Amperemetern verwendet: Ein kleiner Shunt-Widerstand parallel zum Messwerk leitet den Hauptstrom um — das Messwerk misst nur noch einen definierten Bruchteil.
:::
