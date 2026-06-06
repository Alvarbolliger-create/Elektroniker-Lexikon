---
title: Zeigerdiagramm
kategorie: ET
tags: [zeigerdiagramm, phasor, komplexe zahlen, impedanz, wechselstrom, phasenverschiebung]
groessen: U|Spannung|V; I|Strom|A; phi|Phasenwinkel|°; omega|Kreisfrequenz|rad/s
_status: PORT  # ET_alt/Wechselstrom/Zeigerdiagramm.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen & Effektivwert]]
:::
:::vbox
**Verwandte Artikel**
- [[Impedanz]]
:::
:::vbox
**Führt weiter zu**
- [[RL-Reihenschaltung]]
- [[RC-Reihenschaltung]]
:::
:::

---

Im Wechselstromkreis haben Spannung und Strom nicht nur Amplituden, sondern auch Phasen — sie können zeitlich verschoben sein. Das Zeigerdiagramm ist eine grafische Methode, um diese Phasenbeziehungen sichtbar und berechenbar zu machen.

## Darstellung als Zeiger

:::schematic Zeigerdiagramm einer RL-Reihenschaltung: Waagerechte reelle Achse, senkrechte imaginäre Achse; Strom I als Referenzzeiger auf der reellen Achse nach rechts; U_R in Phase mit I (horizontal); U_L senkrecht nach oben (90° vor I); Resultierende U_ges als Zeiger von Ursprung zur Spitze des Vektoradditions-Dreiecks; Winkel phi zwischen U_ges und I eingezeichnet; Beschriftung: I, U_R, U_L, U_ges, phi
/abbildungen/wechselstrom/zeigerdiagramm_rl.svg
:::

Jede sinusförmige Grösse lässt sich als rotierender Zeiger darstellen: Der Zeiger dreht sich mit der Kreisfrequenz omega im Gegenuhrzeigersinn. Seine Länge entspricht dem Scheitelwert (oder Effektivwert — muss konsequent sein), seine Winkelposition zur reellen Achse dem Phasenwinkel phi.

**Konvention:** In der Technik wird häufig der **Strom I** als Referenzzeiger horizontal (phi = 0°) gezeichnet — alle anderen Zeiger werden dazu in Beziehung gesetzt.

| Bauteil | Phasenbeziehung (U gegenüber I) | Zeiger |
|---|---|---|
| Widerstand R | U in Phase mit I | phi = 0°, horizontal |
| Spule L | U eilt I um 90° vor | phi = +90°, senkrecht nach oben |
| Kondensator C | U eilt I um 90° nach | phi = −90°, senkrecht nach unten |

Gedächtnisstütze: *ELI the ICE man* — bei L eilt E (Spannung) vor I, bei C eilt I vor E.

## Addition von Zeigern

Wenn mehrere Spannungen in einem Kreis wirken (Reihenschaltung), addiert man ihre Zeiger grafisch durch Aneinanderhängen. Die Resultierende zeigt Betrag und Phase der Gesamtspannung.

:::formel
U_ges = sqrt(U_R^2 + U_X^2)    # Betrag (Pythagoras, wenn U_R und U_X senkrecht)
:::

Das funktioniert, weil U_R und U_L (oder U_C) um genau 90° verschoben sind — also senkrecht zueinander stehen. Damit ist Pythagoras direkt anwendbar.

## Impedanzdreieck

Das Zeigerdiagramm der Spannungen skaliert direkt zum **Impedanzdreieck** (dividiert durch I):

- Horizontal: Wirkwiderstand R
- Vertikal: Reaktanz X (positiv = induktiv, negativ = kapazitiv)
- Hypotenuse: Impedanz Z

:::formel
Z = sqrt(R^2 + X^2)
:::

:::formel
phi = arctan(X / R)
:::

## Phasenverschiebung ablesen

Im Zeigerdiagramm lässt sich der Phasenwinkel phi direkt ablesen oder mit arctan berechnen:

- phi > 0°: induktive Last — Spannung eilt vor (Spule dominiert)
- phi = 0°: rein ohmscher Charakter — kein Blindanteil
- phi < 0°: kapazitive Last — Strom eilt vor (Kondensator dominiert)

:::tip
In der Praxis gibt phi wichtige Informationen über den Blindleistungsanteil einer Last. Leistungsfaktoren (cos phi) nahe 1 sind energetisch günstig — Motoren und Transformatoren mit phi ≠ 0 müssen durch [[Blindleistungskompensation]] korrigiert werden.
:::
