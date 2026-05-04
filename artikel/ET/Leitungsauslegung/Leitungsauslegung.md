---
title: Leitungsauslegung
kategorie: ET
tags: [leitungsauslegung, querschnitt, spannungsabfall, sicherung, absicherung]
symbol: A
einheit: mm²
---

Zu dünne Leitungen werden heiss. Zu schwache Sicherungen schmelzen zu früh, zu starke schützen nicht. Eine korrekte Auslegung verhindert beides.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Wirkleistung]]
:::
:::vbox
**Verwandte Artikel**
- [[Schutzklassen]]
:::
:::vbox
**Führt weiter zu**
- [[Not-Halt]]
:::
:::

---

## Querschnittsberechnung

Jeder Leiter hat einen spezifischen Widerstand. Bei Kupfer sind es 0.0178 Ω × mm²/m.

:::monospace
R = rho * l / A     # Leitungswiderstand; rho = 0.0178 für Kupfer
:::
| Grösse | Symbol | Einheit |
|---|---|---|
| Spez. Widerstand Kupfer | rho | 0.0178 Ω mm²/m |
| Leiterlänge | l | m |
| Querschnitt | A | mm² |
| Leitungswiderstand | R | Ω |

Faustformel: Für 1 mm² Kupfer, 1 m Länge: R = 0.018 Ω. Hin- und Rückleiter verdoppeln das.

## Spannungsabfall

Ein Leitungswiderstand bedeutet Spannungsverlust unter Last.

:::formel
U_abfall = I * R_leitung
:::
In der Norm wird oft ein maximaler Spannungsabfall von 3 % der Nennspannung gefordert. Bei 230 V sind das 6.9 V.

## Absicherung

Die Sicherung schützt die Leitung, nicht das Gerät. Ihre Auslösung muss sicher unter dem zulässigen Dauerstrom der Leitung liegen.

| Querschnitt | Zulässiger Dauerstrom | Typische Sicherung |
|---|---|---|
| 0.75 mm² | 6 A | 6 A |
| 1.5 mm² | 16 A | 16 A |
| 2.5 mm² | 25 A | 25 A |
| 4 mm² | 32 A | 32 A |
| 6 mm² | 40 A | 40 A |

Die Werte hängen von der Verlegeart und Umgebungstemperatur ab. Bei Bündeln oder erhöhter Temperatur muss der Querschnitt grösser gewählt werden (Derating).

:::warning
Sicherungen nie durch stärkere ersetzen. Die Sicherung ist die letzte Schutzebene vor einem Kabelbrand.
:::

:::norm
NIN (Niederspannungsinstallationsnorm, Schweiz) / VDE 0298-4 (Deutschland): Regelt zulässige Belastbarkeit von Kabeln und Leitungen in Abhängigkeit von Verlegeart, Umgebungstemperatur und Häufung. Die Tabellenwerte im Artikel entsprechen Verlegeart B2 (im Rohr eingebettet) bei 30 °C.
:::
