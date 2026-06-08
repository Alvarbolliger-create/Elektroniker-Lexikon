---
title: Halbleiterspeicher (RAM, ROM)
kategorie: SH
kapitel: Prozessor
tags: [ram, rom, sram, dram, prom, eprom, eeprom, matrixorganisation, speicherzelle, read-zyklus, write-zyklus]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Speicherarten (Übersicht)]]
:::
:::vbox
**Verwandte Artikel**
- [[Programmierbare Logikbausteine (PROM, PAL, PLA)]]
:::
:::

---

→ [[Speicherarten (Übersicht)|RAM und ROM]] unterscheiden sich nicht nur in ihrem äusseren Verhalten — flüchtig oder nichtflüchtig, beschreibbar oder nur lesbar —, sondern vor allem in ihrem **inneren Aufbau**. Wie Tausende einzelner Speicherzellen zu einem adressierbaren Baustein verschaltet werden und wie eine einzelne Zelle überhaupt eine "1" oder "0" festhält, zeigt sich erst beim Blick ins Innere des Chips.

## Matrixorganisation: eine Adresse, eine Zelle

Aus technologischen Gründen werden Speicherzellen nicht linear hintereinander, sondern in einer quadratischen **Matrix** angeordnet:

:::merke
Die anliegende Adresse wird in zwei Hälften zerlegt: Ein **Zeilen-Decoder** wertet die höherwertigen Adressbits aus und aktiviert genau eine Zeilenleitung (y₀ … y₃), ein **Spalten-Decoder** wertet die niederwertigen Adressbits aus und aktiviert genau eine Spaltenleitung (x₁ … x₄). Nur an der Kreuzung dieser beiden aktiven Leitungen liegt ein UND-Gatter, das genau **eine** Speicherzelle freischaltet — alle anderen Zellen bleiben unberührt. Mit vier Adressleitungen (zwei für Zeilen, zwei für Spalten) lassen sich so 16 Speicherzellen eindeutig adressieren. Stapelt man mehrere solcher "Speicherebenen" übereinander, lassen sich unter derselben Adresse gleich mehrere Bits gemeinsam ablegen — ein 16-Bit-RAM benötigt entsprechend 16 parallel angesteuerte Speichermatrizen.
:::

## Die Speicherzelle des SRAM: ein verstecktes Flipflop

Im Innersten jeder SRAM-Zelle steckt ein bekanntes Bauelement:

:::info
Eine 1-Bit-Speicherzelle eines statischen RAM besteht im Kern aus einem → [[Flipflops (SR, D, JK, T)|D-Flipflop]] — ergänzt durch zwei UND-Gatter, die den Zugriff steuern: Gatter G1 lässt nur dann Daten in die Zelle hineinschreiben (`d_in` → D-Eingang), wenn die Adressbedingung x_i = y_i = 1 **und** das Write-Enable-Signal `we` aktiv sind; Gatter G2 schaltet den Zellinhalt nur dann auf den (über Open-Collector realisierten) Datenausgang `D̄_out`, wenn die Adressbedingung erfüllt ist. Ist das Chip-Select-Signal des Bausteins nicht aktiv, können die Decoder die Leitungen x_i und y_i gar nicht erst freischalten — der Open-Collector-Ausgang bleibt gesperrt, die Zelle ist "unsichtbar". Für eine 1-Bit-Zelle eines statischen CMOS-RAM braucht es so insgesamt **sechs Transistoren** — ein 32K×8-RAM mit 262'144 Speicherzellen kommt damit auf rund 1,57 Millionen Transistoren auf einem einzigen Chip.
:::

## Die Speicherzelle des DRAM: ein Kondensator statt sechs Transistoren

Das **dynamische RAM** geht einen radikal anderen Weg:

:::merke
Eine 1-Bit-Zelle eines dynamischen RAM besteht nur aus **einem FET und einem Kondensator**. Ein geladener Kondensator entspricht einer logischen "1", ein entladener einer logischen "0". Dieser drastisch vereinfachte Aufbau erlaubt eine viel höhere Integrationsdichte als beim SRAM — dynamische RAMs sind heute mit Kapazitäten bis zu 32 GBit erhältlich, Tendenz weiter steigend. Der Haken dabei: Kondensatoren verlieren mit der Zeit durch Leckströme ihre Ladung — und damit die gespeicherte Information. Eine zusätzliche Hardware, der **Refresh-Controller**, muss deshalb regelmässig sämtliche Speicherzellen "auffrischen", damit die Daten erhalten bleiben.
:::

| | Speicherkapazität | Zugriffszeit | Betriebsleistung | Hardware |
|---|---|---|---|---|
| **Statisches RAM** | bis > 16 MB | ca. 0,5–100 ns | 50–5000 mW | komplexe Zelle, sechs Transistoren |
| **Dynamisches RAM** | bis > 32 GB | ca. 15–100 ns | 50–500 mW | einfache Zelle, benötigt Refresh-Controller |

Statisches RAM punktet also mit kürzerer Zugriffszeit (der Zeitspanne zwischen dem Anlegen der Adresse und dem Bereitstehen der Daten am Ausgang), dynamisches RAM mit deutlich höherer Integrationsdichte. Eine Sonderform ist das **Zero-Power-RAM**: ein statisches RAM mit eingebauter Batterie, das so — trotz seiner an sich flüchtigen Natur — auch bei Spannungsausfall seine Daten über rund zehn Jahre bewahrt.

## Lese- und Schreibzyklus: zeitlich exakt spezifiziert

Damit ein RAM-Baustein korrekt arbeitet, müssen Adress-, Chip-Select-, Output-Enable- und Write-Enable-Signale exakt definierte zeitliche Abläufe einhalten — ein Datenblatt-Auszug zeigt das eindrücklich:

:::tip
Beim **Lesezyklus (Read-Cycle)** muss zuerst die Adresse stabil anliegen, bevor CS̄ aktiviert wird; erst danach darf OE̅ (Output Enable) aktiv werden — die Daten erscheinen dann nach der spezifizierten Zugriffszeit (z. B. 70–150 ns) am Ausgang, vorher und nachher bleibt der Ausgang hochohmig (High Impedance). Beim **Schreibzyklus (Write-Cycle)** ist die Reihenfolge ähnlich streng geregelt: CS̄ und WE̅ müssen für eine Mindestzeit (Write Pulse Width) aktiv bleiben, während die Daten am Eingang stabil anliegen (Data Valid to End of Write); erst danach dürfen sie sich wieder ändern (Data Hold Time). Werden diese Zeiten nicht eingehalten, kann der Baustein falsche oder undefinierte Werte liefern oder abspeichern — ein häufiger Grund für rätselhafte "Geisterfehler" in selbst entworfenen Schaltungen.
:::

## ROM: Speicherzellen mit "durchgebrannten" Sicherungen

Der innere Aufbau eines **PROM** (Programmable ROM) ähnelt dem RAM stark — Matrixorganisation, Zeilen- und Spaltendecoder —, doch an die Stelle des D-Flipflops tritt eine **Sicherung**:

:::warning
Im Urzustand erzeugt jede adressierte Speicherzelle am Ausgang ihres NAND-Gatters eine "1" (durch einen Pull-up-Widerstand). Soll an dieser Stelle eine "0" gespeichert werden, wird die Sicherung am Ausgang des betreffenden NAND-Gatters gezielt **"durchgebrannt"**: Die Adresse der zu programmierenden Zelle wird angelegt, der zugehörige FET schaltet durch, und ein kräftiger, exakt vom Hersteller spezifizierter Stromimpuls auf der Leseleitung lässt die hauchdünne Metallisierungsbrücke schmelzen. Durchgebrannt → Ausgang bleibt dauerhaft auf "0"; nicht durchgebrannt → Ausgang bleibt auf "1". Dieser Vorgang ist **unumkehrbar** — ein einmal programmiertes PROM lässt sich nicht mehr löschen oder korrigieren. Die Programmierung erfordert spezielle Programmiergeräte, die exakte, dem jeweiligen Speichertyp angepasste Spannungs- und Zeitabläufe einhalten.
:::

## Die ROM-Familie: vom starren MROM zum flexiblen Flash

Aus dem Bedürfnis, diesen "Wegwerf"-Charakter zu überwinden, entstand eine ganze Familie von ROM-Varianten — jede mit eigenem Lösch- und Programmierverfahren:

:::info
**MROM** (Maskable ROM): Der Speicherinhalt wird vom Hersteller im letzten Fertigungsschritt mit einer spezifischen Metallisierungsmaske eingebracht — lohnt sich nur bei sehr grossen Stückzahlen (ab ca. 10'000 Stück) und dauert mehrere Monate; einmal hergestellt, lässt sich der Inhalt nie mehr ändern. **PROM**: vom Anwender selbst programmierbar (Schmelzsicherungen, siehe oben) — danach jedoch ebenfalls unveränderlich. **EPROM** (Erasable PROM): lässt sich mit ultraviolettem Licht löschen — eine rund 20-minütige UV-Bestrahlung durch das charakteristische Quarzfenster im Gehäuse setzt alle Zellen zurück, danach kann ein neues Programm "eingebrannt" werden; das Quarzfenster muss im Betrieb mit einem Aufkleber abgedeckt sein, da auch normales Raumlicht einen kleinen UV-Anteil enthält, der die Daten mit der Zeit löschen würde. **EEPROM** (Electrically Erasable PROM): lässt sich elektrisch löschen, ganz ohne UV-Licht oder externes Programmiergerät — direkt auf der Schaltung; dafür ist die Anzahl möglicher Schreibzyklen auf 10⁵ bis 10⁶ begrenzt, und Schreibzugriffe dauern mit Zugriffszeiten im Millisekundenbereich vergleichsweise lange.
:::

| | RAM | MROM | PROM | EPROM | EEPROM/Flash |
|---|---|---|---|---|---|
| **Schreibzyklen** | beliebig | 1 | 1 | ca. 100 | 10⁵ … 10⁶ |
| **Programmierzeit** | 0,5–100 ns | Monate | Minuten | Minuten | 250 µs |
| **Zugriffszeit** | 0,5–50 ns | ca. 100 ns | 10–100 ns | 10–100 ns | 15–100 ns |

Damit schliesst sich der Kreis: Vom flüchtigen, blitzschnellen RAM über das starre, einmalig programmierte PROM bis hin zu wiederbeschreibbaren EEPROM- und Flash-Speichern überspannt die Familie der Halbleiterspeicher das gesamte Spektrum zwischen "schnell, aber flüchtig" und "langsam, aber dauerhaft" — und liefert damit für jede Anforderung im → [[Aufbau eines Mikroprozessorsystems|Mikroprozessorsystem]] den passenden Baustein. Wie sich Wahrheitstabellen direkt als Speicherinhalt eines PROM "abspeichern" lassen und wie daraus die Familie der → [[Programmierbare Logikbausteine (PROM, PAL, PLA)|programmierbaren Logikbausteine]] entstand, vertieft den Bogen von der reinen Speicherung hin zur programmierbaren Logik.
