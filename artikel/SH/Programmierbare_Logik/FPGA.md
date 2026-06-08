---
title: FPGA (Field Programmable Gate Array)
kategorie: SH
kapitel: Programmierbare_Logik
tags: [fpga, field programmable gate array, cyclone, vhdl, verilog, hardwarebeschreibungssprache, logikzellen]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[CPLD (Complex Programmable Logic Device)]]
:::
:::vbox
**Verwandte Artikel**
- [[VHDL & Verilog]]
- [[Mikrocontroller]]
:::
:::

---

Skaliert man die Architektur eines → [[CPLD (Complex Programmable Logic Device)|CPLD]] noch einmal um Grössenordnungen nach oben — mehr Logikelemente, mehr Speicher, schnellere Schnittstellen, zusätzliche Spezialblöcke —, gelangt man zum **FPGA** (Field Programmable Gate Array): einem Baustein, der ein komplettes digitales System, von einfachen Verknüpfungsschaltungen bis hin zu vollständigen Mikrocontroller-Architekturen, in sich aufnehmen kann.

## Architektur am Beispiel des Cyclone IV von Altera

Das FPGA **Cyclone IV** von Altera lässt sich als "gehobener Mittelklassewagen" unter den FPGAs einordnen — seine Grundarchitektur gleicht im Kern jener eines MAX-II-CPLD, ist jedoch mit deutlich mehr Ressourcen und zusätzlichen Spezialfunktionen ausgestattet:

:::info
Der grösste Baustein der Cyclone-IV-Reihe vereint bis zu **150 000 Logikelemente** auf einem einzigen Chip und besitzt 780 Pins, von denen 475 frei konfigurierbar sind. Für sehr schnelle Schnittstellen stehen bis zu acht **Transceiver** mit bis zu 3,125 Gbit/s zur Verfügung; intern lassen sich bis zu 6,5 Mbit Speicher nutzen, organisiert in spezialisierten Speicherblöcken. Insgesamt bis zu vier **PLLs** (Phase Locked Loop) kompensieren Verzögerungszeiten zwischen verschiedenen Schaltungsteilen — ein wichtiger Faktor bei hochkomplexen, getakteten Systemen. Um sehr schnelle Rechenoperationen zu erreichen, sind ausserdem bis zu 360 fest verdrahtete **Hardware-Multiplizierer** integriert, sodass für rechenintensive Aufgaben — etwa in der digitalen Signalverarbeitung (DSP) — nicht auf "langsamere" Logikelemente zurückgegriffen werden muss.
:::

## FPGA oder Mikrocontroller?

Eine naheliegende Frage: Werden FPGAs in Zukunft klassische Mikrocontroller verdrängen? Die Antwort fällt differenziert aus:

:::merke
Da FPGAs deutlich teurer sind als Mikroprozessoren, werden sie den klassischen Mikrocontroller **nicht** verdrängen — sie haben jedoch ihre klare Berechtigung dort, wo sehr schnelle Hardwaresysteme gefragt sind, etwa bei schnellen digitalen Oszilloskopen oder Übertragungssystemen im Gigabit-Bereich. Ihr grosser Vorteil liegt zusätzlich in der hohen **Flexibilität bei Schaltungsänderungen** — eine Anpassung erfordert keinen neuen Chip, sondern lediglich eine neue Konfiguration. FPGAs bieten darüber hinaus die Möglichkeit, **ganze Mikrocontrollersysteme** direkt im Baustein zu implementieren — ein "massgeschneidertes" System, das exakt auf die Bedürfnisse des Anwenders zugeschnitten werden kann (Anzahl Ports, Schnittstellen, RAM-Grösse, Timer, Interrupts usw.).
:::

:::tip
Altera hat dafür das **NIOS-System** entwickelt — einen konfigurierbaren → [[Mikrocontroller|Mikrocontroller]] (NIOS-II-Prozessorkern), der vollständig in FPGAs implementiert werden kann. Seine Rechenleistung bewegt sich im Bereich von etwa 80 MHz/MIPS — vergleichbar mit klassischen Prozessorkernen wie dem ARM7. Ist in einem System ohnehin bereits ein FPGA vorhanden, kann dieses zugleich die Aufgabe eines externen Mikrocontrollers übernehmen; bei kleineren Systemen bleibt jedoch der Stromverbrauch eines dedizierten externen Prozessors meist geringer. Für erste Prototypen und flexible Entwicklungsplattformen sind FPGAs in jedem Fall hervorragend geeignet.
:::

Die Programmierung eines FPGA stellt hohe Anforderungen an Entwickler und Entwicklungssoftware:

:::warning
Da die Logik beim Konfigurieren auf viele verteilte Logikzellen "ausgelagert" wird, hängt die **Signallaufzeit** entscheidend davon ab, wie diese Zellen physisch angeordnet sind und welche Wegstrecken die Signale dabei zurücklegen müssen. Eine genaue Simulation ist deshalb unverzichtbar — die Entwicklungssoftware muss dafür mit den exakten Architekturdaten des verwendeten Bausteins "gefüttert" werden. Entworfen wird die gewünschte Logik dabei in der Regel nicht mehr schaltplanbasiert, sondern mit einer → [[VHDL & Verilog|Hardwarebeschreibungssprache]] wie VHDL oder Verilog, aus der die Entwicklungssoftware automatisch die passende Konfiguration für die Logikzellen ableitet.
:::

## Logik mit Multiplexern statt Look-up-Tables

Nicht alle FPGA-Familien setzen auf die LUT-Architektur — manche realisieren ihre Logikfunktionen stattdessen mit kaskadierten **Multiplexern**:

:::merke
Ein einfacher 2:1-Multiplexer mit Steuereingang C realisiert die Funktion Z = (C ∧ A) ∨ (C̄ ∧ B): Bei C = 0 wird der Eingang B durchgeschaltet, bei C = 1 der Eingang A. Verschaltet man mehrere solcher Multiplexer hintereinander — wobei einzelne Eingänge fest auf 0 oder 1 gelegt oder mit weiteren Variablen belegt werden —, lassen sich beliebig komplexe logische Verknüpfungen aufbauen, etwa eine vierstellige Funktion der Form Z = (A ∧ C) ∨ (A ∧ C̄ ∧ D) ∨ (A ∧ B ∧ C̄ ∧ D̄) ∨ (Ā ∧ C̄ ∧ D̄). Dieses Vorgehen ist eng verwandt mit der Funktionsweise des → [[Multiplexer (MUX)|Multiplexers]] als universellem, "programmierbarem" Logikbaustein — nur eben in stark miniaturisierter, massenhaft wiederholter Form direkt auf dem Chip.
:::

Damit schliesst sich der Kreis der programmierbaren Logikfamilien: vom einfachen → [[Programmierbare Logikbausteine (PROM, PAL, PLA)|PROM]] über → [[GAL (Generic Array Logic)|GAL]] und → [[CPLD (Complex Programmable Logic Device)|CPLD]] bis zum FPGA — überall begegnen einem dieselben Grundprinzipien (programmierbare Verknüpfungsfelder, Look-up-Tables, Multiplexer-Logik, konfigurierbare Register), lediglich in immer grösserem Massstab und mit immer leistungsfähigeren Werkzeugen umgesetzt.
