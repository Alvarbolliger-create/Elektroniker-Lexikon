---
title: Zustandsautomaten (FSM)
kategorie: SH
kapitel: Flipflop
tags: [fsm, finite state machine, zustandsdiagramm, zustandsautomat, schaltungsentwurf, state event technik]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Synchrone Zähler]]
:::
:::vbox
**Führt weiter zu**
- [[Programmierbare Logikbausteine (PROM, PAL, PLA)]]
:::
:::

---

→ [[Synchrone Zähler|Synchrone Zähler]] und → [[Frequenzteiler|Frequenzteiler]] sind im Grunde nur Spezialfälle eines viel allgemeineren Konzepts: Beide lassen sich als Schaltung auffassen, die mit jeder Taktflanke einen **definierten Folgezustand** annimmt. Verallgemeinert man dieses Prinzip, gelangt man zum **endlichen Automaten** (engl. *Finite State Machine*, FSM) — einem systematischen Entwurfsverfahren, mit dem sich praktisch jede sequenzielle Schaltung konstruieren lässt, die sich "Schritt für Schritt" durch eine Folge von Zuständen bewegt.

## Aufbau eines Zustandsautomaten

Jede FSM lässt sich auf dasselbe Blockschaltbild zurückführen:

:::merke
Eine FSM besteht aus drei Teilen: einer **kombinatorischen Logik für den Folgezustand** ("Next State Combinational Logic"), die aus dem aktuellen Zustand und eventuellen Eingangssignalen den nächsten Zustand berechnet; einem **Zustandsregister** ("State Register") — einer Bank von → [[Flipflops (SR, D, JK, T)|D-Flipflops]], die diesen Folgezustand bei der nächsten aktiven Taktflanke übernehmen und so den aktuellen Zustand "speichern"; sowie einer **Ausgangslogik** ("Output Combinational Logic"), die aus dem gespeicherten Zustand die eigentlichen Ausgangssignale ableitet. Hängen die Ausgänge — wie hier beschrieben — ausschliesslich vom *aktuellen* Zustand ab (nicht zusätzlich von momentanen Eingängen), spricht man von einer **Moore-Maschine**.
:::

![Moore-Maschinen-Blockdiagramm und 8-Zustands-FSM eines Frequenzteilers: oben das Blockschaltbild mit Inputs, Next-State-Logik, Zustandsregister (D-FFs) und Ausgangslogik; unten das zugehörige Zustandsdiagramm mit 8 Zuständen (S0:000 bis S7:111) und den getakteten Übergangspfeilen](abbildungen/fsm_moore_8zustaende.png)

Der Zustand wird dabei rückgekoppelt: Der Inhalt des Zustandsregisters fliesst zurück in die Next-State-Logik, sodass sich aus dem aktuellen Zustand und eventuellen Eingangswerten der nächste ergibt — exakt das Funktionsprinzip, das bereits einem → [[Synchrone Zähler|synchronen Zähler]] zugrunde liegt, hier jedoch konsequent verallgemeinert.

## Der Entwurfsweg: von der Anforderung zur Schaltung

Das systematische Vorgehen beim Entwurf einer FSM — die **State-Event-Technik** — lässt sich in klar abgegrenzten Schritten beschreiben, die sich am Beispiel eines synchronen Lauflichts (Shift-Left-Effekt, realisiert mit D-Flipflops, Datenübernahme auf die steigende Taktflanke) zeigen lassen:

1. **Anforderung als Zeitdiagramm festhalten**: Zunächst wird das gewünschte Verhalten als Zeitdiagramm der Ausgänge skizziert — z. B. ein "wanderndes" Bitmuster, das die Zustände A, B, C, A, B, C, … durchläuft (der Zustand D zeigt dabei exemplarisch, dass sich der Ablauf nach einer vollen Periode wiederholen muss).
2. **Zustände definieren und kodieren**: Jedem im Diagramm erkennbaren "Bild" wird ein eindeutiger, binär kodierter Zustand zugewiesen — z. B. S0 = 00, S1 = 01, S2 = 10, S3 = 11.
3. **Zustandsdiagramm zeichnen**: Die Übergänge zwischen den Zuständen werden als gerichteter Graph dargestellt — Kreise für die Zustände, Pfeile (beschriftet mit der auslösenden Taktflanke bzw. den nötigen Eingangsbedingungen) für die Übergänge. Ein eigens markierter Startzustand zeigt, in welchem Zustand die Schaltung nach dem Einschalten (Powerup/Reset) beginnt.
4. **Zustandstabelle (Wahrheitstabelle) aufstellen**: Für jeden möglichen Vorzustand (Q-Werte) wird eingetragen, welcher Folgezustand (D-Werte am Eingang der Flipflops) sowie welche Ausgangswerte sich ergeben sollen.
5. **Schaltfunktionen ermitteln**: Aus der Zustandstabelle werden — z. B. mittels KV-Diagramm — die Verknüpfungsgleichungen für jeden D-Eingang sowie für jeden Ausgang abgeleitet.
6. **Schaltung aufbauen und simulieren**: Aus den gewonnenen Gleichungen wird die kombinatorische Logik vor jedem D-Flipflop aufgebaut — fertig ist die FSM.

:::tip
Im Lauflicht-Beispiel ergeben sich aus der Zustandstabelle die Gleichungen D₁ = (Q₁ ∧ Q̄₀) ∨ (Q₀ ∧ Q̄₁) — eine reine **EXOR-Verknüpfung** — sowie D₀ = Q₁ ∨ Q̄₀, dazu drei einfache Ausgangsgleichungen für die LED-Treiber (LED2 = Q₁ ∧ Q₀, LED1 = Q₁ ∧ Q̄₀, LED0 = Q̄₁ ∧ Q₀). Aus diesen wenigen Gleichungen lässt sich die komplette Schaltung mit nur zwei D-Flipflops und einer Handvoll Gatter aufbauen — ein eindrucksvolles Beispiel dafür, wie kompakt sich auch optisch komplex wirkende Abläufe wie ein Lauflicht mit der State-Event-Technik realisieren lassen.
:::

![FSM-Zustandsdiagramm des 4-Zustands-Lauflichts: vier Zustände S0:00, S1:01, S2:10, S3:11 mit Powerup-Reset-Pfeil auf S0 und Übergangspfeilen zwischen den Zuständen; darunter die vollständige Zustandstabelle mit aktuellem Zustand (Q1,Q0), Folgezustand (D1,D0) und den Ausgangswerten LED2, LED1, LED0](abbildungen/fsm_lauflicht_4zustaende.png)

## Beispiel: Frequenzteiler 5:1 mit FSM

Dieselbe Methode lässt sich auch zum Entwurf eines → [[Frequenzteiler|Frequenzteilers]] mit beliebigem Tastverhältnis einsetzen. Gefordert sei ein **5:1-Frequenzteiler** mit einem Tastverhältnis von 3:2 (Ausgang Z drei Takte lang High, zwei Takte lang Low). Da fünf Zustände (S0…S4) mindestens drei Bits benötigen, mit drei Bits aber acht Zustände kodierbar sind, bleiben die Zustände S5, S6 und S7 unbenutzt — sie werden in der Zustandstabelle als **"Don't cares"** behandelt:

:::info
"Don't cares" sind Zustände, die im normalen Betrieb nie auftreten (hier, weil der Zähler nach S4 stets nach S0 zurückspringt und S5…S7 nie erreicht). Bei der Minimierung der Schaltfunktionen dürfen solche Felder im KV-Diagramm frei mit 0 oder 1 belegt werden — je nachdem, was die resultierende Gleichung am stärksten vereinfacht. Im 5:1-Beispiel ergeben sich dadurch die kompakten Gleichungen D₂ = Q₀ ∧ Q₁, D₁ = (Q̄₀ ∧ Q₁) ∨ (Q₀ ∧ Q̄₁) und D₀ = Q̄₀ ∧ Q̄₂ sowie für den Ausgang Z = Q₂ ∨ Q₁ — realisiert durch drei D-Flipflops und wenige vorgeschaltete Gatter.
:::

## Beispiel: Zähler mit Eingangssteuerung — der "Turboeingang"

Die State-Event-Technik stösst an ihre wahre Stärke, sobald **Eingangssignale** den weiteren Ablauf beeinflussen sollen — die Schaltung verhält sich dann nicht mehr starr nach demselben Muster, sondern reagiert auf äussere Bedingungen. Ein anschauliches Beispiel ist ein **2-Bit-Vorwärtszähler mit Turboeingang T**: Bei T = 0 zählt die Schaltung in Einerschritten (+1), bei T = 1 in Zweierschritten (+2).

:::merke
Im Zustandsdiagramm gehen von **jedem** Zustand nun **zwei** Pfeile aus — einer für T = 0, einer für T = 1 — und führen je nach Eingangswert zu unterschiedlichen Folgezuständen. Eine nützliche Kontrollregel beim Zeichnen lautet deshalb: *Bei einem Eingang müssen von jedem Zustand stets zwei Pfeile wegführen.* Aus der vollständigen Zustandstabelle (die nun zusätzlich den Eingang T als Spalte enthält) lassen sich wie gewohnt per KV-Diagramm die Gleichungen ableiten — hier ergeben sich D₁ = (Q₀ ∧ Q̄₁) ∨ (Q̄₀ ∧ T) ∨ (Q̄₀ ∧ Q₁ ∧ T̄) und D₀ = (Q₀ ∧ T) ∨ (Q̄₀ ∧ T̄), wobei sich D₀ als reine **EXNOR-Verknüpfung** von Q₀ und T erkennen lässt.
:::

So entsteht aus einer einfachen Anforderung — "zähle normal oder im Doppelschritt, je nach Steuersignal" — über das Zustandsdiagramm und die Zustandstabelle eine vollständig systematisch hergeleitete Schaltung, ganz ohne Rätselraten oder Try-and-Error.

## Bedeutung der FSM-Technik

Die State-Event-Technik ist damit weit mehr als nur eine Entwurfsmethode für Zähler und Frequenzteiler — sie ist das universelle Werkzeug, mit dem sich **jede** sequenzielle, getaktete Schaltung systematisch entwickeln lässt: Ampelsteuerungen, Bus-Protokolle, Steuerwerke von Prozessoren und unzählige weitere Anwendungen folgen demselben Schema aus Zustandsdiagramm, Zustandstabelle und daraus abgeleiteter Schaltungslogik. In der Praxis werden grössere FSMs heute kaum noch mit diskreten Flipflops aufgebaut, sondern direkt in → [[Programmierbare Logikbausteine (PROM, PAL, PLA)|programmierbare Logikbausteine]] oder per Hardwarebeschreibungssprache in → [[FPGA|FPGAs]] "gegossen" — das zugrundeliegende Entwurfsprinzip bleibt dabei jedoch exakt dasselbe.
