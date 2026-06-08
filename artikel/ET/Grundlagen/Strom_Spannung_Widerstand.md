---
title: Strom, Spannung, Widerstand
kategorie: ET
tags: [strom, spannung, widerstand, ohm, leitwert, grundlagen, ohmsches gesetz, kennlinie, differenzieller widerstand, dynamischer widerstand, arbeitspunkt, diode]
groessen: U|Spannung|V; I|Strom|A; R|Widerstand|Ohm; G|Leitwert|S; Q|Ladung|C
_status: PORT  # ET_alt/Grundlagen/Strom_Spannung_Widerstand.md
---

:::hbox
:::vbox
**Verwandte Artikel**
- [[Diode]]
- [[Kirchhoffsche Gesetze]]
- [[NTC & PTC]]
:::
:::vbox
**Führt weiter zu**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
- [[Elektrische Leistung]]
- [[Leiterwiderstand]]
:::
:::

---

Strom, Spannung und Widerstand sind die drei Grundgrössen der Elektrotechnik. Jede Schaltungsanalyse beginnt hier — wer diese drei versteht, kann jede Gleichstromschaltung lösen.

## Spannung

Spannung ist der Unterschied im elektrischen Potenzial zwischen zwei Punkten. Sie ist die Ursache für Stromfluss: Ohne Spannungsdifferenz kein Strom. Man misst Spannung immer zwischen zwei Punkten — eine einzelne Leitung hat keine Spannung, nur ein Potenzial.

**Einheit:** Volt (V), benannt nach Alessandro Volta.

Beispiele: Batterie 1,5 V, USB 5 V, Schweizer Netz 230 V, Auto-Bordnetz 12 V.

## Strom

Strom ist der gerichtete Fluss elektrischer Ladungsträger. In Metallen sind das Elektronen, die sich von − nach + bewegen. Die **technische Stromrichtung** ist jedoch von + nach −, entgegen dem Elektronenfluss — eine historische Konvention aus der Zeit vor der Elektronenentdeckung.

:::formel
I = Q / t    # Strom I (A) = Ladung Q (C) geteilt durch Zeit t (s)
:::

**Einheit:** Ampere (A). 1 A = 1 C/s, also 1 Coulomb Ladung pro Sekunde.

## Wirkungen des Stroms

Elektrischer Strom hat vier grundlegende Wirkungen, die technisch genutzt werden:

| Wirkung | Erklärung | Anwendung |
|---|---|---|
| Wärmewirkung | I² · R → Wärme | Heizung, Glühlampe, Sicherung |
| Magnetische Wirkung | Strom erzeugt Magnetfeld | Motor, Relais, Elektromagnet |
| Lichtwirkung | Elektronen regen Atome zur Lichtemission an | LED, Leuchtstofflampe |
| Chemische Wirkung | Ionen werden an Elektroden abgeschieden | Elektrolyse, Akkumulator |

:::warning
**Physiologische Wirkung**: Strom durch den menschlichen Körper kann Muskelkrämpfe, Herzflimmern und Tod verursachen. Bereits 10 mA können den Muskel verkrampfen ("loslassen" nicht mehr möglich), ab 30–80 mA droht Herzflimmern. → [[Gefahren des Stroms]]
:::

## Ohmsches Gesetz

Für einen **ohmschen** (linearen) Leiter ist der Widerstand R konstant — er hängt nicht von Spannung oder Strom ab. Das Gesetz gilt für metallische Widerstände bei konstanter Temperatur.

:::formel
U = R * I
:::

| Gesucht | Formel | Anwendung |
|---|---|---|
| Spannung U | U = R · I | Spannungsfall berechnen |
| Strom I | I = U / R | Strom im Kreis |
| Widerstand R | R = U / I | Messung am Bauteil |

Das CAS kann die Formel automatisch nach jeder Grösse umformen — nur eine Form merken reicht.

:::tip
**Eselsbrücke URIner**: U oben, R und I unten nebeneinander. Daumen auf die gesuchte Grösse → die restlichen zwei zeigen die Rechenoperation.
:::

## Leitwert

Der Leitwert G ist der Kehrwert des Widerstands. Er gibt an, wie gut ein Leiter den Strom durchlässt. Bei Parallelschaltungen addieren sich die Leitwerte direkt — das ist oft einfacher als mit Widerständen zu rechnen.

:::formel
G = 1 / R
:::

**Einheit:** Siemens (S). Ein Widerstand von 10 Ω hat den Leitwert 0,1 S.

## Differenzieller Widerstand

Das ohmsche Gesetz gilt nur für **lineare Bauteile**. Bei nichtlinearen Bauteilen wie Dioden, Glühlampen oder Varistoren ändert sich der Widerstand mit dem Betriebspunkt. Aus der U-I-Kennlinie lässt sich an jedem Punkt eine Steigung ablesen — das ist der **differenzielle (dynamische) Widerstand** r_dif:

:::formel
r_dif = delta_U / delta_I    # Steigung der Kennlinie am Arbeitspunkt
:::

:::schematic
/abbildungen/grundlagen/differenzieller_widerstand.svg
:::

Im Gegensatz dazu ist R = U/I der **statische Widerstand** — der Quotient der absoluten Werte. Beide sind nur am linearen Bauteil gleich. Bei einer Diode im Durchlassbetrieb ist der statische Widerstand (z. B. 0,7 V / 20 mA = 35 Ω) viel grösser als der differenzielle Widerstand (wenige Ohm), der angibt, wie stark der Strom auf eine kleine Spannungsänderung reagiert.

| Bauteil | Verhalten |
|---|---|
| Metallwiderstand (Raumtemperatur) | R konstant → ohmsches Gesetz gilt |
| Glühlampe | R steigt stark mit Temperatur |
| Diode | R sehr klein in Durchlassrichtung, sehr gross in Sperrrichtung |
| Varistor (VDR) | R sinkt bei hoher Spannung → Überspannungsschutz |
| NTC/PTC | R temperaturabhängig → [[NTC & PTC]] |

:::warning
Einen nichtlinearen Widerstand einfach als R = U/I zu behandeln ist nur für den jeweiligen Betriebspunkt gültig. Für andere Spannungen gilt dieser Wert nicht mehr.
:::
