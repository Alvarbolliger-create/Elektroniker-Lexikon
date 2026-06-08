---
title: Asynchrone Zähler
kategorie: SH
kapitel: Flipflop
tags: [asynchroner zaehler, vorwaertszaehler, rueckwaertszaehler, bcd-zaehler, modulo-zaehler, toggle-flipflop, umschaltbare zaehlrichtung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops (SR, D, JK, T)]]
:::
:::vbox
**Verwandte Artikel**
- [[Synchrone Zähler]]
:::
:::vbox
**Führt weiter zu**
- [[Frequenzteiler]]
:::
:::

---

Reiht man mehrere → [[Flipflops (SR, D, JK, T)|Toggle-Flipflops]] aneinander, von denen jedes mit der halben Frequenz seines Vorgängers kippt, entsteht beinahe von selbst ein **Zähler**: An den Ausgängen liegt nach jedem Taktimpuls ein Binärwort an, das die Anzahl der bisher gezählten Impulse repräsentiert. Man unterscheidet grundsätzlich zwischen **asynchronen** und **synchronen** Zählern sowie zwischen **Vorwärts-** und **Rückwärtszählern**: Ein Vorwärtszähler **inkrementiert** seinen Zählerstand bei jedem Takt um 1, ein Rückwärtszähler **dekrementiert** ihn entsprechend.

:::merke
Bei einem **asynchronen** Zähler erhält nicht jedes Flipflop den Systemtakt direkt — stattdessen taktet der Ausgang einer Stufe jeweils die nächste. Die Flipflops kippen dadurch nacheinander, "wellenartig" ("Ripple-Counter"). Das macht die Schaltung sehr einfach und benötigt kein zusätzliches Verknüpfungsnetzwerk — allerdings addieren sich die Schaltverzögerungen (Laufzeiten) der einzelnen Stufen. Bei → [[Synchrone Zähler|synchronen Zählern]] hingegen erhalten alle Flipflops denselben Takt gleichzeitig, was höhere Geschwindigkeiten erlaubt, jedoch zusätzliche Verknüpfungslogik an den J-/K- bzw. D-Eingängen erfordert.
:::

## Vorwärtszähler mit Toggle-Flipflops

Der einfachste asynchrone Vorwärtszähler entsteht, indem man mehrere → [[Flipflops (SR, D, JK, T)|T-Flipflops]] (oder Master-Slave-JK-Flipflops mit fest verbundenem J = K = 1, also im Toggle-Betrieb) in Reihe schaltet: Der Q-Ausgang einer Stufe taktet den Eingang der nächsten. Jede Stufe halbiert dabei die Frequenz ihres Vorgängers — exakt das Funktionsprinzip des → [[Frequenzteiler|Frequenzteilers]].

:::warning
Da sich die Schaltverzögerungen der Flipflops entlang der Kette **aufsummieren**, sinkt die maximal mögliche Zählfrequenz mit der Anzahl der Stufen. Bei einer Laufzeit von z. B. 10 ns pro Flipflop ergibt sich für einen 8-Bit-Zähler eine maximale Taktfrequenz von f_max = 1 / (8 · 10 ns) = 1 / (100 ns) = 10 MHz — bei höheren Stufenzahlen wird diese Grenze schnell zum limitierenden Faktor und macht den Wechsel zu synchronen Architekturen erforderlich.
:::

:::merke
**Beim Vorwärtszähler gilt:** Welcher Ausgang die nächste Stufe taktet, hängt von der Flankenempfindlichkeit der verwendeten Flipflops ab — bei **negativ flankengetriggerten** Flipflops wird der **Q-Ausgang** auf den Takteingang der Folgestufe geführt, bei **positiv flankengetriggerten** Flipflops hingegen der **Q̄-Ausgang**. Nur so entsteht beim Überlauf jeder Stufe (von 1 zurück auf 0) genau die aktive Taktflanke, die die nächsthöhere Stufe inkrementieren soll.
:::

![Timing-Diagramm des 3-Bit-asynchronen Vorwärtszählers: Takt (C) sowie Ausgänge Q0, Q1 und Q2 — Q0 kippt bei jeder fallenden Taktflanke, Q1 bei jeder fallenden Flanke von Q0, Q2 bei jeder fallenden Flanke von Q1; der Binärwert an Q2Q1Q0 zählt von 000 bis 111 und überläuft dann zu 000](abbildungen/asynczaehler_vorwaerts_timing.png)

## Vorwahl, BCD-Zähler und Kaskadierung

In der Praxis benötigt man Zähler oft nicht nur in reiner Zweierpotenz-Form (Modulo 2, 4, 8, 16, …), sondern auch mit beliebig wählbarem Endwert oder fester Modulo-Zahl:

- **Vorwärtszähler mit taktunabhängigem Set/Reset**: Über zusätzliche, asynchrone (also nicht an den Takt gebundene) Set- und Reset-Eingänge der Flipflops lässt sich ein beliebiger Startwert direkt vorladen ("Vorwahlmöglichkeit") — der Zähler beginnt seinen Lauf nicht zwangsläufig bei 0.
- **BCD-Zähler (Modulo-10-Zähler)**: Ein einfacher 4-Bit-Zähler würde bis 15 zählen, bevor er überläuft. Verknüpft man die Ausgänge jedoch mit einem zusätzlichen NAND-Gatter, das beim Erreichen des Zählerstands 10 (1010) sämtliche Flipflops asynchron zurücksetzt, "springt" der Zähler sofort wieder auf 0 — es entsteht ein **Modulo-10- bzw. BCD-Zähler**, der die Ziffern 0…9 durchläuft. Mehrere solcher Dekaden lassen sich kaskadieren (Übertrag der höchsten Stufe taktet die nächste Dekade) und bilden so z. B. einen Zähler von 0 bis 99.

:::tip
Wie viele Flipflop-Stufen für eine bestimmte Zählreichweite nötig sind, lässt sich leicht abschätzen: Um z. B. bis 1023 zählen zu können (1024 verschiedene Zustände), benötigt man n = log(1024) / log(2) = 10 Flipflops. Allgemein gilt: n = ⌈log₂(Anzahl Zustände)⌉.
:::

## Rückwärtszähler

Ein asynchroner **Rückwärtszähler** lässt sich aus denselben Bausteinen aufbauen — mit einer entscheidenden Umkehrung:

:::merke
**Beim Rückwärtszähler gilt** das genaue Gegenteil der Vorwärtszähler-Regel: Bei negativ flankengetriggerten Flipflops wird nun der **Q̄-Ausgang** auf den Takteingang der Folgestufe geführt, bei positiv flankengetriggerten der **Q-Ausgang**. Anschaulich entsteht dadurch ein Zählverhalten, bei dem die invertierten Ausgänge wie ein Vorwärtszähler hochzählen, während die "normalen" Q-Ausgänge gleichzeitig dasselbe Bitmuster rückwärts durchlaufen — ein Rückwärtszähler lässt sich folglich auch aus einem Vorwärtszähler gewinnen, indem man schlicht dessen Ausgänge invertiert abliest (oder umgekehrt).
:::

![Timing-Diagramm des 3-Bit-asynchronen Rückwärtszählers: Takt (C) sowie Ausgänge Q0/Q̄0, Q1/Q̄1 und Q2/Q̄2 — der Binärwert an Q2Q1Q0 zählt von 111 herunter bis 000 und springt dann wieder auf 111; die invertierten Ausgänge Q̄0/Q̄1/Q̄2 laufen spiegelbildlich als Vorwärtszähler](abbildungen/asynczaehler_rueckwaerts_timing.png)

## Zähler mit umschaltbarer Zählrichtung

Soll ein und derselbe Zähler je nach Bedarf vor- oder rückwärts zählen können, schaltet man zwischen die jeweilige Stufe und die Folgestufe einen **2:1-Multiplexer**: Ein Steuersignal (Up/Down) entscheidet, ob der Q- oder der Q̄-Ausgang der vorherigen Stufe zur Taktung der nächsten durchgeschaltet wird. Damit lässt sich die Zählrichtung jederzeit per Steuerleitung umschalten, ohne die Schaltung neu zu verdrahten — ein Prinzip, das eng mit der Funktionsweise des → [[Multiplexer (MUX)|Multiplexers]] als universellem Auswahlbaustein verwandt ist.

Asynchrone Zähler bilden damit das Fundament für eine ganze Familie abgeleiteter Schaltungen: Schaltet man die letzte Stufe als reines Verhältnisglied, entsteht ein → [[Frequenzteiler|Frequenzteiler]]; benötigt man höhere Geschwindigkeit oder beliebige, nicht binäre Zählfolgen, führt der Weg zum → [[Synchrone Zähler|synchronen Zähler]].
