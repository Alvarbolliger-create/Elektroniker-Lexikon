---
title: Elektromagnet
kategorie: ET
tags: [elektromagnet, relais, solenoid, anzugskraft, magnetischer kreis, kern, luftspalt]
groessen: F|Anzugskraft|N; B|Flussdichte|T; A|Kernfläche|m²; mu_0|Feldkonstante|H/m; I|Strom|A; N|Windungszahl|—
_status: PORT  # ET_alt/Magnetfelder/Elektromagnet.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Führt weiter zu**
- [[Magnetischer Widerstand (Reluktanz)]]
:::
:::

---

Ein Elektromagnet erzeugt ein steuerbares Magnetfeld durch elektrischen Strom. Er ist die Grundlage für Relais, Schütze, Solenoide, Lautsprecher und Elektromotoren.

## Aufbau

Ein Elektromagnet besteht aus einer Spule, die auf einem Eisenkern gewickelt ist. Der Eisenkern verstärkt das Magnetfeld um das mu_r-fache gegenüber Luft (typisch 1000× bis 10 000×). Meist ist ein Luftspalt vorhanden, damit ein beweglicher Anker angezogen werden kann.

:::schematic Elektromagnet (Relais): U-förmiger Eisenkern mit Spulenwicklung (N Windungen, Strom I); Luftspalt zwischen Kern und Anker; Anker als bewegliches Eisenstück oben; Magnetfeldlinien geschlossen durch Kern, Luftspalt und Anker; Beschriftung: N, I, Luftspalt, Anker, Anzugskraft F
/abbildungen/magnetfelder/elektromagnet_aufbau.svg
:::

| Komponente | Funktion |
|---|---|
| Spule (N Windungen, Strom I) | Erzeugt die Durchflutung Theta = N·I |
| Eisenkern | Konzentriert und leitet das Magnetfeld |
| Luftspalt | Ermöglicht mechanische Bewegung des Ankers |
| Anker | Bewegliches Eisenstück, wird angezogen |

## Anzugskraft

Die Kraft, mit der der Anker angezogen wird, hängt von der Flussdichte B im Luftspalt und der Querschnittsfläche A ab. Die Formel gilt für einen einzelnen Luftspalt:

:::formel
F = B^2 * A / (2 * mu_0)    # Anzugskraft in Newton
:::

Die Kraft steigt quadratisch mit B — und B steigt mit dem Strom. Doppelter Strom → vierfache Kraft (vereinfacht, ohne Sättigung).

## Relais und Schütz

Das Relais ist die wichtigste Anwendung des Elektromagnets in der Elektrotechnik:

- Kleiner Steuerstrom in der Spule (mA) schaltet einen grossen Laststrom (A bis kA)
- Galvanische Trennung zwischen Steuerkreis und Lastkreis
- Schütz: Ein Relais für grosse Ströme (Motorschutz, Hauptschalter)

:::warning
Beim Abschalten der Relaisspule entsteht eine hohe Induktionsspannung (→ [[Selbstinduktion & Induzierte Spannung]]). Immer **Freilaufdiode** parallel zur Spule einbauen, wenn Transistoren oder ICs die Spule schalten.
:::

## Solenoid

Ein Solenoid ist ein Elektromagnet mit axial beweglichem Tauchkern (Eisenstab). Er wird in Ventilen (Hydraulik, Pneumatik), Türöffnern und Schlössern eingesetzt. Beim Einschalten zieht der Kern in die Spule — beim Ausschalten bringt eine Feder ihn zurück.

:::tip
Die Anzugskraft eines Elektromagnets ist deutlich grösser als die Haltekraft (wegen des grösseren Luftspalts beim Anziehen). Relais haben deshalb eine Anzugsspannung (höher) und eine Abfallspannung (tiefer) — der Bereich dazwischen ist der Hysteresbereich.
:::
