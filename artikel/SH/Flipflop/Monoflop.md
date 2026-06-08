---
title: Monoflop (Monostabile Kippstufe)
kategorie: SH
kapitel: Flipflop
tags: [monoflop, monostabile kippstufe, retriggerbar, nicht retriggerbar, impulsformung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops (SR, D, JK, T)]]
:::
:::

---

Ein → [[Flipflops (SR, D, JK, T)|Flipflop]] ist **bistabil**: Es verharrt in jedem seiner beiden Zustände, bis ein Eingangssignal es aktiv umschaltet. Das **Monoflop** (auch monostabile Kippstufe genannt) tickt anders: Es besitzt nur **einen** stabilen Ruhezustand — durch einen Auslöseimpuls (Trigger) gerät es kurzzeitig in seinen zweiten, instabilen Zustand und kehrt danach von selbst, nach einer fest einstellbaren Zeitspanne, wieder in die Ruhelage zurück.

## Funktionsprinzip: definierte Impulse erzeugen

Ein Monoflop wandelt einen beliebig geformten Auslöseimpuls — z. B. eine kurze, "verschmierte" Taktflanke oder ein prellendes Tastsignal — in einen Ausgangsimpuls **exakt definierter Dauer** um. Diese Dauer t_Q wird nicht durch das Triggersignal bestimmt, sondern durch eine extern beschaltete RC-Kombination:

:::formel
t_Q = k · R_T · C_T
:::

wobei k eine baustein­abhängige Konstante ist und R_T sowie C_T das zeitbestimmende Bauteilpaar bilden. Über die Wahl dieser beiden Bauteile lässt sich die Impulsdauer von Mikrosekunden bis hin zu mehreren Sekunden frei einstellen — das Monoflop wird damit zum universellen Werkzeug der **Impulsformung**.

## Zwei Bauformen: nicht retriggerbar und retriggerbar

In der Praxis unterscheidet man zwei Varianten, die sich in ihrem Verhalten bei einem **erneuten** Trigger-Impuls — während der Ausgangsimpuls noch läuft — grundlegend unterscheiden:

:::merke
Ein **nicht retriggerbares** Monoflop (im Schaltzeichen durch eine "1" im Impulssymbol gekennzeichnet) ignoriert während eines laufenden Ausgangsimpulses jeden weiteren Trigger-Eingang vollständig — die Impulsdauer bleibt exakt t_Q, unabhängig davon, wie oft währenddessen erneut getriggert wird. Ein **retriggerbares** Monoflop (Schaltzeichen ohne die "1") hingegen verlängert seinen Ausgangsimpuls bei jedem neuen Trigger-Ereignis um eine weitere volle Periode t_Q — solange die Trigger-Impulse schneller aufeinanderfolgen als t_Q verstreicht, bleibt der Ausgang dauerhaft aktiv und "läuft nicht ab".
:::

![Signal-Zeit-Diagramme beider Monoflop-Typen: oben das nicht-retriggierbare Monoflop (nach dem ersten Trigger erzeugt Q genau einen Impuls der Dauer t₀, weitere Trigger während des Impulses werden ignoriert), unten das retriggierbare Monoflop (jeder neue Trigger verlängert den Q-Impuls um eine weitere Periode t₀)](abbildungen/monoflop_timing_beide.png)

Welche Variante die richtige ist, hängt vollständig von der Anwendung ab — beide Verhaltensweisen lassen sich gezielt nutzen, wie das folgende Beispiel zeigt.

## Anwendungsbeispiel: Watchdog-Schaltung

Eine klassische Anwendung, die **beide** Monoflop-Varianten gleichzeitig nutzt, ist der **Watchdog** — eine Überwachungsschaltung, die prüft, ob ein Mikrocontroller noch ordnungsgemäss arbeitet, und im Fehlerfall automatisch einen Reset auslöst:

:::tip
Eine typische Realisierung mit dem IC **74HCT123** (Doppel-Monoflop) verwendet zwei gekoppelte Stufen: **Monoflop A** ist *retriggerbar* und auf eine Zeit von z. B. 20 ms eingestellt — der überwachte Mikrocontroller muss es in genau diesem Rhythmus durch ein "Lebenszeichen"-Signal (z. B. ein periodisches Toggeln eines Ausgangs-Pins) immer wieder neu antriggern. Solange dies zuverlässig geschieht, bleibt der Ausgang von Monoflop A dauerhaft aktiv, und **Monoflop B** — *nicht retriggerbar* und für die eigentliche Reset-Pulsbreite zuständig — wird nicht ausgelöst. Bleibt das Lebenszeichen jedoch aus (etwa weil sich die Software des Controllers "aufgehängt" hat), läuft Monoflop A nach 20 ms ab; genau diese fallende Flanke triggert nun Monoflop B, das einen sauberen, exakt bemessenen Reset-Impuls erzeugt und den Mikrocontroller neu startet.
:::

So entsteht aus zwei einfachen, zeitbestimmenden Kippstufen eine vollständige Selbstüberwachung — ein Prinzip, das in praktisch jedem eingebetteten System zur Steigerung der Betriebssicherheit eingesetzt wird. Während das Monoflop einmalige, definierte Zeitspannen erzeugt, übernehmen → [[Asynchrone Zähler|Zähler]] und → [[Frequenzteiler|Frequenzteiler]] die Aufgabe, fortlaufende, sich wiederholende Zeitraster aus einem Taktsignal abzuleiten.
