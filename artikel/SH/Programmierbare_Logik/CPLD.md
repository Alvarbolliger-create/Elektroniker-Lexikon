---
title: CPLD (Complex Programmable Logic Device)
kategorie: SH
kapitel: Programmierbare_Logik
tags: [cpld, logic array block, lab, logic element, le, input output element, ioe, maxii]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[GAL (Generic Array Logic)]]
:::
:::vbox
**Führt weiter zu**
- [[FPGA (Field Programmable Gate Array)]]
:::
:::

---

Ein einzelnes → [[GAL (Generic Array Logic)|GAL]] stösst bei umfangreicheren Schaltungen schnell an seine Grenzen — zu wenige Ein-/Ausgänge, zu wenig Logikkapazität für ein komplettes Steuerwerk oder einen Mikrocontroller-Zusatzbaustein. Die naheliegende Idee: **mehrere** GAL-ähnliche Logikblöcke auf einem einzigen Chip zusammenzufassen und über ein internes Verbindungsnetz miteinander zu koppeln. Genau das leistet das **CPLD** (Complex Programmable Logic Device).

## Ältere CPLDs: viele GAL-Strukturen, verbunden durch eine PIM

Frühe CPLD-Generationen orientierten sich noch eng an der GAL-Architektur:

:::merke
Ein älteres CPLD ist aus mehreren **Logikblöcken** zusammengesetzt, von denen jeder ungefähr einem GAL22V10 entspricht. Diese Logikblöcke sind über ein zentrales Verknüpfungsnetz verbunden, die sogenannte **PIM** (Programmable Interconnect Matrix). Da jeder einzelne Logikblock bereits Tausende von Sicherungen besitzt, steigt die Gesamtzahl der zu programmierenden Verbindungen bei grossen CPLDs drastisch an — beim GAL16V8 sind es etwa 2200, beim GAL22V10 bereits rund 5800. Ein Vorteil dieser Architektur: Da Aufbau und Verbindungsstruktur genau bekannt sind, lassen sich die Signallaufzeiten exakt vorhersagen. Nachteilig wirkt sich hingegen der vergleichsweise hohe Stromverbrauch aus.
:::

Mit wachsender Chipgrösse wurde der Aufwand für das Chipdesign GAL-basierter CPLDs jedoch zu hoch. Der Firma Altera gelang der Durchbruch, indem sie CPLDs auf Basis flexibler **Logikelemente**, eines geschickten internen Verbindungssystems (Interconnect) und sogenannter **Look-up-Tables** (LUT) entwickelte — eine Technologie, die ursprünglich aus der → [[FPGA (Field Programmable Gate Array)|FPGA]]-Welt stammt. Damit hat die FPGA-Technologie auch in moderne CPLDs Einzug gehalten, wobei Altera bei diesen Bausteinen die Signallaufzeiten weiterhin exakt definieren kann.

## Architektur am Beispiel des Altera MAX II (MAXII EPM2210F324C3)

Ein typischer Vertreter dieser modernen CPLD-Generation ist der Baustein **MAXII EPM2210F324C3**: Von seinen 324 Pins stehen dem Anwender 272 als frei nutzbare I/Os zur Verfügung. Der Chip enthält 2210 Logikelemente sowie einen integrierten Flash-Speicher — ein Teil davon (CFM, Configuration Flash Memory) speichert das Konfigurations-"Programm", die übrigen 8 kBit (UFM, User Flash Memory) stehen dem Anwender als nichtflüchtiger Datenspeicher zur Verfügung, sodass auf ein separates externes Flash-Bauteil verzichtet werden kann. Die maximale diagonale Laufzeit über den ganzen Chip beträgt für kombinatorische Logik rund 7 ns.

:::tip
Die MAX-II-Familie zeichnet sich besonders durch drei Eigenschaften aus, die für CPLDs in Steuerungsanwendungen prädestinieren: **Instant-on** (sofort nach dem Einschalten betriebsbereit, ohne Konfigurationsladevorgang), **nichtflüchtige Speicherung** der Konfiguration sowie **Wiederprogrammierbarkeit**. Damit eignen sich diese Bausteine ideal für typische Steuerungsaufgaben wie das zeitlich versetzte Aufschalten mehrerer Versorgungsspannungen (Sequencing), die Konfiguration und Initialisierung anderer Bausteine (z. B. von FPGAs), I/O-Erweiterungen für Mikrocontroller oder das "Bridging" zwischen unterschiedlichen Schnittstellen.
:::

## Innerer Aufbau: LABs, Logic Elements und IOEs

Die MAX-II-Architektur ist matrixförmig aus mehreren Hauptbausteinen aufgebaut:

:::info
Ein **Logic Array Block (LAB)** fasst jeweils zehn **Logic Elements (LE)** zusammen und besitzt zusätzlich ein lokales Verbindungssystem (Local Interconnect), über das sich die LEs innerhalb desselben LAB verbinden lassen. Über die sogenannte **DirectLink-Connection** kann jedes LAB zudem direkt auf das lokale Netzwerk eines benachbarten LAB zugreifen — das beschleunigt häufige, kurze Verbindungen erheblich und entlastet das globale **MultiTrack-Interconnect-System** (Row-/Column-Interconnect), über das auch räumlich entfernte LABs — mit etwas grösserer Laufzeit — miteinander gekoppelt werden können. An allen vier Seiten des Bausteins sitzen ausserdem **Input-Output-Elements (IOE)**, über die sich jeder einzelne Pin individuell als Eingang, Ausgang, Tristate, bidirektional oder mit Schmitt-Trigger konfigurieren lässt.
:::

Das **Logic Element (LE)** bildet die kleinste Logikeinheit dieser Architektur:

:::merke
Jedes LE enthält eine **Look-up-Table (LUT)** mit vier Eingängen — eine LUT ist im Kern nichts anderes als ein statisches 16 × 1-Bit-RAM, in dem die komplette Wahrheitstabelle einer vierstelligen Logikfunktion direkt abgelegt wird (dasselbe Grundprinzip wie beim → [[Programmierbare Logikbausteine (PROM, PAL, PLA)|PROM]] — nur in winzigem Massstab und massenhaft auf dem Chip verteilt). Über einen **Register-Bypass** kann das im LE enthaltene, "universelle" Flipflop (konfigurierbar als D-, T-, JK- oder RS-Typ) bei rein kombinatorischer Logik umgangen werden. LUT und Flipflop verfügen über getrennte Ausgänge — ein LE kann also gleichzeitig zwei voneinander unabhängige Aufgaben lösen. Für grössere kombinatorische Funktionen (z. B. mit acht Eingängen) lassen sich mehrere LUTs kaskadieren: Ein zusätzlicher → [[Multiplexer (MUX)|Multiplexer]], gesteuert durch das höchstwertige Eingangsbit, wählt dabei zwischen den Ausgängen zweier LUTs mit je zwei "echten" Eingängen.
:::

Die Aufgabe, all diese Verbindungen korrekt zu setzen, übernimmt eine spezialisierte Entwicklungssoftware (bei Altera: Quartus) — sie konfiguriert die einzelnen LEs und verbindet sie über die Interconnect-Systeme so, dass am Ende exakt die gewünschte Schaltung entsteht.

Damit sind CPLDs faktisch "Mini-FPGAs mit garantierten Laufzeiten" — der nächste, konsequente Schritt in derselben Technologielinie ist das vollwertige → [[FPGA (Field Programmable Gate Array)|FPGA]], das dieselben Grundbausteine in noch deutlich grösserem Massstab vereint.
