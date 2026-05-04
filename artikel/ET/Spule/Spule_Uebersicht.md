---
title: Spule (Übersicht)
kategorie: ET
tags: [spule, induktivität, bauteil, passiv, magnetfeld, gegeninduktivität, henry, freilaufdiode, selbstinduktion, wechselstrom, kopplungsfaktor]
symbol: L
einheit: H
---

Eine Spule speichert Energie im Magnetfeld. Sie widersetzt sich Änderungen des Stroms. Je schneller sich der Strom ändert, desto stärker ihre Reaktion.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator (Übersicht)]]
- [[Transformator]]
:::
:::vbox
**Führt weiter zu**
- [[Induktivität & Einheiten]]
- [[Selbstinduktion]]
- [[Spule Typen]]
:::
:::

---

## Schaltsymbol

Eine Reihe von Bögen oder Spiralen.

:::schematic Spule (IEC)
/schaltplaene/symbole/L.svg
:::

Bei Spulen mit Kern ist eine gerade Linie parallel gezeichnet. Bei Eisenkern sind es zwei parallele Linien.

## Aufbau

Leiterdraht zu einer Spirale gewickelt. Das erzeugt beim Stromfluss ein Magnetfeld im Innern. Dieses Feld speichert die Energie.

Mit Kern aus Ferrit oder Eisen wird das Feld konzentriert und die Induktivität steigt.

## Grundgrössen

:::monospace
U = L * dI/dt          # Spannung proportional zur Stromänderungsrate
E = 0.5 * L * I^2     # gespeicherte Energie
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Induktivität | L | H (Henry) |
| Spannung | U | V |
| Strom | I | A |
| Energie | E | J |

## Bauformen

**Luftspule**: Ohne Kern. Stabil, kein Sättigungseffekt. Für hohe Frequenzen.

**Ferritkern**: Kompakt, hohe Induktivität. Typisch in Schaltnetzteilen und Filtern.

**Drosselspule**: Grosse Induktivität für Gleichstromfilterung (Netzdrossel).

**Transformator**: Zwei oder mehr Spulen auf demselben Kern. Überträgt Energie magnetisch.

## Reihen- und Parallelschaltung

### Ohne Kopplung (getrennte Kerne)

:::schematic Spulen in Reihe
/schaltplaene/spule_reihe.svg
:::

:::monospace
L_ges = L1 + L2 + ... + Ln         # Reihenschaltung
1/L_ges = 1/L1 + 1/L2 + ... + 1/Ln # Parallelschaltung
:::
### Mit Kopplung (gemeinsamer Kern)

:::schematic Spulen mit Kopplung
/schaltplaene/spule_kopplung.svg
:::

Teilen sich zwei Spulen denselben Kern, beeinflusst das Magnetfeld der einen die andere. Diese Gegeninduktivität M verändert die Gesamtinduktivität:

:::monospace
M = k * sqrt(L1 * L2)              # Gegeninduktivität (k = Kopplungsfaktor, 0 bis 1)

L_ges = L1 + L2 + 2 * M           # gleichsinnig gewickelt (Felder addieren sich)
L_ges = L1 + L2 - 2 * M           # gegensinnig gewickelt (Felder schwächen sich)
:::
Ein Kopplungsfaktor k = 1 bedeutet ideale Kopplung (Transformator). k = 0 bedeutet keine Kopplung.

## Verhalten

Bei Gleichstrom ist die Spule ein normaler Widerstand. Beim Einschalten widersetzt sie sich dem Stromaufbau. Beim Ausschalten versucht sie den Strom aufrechtzuerhalten und kann dabei hohe Spannungen erzeugen.

:::warning
Beim Unterbrechen des Stroms durch eine Spule entsteht eine Spannungsspitze. Diese kann Transistoren und andere Bauteile zerstören. Immer eine Freilaufdiode parallel zur Spule schalten.
:::
