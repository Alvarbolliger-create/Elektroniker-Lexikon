---
title: Schieberegister
kategorie: SH
kapitel: Logik
tags: [schieberegister, sipo, piso, sisO, pipo, schieberichtung, lauflicht, universalschieberegister, 74194]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops (SR, D, JK, T)]]
:::
:::vbox
**Führt weiter zu**
- [[Serielle Datenübertragung (Grundlagen)]]
:::
:::

---

Ein **Schieberegister** ist eine Kette von Flipflops, die es erlaubt, eine am Eingang anliegende Information mit jedem Takt um eine Stufe weiterzuschieben. Nach dem Durchlaufen der Kette steht die Information am Ausgang verzögert, aber unverändert zur Verfügung — das macht Schieberegister zum zentralen Baustein für serielle Datenübertragung und Seriell-Parallel-Wandlung.

## Grundaufbau

Ein Schieberegister besteht aus mehreren in Serie geschalteten **D-Flipflops** (oder JK-Flipflops, deren Eingänge entsprechend beschaltet sind), deren Takteingänge **gemeinsam** mit demselben Clock-Signal versorgt werden — es handelt sich also um eine synchrone Schaltung. Bei jeder aktiven Taktflanke übernimmt das erste Flipflop den Wert am DATA-Eingang, während gleichzeitig der vorher gespeicherte Wert jeder Stufe an die nächste Stufe weitergereicht wird. So "wandert" die eingegebene Information takt­weise durch die Kette.

:::merke
Bei einem 4-Bit-Schieberegister steht die seriell eingegebene Information bereits nach **vier Takten** parallel an den Ausgängen Z0…Z3 zur Verfügung — es findet also eine **Seriell-Parallel-Wandlung** der Eingangsdaten statt. Nach sieben Takten wurde dieselbe Information am letzten Ausgang wieder "hinausgeschoben".
:::

## Die vier Betriebsarten

Je nachdem, ob Daten seriell oder parallel ein- bzw. ausgegeben werden, unterscheidet man vier grundlegende Betriebsarten:

| Betriebsart | Dateneingang | Datenausgang | Funktion | Abkürzung |
|---|---|---|---|---|
| 1 | Seriell | Seriell | — | **SISO** (Serial In, Serial Out) |
| 2 | Seriell | Parallel | Seriell-Parallel-Wandlung | **SIPO** (Serial In, Parallel Out) |
| 3 | Parallel | Seriell | Parallel-Seriell-Wandlung | **PISO** (Parallel In, Serial Out) |
| 4 | Parallel | Parallel | Pufferregister | **PIPO** (Parallel In, Parallel Out) |

![Die vier Betriebsarten von Schieberegistern als Blockdiagramme: (1) SISO — serieller Eingang, serieller Ausgang; (2) SIPO — serieller Eingang, parallele Ausgänge; (3) PISO — parallele Eingänge, serieller Ausgang; (4) PIPO — parallele Eingänge, parallele Ausgänge; mit Schiebetakt und Steuereingang C](abbildungen/schieberegister_betriebsarten.png)

## Schieberichtung umschalten

Bei einer einfachen Kette wird der Ausgang jeder Stufe stets auf den Eingang der nächsten geführt — das Register kann nur in eine Richtung schieben. Führt man stattdessen die Stufenausgänge über **Multiplexer**, lässt sich die Schieberichtung per Steuersignal umschalten:

:::tip
Mit zwei Steuereingängen S₀ und S₁ vor jeder D-Flipflop-Stufe lassen sich vier Betriebsmodi realisieren: **Speicherbetrieb** (S₁S₀ = 00, der Inhalt bleibt trotz aktiver Taktflanke unverändert), **paralleles Laden** (01), **Rechtsschieben** (10) und **Linksschieben** (11). Genau dieses Prinzip setzt das Universalschieberegister 74194 um.
:::

## Anwendung: Lauflicht (Ringregister)

Verbindet man den letzten Ausgang eines Schieberegisters wieder mit dessen Eingang, entsteht ein **Ringregister**: Eine einmal eingegebene "1" zirkuliert dauerhaft durch die Kette und lässt — an LEDs ausgegeben — ein klassisches **Lauflicht** entstehen. Beim Einschalten muss eine solche Schaltung allerdings einmalig "initialisiert" werden (z. B. über den Set-Eingang des ersten Flipflops), da sonst kein definierter Schiebezustand vorliegt.

## Das Universalschieberegister 74194

Der IC **74194** (SRG4) ist ein 4-Bit-Schieberegister mit internen Multiplexern und vereint alle vier Betriebsarten in einem Baustein:

| B | A | Funktion |
|---|---|---|
| 0 | 0 | Speicherbetrieb (auch bei aktiver Taktflanke an C4) |
| 0 | 1 | Serielles Rechtsschieben — Eingang SIR durchgeschaltet |
| 1 | 0 | Serielles Linksschieben — Eingang SIL durchgeschaltet |
| 1 | 1 | Paralleles Laden |

:::info
Über den asynchronen **Clear**-Eingang lässt sich das Register jederzeit taktunabhängig in den Zustand "alle Ausgänge Low" zurücksetzen. Verwandte integrierte Schieberegister sind der 74164 (8-Bit), der 74299 (8-Bit) und der 74673 (16-Bit). Schieberegister bilden damit die technische Grundlage für die → [[Serielle Datenübertragung (Grundlagen)|serielle Datenübertragung]], etwa beim Umsetzen paralleler Mikrocontroller-Daten auf eine serielle Leitung (und umgekehrt) bei Schnittstellen wie SPI.
:::
