---
title: Diode
kategorie: EK
kapitel: Halbleiter
tags: [diode, siliziumdiode, germaniumdiode, kennlinie, durchlassspannung, sperrstrom, gleichrichter, freilaufdiode, verpolungsschutz, schottky, 1n4007, 1n4148, clipper, clamper]
groessen: U_F|Durchlassspannung|V; I_R|Sperrstrom|A; U_R|max. Sperrspannung|V; I_F|Durchlassstrom|A
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[pn-Übergang]]
:::
:::vbox
**Verwandte Artikel**
- [[Schottky-Diode]]
- [[Zener-Diode]]
- [[Gleichrichter]]
:::
:::vbox
**Führt weiter zu**
- [[Thyristor]]
- [[LED]]
- [[Optokoppler]]
:::
:::

---

Eine Diode lässt Strom nur in eine Richtung durch. In Durchlassrichtung fällt ca. 0.7 V ab (Silizium). In Sperrrichtung fliesst praktisch kein Strom — bis zum Durchbruch.

## Schaltsymbol

:::schematic Diodensymbol (Anode links, Kathode rechts)
/schaltplaene/symbole/D.svg
:::

Die Spitze des Dreiecks zeigt in Durchlassrichtung (von Anode A zur Kathode K). Auf dem Gehäuse markiert ein Ring die Kathode.

## Kennlinie

:::plot
var: U
range: -0.5, 0.85
xlabel: Spannung U (V)
ylabel: Strom I (normiert)
Silizium:   max(0, exp(15 * (U - 0.65)) - 1) / 80
Germanium:  max(0, exp(18 * (U - 0.30)) - 1) / 80
Sperrstrom: min(0, U) * 0.02
:::

In Durchlassrichtung steigt der Strom exponentiell — die Spannung bleibt dabei nahezu konstant. Silizium: ca. 0.7 V, Germanium: ca. 0.3 V.

In Sperrrichtung fliesst nur ein kleiner Leckstrom (µA-Bereich). Bei Überschreitung der Sperrspannung bricht die Diode durch.

:::info
Die Diode ist kein ohmscher Widerstand — das Ohmsche Gesetz gilt hier nicht. Der Widerstand der Diode hängt stark vom Arbeitspunkt ab.
:::

## Wichtige Kenndaten

| Kenngrösse | Bedeutung | Typischer Wert |
|---|---|---|
| U_F | Durchlassspannung (bei Nennstrom) | 0.6–0.8 V (Si) |
| I_R | Sperrstrom | 1 nA – 10 µA |
| U_R(max) | Max. Sperrspannung | 50–1000 V |
| I_F(max) | Max. Dauerstrom | 0.15–1000 A |
| t_rr | Sperrerholzeit | 4 ns – 4 µs |

## Bauformen und Typenvergleich

| Typ | I_F | U_R | Besonderheit |
|---|---|---|---|
| 1N4001–1N4007 | 1 A | 50–1000 V | Gleichrichter, günstiger Standard |
| 1N4148 | 0.15 A | 100 V | Schaltdiode, t_rr = 4 ns |
| 1N5819 (Schottky) | 1 A | 40 V | 0.35 V Durchlassspannung |
| BYV27 | 1 A | 200 V | schnelle Diode, t_rr = 20 ns |
| MUR460 | 4 A | 600 V | Ultrafast, Schaltregler |

## Anwendungen

**Gleichrichter**: Wandelt Wechselspannung in pulsierende Gleichspannung um. → [[Gleichrichter]]

**Verpolungsschutz**: Diode in Reihe mit der Versorgung. Bei falscher Polung sperrt sie und schützt die Schaltung. Nachteil: 0.7 V Spannungsabfall.

**Freilaufdiode**: Parallelgeschaltet zu einer induktiven Last (Relais, Motor). Beim Abschalten baut die Spule eine Gegenspannung auf — die Freilaufdiode begrenzt diese auf –0.7 V und schützt den Schalttransistor.

:::warning
Ohne Freilaufdiode entstehen beim Abschalten induktiver Lasten Spannungsspitzen von 10× Versorgungsspannung und mehr. Ein MOSFET oder BJT ohne Freilaufdiode an einem Relais wird zuverlässig zerstört.
:::

## Begrenzer (Clipper)

Dioden begrenzen die Amplitude eines Signals:

:::schematic Shunt-Begrenzer (Diode parallel zur Last)
/Diagramm/diode_0.svg
:::

Positive Halbwelle wird auf ca. 0.7 V begrenzt. **Anwendung**: Schutz von ADC-Eingängen vor Überspannung.

:::schematic Doppelter Zener-Begrenzer (symmetrisch)
/Diagramm/diode_1.svg
:::

Zwei antiparallele Zenerdioden: Signal wird symmetrisch auf ±(U_Z + 0.7 V) begrenzt.

## Klemm-Schaltungen (Clamper)

Verschieben den Gleichanteil eines Signals, ohne die Wellenform zu verändern:

:::schematic Positiver Klemmer
/Diagramm/diode_2.svg
:::

- Negative Halbwelle lädt den Kondensator, bis die Diode sperrt
- Das gesamte Signal wird nach oben verschoben, so dass das Minimum bei ~0 V liegt
- **Anwendung**: Spannungsvervielfacher, Videoschaltungen
