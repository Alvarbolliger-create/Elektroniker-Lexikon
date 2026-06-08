---
title: Sample & Hold-Schaltung
kategorie: SH
kapitel: Wandler
tags: [sample and hold, abtast-halte-glied, kondensator, abtastzeitpunkt, opv]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[AD-Wandler (Verfahren im Überblick)]]
:::
:::

---

Ein analoges Signal — etwa eine Spannung, die Temperatur oder Helligkeit abbildet — ändert sich meist fortlaufend. Ein → [[AD-Wandler (Verfahren im Überblick)|AD-Wandler]] braucht jedoch eine gewisse Zeit, um aus diesem Signal eine digitale Zahl zu ermitteln. Würde sich die Eingangsspannung während dieser Wandlungszeit weiter ändern, entstünde ein verfälschtes, "verwischtes" Ergebnis. Genau dieses Problem löst die **Sample & Hold-Schaltung** (Abtast-Halte-Glied).

## Das Problem: ein bewegliches Ziel

:::merke
Jede AD-Wandlung benötigt eine gewisse Zeitspanne — von wenigen Mikrosekunden bis hin zu Millisekunden. Würde der Wandler direkt am sich ständig ändernden Eingangssignal arbeiten, würde er während dieser Zeitspanne unterschiedliche Momentanwerte "sehen" und ein in sich widersprüchliches Resultat liefern. Die Lösung: Das Analogsignal wird in regelmässigen Abständen kurz "eingefroren" — **abgetastet** (Sample) — und für die Dauer der Wandlung **gehalten** (Hold), sodass der Wandler in aller Ruhe arbeiten kann.
:::

## Aufbau: zwei Impedanzwandler und ein Kondensator

:::tip
Das Herzstück der Schaltung ist ein **Speicherkondensator** C, der über einen elektronischen Schalter S geladen und wieder von der restlichen Schaltung getrennt werden kann. Davor und danach sitzt je ein als **Impedanzwandler** (Spannungsfolger) beschalteter Operationsverstärker — ein Aufbau, der direkt auf den Grundlagen aus → [[OPV Grundlagen|OPV Grundlagen]] aufbaut: OP1 entkoppelt das empfindliche Eingangssignal von der nachfolgenden Schaltung, ohne es zu verfälschen, und kann zugleich genügend Strom liefern, um den Kondensator schnell umzuladen. OP2 bildet eine extrem hochohmige Last für den Kondensator — er "belastet" ihn praktisch nicht, sodass sich dieser bei geöffnetem Schalter nicht über die nachfolgende Schaltung entladen kann.
:::

## Der Ablauf: Sample, dann Hold

Im **Sample**-Zustand ist der Schalter S geschlossen (idealerweise mit 0 Ω Widerstand) — der Kondensator lädt sich verzögerungsfrei auf die aktuelle Eingangsspannung auf und folgt ihr. Im **Hold**-Zustand öffnet der Schalter (idealerweise mit unendlich hohem Widerstand) — der Kondensator behält seine zuletzt aufgenommene Ladung und damit seine Spannung bei, während der nachgeschaltete AD-Wandler in Ruhe arbeitet.

:::info
Den genauen Zeitpunkt, wann zwischen Sample und Hold umgeschaltet wird, bestimmt **der AD-Wandler selbst** — die Sample & Hold-Stufe ist heute meist direkt in den AD-Wandler-Baustein integriert (z. B. der Klassiker LF398). An den Kondensator selbst werden dabei zwei widersprüchliche Anforderungen gestellt: Er soll eine möglichst **kleine Kapazität** besitzen, damit er sich schnell umladen lässt — und gleichzeitig einen möglichst **hohen Isolationswiderstand**, damit er die gespeicherte Spannung während der Hold-Phase nicht durch Leckströme verliert.
:::

## Das abgetastete Signal: eine Treppenfunktion

Tastet man ein sich kontinuierlich änderndes Signal in festen Zeitabständen ab und hält jeden Wert bis zur nächsten Abtastung, entsteht aus der ursprünglich glatten Kurve eine **Treppenfunktion**: Jede "Stufe" entspricht einem festgehaltenen Momentanwert, der dem AD-Wandler für die Dauer seiner Wandlung als stabiler Eingangswert zur Verfügung steht.

![Signalverlauf einer Sample & Hold-Schaltung: das kontinuierlich veränderliche Eingangssignal wird in regelmässigen Abständen abgetastet (Sample) und bis zur nächsten Abtastung gehalten (Hold) — der AD-Wandler erhält eine stabile Treppenfunktion als Eingangssignal](abbildungen/sample_hold_signalverlauf.png)

:::warning
Wie oft pro Sekunde abgetastet werden muss, damit aus dieser Treppenfunktion später wieder ein originalgetreues Abbild des Eingangssignals rekonstruiert werden kann, ist keine triviale Frage — sie ist Gegenstand des → [[Abtasttheorem (Nyquist-Shannon)|Abtasttheorems]]: Wird zu selten abgetastet, gehen Informationen über schnelle Signalanteile unwiederbringlich verloren.
:::

Damit liefert die Sample & Hold-Schaltung dem nachfolgenden Wandler genau das, was dieser braucht: ein über die gesamte Wandlungszeit stabiles Eingangssignal. Wie aus diesem "eingefrorenen" Analogwert nun tatsächlich eine digitale Zahl entsteht — und welche unterschiedlichen Strategien es dafür gibt —, zeigt der Überblick über die → [[AD-Wandler (Verfahren im Überblick)|AD-Wandler-Verfahren]].
