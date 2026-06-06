---
title: Auf- und Entladung (RL)
kategorie: ET
tags: [spule, RL, zeitkonstante, tau, laden, entladen, exponentialkurve, transient, stromaufbau]
groessen: tau|Zeitkonstante|s; R|Widerstand|Ohm; L|Induktivität|H; I_L|Spulenstrom|A; U_L|Spulenspannung|V; I_0|Endstrom|A
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Induktivität & Einheiten]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Auf- und Entladung (Kondensator)]]
:::
:::vbox
**Führt weiter zu**
- [[RL-Reihenschaltung]]
:::
:::

---

Beim RL-Kreis ist es der **Strom**, der exponentiell ansteigt und abfällt — dual zum RC-Kreis, wo die Spannung exponentiell verläuft. Die Spule kann den Strom nicht sprunghaft ändern; er nähert sich dem Endwert mit der Zeitkonstante tau = L/R.

## Zeitkonstante tau = L / R

:::schematic RL-Ladeschaltung: Spannungsquelle U_0 in Reihe mit Schalter S, Widerstand R und Spule L; Strom I_L fliesst im Uhrzeigersinn; Spannung U_R am Widerstand und U_L an der Spule eingezeichnet; beim Schliessen von S baut sich der Strom exponentiell auf
/schaltplaene/spule/rl_ladeschaltung.svg
:::

:::formel
tau = L / R
:::

| Vielfaches von tau | Strom I_L / I_0 (Aufbau) | Strom I_L / I_0 (Abbau) |
|---|---|---|
| 1 × tau | 63 % | 37 % |
| 2 × tau | 86 % | 14 % |
| 3 × tau | 95 % | 5 % |
| 5 × tau | 99 % | 1 % |

**Faustregel**: Nach 5 · tau gilt der Vorgang als abgeschlossen.

## Ladevorgang (Stromaufbau)

Wird an einen RL-Kreis eine Spannung U_0 angelegt, baut sich der Strom exponentiell auf. Anfangs ist der Strom null (Spule wirkt wie Leerlauf), am Ende fliesst I_0 = U_0/R (Spule wirkt wie Kurzschluss):

:::formel
I_L(t) = I_0 * (1 - e^(-t / tau))    # I_0 = U_0 / R
:::

Die Spannung an der Spule ist anfangs maximal (U_L = U_0) und sinkt dann auf null:

:::formel
U_L(t) = U_0 * e^(-t / tau)
:::

## Entladevorgang (Stromabbau)

Wird die Quelle abgetrennt (Schalter öffnet), treibt die Energie im Magnetfeld den Strom weiter — die Spule "möchte" den Strom aufrechterhalten. Der Strom klingt exponentiell ab:

:::formel
I_L(t) = I_0 * e^(-t / tau)
:::

:::warning
Beim Öffnen des Schalters muss der Strom irgendwo fliessen. Gibt es keinen Weg (offener Schalter), baut die Spule eine sehr hohe Abschaltspannung auf. Diese Induktionsspannung kann Transistoren und Schalter zerstören. Immer [[Spule (Übersicht)|Freilaufdiode]] vorsehen!
:::

## Konstante Spannung direkt an L (kein R)

Liegt eine konstante Spannung U_0 **direkt** an der Spule (kein Serienwiderstand), gilt u_L = L · di/dt → der Strom steigt **linear**:

:::formel
i_L(t) = U_0 / L * t    # linearer Stromaufbau bei konstanter Spannung
:::

Das ist das RL-Äquivalent zum Konstantstrom-Laden des Kondensators: Statt konstanter Strom → lineare Spannung gilt hier konstante Spannung → linearer Strom. Dieser Fall tritt in Schaltreglern (Boost, Buck) exakt während der Einschaltphase auf — die Drosselspannung ist für die Einschaltzeit nahezu konstant, der Strom steigt linear.

| Methode | Kondensator | Spule |
|---|---|---|
| Konstanter Antrieb | Konstantstrom I | Konstante Spannung U |
| Resultat | Lineare Spannung: U_C = I·t/C | Linearer Strom: I_L = U·t/L |
| Praktisch | Sägezahn-ADC, Dreieckgenerator | Schaltregler, Boost/Buck-Wandler |

## Vergleich RC ↔ RL

| Eigenschaft | RC-Kreis | RL-Kreis |
|---|---|---|
| Zeitkonstante | tau = R · C | tau = L / R |
| Gespeicherte Grösse | Spannung U_C | Strom I_L |
| Springt nicht | U_C (Spannung) | I_L (Strom) |
| Anfangszustand | U_C(0) | I_L(0) |
| Ladeformel | U_C = U_0 · (1 − e^(−t/tau)) | I_L = I_0 · (1 − e^(−t/tau)) |

:::plot
var: t
range: 0, 5
colors: #dc2626, #0284c7
xlabel: Zeit (tau)
ylabel: Normiert
Strom I_L (Aufbau):       1 - exp(-t)
Spannung U_L (Abklingen):  exp(-t)
:::

:::monospace
Beispiel: L = 100 mH, R = 50 Ohm, U_0 = 12 V
tau = 100e-3 / 50 = 2 ms
I_0 = 12 / 50 = 240 mA
Strom nach 1 tau (2 ms): I = 240 * 0.63 = 151 mA
:::
