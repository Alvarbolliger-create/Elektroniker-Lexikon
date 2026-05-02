---
title: Gleichrichter
kategorie: EK
tags: [gleichrichter, diode, brückengleichrichter, netzteil, wechselstrom, siebkondensator, graetz, einweggleichrichter, ripple, welligkeit, scheitelspannung]
symbol: —
einheit: —
---

Ein Gleichrichter wandelt Wechselspannung in eine pulsierende Gleichspannung um. Er ist der erste Schritt in fast jedem Netzteil.

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Lineare Regler]]
- [[Transformator: Aufbau & Funktionsprinzip]]
:::
:::vbox
**Führt weiter zu**
- [[Lineare Regler]]
- [[Buck (Step-down)]]
:::
:::

---

## Einweggleichrichter (M1U)

Eine einzelne Diode lässt nur die positive Halbwelle durch. Die negative Halbwelle wird gesperrt.

- Welligkeit: **50 Hz** (gleiche Frequenz wie Eingang)
- Nur eine Diode — einfachst mögliche Schaltung
- Schlechter Wirkungsgrad, hohe Restwelligkeit
- Heute kaum mehr verwendet (nur noch für Hilfsspannungen mit sehr geringer Leistung)

:::plot
var: t
range: 0, 12.56
xlabel: Zeit
ylabel: Spannung (normiert)
Eingangsspannung (AC):    sin(t)
Einweggleichrichter:      max(sin(t), 0)
:::

## Brückengleichrichter (B2U) — Graetzschaltung

Vier Dioden in Brückenanordnung. Beide Halbwellen werden gleichgerichtet. Die negative Halbwelle wird umgepolt.

- Welligkeit: **100 Hz** (doppelte Frequenz)
- Vier Dioden (oft als fertiger Brückengleichrichter-IC erhältlich)
- Sperrspannung je Diode: Spitzenwert der Eingangsspannung
- **Standardschaltung** in fast allen Netzteilen

:::plot
var: t
range: 0, 12.56
xlabel: Zeit
ylabel: Spannung (normiert)
Eingangsspannung (AC):    sin(t)
Brückengleichrichter:     abs(sin(t))
:::

## Mittelpunktgleichrichter (M2)

Zwei Dioden und ein Transformator mit **Mittelanzapfung**. Die Mittelanzapfung bildet den Nullpunkt der Ausgangsspannung.

- Welligkeit: **100 Hz** (wie Brückengleichrichter)
- Nur zwei Dioden — dafür spezieller Trafo nötig
- Sperrspannung je Diode: doppelte Ausgangsspannung (Volle Trafo-Sekundärspannung liegt an der sperrenden Diode)
- Verwendet bei tiefen Spannungen (<10 V) und Schaltnetzteilen mit Mittelanzapfung

:::plot
var: t
range: 0, 12.56
xlabel: Zeit
ylabel: Spannung (normiert)
Eingangsspannung (AC):    sin(t)
Mittelpunktgleichrichter: abs(sin(t))
:::

## Vergleich der drei Typen

| Schaltung | Kürzel | Dioden | Welligkeit | Sperrspannung Diode |
|---|---|---|---|---|
| Einweggleichrichter | M1U | 1 | 50 Hz | = Û_ein |
| Brückengleichrichter | B2U | 4 | 100 Hz | = Û_ein |
| Mittelpunktgleichrichter | M2 | 2 | 100 Hz | = 2 × Û_aus |

## Siebkondensator

Nach dem Gleichrichter wird ein grosser Elektrolytkondensator geschaltet. Er glättet die Welligkeit. Zwischen den Spannungsspitzen liefert er den Strom.

```
C = I_last / (f * U_welligkeit)     # Mindestkapazität für gegebene Restwelligkeit
```

Typisch: 1000 bis 10000 µF bei kleinen Netzteilen.

## Spitzenspannung nach Gleichrichter

Die Kondensatorspannung lädt sich auf den Scheitelwert auf, abzüglich zweier Dioden-Abfälle.

Bei 230 V Netz: 325 V Scheitelwert minus 2 × 0.7 V = ca. 323 V DC (ungeregelt).

:::warning
Ungeregelte Gleichspannung nach dem Gleichrichter ist deutlich höher als der Effektivwert der Eingangsspannung. Ein Netzteil für 12 V Ausgang hat intern oft 40 bis 50 V DC vor dem Regler.
:::
