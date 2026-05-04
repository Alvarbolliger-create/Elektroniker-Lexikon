---
title: Selbstinduktion
kategorie: ET
tags: [selbstinduktion, spule, induktivität, gegenspannung, freilaufdiode, lenzsche regel, energiespeicher, induzierte spannung]
symbol: U_L
einheit: V
---

Ändert sich der Strom durch eine Spule, erzeugt die Spule selbst eine Spannung, die der Änderung entgegenwirkt. Das ist Selbstinduktion.

:::hbox
:::vbox
**Voraussetzungen**
- [[Induktivität & Einheiten]]
:::
:::vbox
**Verwandte Artikel**
- [[Transformator]]
:::
:::vbox
**Führt weiter zu**
- [[Buck (Step-down)]]
- [[Boost (Step-up)]]
:::
:::

---

## Warum passiert das?

Ein Magnetfeld kann nur entstehen und vergehen, wenn Energie fliesst. Die Spule nimmt Energie auf, wenn der Strom steigt, und gibt sie zurück, wenn der Strom sinkt. Diese Energiebewegung erzeugt eine Spannung.

:::monospace
U_L = L * (dI / dt)     # Spannung steigt mit der Änderungsrate des Stroms
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Induzierte Spannung | U_L | V |
| Induktivität | L | H |
| Stromänderung | dI/dt | A/s |

## Zeitkonstante

:::formel
τ = L / R
:::
| Zeit | Stromzustand |
|---|---|
| 1 × τ | 63 % des Endwerts |
| 2 × τ | 86 % |
| 3 × τ | 95 % |
| 5 × τ | 99 % (gilt als erreicht) |

## Einschalten

Beim Einschalten steigt der Strom langsam. Die Spule bremst ihn. Nach fünf Zeitkonstanten hat der Strom seinen Endwert erreicht.

## Ausschalten

Hier wird es gefährlich. Wenn der Strom schlagartig unterbrochen wird, versucht die Spule ihn aufrechtzuerhalten. Die Spannung kann dabei auf Hunderte von Volt steigen, auch wenn die Versorgung nur 12 V hatte.

## Freilaufdiode

Eine Diode parallel zur Spule, in Sperrrichtung zur Versorgung. Beim Ausschalten leitet sie den Strom ab. Die Spannungsspitze ist auf etwa 0.7 V begrenzt.

**Alternativen zur Freilaufdiode:**
- **TVS-Diode**: Schnelleres Ansprechen als normale Diode, definierte Klemmspannung. Sinnvoll wenn die Abfallzeit der Spule kurz gehalten werden muss.
- **RC-Snubber**: Widerstand und Kondensator in Reihe parallel zur Spule. Dämpft Spannungsspitzen bei hohen Schaltfrequenzen.

:::warning
Jede Spule in einer geschalteten Schaltung braucht eine Freilaufdiode oder einen anderen Schutz. Ohne sie werden Transistoren und MOSFETs zerstört.
:::

## Gespeicherte Energie

:::monospace
E = 0.5 * L * I^2      # Energie in der Spule bei Strom I
:::
Diese Energie wird beim Abschalten irgendwo abgebaut, entweder in der Freilaufdiode oder in einem Funken.
