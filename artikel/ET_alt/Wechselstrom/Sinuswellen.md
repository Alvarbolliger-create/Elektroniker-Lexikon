---
title: Sinuswellen
kategorie: ET
tags: [sinuswelle, wechselstrom, amplitude, frequenz, phase, effektivwert, scheitelwert, RMS, scheitelfaktor, 50Hz, periode]
symbol: u(t)
einheit: V, Hz
---

Wechselspannung im Stromnetz und in vielen Signalen hat die Form einer Sinuswelle. Sie ist die reinste Form einer periodischen Schwingung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Zeigerdiagramm]]
:::
:::vbox
**Führt weiter zu**
- [[Impedanz]]
- [[RLC-Schaltungen]]
:::
:::

---

:::plot
var: t
range: 0, 12.56
xlabel: Zeit (t)
ylabel: Spannung
Sinuswelle:  sin(t)
Effektivwert: 0.707
:::

## Allgemeine Gleichung

:::formel
u(t) = U_peak * sin(2 * π * f * t + φ)
u(t) = U_peak * sin(ω * t + φ)       # kompakte Schreibweise mit Kreisfrequenz
ω    = 2 * π * f                      # Kreisfrequenz in rad/s
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Scheitelwert | U_peak | V |
| Kreisfrequenz | ω | rad/s |
| Frequenz | f | Hz |
| Phasenwinkel | φ | rad oder ° |

Die Kreisfrequenz ω ist die gebräuchliche Schreibweise in Impedanzformeln (Z_C = 1/(j·ω·C), Z_L = j·ω·L) und vereinfacht die Notation erheblich.

## Die drei Kennwerte

**Amplitude (Scheitelwert)** ist der maximale Ausschlag. Das Stromnetz hat 325 V Scheitelwert, nicht 230 V.

**Frequenz f** in Hertz ist die Anzahl Schwingungen pro Sekunde. Netzfrequenz in der Schweiz: 50 Hz.

**Phase φ** beschreibt den zeitlichen Versatz zwischen zwei Signalen. Gleiche Frequenz, aber verschoben.

## Scheitelwert und Effektivwert

Der Effektivwert gibt die Gleichspannung an, die dieselbe Heizwirkung hätte.

:::formel
U_eff = U_peak / sqrt(2)    # gilt nur für reine Sinuswelle
f = 1 / T                   # Frequenz aus Periodendauer
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Effektivwert | U_eff | V |
| Scheitelwert | U_peak | V |
| Frequenz | f | Hz |
| Periodendauer | T | s |

## Netzspannung als Beispiel

Das Schweizer Netz liefert 230 V Effektivwert bei 50 Hz.

| Grösse | Wert |
|---|---|
| Effektivwert | 230 V |
| Scheitelwert | 325 V |
| Periodendauer | 20 ms |
| Frequenz | 50 Hz |

:::tip
Multimeter zeigen immer den Effektivwert. Ein Oszilloskop zeigt den echten Verlauf. Wer den Scheitelwert messen will, braucht ein Oszilloskop oder rechnet mit sqrt(2) × U_eff.
:::
