---
title: Diode
kategorie: EK
tags: [diode, halbleiter, gleichrichter, sperrschicht, kennlinie, schottky, freilaufdiode, verpolungsschutz, durchlassspannung, sperrstrom, clipper, clamper, 1n4007, 1n4148]
symbol: D
einheit: —
---

Eine Diode lässt Strom nur in eine Richtung durch. In Durchlassrichtung fällt etwa 0.7 V ab. In Sperrrichtung fliesst praktisch kein Strom.

:::hbox
:::vbox
**Voraussetzungen**
- [[p-n-Übergang]]
:::
:::vbox
**Verwandte Artikel**
- [[Zener-Diode]]
- [[Gleichrichter]]
:::
:::vbox
**Führt weiter zu**
- [[Zener-Diode]]
- [[Thyristor]]
- [[LED-Ansteuerung]]
:::
:::

---

## Schaltsymbol

Ein Dreieck mit einer Linie am spitzen Ende. Der Strom fliesst in Richtung des Dreiecks (von Anode zu Kathode). Die Linie ist die Kathode, meist mit einem Ring auf dem Gehäuse markiert.

:::schematic Diodensymbol (Anode links, Kathode rechts)
/schaltplaene/symbole/D.svg
:::

## Kennlinie

In Durchlassrichtung fliesst Strom ab ca. 0.6 bis 0.7 V. Die Spannung steigt kaum noch, der Strom steigt stark. Das ist das typische Diodenverhalten.

In Sperrrichtung fliesst ein sehr kleiner Leckstrom, praktisch vernachlässigbar. Wird die Sperrspannung überschritten, bricht die Diode durch, was sie zerstört.

:::plot
var: U
range: -0.5, 0.85
xlabel: Spannung U (V)
ylabel: Strom I (normiert)
Durchlasskennlinie: max(0, exp(15 * (U - 0.65)) - 1) / 80
Sperrstrom:        min(0, U) * 0.02
:::

:::info
Die Diode ist kein ohmscher Widerstand. Das Ohmsche Gesetz gilt hier nicht.
:::

## Anwendungen

**Gleichrichter**: Wechselspannung in Gleichspannung umwandeln. Aus einer Sinuswelle wird eine pulsierende Gleichspannung.

**Verpolungsschutz**: Diode in Reihe mit der Versorgung schützt gegen falsch gepolte Batterie oder Stecker.

**Freilaufdiode**: Schützt vor Spannungsspitzen bei Spulen und Relais.

## Bauformen und Typenvergleich

| Typ | Merkmale | Einsatz |
|---|---|---|
| 1N4001 bis 1N4007 | 1 A, bis 1000 V | Gleichrichter, Netzteil |
| 1N4148 | 0.15 A, Schaltdiode | Signalverarbeitung |
| Schottky (z.B. 1N5819) | 0.3 V Durchlassspannung | Effizienz, Hochfrequenz |
| Zener | Definierte Durchbruchspannung | Spannungsreferenz |
| LED | Licht bei Stromfluss | Anzeige, Beleuchtung |

## Begrenzer-Schaltungen (Clipper)

Dioden begrenzen die Amplitude eines Signals auf einen definierten Wert.

**Shunt-Begrenzer** (Parallelschaltung zur Last):

:::schematic
/Diagramm/diode_0.svg
:::
**Doppelter Zener-Begrenzer** (symmetrische Begrenzung):
:::schematic
/Diagramm/diode_1.svg
:::
Zwei antiparallele Zenerdioden: Positive Halbwelle begrenzt auf U_Z + 0.7V, negative auf -(U_Z + 0.7V).

**Anwendung**: Schutz von ADC-Eingängen, Signalkonditionierung.

## Klemm-Schaltungen (Clamper)

Klemm-Schaltungen verschieben den Gleichspannungsanteil eines Signals, ohne die Wellenform zu verändern.

**Positiver Klemmer**:

:::schematic
/Diagramm/diode_2.svg
:::
- Negative Halbwelle lädt C auf, bis Diode sperrt
- Positive Halbwelle erscheint um U_peak angehoben am Ausgang
- Das gesamte Signal wird so angehoben, dass das Minimum bei ~0V liegt

**Negativer Klemmer**: Diode umgepolt → Signal wird nach unten verschoben.

**Anwendung**: Videoschaltungen, Gleichrichter-Pumpschaltungen, Spannungsvervielfacher.

## Schottky-Diode vs. Standard-PN-Diode

Der wichtigste Unterschied liegt im Halbleiteraufbau:

**Standard-Silizium-PN-Diode** (z.B. 1N4007): Übergang zwischen p-dotiertem und n-dotiertem Halbleiter. Es gibt Minoritätsladungsträger (Löcher im n-Gebiet, Elektronen im p-Gebiet), die beim Sperren erst ausgeräumt werden müssen. Das dauert — die Diode hat eine merkliche Sperrverzögerungszeit (Reverse-Recovery-Time, t_rr).

**Schottky-Diode**: Übergang zwischen Metall (z.B. Molybdän) und n-dotiertem Halbleiter. Es gibt keine Minoritätsladungsträger — der Übergang ist ein Majoritätsträger-Bauteil. Deshalb:
- Viel geringere Durchlassspannung: **0.15 bis 0.45 V** (statt 0.7 V)
- Nahezu keine Sperrverzögerungszeit (Schaltzeiten < 1 ns)
- Höherer Leckstrom in Sperrrichtung

:::info
Schottky-Dioden werden in Schaltreglern als Freilaufdiode und als Gleichrichter eingesetzt, weil jede eingesparte Volt Durchlassspannung direkt den Wirkungsgrad erhöht. Bei einem 5-V-Schaltregler mit 1 A bedeutet 0.4 V weniger Durchlassspannung = 400 mW weniger Verlust.
:::

:::warning
Immer den Vorwiderstand berechnen. Ohne Begrenzung zieht eine Diode so viel Strom, bis sie brennt.
:::
