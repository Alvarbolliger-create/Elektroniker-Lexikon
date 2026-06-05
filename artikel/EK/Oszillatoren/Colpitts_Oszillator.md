---
title: Colpitts-Oszillator
kategorie: EK
tags: [colpitts, oszillator, LC, schwingkreis, transistor, HF, hartley, rückkopplungsfaktor, VCO, phasenjitter]
symbol: f_0
einheit: Hz
---

Der Colpitts-Oszillator ist ein LC-Oszillator für höhere Frequenzen (100 kHz bis GHz). Er verwendet einen Schwingkreis mit einer Spule und zwei Kondensatoren als Spannungsteiler für die Rückkopplung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[Schwingkreis LC]]
- [[Transistor NPN]]
:::
:::vbox
**Verwandte Artikel**
- [[Wien-Brücken-Oszillator]]
- [[RC-Phasenschieber-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[Quarz-Oszillator]]
:::
:::

---

## Schaltungsprinzip

Der Colpitts verwendet zwei Kondensatoren (C1, C2) in Reihe mit einer Spule L. Der Mittelknoten zwischen C1 und C2 liefert das Rückkopplungssignal.

:::schematic
/Diagramm/colpitts_oszillator_0.svg
:::
**Funktionsprinzip**:
- L und C1||C2 bilden einen Parallelschwingkreis
- Der Spannungsteiler C1/C2 liefert die Rückkopplungsspannung an die Basis
- Der Transistor invertiert das Signal um 180°
- Der Schwingkreis dreht weitere 180° → 360° gesamt → Schwingbedingung

Das Verhältnis C1/C2 bestimmt den Rückkopplungsfaktor β.

---

## Formeln

:::formel
C_ser = C1 × C2 / (C1 + C2)         # Serienkapazität (wirksam für f₀)
f_0   = 1 / (2π × √(L × C_ser))     # Resonanzfrequenz
β     = C1 / C2                       # Rückkopplungsfaktor (Spannungsteiler)
A_min = C2 / C1                       # Mindestverstärkung des Transistors
:::
| Grösse | Symbol | Einheit | Beschreibung |
|---|---|---|---|
| Resonanzfrequenz | f₀ | Hz | Schwingfrequenz |
| Serienkapazität | C_ser | F | C1 und C2 in Reihe |
| Rückkopplungsfaktor | β | — | Verhältnis C1/C2 |
| Mindestverstärkung | A_min | — | = C2/C1 |

---

## Vertiefung

**Vorteil gegenüber RC-Oszillatoren**:
- Sehr stabile Frequenz durch hohe Güte Q des LC-Schwingkreises
- Erreichbar bis in den GHz-Bereich
- Phasenjitter gering (wichtig für HF-Anwendungen)

**Nachteil**:
- Spule nötig (teuer, gross, frequenzabhängig)
- Abstimmung schwieriger als bei RC-Oszillatoren
- Güte Q des Schwingkreises begrenzt die Frequenzstabilität

:::info
**Colpitts vs. Hartley**: Beim Hartley-Oszillator sind zwei Spulen (oder eine Anzapfung) und ein Kondensator verbaut. Beim Colpitts ist es umgekehrt: eine Spule und zwei Kondensatoren. Colpitts ist bei höheren Frequenzen bevorzugt, weil Kondensatoren im HF-Bereich besser verfügbar sind.
:::

| Vergleich | Colpitts | Hartley | Wien-Brücke |
|---|---|---|---|
| Frequenznetzwerk | L + C1, C2 | L1, L2 + C | RC-Brücke |
| Frequenzbereich | 100 kHz – GHz | 100 kHz – 100 MHz | 1 Hz – 1 MHz |
| Abstimmung | C1/C2 oder L | C oder L-Anzapfung | R oder C |
| Typische Anwendung | HF-Sender, VCO | AM-Radio | Audiogenerator |
