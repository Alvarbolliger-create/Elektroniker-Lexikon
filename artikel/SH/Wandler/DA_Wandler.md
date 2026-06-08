---
title: DA-Wandler (Digital-Analog-Umsetzer)
kategorie: SH
kapitel: Wandler
tags: [da-wandler, digital-analog-umsetzer, teilstroeme, addierer, bipolarer ausgang, genauigkeit]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)]]
- [[OPV Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[R-2R-Netzwerk]]
- [[DA-Wandlung mit PWM]]
:::
:::

---

So unverzichtbar der Weg von analog zu digital ist — am Ende soll ein digitales System fast immer auch wieder mit der analogen Aussenwelt kommunizieren: ein Lautsprecher, ein Motor, eine Anzeige. Genau diesen Rückweg übernimmt der **DA-Wandler (Digital-Analog-Umsetzer)**: Er bildet eine digitale Zahl Z — meist 8, 10, 12 oder mehr Bit breit — auf eine proportionale analoge Ausgangsspannung U_a ab, dargestellt durch das DIN-Normsymbol "#/∩".

## Das Grundprinzip: gewichtete Teilströme addieren

:::merke
Eine naheliegende Idee: Man bildet für jedes Bit der digitalen Zahl einen eigenen Strompfad mit einem eigens dimensionierten Widerstand und addiert die resultierenden Teilströme zu einem Gesamtstrom auf. Damit dieser Gesamtstrom die digitale Zahl korrekt widerspiegelt, müssen die Widerstände — ganz im Sinne der → [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)|binären Wertigkeiten]] — gestaffelt sein: 2R, 4R, 8R, 16R für die Bits z₃ bis z₀. Der Strom im Pfad mit 2R trägt damit die Wertigkeit 8, jener mit 4R die Wertigkeit 4, mit 8R die Wertigkeit 2 und mit 16R die Wertigkeit 1 — exakt das Muster des Binärsystems, bei dem sich der Stellenwert mit jeder Position nach links verdoppelt.
:::

## Der Addierer: ein Operationsverstärker als Summierer

Geschaltet werden die digital gesteuerten Schalter z₃ … z₀ durch das Eingangssignal selbst — jeder geschlossene Schalter speist seinen Teilstrom in den gemeinsamen Summenpunkt ein. Ein als **Addierer** beschalteter Operationsverstärker (→ [[OPV Grundlagen|Grundschaltung Invertierender Verstärker]]) summiert diese Teilströme und wandelt die Summe über seinen Rückkopplungswiderstand R_FB = R in eine proportionale Ausgangsspannung um:

:::formel
U_a = −U_Ref · Z / (Z_max + 1)
:::

:::tip
Für einen 4-Bit-DA-Wandler mit U_Ref = 5,000 V ergibt sich daraus eine exakt lineare Treppenfunktion: Z = 0000 liefert U_a = 0,0000 V, Z = 0001 liefert U_a = −0,3125 V, bis hin zu Z = 1111 mit U_a = −4,6875 V — in 16 gleich grossen Stufen von je U_LSB = U_Ref / 16 = 0,3125 V. Zählt man die Eingangszahl im Takt von 0000 bis 1111 hoch, entsteht am Ausgang exakt jene charakteristische **Treppenkurve**, die — verglichen mit dem geraden Idealverlauf eines DA-Wandlers mit unendlich feiner Auflösung — die grundsätzliche Quantisierungsgrenze jedes realen Wandlers sichtbar macht.
:::

## Vor- und Nachteile dieser einfachen Lösung

Der direkte Aufbau mit gewichteten Widerständen überzeugt durch seine **Einfachheit** — die Funktionsweise lässt sich unmittelbar aus dem Schaltbild ablesen. Dem stehen jedoch handfeste praktische Probleme gegenüber:

:::warning
Diese Schaltung benötigt für jedes Bit einen **eigenen Widerstandswert** — bei einem 12-Bit-Wandler also zwölf unterschiedliche, jeweils äusserst präzise zu fertigende Widerstände. Schon kleinste Fertigungstoleranzen schlagen sich direkt in **Linearitätsfehlern** nieder. Hinzu kommt: Die Referenzspannungsquelle wird von den verschiedenen Pfaden **ungleichmässig belastet** — je nachdem, wie viele und welche Schalter gerade geschlossen sind, fliesst ein unterschiedlich grosser Gesamtstrom aus ihr ab, was wiederum die Linearität beeinträchtigt. Eine verbesserte Variante mit **Wechselschaltern** — die jeden Pfad permanent entweder zur Referenzspannung oder zur virtuellen Masse des OPs führen — behebt zumindest dieses zweite Problem: Die Referenzquelle wird nun unabhängig vom Zahlenwert stets gleichmässig belastet.
:::

## DA-Wandler mit bipolarem Ausgang

Viele Anwendungen — etwa Audiosignale — benötigen nicht nur positive, sondern auch negative Ausgangsspannungen. Eine zusätzliche Schaltungsstufe macht das möglich:

:::info
Ein zweiter Operationsverstärker (OV2), als invertierender Addierer beschaltet, addiert zur Spannung U₁ des eigentlichen DA-Umsetzers eine konstante Offsetspannung von der halben Referenzspannung hinzu. Daraus ergibt sich die Formel U_a = U_Ref · Z/(Z_max+1) − ½ · U_Ref. Bei einem 8-Bit-Wandler mit bipolarem Ausgang und U_Ref = 5 V liefert der Code 1111 1111 dann U_a = +2,48 V, der Code 1000 0000 genau U_a = 0,00 V (die "Mitte" des Bereichs) und der Code 0000 0000 schliesslich U_a = −2,50 V — der gesamte Wertebereich ist so symmetrisch um den Nullpunkt verteilt und deckt −128 ≤ Z ≤ +127 ab.
:::

## Genauigkeit: wo die Grenzen liegen

Wie schon beim → [[AD-Wandler — Auflösung & Fehler|AD-Wandler]] entstehen auch beim DA-Wandler unvermeidliche Fehler: Ein **Nullpunktfehler** entsteht durch kleine Sperrströme, die selbst bei geöffneten Schaltern fliessen und vom Addierer mit aufsummiert werden; ein **Vollausschlagfehler** rührt daher, dass auch geschlossene Schalter und der Rückkopplungswiderstand nicht exakt ideal sind. Beide Fehler lassen sich weitgehend abgleichen. Die **Nichtlinearität** dagegen — typischerweise auf ±½ LSB begrenzt — lässt sich grundsätzlich nicht korrigieren: Ist nur das höchstwertige Bit gesetzt, fliesst der Strom über genau einen Schalter; senkt man den Wert um eins ab, müssen alle niedrigeren Schalter zusammen exakt den gleichen Strom liefern — gelingt das nicht perfekt, "springt" die Ausgangsspannung an dieser Stelle.

Damit ist klar, *wie* aus einer Zahl ein gewichteter Strom und daraus eine Spannung wird — doch das Problem der ungleich belasteten Referenzquelle und der vielen unterschiedlichen Präzisionswiderstände bleibt. Eine clevere Schaltungsidee löst beide Probleme auf einen Schlag: das → [[R-2R-Netzwerk|R-2R-Netzwerk]].
