---
title: Tastkopf 1:1 vs. 10:1
kategorie: MT
tags: [tastkopf, probe, oszilloskop, dämpfung, bandbreite, kapazität, kompensation, 10:1, 1:1, eingangskapazität, massekabel]
symbol: —
einheit: —
---

Der Tastkopf verbindet das Oszilloskop mit dem Messobjekt. Die Wahl zwischen 1:1 und 10:1 beeinflusst Bandbreite und wie stark die Schaltung belastet wird.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszilloskop: Aufbau & Bedienung]]
:::
:::vbox
**Verwandte Artikel**
- [[Signalintegrität]]
:::
:::vbox
**Führt weiter zu**
- [[Signalintegrität]]
:::
:::

---

## 1:1 Tastkopf

Kein Teiler. Das Signal kommt ungedämpft ans Oszilloskop. Maximale Empfindlichkeit.

Nachteil: Hohe Eingangskapazität (80 bis 150 pF). Das belastet hochohmige Schaltungen und begrenzt die Bandbreite auf oft unter 10 MHz.

## 10:1 Tastkopf

Ein Widerstandsteiler im Kopf dämpft das Signal um Faktor 10. Das Oszilloskop zeigt dann den zehnfachen Wert an (kompensiert durch Einstellung).

Vorteil: Eingangskapazität sinkt auf 10 bis 20 pF. Bandbreite steigt auf 100 bis 500 MHz. Die Schaltung wird viel weniger belastet.

Nachteil: 10× weniger Empfindlichkeit. Für sehr kleine Signale ungünstig.

## Kompensation

Jeder 10:1 Tastkopf hat einen kleinen Einstellschraubenzieher-Trimmer. Damit wird die Kapazität des Teilers an das Oszilloskop angepasst.

Test: Rechtecksignal (meist eingebaut im Oszilloskop) messen. Flanken sollen scharf und gerade sein. Überschwinger = zu wenig Kapazität. Abgerundete Flanken = zu viel.

## Wann welchen Typ?

| Situation | Tastkopf |
|---|---|
| Kleine Signale unter 1 V | 1:1 |
| Hochfrequenz über 10 MHz | 10:1 |
| Hochohmige Schaltungen | 10:1 |
| Standard-Messungen | 10:1 |

:::warning
Massekabel so kurz wie möglich halten. Ein langes Massekabel wirkt als Antenne und erzeugt Rauschen und Schwingungen im Messbild, die nicht in der Schaltung vorhanden sind.
:::
