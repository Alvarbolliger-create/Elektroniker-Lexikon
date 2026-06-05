---
title: Selbstinduktion & Induzierte Spannung
kategorie: ET
tags: [selbstinduktion, induzierte spannung, lenzsche regel, flussänderung, induktionsgesetz, faraday]
groessen: u_i|induzierte Spannung|V; N|Windungszahl|—; Phi|magnetischer Fluss|Wb; L|Induktivität|H; i|Strom|A
_status: PORT  # ET_alt/Spule/Selbstinduktion.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Spule (Übersicht)]]
:::
:::vbox
**Verwandte Artikel**
- [[Magnetisierungskurve & Hysterese]]
:::
:::vbox
**Führt weiter zu**
- [[Auf- und Entladung (RL)]]
:::
:::

---

Wenn sich der magnetische Fluss durch eine Spule ändert, entsteht eine Spannung — egal ob der Fluss durch eine äussere Quelle oder durch den eigenen Strom der Spule erzeugt wird. Letzteres nennt man Selbstinduktion.

## Faradaysches Induktionsgesetz

Eine Flussänderung in einer Spule mit N Windungen erzeugt eine Spannung proportional zur Änderungsgeschwindigkeit. Das ist das Grundprinzip aller Transformatoren und Induktivitäten.

:::formel
u_i = -N * dPhi / dt    # induzierte Spannung (negatives Vorzeichen = Lenzsche Regel)
:::

Das Minuszeichen zeigt die Richtung an: Die induzierte Spannung wirkt immer so, dass sie ihrer Ursache entgegenwirkt ([[#Lenzsche Regel]]).

## Induzierte Spannung über Stromänderung

Für eine lineare Spule ist der Fluss proportional zum Strom: Phi = L · i / N. Eingesetzt ergibt sich die für Schaltungen wichtigste Form:

:::formel
U_L = L * di / dt    # Spannung an der Spule (Vorzeichen gemäss Zählpfeilrichtung)
:::

Diese Formel zeigt: Eine Spule "widersteht" Stromänderungen. Je schneller sich der Strom ändert und je grösser L, desto grösser die induzierte Spannung.

:::info
**Vorzeichenkonvention:** Manche Bücher schreiben `u_i = −L · di/dt` (Faraday-Konvention: induzierte EMK wirkt entgegen). Für Schaltungsberechnungen wird meist `U_L = L · di/dt` verwendet — die Spannung am Bauteil in Stromrichtung. Beide sind korrekt, solange die Zählpfeile konsequent definiert sind.
:::

:::monospace
Beispiel: L = 10 mH, Strom steigt in 1 ms von 0 auf 2 A
di/dt = 2 / 0.001 = 2000 A/s
U_L = 10e-3 * 2000 = 20 V
:::

## Berechnung U_L aus einem Stromdiagramm

Wenn der Strom stückweise linear verläuft (wie in Prüfungsaufgaben üblich), ist di/dt in jedem Abschnitt konstant — und damit auch U_L.

**Vorgehen:**
1. Steigung jedes Abschnitts ablesen: di/dt = ΔI / Δt
2. U_L = L × di/dt berechnen
3. Resultat abschnittweise einzeichnen

:::monospace
Beispiel: L = 5 mH, Strom-Diagramm mit drei Abschnitten

Abschnitt 1 (0–2 ms): I steigt von 0 auf 4 mA
  di/dt = 4e-3 / 2e-3 = 2 A/s  →  U_L = 5e-3 * 2 = +10 mV

Abschnitt 2 (2–4 ms): I = 4 mA konstant
  di/dt = 0  →  U_L = 0 mV

Abschnitt 3 (4–6 ms): I fällt von 4 mA auf 0
  di/dt = -4e-3 / 2e-3 = -2 A/s  →  U_L = 5e-3 * (-2) = -10 mV
:::

:::tip
Drei Faustregeln für Graphen:
- Strom konstant → U_L = 0 (Spule wirkt wie Draht)
- Strom steigt → U_L positiv
- Strom fällt → U_L negativ
- Steilere Flanke = grösseres |di/dt| = grösseres |U_L|
:::

## Lenzsche Regel

:::schematic
/abbildungen/spule/lenzsche_regel_gegenrichtung.svg
:::

Die induzierte Spannung (und der daraus resultierende Strom) wirkt immer **der Flussänderung entgegen** — daher das Minuszeichen. Das ist eine Folge der Energieerhaltung.

**Konsequenzen:**
- Eine Spule **verzögert** Stromänderungen — sie kann den Strom nicht sprunghaft ändern.
- Wird ein Stromkreis mit Spule **unterbrochen**, bricht der Strom schlagartig zusammen. Die Spule versucht dagegen anzukämpfen und erzeugt dabei eine sehr hohe Induktionsspannung (Abschaltspannung).

:::warning
Beim Abschalten induktiver Lasten (Relais, Motoren, Transformatoren) entstehen hohe Induktionsspannungen — typisch das 5- bis 100-fache der Betriebsspannung. Diese zerstören Transistoren und andere Halbleiter. Schutzmassnahme: **Freilaufdiode** parallel zur Spule (→ EK-Bereich).
:::

## Induzierte Spannung (Bewegung im Feld)

Ein Leiter der Länge l, der sich mit Geschwindigkeit v senkrecht zu einem Magnetfeld B bewegt, hat eine induzierte Spannung — Grundlage aller Generatoren:

:::formel
u_i = B * l * v    # Geschwindigkeitsinduktion
:::

Je schneller die Bewegung, je länger der Leiter, je stärker das Feld — desto grösser die Spannung. In einem Generator dreht sich eine Spule im Feld, was eine sinusförmige Wechselspannung ergibt.
