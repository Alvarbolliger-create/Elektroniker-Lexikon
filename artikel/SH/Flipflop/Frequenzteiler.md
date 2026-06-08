---
title: Frequenzteiler
kategorie: SH
kapitel: Flipflop
tags: [frequenzteiler, teilerverhaeltnis, asynchron, synchron, taktfrequenz, gerades verhaeltnis, ungerades verhaeltnis]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Asynchrone Zähler]]
:::
:::vbox
**Verwandte Artikel**
- [[Synchrone Zähler]]
:::
:::

---

Ein → [[Asynchrone Zähler|Toggle-Flipflop]] kippt bei jedem zweiten Eingangsimpuls — an seinem Ausgang erscheint deshalb genau die halbe Eingangsfrequenz. Damit ist im Grunde bereits der einfachste **Frequenzteiler** beschrieben: Grundsätzlich kann **jeder Zähler** auch als Frequenzteiler betrieben werden — man muss lediglich denjenigen Ausgang abgreifen, dessen Frequenz im gewünschten Verhältnis zur Eingangsfrequenz steht.

![Timing-Diagramm einer 3-stufigen Frequenzteiler-Kette: Eingang A (1 MHz) → T-FF-Ausgang B (500 kHz) → T-FF-Ausgang C (250 kHz) → T-FF-Ausgang D (125 kHz); jede Stufe halbiert exakt die Frequenz ihrer Vorgängerstufe und liefert ein symmetrisches Rechtecksignal](abbildungen/frequenzteiler_3stufen_timing.png)

## Asynchrone Frequenzteiler mit ungeradem Teilerverhältnis

Ein asynchroner **3:1-Teiler** lässt sich aus zwei T-Flipflops und einem zusätzlichen UND-Gatter aufbauen: Die beiden Flipflops zählen wie gewohnt im Dualcode (00, 01, 10, 00, …), das UND-Gatter erkennt jedoch den Zustand "10" (Q0 = 0, Q1 = 1) und setzt darüber beide Flipflops vorzeitig zurück — der Zähler durchläuft dadurch nur die drei Zustände 00, 01, 10, bevor er wieder bei 00 beginnt. Am Ausgang Q1 erscheint so ein Signal, dessen Frequenz exakt einem Drittel der Eingangsfrequenz C entspricht.

:::merke
- Das Verhältnis von Eingangsfrequenz (an C) zu Ausgangsfrequenz (an Q1) beträgt nun 3:1.
- Die **Laufzeit des rückführenden NAND-/UND-Gatters** bestimmt die Dauer der dabei entstehenden kurzen Zwischenimpulse an Q0.
- Das Ausgangssignal Q1 verfügt **nicht mehr über das gleiche Puls-Pausen-Verhältnis** (Dutycycle) wie das Eingangssignal C — bei ungeraden Teilerverhältnissen ist ein symmetrisches 1:1-Tastverhältnis am Ausgang grundsätzlich nicht erreichbar.
:::

Auf demselben Weg lassen sich beliebige ungerade Teilerverhältnisse realisieren — z. B. ein 5:1- oder ein 10:1-Teiler —, indem die Rückführlogik so angepasst wird, dass sie genau den gewünschten Zählerstand erkennt und den Zähler an dieser Stelle vorzeitig zurücksetzt.

## Asynchrone Frequenzteiler mit geradem Verhältnis

Ein **gerades** Teilerverhältnis lässt sich elegant aus einem ungeraden ableiten:

:::tip
Gerade Teilerverhältnisse bildet man, indem man das gewünschte Verhältnis durch zwei dividiert und zunächst den entsprechenden **ungeraden** Teiler aufbaut. Anschliessend wird ein einzelnes zusätzliches T-Flipflop **nachgeschaltet**, um das vorgeschriebene Gesamt-Teilerverhältnis zu erreichen. Dieses nachgeschaltete Flipflop sorgt im selben Zug dafür, dass das Puls-Pausen-Verhältnis des Ausgangssignals wieder 1:1 beträgt (Dutycycle 50 %) — ein angenehmer Nebeneffekt, da jedes T-Flipflop von sich aus ein perfekt symmetrisches Ausgangssignal liefert.
:::

Ein 6:1-Teiler entsteht so beispielsweise aus einem 3:1-Teiler mit nachgeschaltetem 2:1-Teiler (einem einzelnen T-Flipflop): 6 = 3 · 2. Auf dieselbe Weise lässt sich z. B. ein 10:1-Teiler mit symmetrischem Ausgangssignal aus einem 5:1-Teiler und einem nachgeschalteten T-Flipflop aufbauen — eine in Multisim häufig untersuchte Beispielschaltung, deren Oszilloskopbild ein exakt symmetrisches Rechtecksignal am Ausgang zeigt.

## Synchrone Frequenzteiler

Auch ein → [[Synchrone Zähler|synchroner Zähler]] lässt sich als Frequenzteiler betreiben — der Entwurf ist hier allerdings deutlich anspruchsvoller:

:::warning
Das Entwerfen synchroner Frequenzteiler ist vergleichsweise kompliziert und verlangt eine genaue Analyse des gewünschten Zeitdiagramms: Für jedes Flipflop muss eine individuelle **Zusatzlogik** ermittelt werden, die dessen J-/K- bzw. D-Eingänge so ansteuert, dass der Ausgang exakt im gewünschten Rhythmus kippt — die Schaltflanken müssen dabei "vor der eigentlichen Schaltflanke" korrekt vorbereitet sein. Ein typisches Beispiel ist ein synchroner 3:1-Teiler mit JK-Master-Slave-Flipflops, dessen zweiter Ausgang Q1 ein Signal mit dreifacher Periodendauer (3T) gegenüber dem ersten Ausgang Q0 liefert.
:::

In der Praxis greift man deshalb häufig auf fertige integrierte **programmierbare Frequenzteiler-ICs** zurück (z. B. den Baustein 74167), bei denen sich das gewünschte Teilerverhältnis aus einer Reihe vorgegebener Werte auswählen lässt, ohne die interne Schaltungslogik selbst entwerfen zu müssen.

Wie sich ein solcher synchroner Entwurf systematisch — Schritt für Schritt anhand eines Zeitdiagramms — in eine konkrete Schaltung überführen lässt, zeigt die allgemeine Entwurfsmethode der → [[Zustandsautomaten (FSM)|State-Event-Technik]], mit der sich nicht nur Frequenzteiler, sondern beliebige sequenzielle Schaltungen konstruieren lassen.
