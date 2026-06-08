---
title: GAL (Generic Array Logic)
kategorie: SH
kapitel: Programmierbare_Logik
tags: [gal, generic array logic, olmc, output macro logic cell, gal16v8, gal22v10, programmierung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Programmierbare Logikbausteine (PROM, PAL, PLA)]]
:::
:::vbox
**Führt weiter zu**
- [[CPLD (Complex Programmable Logic Device)]]
:::
:::

---

→ [[Programmierbare Logikbausteine (PROM, PAL, PLA)|PROM, PAL und PLA]] teilen einen entscheidenden Schwachpunkt: Sie basieren auf einmalig durchtrennbaren **Sicherungen** (Fuse-Technologie) — ein Programmierfehler bedeutet den Verlust des gesamten Bausteins. Gerade in der Entwicklungsphase, in der eine Schaltung oft mehrfach angepasst werden muss, führt das zu einem hohen "Verbrauch" an Bausteinen. Der Firma Lattice gelang es, die aus EEPROMs bekannte CMOS-Technik auch auf programmierbare Logikbausteine zu übertragen — es entstand das **GAL** (Generic Array Logic): elektrisch löschbare und beliebig oft neu programmierbare Bausteine.

## Konfigurierbare Ausgänge als Schlüssel zur Flexibilität

Die enorme Vielseitigkeit des GAL beruht auf seinen **konfigurierbaren Ausgängen**:

:::merke
Die Architektur eines GAL gleicht im Kern jener eines PAL: ein programmierbares UND-Feld, gefolgt von einem fest verdrahteten ODER-Feld. Der entscheidende Unterschied liegt jedoch an den Ausgängen — diese können wahlweise als reine Logikeingänge, als kombinatorische Logikausgänge, als Tristate-Ausgänge oder als getaktete Register (→ [[Flipflops (SR, D, JK, T)|D-Flipflops]]) geschaltet werden. Diese Konfiguration übernimmt eine spezielle Schaltung an jedem Ausgangspin: die **OLMC** (Output Logic Macro Cell).
:::

## Die fünf Betriebsarten der OLMC

Beim klassischen GAL16V8 sind 64 UND-Terme in acht Gruppen zu je acht Termen zusammengefasst und auf je eine OLMC geführt. Über spezifische, von der Entwicklungssoftware gesetzte **Steuerbits** lässt sich jede OLMC in eine von fünf grundlegenden Betriebsarten versetzen:

| Konfiguration | Funktionsweise |
|---|---|
| **Input** | Der Enable-Eingang des Treibers liegt dauerhaft auf Low — der gesamte Schaltungsteil bleibt hochohmig "abgekoppelt", der Pin wirkt nur als Eingang (Small-PAL-Mode) |
| **Output** (kombinatorisch) | Der Treiber ist permanent aktiv (Enable = High); alle acht UND-Terme sind auf das ODER-Gatter geführt; ein Steuerbit am XOR legt fest, ob das Ergebnis invertiert ausgegeben wird (steuerbarer Inverter) |
| **I/O** | Ein UND-Term steuert den Enable-Eingang des Treibers selbst — je nach dessen Ergebnis arbeitet der Pin als Eingang oder als kombinatorischer Ausgang; die übrigen sieben Terme bilden die eigentliche Logik |
| **Register** | Alle acht UND-Terme speisen ein → [[Flipflops (SR, D, JK, T)|D-Flipflop]], dessen Ausgang den Pin treibt — geeignet für sequenzielle Logik; der Q̄-Ausgang wird zusätzlich ins UND-Feld zurückgeführt, sodass auch rückgekoppelte Schaltungen (Zähler, Schieberegister) realisierbar sind |
| **Tristate** | Ein einzelner UND-Term schaltet den kombinatorischen Ausgang gezielt in den hochohmigen Zustand — die übrigen sieben Terme stehen für die disjunktive Form der Logik zur Verfügung |

:::tip
Bei der **Register**-Konfiguration ist zu beachten, dass der Takt der Logik gleichzeitig auf **alle** OLMCs des Bausteins geführt wird — beim GAL16V8 lässt sich daher nur sequenzielle Logik mit einem **gemeinsamen** Taktsignal realisieren. Das Output-Enable-Signal (OE) wirkt ebenfalls auf alle Register-Ausgänge gemeinsam und erlaubt es, sie — etwa für Buskopplungen — gemeinsam in den Tristate-Zustand zu versetzen.
:::

## Programmierung: Steuerbits an festen Speicherplätzen

Die Konfiguration eines GAL erfolgt durch das Setzen lokaler und globaler Steuerbits an klar definierten Positionen der internen Verknüpfungsmatrix:

:::info
Beim GAL16V8 besteht die UND-Matrix aus 64 Zeilen mit je 32 Spalten — die 2048 Kreuzungspunkte tragen je ein Steuerbit (Bits 0…2047). Anschliessend folgen die acht frei wählbaren **XOR(n)**-Bits (2048…2055, z. B. für Versionsnummer oder Herstellerdatum), die **lokalen** AC1(n)-Bits (2120…2127, "AC" steht für Architecture Control) sowie die PTD(n,i)-Bits (2128…2191). Das **globale** Bit **SYN** liegt auf Platz 2192, das globale Bit **AC0** auf Platz 2193. "Lokal" bedeutet dabei, dass ein Steuerbit nur für die zugehörige OLMC gilt; "global" bedeutet, dass es den ganzen Chip bzw. alle OLMCs gleichermassen betrifft.
:::

## Das GAL22V10: mehr Ein-/Ausgänge, differenziertere Steuerung

Eine leistungsfähigere Variante ist das **GAL22V10**:

:::merke
Das GAL22V10 verfügt über mehr Ein- und Ausgänge als das GAL16V8. Zudem besitzt nicht jede OLMC die gleiche Anzahl UND-Terme — sie schwankt zwischen 8 und 16, womit sich auch komplexere logische Verknüpfungen lösen lassen. Der Takteingang wird in die Verknüpfungsmatrix zurückgeführt und steht dort selbst zur Bildung logischer Verknüpfungen zur Verfügung. Auch die Steuerung der Tristate-Ausgänge ist differenzierter: Im Gegensatz zum GAL16V8 kann hier **jeder Ausgang einzeln** in den Tristate-Zustand versetzt werden. Zusätzlich existiert die Möglichkeit, alle Register gleichzeitig und unabhängig vom Takt auf "0" zu setzen (**asynchroner Reset**) bzw. auf die steigende Taktflanke gemeinsam auf "1" zu setzen (**synchroner Preset**).
:::

Mit dem GAL ist damit der entscheidende Schritt von der "Wegwerf"-Logik hin zu wiederverwendbaren, flexibel konfigurierbaren Bausteinen vollzogen. Der nächste logische Schritt — deutlich mehr Logikkapazität in einem einzigen Chip zu vereinen, indem man viele GAL-ähnliche Strukturen über ein internes Verbindungsnetz koppelt — führt zum → [[CPLD (Complex Programmable Logic Device)|CPLD]].
