---
title: Aliasing
kategorie: SH
kapitel: Abtasttheorem
tags: [aliasing, spiegelfrequenz, unterabtastung, anti-aliasing-filter]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Abtasttheorem (Nyquist-Shannon)]]
:::
:::vbox
**Verwandte Artikel**
- [[Tiefpass]]
:::
:::

---

Im Artikel → [[Abtasttheorem (Nyquist-Shannon)|Abtasttheorem]] haben wir gesehen, dass sich in den Stützpunkten eines AD-Wandlers immer ein ganzes Spektrum möglicher Frequenzen "versteckt" — und dass nur das Signal, dessen Frequenz kleiner als die halbe Abtastfrequenz ist, korrekt rekonstruiert werden kann. Was aber, wenn ausgerechnet eine Störung mit einer "verbotenen" Frequenz ins System gelangt? Genau dieser Fall trägt einen eigenen Namen: **Aliasing**.

## Wenn sich eine Störfrequenz als Nutzsignal tarnt

:::merke
**Aliasing** (auch Spiegelfrequenz-Effekt genannt) bezeichnet das Phänomen, dass eine Frequenzkomponente, die das Abtasttheorem verletzt, nach der Abtastung als eine völlig andere — niedrigere — "Geister-Frequenz" erscheint und sich dabei direkt in die Bandbreite des eigentlichen Nutzsignals "spiegelt". Das digitale System kann diese gespiegelte Frequenz nicht mehr von einer echten Nutzsignal-Komponente unterscheiden: Es entsteht eine **Signalverfälschung**, die sich nachträglich nicht mehr korrigieren lässt.
:::

## Das Beispiel: ein 9-kHz-Störsignal bei 10 kHz Abtastrate

Nehmen wir ein Nutzsignal mit einer Bandbreite von 0…2 kHz, das mit f_Abtast = 10 kHz abgetastet wird — für das Nutzsignal selbst ist das Abtasttheorem damit komfortabel erfüllt. Nun koppelt sich plötzlich eine Störung mit 9 kHz ein. Für dieses 9-kHz-Signal gilt die Bedingung f_Abtast ≥ 2 × f_Signal aber nicht mehr (10 kHz < 2 × 9 kHz)!

:::tip
Tastet man das 9-kHz-Störsignal mit 10 kHz ab, durchläuft es exakt dieselben Stützpunkte wie ein gedachtes Sinussignal mit nur **1 kHz** — die Differenz F_Abtast − F_Signal = 10 kHz − 9 kHz = 1 kHz. Genau diese 1-kHz-"Spiegelung" erscheint nun am Ausgang des AD-Wandlers — und sie liegt mitten in der Bandbreite unseres 0…2-kHz-Nutzsignals! Aus Sicht des digitalen Systems ist diese Geister-Frequenz von einer echten 1-kHz-Nutzsignal-Komponente nicht mehr zu unterscheiden.
:::

## Ein Fehler ohne Korrekturmöglichkeit

:::warning
Sobald sich eine Spiegelfrequenz erst einmal in die Bandbreite des Nutzsignals "eingemischt" hat, ist der Schaden bereits angerichtet — er lässt sich **durch keine nachträgliche digitale Filterung mehr rückgängig machen**. Auch ein Tiefpass am Ausgang des nachfolgenden DA-Wandlers (mit Grenzfrequenz F_Abtast/2) hilft hier nichts: Er kann die 1-kHz-"Spiegelung" nicht von der echten 1-kHz-Nutzsignal-Information trennen, weil beide nun ununterscheidbar im selben Frequenzbereich liegen. Das Originalsignal kann nicht mehr originalgetreu reproduziert werden — die Information ist unwiderruflich verloren.
:::

## Die Lösung: dem Übel an der Wurzel begegnen

Wenn sich Aliasing im Nachhinein nicht mehr beheben lässt, bleibt nur eine Konsequenz: Es darf gar nicht erst entstehen. Genau das leistet ein vorgeschaltetes Filter:

:::info
Die einzig wirksame Massnahme gegen Aliasing ist ein **Anti-Aliasing-Filter** — ein → [[Tiefpass|Tiefpassfilter]] mit der Grenzfrequenz F_Abtast/2, das **direkt vor** dem AD-Wandler eingebaut wird. Seine Aufgabe: alle Frequenzanteile, die grösser als die halbe Abtastfrequenz sind — egal ob es sich um Störungen, Rauschen oder andere unerwünschte Signalanteile handelt —, konsequent "abzuschneiden", bevor sie überhaupt zum Wandler gelangen. Damit wird das Abtasttheorem am Eingang aktiv "geschützt": Was der Wandler gar nicht erst zu sehen bekommt, kann sich auch nicht ins Nutzsignal spiegeln.
:::

![Vollständige AD/DA-Systemstruktur mit Anti-Aliasing: Sensor → Tiefpass A (schneidet Frequenzen > f_Abtast/2 ab, koppelt Hochfrequenz ab) → AD-Wandler → CPU → DA-Wandler → Tiefpass B (glättet das treppenförmige Ausgangssignal) → Aktor; beide Tiefpässe haben die Grenzfrequenz f_Abtast/2](abbildungen/antialias_system_tiefpaesse.png)

## Die gleiche Vorsicht gilt für die Rückwandlung

Dieselbe Überlegung gilt spiegelbildlich auch für den Weg zurück von digital nach analog: Das "treppenförmige" Signal am Ausgang eines DA-Wandlers enthält durch seine eckige Form zusätzliche, unerwünschte Frequenzanteile — vergleichbar mit dem Frequenzspektrum eines Rechtecksignals, das sich aus einer Grundschwingung und vielen Oberschwingungen zusammensetzt. Auch hier "spiegeln" sich Anteile um Vielfache der Abtastfrequenz, allerdings mit stetig abnehmender Amplitude. Ein zweiter Tiefpass — diesmal **nach** dem DA-Wandler, ebenfalls mit Grenzfrequenz F_Abtast/2 — schneidet diese künstlich entstandenen Frequenzanteile wieder ab und glättet das treppenförmige Signal zu einer sauberen Kurve.

## Drei Regeln, die das Originalsignal retten

Damit lässt sich zusammenfassen, unter welchen Bedingungen ein analoges Signal den Weg durch die digitale Welt unbeschadet übersteht:

1. Das Abtasttheorem ist einzuhalten: f_Abtast ≥ 2 × f_Signal
2. Ein Tiefpass mit Grenzfrequenz F_Abtast/2 wird **vor** dem AD-Wandler eingesetzt (Anti-Aliasing-Filter)
3. Ein Tiefpass mit Grenzfrequenz F_Abtast/2 wird **nach** dem DA-Wandler eingesetzt (Glättung)

Wer diese drei Punkte beachtet, kann sicher sein, dass sein digitales System ein analoges Signal originalgetreu erfasst, verarbeitet und wieder ausgibt — ohne dass sich irgendwo ungebetene "Geister-Frequenzen" einschleichen. Damit ist die Brücke zwischen analoger und digitaler Welt vollständig beschrieben — von der Wahl der richtigen Abtastfrequenz über die nötigen Schutzfilter bis hin zu den eigentlichen Wandlerschaltungen, die im Kapitel → [[AD-Wandler (Verfahren im Überblick)|AD-Wandler]] im Detail vorgestellt werden.
