---
title: Innenwiderstand & Messfehler
kategorie: MT
tags: [innenwiderstand, messfehler, multimeter, belastung, messgenauigkeit]
symbol: R_i
einheit: Ω
---

Jedes Messgerät beeinflusst die Schaltung die es misst. Der Innenwiderstand bestimmt wie stark. Wer das ignoriert, misst Werte die nicht stimmen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom-, Spannungs-, Widerstandsmessung]]
:::
:::vbox
**Verwandte Artikel**
- [[TrueRMS vs. Mittelwert]]
:::
:::vbox
**Führt weiter zu**
- [[Vierleitermessung]]
:::
:::

---

## Spannungsmessung: Innenwiderstand zu tief

Das Voltmeter liegt parallel zur Messstelle. Sein Innenwiderstand (typisch 1 bis 10 MΩ) bildet einen Spannungsteiler mit dem Schaltungswiderstand.

Bei niederohmigen Schaltungen: kein Problem. 10 MΩ parallel zu 1 kΩ ergibt kaum eine Änderung.

Bei hochohmigen Schaltungen: Problem. 10 MΩ parallel zu 5 MΩ ergibt nur noch 3.33 MΩ. Die gemessene Spannung ist deutlich tiefer als die echte.

## Strommessung: Innenwiderstand zu hoch

Das Amperemeter liegt in Reihe. Sein Innenwiderstand (typisch einige mΩ bis wenige Ω je nach Messbereich) verändert den Gesamtwiderstand.

Bei hochohmigen Schaltungen: kein Problem. Bei niederohmigen Schaltungen (z.B. Shunt-Messung): der Innenwiderstand des Amperemeters kann grösser sein als der zu messende Widerstand.

## Widerstandsmessung: Parallelwiderstände

Das Ohmmeter legt selbst eine Messspannung an. Parallel liegende Bauteile (andere Widerstände, Dioden in Durchlassrichtung) verfälschen das Ergebnis.

Immer mindestens einen Anschluss abheben oder das Bauteil auslöten.

## Systematische Fehler

| Fehlerquelle | Wirkung | Behebung |
|---|---|---|
| Messleitungswiderstand | Fehler bei R-Messung | Nullabgleich oder Vierleitermessung |
| Thermospannungen | Drift bei Kleinstsignalen | Messleitungen gleicher Temp. |
| Offsetspannung ADC | Nullpunktfehler | Kalibrierung |
| Frequenzgang | Fehler bei hohen Frequenzen | TrueRMS-Gerät, Bandbreite prüfen |

:::tip
Messbereich immer von oben einpendeln: grössten Bereich wählen, dann schrittweise kleiner. Nie ein unbekanntes Signal direkt im kleinen Bereich messen.
:::
