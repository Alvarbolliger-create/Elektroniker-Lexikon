---
title: Elektrisches Feld
kategorie: ET
tags: [elektrisches feld, feldlinien, feldstärke, flussdichte, permittivität, coulomb, influenz, faradayscher käfig]
groessen: E|Feldstärke|V/m; D|elektrische Flussdichte|C/m²; epsilon_r|relative Permittivität|—; F|Kraft|N; Q|Ladung|C
_status: PORT+ERWEITERN  # ET_alt/Grundlagen/Elektrisches_Feld.md — Influenz + Flussdichte ergänzt
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Führt weiter zu**
- [[Plattenkondensator & Influenz]]
:::
:::

---

Ein elektrisches Feld entsteht um jede elektrische Ladung. Es überträgt die Kraftwirkung zwischen Ladungen und ist die physikalische Grundlage des Kondensators. Zwischen den Platten eines Kondensators ist ein elektrisches Feld gespeichert.

## Feldlinien

Feldlinien zeigen die Richtung der Kraft auf eine positive Probeladung:
- Sie starten an positiven Ladungen und enden an negativen
- Sie schneiden sich nie
- Enger Abstand = stärkeres Feld; weiter Abstand = schwächeres Feld
- Im homogenen Feld (z. B. zwischen Kondensatorplatten) verlaufen sie parallel und gleichmässig

:::schematic Homogenes elektrisches Feld zwischen zwei parallelen Kondensatorplatten; linke Platte positiv (+), rechte Platte negativ (−); parallele, gleichmässig verteilte Feldlinien von + nach −; Plattenabstand d und Spannung U eingezeichnet
/abbildungen/grundlagen/elektrisches_feld_plattenkondensator.svg
:::

## Elektrische Feldstärke

Die Feldstärke E gibt an, wie gross die Kraft auf eine Probeladung ist:

:::formel
E = U / d    # Feldstärke im homogenen Feld (Plattenkondensator)
:::

**Einheit:** V/m (Volt pro Meter). Im Plattenkondensator mit Plattenabstand d und Spannung U ist das Feld homogen und die Formel exakt.

Allgemein gilt F = Q · E, also eine Kraft auf die Ladung Q im Feld E.

## Elektrische Flussdichte D

Die elektrische Flussdichte D (auch: "Verschiebungsdichte") ist direkt mit den **freien Ladungen** auf den Kondensatorplatten verknüpft:

:::formel
D = Q / A    # D (C/m²) = Ladung Q (C) / Plattenfläche A (m²)
:::

Dieser Zusammenhang gilt **immer** — unabhängig davon, welches Dielektrikum zwischen den Platten sitzt. Ändert man das Material bei unveränderter Ladung Q, bleibt D konstant.

Die Verbindung zur Feldstärke E führt das Material ein:

:::formel
D = epsilon_0 * epsilon_r * E
:::

Wird ein Dielektrikum (epsilon_r > 1) eingeschoben, polarisieren sich die Moleküle und schwächen das E-Feld ab. D bleibt gleich (freie Ladung unverändert), aber E sinkt um den Faktor epsilon_r. Das Material steckt also im Übergang D → E, nicht in D selbst.

| Grösse | Bedeutung |
|---|---|
| epsilon_0 = 8,854 · 10⁻¹² F/m | Elektrische Feldkonstante (Vakuum) |
| epsilon_r | Relative Permittivität des Dielektrikums |
| epsilon_r = 1 | Vakuum, Luft |
| epsilon_r = 2–10 | Typische Kunststoffe, Keramik |
| epsilon_r > 1000 | Spezialkeramik (Kondensatorfüllung) |

## Coulombsches Gesetz

Zwei Punktladungen Q1 und Q2 im Abstand r ziehen sich an (verschiedene Vorzeichen) oder stossen sich ab (gleiche Vorzeichen):

:::formel
F = Q1 * Q2 / (4 * pi * epsilon_0 * r^2)
:::

Die Kraft nimmt mit dem Quadrat des Abstands ab — wie die Schwerkraft.

## Influenz & Faradayscher Käfig

**Influenz**: Wird ein leitender Körper in ein elektrisches Feld gebracht, verschieben sich die freien Elektronen: negative Ladungen sammeln sich auf der der Feldquelle zugewandten Seite, positive auf der abgewandten. Der Körper selbst bleibt neutral, aber die Ladungen sind getrennt.

:::schematic Influenz: Neutraler leitender Block in einem äusseren elektrischen Feld (Feldlinien von links nach rechts); linke Seite des Blocks mit negativen Ladungen (−), rechte Seite mit positiven (+); Feldlinien biegen sich um den Block; im Innern des Leiters keine Feldlinien
/abbildungen/grundlagen/influenz.svg
:::

**Faradayscher Käfig**: Ein geschlossenes leitendes Gehäuse schirmt das Innere vollständig vom äusseren elektrischen Feld ab. Das Feld im Innern ist null. Anwendungen: Abschirmung von Messgeräten, EMV-Gehäuse, Mikrowellengehäuse.

## Durchschlag

Wird die elektrische Feldstärke zu gross, reisst das Dielektrikum: Es ionisiert und leitet plötzlich Strom — der **elektrische Durchschlag**.

| Material | Durchschlagfeldstärke |
|---|---|
| Luft | 3 MV/m (3 kV/mm) |
| Papier (Öl getränkt) | 10–20 MV/m |
| Keramik | 10–40 MV/m |
| PTFE (Teflon) | ca. 20 MV/m |

:::warning
Kondensatoren dürfen ihre **Nennspannung** nicht überschreiten — sonst droht Durchschlag. Elkos (Elektrolytkondensatoren) haben zudem eine Polung, die eingehalten werden muss. Falsche Polung oder Überspannung führt zu unkontrolliertem Durchschlag und ggf. Explosion.
:::
