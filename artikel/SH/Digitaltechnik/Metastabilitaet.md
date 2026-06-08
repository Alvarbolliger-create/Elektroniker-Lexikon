---
title: Metastabilität
kategorie: SH
kapitel: Digitaltechnik
tags: [metastabilitaet, setup-zeit, hold-zeit, synchronisierung, taktdomaene]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops (SR, D, JK, T)]]
:::
:::

---

Ein → [[Flipflops (SR, D, JK, T)|Flipflop]] übernimmt seinen Eingangswert exakt im Moment der aktiven Taktflanke. Damit dies zuverlässig gelingt, muss das Eingangssignal eine gewisse Zeit vor und nach der Flanke stabil anliegen. Wird diese Bedingung verletzt, kann das Flipflop in einen undefinierten Schwebezustand geraten — die **Metastabilität**.

## Setup-Zeit und Hold-Zeit

Jedes flankengesteuerte Flipflop besitzt zwei kritische Zeitfenster rund um die aktive Taktflanke:

:::merke
Die **Setup-Zeit** (t_su) ist die minimale Zeitspanne, während der das Datensignal **vor** der aktiven Taktflanke bereits stabil anliegen muss. Die **Hold-Zeit** (t_h) ist die minimale Zeitspanne, während der das Datensignal **nach** der Taktflanke noch stabil bleiben muss. Nur wenn beide Bedingungen eingehalten werden, übernimmt das Flipflop den Eingangswert sicher und mit garantierter Verzögerung an seinem Ausgang.
:::

Ändert sich der Dateneingang **innerhalb** dieses Setup-/Hold-Fensters — also zu nahe an der Taktflanke —, kann das interne, aus rückgekoppelten Gattern aufgebaute Speicherelement des Flipflops für eine unbestimmte Zeit in einem Zwischenzustand verharren, der weder sicher als 0 noch als 1 interpretiert werden kann.

## Der metastabile Zustand

:::warning
Im **metastabilen Zustand** liegt der Ausgang eines Flipflops auf einem Pegel, der zwischen den definierten Low- und High-Bereichen schwebt — vergleichbar mit einer Kugel, die exakt auf der Spitze eines Hügels balanciert: Theoretisch könnte sie dort beliebig lange verharren, in der Praxis kippt sie nach einer unvorhersehbaren Zeit nach der einen oder anderen Seite. Genauso "entscheidet" sich ein metastabiles Flipflop irgendwann für 0 oder 1 — wann genau und wofür, ist jedoch nicht vorhersagbar. Schlimmer noch: Verschiedene nachgeschaltete Gatter können den schwebenden Pegel **unterschiedlich** interpretieren, sodass in derselben Schaltung gleichzeitig eine 0 und eine 1 "gelesen" werden — ein klassischer Quell für sporadische, schwer reproduzierbare Fehler.
:::

## Wann tritt Metastabilität auf?

Solange alle Signale innerhalb derselben **Taktdomäne** synchron zueinander erzeugt werden, lässt sich die Einhaltung von Setup- und Hold-Zeit durch sorgfältiges Schaltungsdesign garantieren. Kritisch wird es jedoch beim Übergang zwischen **asynchronen Signalquellen**:

:::tip
Typische Auslöser für Metastabilität sind asynchrone Eingangssignale, die nicht zum Systemtakt passen — etwa ein Tastendruck, ein externes Sensorsignal oder ein Datensignal aus einer anderen **Taktdomäne** (z. B. beim Übergang zwischen zwei Schaltungsteilen mit unterschiedlichen Taktfrequenzen). Da ein solches Signal jederzeit, also auch genau im Setup-/Hold-Fenster, wechseln kann, lässt sich eine Verletzung der Zeitbedingungen prinzipiell nie vollständig ausschliessen — sie kann nur auf ein praktisch vernachlässigbares Mass reduziert werden.
:::

## Die Lösung: Synchronisierer-Ketten

Da sich Metastabilität nicht verhindern, sondern nur in ihrer Auswirkung entschärfen lässt, wird in der Praxis eine **Synchronisierer-Kette** eingesetzt: Das asynchrone Signal durchläuft zunächst ein erstes, mit dem Systemtakt getaktetes Flipflop. Dessen Ausgang darf zwar kurzzeitig metastabil sein — er erhält jedoch eine ganze Taktperiode lang Zeit, sich auf einen stabilen Pegel "festzulegen", bevor ihn ein zweites, nachgeschaltetes Flipflop übernimmt. Erst der Ausgang dieser zweiten (oder bei hohen Anforderungen auch dritten) Stufe gilt als sicher synchronisiert und darf in der eigentlichen Schaltung weiterverarbeitet werden.

Die mittlere Zeit zwischen zwei metastabilitätsbedingten Fehlfunktionen wird als **MTBF** (Mean Time Between Failures) bezeichnet — sie lässt sich durch zusätzliche Synchronisierer-Stufen und schnellere Flipflops auf Werte vergrössern, die für die jeweilige Anwendung praktisch keine Rolle mehr spielen. Damit ist die Synchronisierer-Kette das Standardwerkzeug überall dort, wo digitale Schaltungen mit der "unberechenbaren" analogen Aussenwelt oder mit anderen Taktdomänen kommunizieren müssen.
