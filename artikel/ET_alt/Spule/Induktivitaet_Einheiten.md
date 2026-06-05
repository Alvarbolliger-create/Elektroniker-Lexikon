---
title: Induktivität & Einheiten
kategorie: ET
tags: [induktivität, henry, spule, einheit, permeabilität, windungszahl, induktionsgesetz, sättigung, µH, mH]
symbol: L
einheit: H
---

Die Induktivität beschreibt, wie stark eine Spule dem Stromfluss widersteht, wenn er sich ändert. Grössere Induktivität bedeutet stärkere Reaktion auf Stromänderungen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Spule (Übersicht)]]
:::
:::vbox
**Führt weiter zu**
- [[Selbstinduktion]]
- [[Sättigung und Hysterese]]
:::
:::

---

Die Einheit ist Henry (H). Ein Henry ist gross. In der Praxis sind mH und µH häufiger.

:::formel
U_L = L * (dI / dt)     # Grundformel der Induktivität
E = 0.5 * L * I^2       # Gespeicherte Energie
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Induktivität | L | H |
| Spannung | U_L | V |
| Stromänderung | dI/dt | A/s |
| Energie | E | J |

## Typische Werte

| Anwendung | Induktivität |
|---|---|
| Schaltnetzteil (Buck) | 10 µH bis 100 µH |
| EMV-Drossel | 1 mH bis 100 mH |
| Netztransformator | einige H |
| Luftspule, wenige Windungen | einige nH |

## Abhängigkeit vom Aufbau

:::formel
L = µ * N^2 * A / l
:::
| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Permeabilität | µ | H/m | µ = µᵣ × µ₀, Materialeigenschaft des Kerns |
| Windungszahl | N | — | quadratischer Einfluss auf L |
| Kernquerschnitt | A | m² | grösserer Kern → mehr L |
| magn. Weglänge | l | m | längerer Pfad → weniger L |

Doppelt so viele Windungen ergeben viermal mehr Induktivität. Wird der Kern magnetisch gesättigt, bricht L schlagartig ein — mehr dazu unter [[Sättigung und Hysterese]].
