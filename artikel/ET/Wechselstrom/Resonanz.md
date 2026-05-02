---
title: Resonanz
kategorie: ET
tags: [resonanz, schwingkreis, resonanzfrequenz, güte, bandbreite, LC, RLC, serienschwingkreis, parallelschwingkreis]
symbol: f_0
einheit: Hz
---

Bei der Resonanzfrequenz heben sich induktiver und kapazitiver Widerstand auf. Die Schaltung schwingt mit minimaler Dämpfung. Das wird gezielt für Filter und Oszillatoren genutzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[RLC-Schaltungen]]
:::
:::vbox
**Verwandte Artikel**
- [[Filter Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[LC-Filter]]
- [[Quarz-Oszillator]]
:::
:::

---

## Resonanzbedingung

```
ω_0 = 1 / sqrt(L * C)              # Resonanzkreisfrequenz
f_0 = 1 / (2 * pi * sqrt(L * C))   # Resonanzfrequenz
```

Bei f_0 gilt X_L = X_C. Im Reihenschwingkreis ist die Impedanz minimal (Stromresonanz). Im Parallelschwingkreis ist sie maximal (Spannungsresonanz).

## Güte Q und Dämpfung d

```
Q = (ω_0 * L) / R                  # Gütefaktor (Reihenschwingkreis)
Q = (1 / R) * sqrt(L / C)          # Güte aus Bauteilwerten

d = 1 / Q                          # Dämpfung (Kehrwert der Güte)
d = R / (ω_0 * L)
d = R * sqrt(C / L)
```

Hohe Güte Q: schmale Resonanzspitze, wenig Verlust. Niedriges Q (hohes d): breite, flache Kurve, stark gedämpft.

Der Verlustwiderstand R der Spule (Kupferwiderstand der Wicklung) begrenzt Q in der Praxis.

## Bandbreite

```
B = f_0 / Q                        # Bandbreite zwischen den −3dB-Punkten
B = d * f_0
B = R / (2 * pi * L)               # direkt aus Bauteilwerten (Reihenschwingkreis)
```

An den Grenzfrequenzen f1 (untere) und f2 (obere) ist der Strom auf 1/√2 (≈ 0.707) des Maximalwerts abgefallen — das entspricht −3 dB.

| Grösse | Symbol | Einheit |
|---|---|---|
| Gütefaktor | Q | — |
| Dämpfung | d | — |
| Bandbreite | B | Hz |
| Resonanzfrequenz | f_0 | Hz |

## Reihenschwingkreis (Spannungsresonanz)

R, L und C in Reihe. Bei Resonanz ist Z = R minimal, der Strom maximal.

```
Z = sqrt(R^2 + (X_L - X_C)^2)
U_L = U_C = Q * U_ein      # Spannungsüberhöhung bei Resonanz
```

Verhalten in Abhängigkeit der Frequenz:

| Frequenz | Charakter | Phasenwinkel φ |
|---|---|---|
| f < f_0 | kapazitiv (X_C überwiegt) | φ < 0 |
| f = f_0 | resistiv (X_L = X_C) | φ = 0 |
| f > f_0 | induktiv (X_L überwiegt) | φ > 0 |

:::warning
Die Spannung über Spule und Kondensator kann im Reihenschwingkreis ein Vielfaches der Eingangsspannung erreichen. Bei Q = 50 und 10 V Eingang entstehen 500 V über dem Kondensator. Das kann Bauteile zerstören.
:::

## Parallelschwingkreis (Stromresonanz)

R, L und C parallel. Bei Resonanz ist die Impedanz maximal, der Strom aus der Quelle minimal.

```
Q_parallel = R / (ω_0 * L)         # Güte Parallelschwingkreis
```

Bei Resonanz heben sich die Blindströme durch L und C gegenseitig auf — der Gesamtstrom ist minimal und in Phase mit der Spannung. Man spricht von **Stromresonanz**.

Der Strom zirkuliert zwischen L und C (Schwingkreisstrom), ohne die Quelle zu belasten. Je höher Q, desto grösser dieser Kreuzstrom im Vergleich zum Quellenstrom.

**Unterschied Reihe vs. Parallel:**

| | Reihenschwingkreis | Parallelschwingkreis |
|---|---|---|
| Bei Resonanz | Z minimal, I maximal | Z maximal, I minimal |
| Gefahr | Spannungsüberhöhung | Stromüberhöhung im Kreis |
| Anwendung | Serienfilter (sperrt Frequenzen ausserhalb f0) | Parallelfilter (sperrt f0) |

## Anwendungen

**Quarz**: Sehr hohe Güte (Q bis 100 000). Stabile Frequenzreferenz in Uhren und Mikrocontrollern.

**LC-Filter**: Steilere Flanken als RC-Filter, geeignet für HF-Anwendungen.

**Antennenkreis**: Im Empfänger wird der Schwingkreis auf die Empfangsfrequenz abgestimmt.
