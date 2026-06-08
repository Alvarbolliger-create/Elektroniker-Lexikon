---
title: Pull-Up- und Pull-Down-Widerstände
kategorie: SH
kapitel: Logik
tags: [pull-up, pull-down, definierter pegel, eingang, widerstand, undefinierter zustand]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter (UND, ODER, NICHT, NAND, NOR, EXOR)]]
:::
:::vbox
**Verwandte Artikel**
- [[Schaltpegel & Störabstand]]
:::
:::

---

Ein offener, nirgends angeschlossener Eingang eines Logikgatters liegt auf keinem definierten Pegel — er "schwebt" und nimmt durch eingestreute Störungen praktisch zufällige Werte an. **Pull-Up-** und **Pull-Down-Widerstände** legen einen solchen Eingang fest auf einen definierten Ruhepegel, ohne dabei den eigentlichen Signalbetrieb zu stören.

## Das Grundproblem: offene Eingänge

:::warning
Bei digitalen Schaltungen gibt es **keine unbenutzten Eingänge**! Ein offener Eingang verhält sich wie eine kleine Antenne — er nimmt Störsignale auf und kann je nach Augenblick als Low oder High interpretiert werden. Das führt zu unvorhersagbarem Schaltverhalten und in CMOS-Gattern sogar zu erhöhter Verlustleistung, da beide Eingangstransistoren gleichzeitig leicht leitend werden können. Offene Eingänge müssen deshalb **zwingend** an ein definiertes Signal gelegt werden.
:::

## Funktionsweise

Ein **Pull-Up-Widerstand** verbindet die Leitung über einen hochohmigen Widerstand mit der Versorgungsspannung (V_CC). Solange kein aktiver Treiber die Leitung aktiv auf Low zieht, liegt sie über den Widerstand sicher auf **High**. Ein **Pull-Down-Widerstand** funktioniert spiegelbildlich: Er verbindet die Leitung mit Masse (GND), sodass sie im Ruhezustand sicher auf **Low** liegt.

:::merke
Pull-Up → Ruhepegel **High** (Widerstand nach V_CC). Pull-Down → Ruhepegel **Low** (Widerstand nach GND). Sobald ein Taster, Sensor oder Treiber aktiv den jeweils anderen Pegel anlegt, "gewinnt" dieser über den hochohmigen Widerstand — die Leitung wird auf den aktiven Pegel gezogen, ohne dass ein Kurzschluss entsteht.
:::

## Dimensionierung: ein Rechenbeispiel

Die Grösse des Widerstands ist ein Kompromiss: Er muss klein genug sein, um den Eingangspegel sicher zu erreichen, aber gross genug, um den treibenden Ausgang nicht unnötig zu belasten. Beim Verbinden eines TTL-Ausgangs mit einem 5-V-CMOS-Eingang lässt sich der nötige Pull-Up-Widerstand wie folgt abschätzen:

:::formel
R_Pu(low) = (U_CC − U_OL) / I_OL

Mit U_CC = 5 V, U_OL = 0.5 V und I_OL = 16 mA ergibt sich R_Pu = 281 Ω — bei diesem Wert würde der Widerstand das TTL-Gatter aber dauerhaft mit 16 mA belasten. Wählt man stattdessen I_OL = 1.0 mA, ergibt sich R_Pu = 4500 Ω.
:::

In der Praxis wählt man deshalb einen Wert dazwischen, der das treibende Gatter nicht unnötig stark belastet — typisch sind Widerstände im Bereich von **4.7 kΩ bis 47 kΩ**. Im High-Zustand fliesst praktisch kein Strom mehr durch den Pull-Up (der CMOS-Eingang ist hochohmig), sodass die Spannung am Eingang nahezu vollständig auf V_CC angehoben wird und der Pegel V_IH sicher überschritten wird.

:::tip
Pull-Up- und Pull-Down-Widerstände sind die einfachste Form der **Pegelanpassung** zwischen unterschiedlichen → [[Logikfamilien (TTL, CMOS, BiCMOS, ECL)]]. Sie spielen ausserdem eine zentrale Rolle bei → [[Opencollector & Open-Drain]]-Ausgängen, bei Tastereingängen von Mikrocontrollern (interner Pull-Up gegen "Prellen" und schwebende Pegel) und überall dort, wo ein Bus im Ruhezustand auf einem definierten Pegel liegen muss. Welche konkreten Pegelwerte dabei einzuhalten sind, beschreibt → [[Schaltpegel & Störabstand]].
:::
