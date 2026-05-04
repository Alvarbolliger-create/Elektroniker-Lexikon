---
title: Sternpunkterdung
kategorie: SI
tags: [sternpunkt, massestern, ground star, EMV, brummschleife, HF, erdung, groundplane, impedanz, analog, digital, massefläche]
symbol: —
einheit: —
---

Bei der Sternpunkterdung werden alle Masseleitungen an einem einzigen Punkt zusammengeführt. Das vermeidet Masseschleifen und -probleme — kann aber bei HF-Signalen das Gegenteil bewirken.

:::hbox
:::vbox
**Voraussetzungen**
- [[Schutzerde (PE) vs. Signalmasse (GND)]]
- [[EMV Pre-Compliance]]
:::
:::vbox
**Verwandte Artikel**
- [[PCB Aufbau & Material]]
- [[Wellenwiderstand]]
- [[Übersprechen (Crosstalk)]]
:::
:::

---

## Was ist Sternpunkterdung?

Alle Massepfade führen zu einem gemeinsamen Punkt — dem Sternpunkt. Von diesem Punkt geht genau eine Verbindung zur Schutzerde (PE).

:::schematic
/Diagramm/sternpunkterdung_0.svg
:::
Vorteil: Es gibt keine Masseschleifen. Jeder Stromkreis hat seinen eigenen, definierten Rückweg.

## Masseschleifen und Brummen

Wenn GND an mehreren Punkten mit PE verbunden ist (oder mehrere Geräte mit eigener GND-PE-Verbindung zusammengeschlossen werden), entsteht eine Masseschleife.

Kleinste Potenzialunterschiede zwischen den Erdungspunkten (einige Millivolt bis Volt) treiben Kreisströme durch die Schleife. Bei 50 Hz entsteht 50-Hz-Brummen in Audiogeräten und analogen Messsystemen.

**Lösung**: Sternpunkterdung — genau eine Erde.

## Wann hilft Sternpunkterdung

- Audio- und Messsysteme mit empfindlichen Analogsignalen
- Systeme mit mehreren Netzteilen, die zusammenarbeiten
- Leistungs-Elektronik neben Analogelektronik (hohe dI/dt getrennt von empfindlichen Signalen führen)

## Wo Sternpunkterdung schadet: HF-Schaltungen

Bei HF-Signalen (> 1 MHz) verhält sich eine Leiterbahn nicht mehr wie ein idealer Leiter. Sie hat eine Eigenimpedanz:

:::monospace
Z_Leitung = R + jωL    # bei HF dominiert ωL (Induktivität)
:::
Eine lange Masseleitung zum Sternpunkt hat bei HF eine hohe Impedanz. Das Ergebnis:
- Rückstrompfad ist nicht mehr direkt unter der Signalleitung
- HF-Ströme fliessen unkontrolliert
- Strahlung und Empfindlichkeit steigen

**Bei HF richtig**: Flächige Massefläche (Groundplane), kurze direkte Rückwege. Der Rückstrom fliesst auf dem direkten Weg direkt unter der Signalleitung.

## Das Dilemma

| Situation | Beste Massestrategie |
|---|---|
| Analoge Schaltung, NF (< 100 kHz) | Sternpunkterdung |
| Digitale Schaltung, HF (> 1 MHz) | Massefläche (Groundplane) |
| Mischsignal (Analog + Digital) | Massefläche mit einer einzigen Verbindung zwischen Analog- und Digital-GND |

## Praxis: PCB mit Analog und Digital

Standardempfehlung: Getrennte Masseflächen für Analog und Digital, die an einem einzigen Punkt verbunden sind (nahe beim ADC oder DAC, wo die Signale wechseln).

Kontrovers: Neuere Forschungen zeigen, dass eine einzige durchgehende Massefläche mit gezielter Leitungsführung oft besser ist als getrennte Flächen.

:::tip
In der Praxis: Digitalleitungen nicht über die analoge Massefläche routen. Dann spielt es oft keine grosse Rolle ob eine oder zwei Flächen.
:::
