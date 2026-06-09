---
title: Was ist ESD?
kategorie: FT
tags: [ESD, elektrostatische entladung, schutz, halbleiter, schäden, HBM, MOSFET, gate-oxid, latenter schaden, statisch, kV]
symbol: —
einheit: V
---

ESD (Electrostatic Discharge) ist die plötzliche Entladung statischer Elektrizität. Für den Menschen kaum spürbar, für Halbleiter oft tödlich.

:::hbox
:::vbox
**Voraussetzungen**
- [[Halbleiter Grundlagen]]
- [[Elektrisches Feld]]
:::
:::vbox
**Verwandte Artikel**
- [[Schutzmassnahmen ESD]]
:::
:::vbox
**Führt weiter zu**
- [[Schutzmassnahmen ESD]]
:::
:::

---

## Wie entsteht statische Aufladung?

Durch Reibung zweier Materialien trennen sich Ladungen. Kunststoff, Synthetik und trockene Luft laden besonders stark auf.

Ein Mensch kann sich auf mehrere tausend Volt aufladen, ohne es zu merken. Der Entladestrom beim Berühren fliesst in Nanosekunden.

## Warum sind Halbleiter empfindlich?

Dünne Oxidschichten in MOSFETs (Gate-Oxid) halten nur wenige Volt aus. Ein ESD-Impuls von ein paar hundert Volt zerstört die Schicht sofort. Der Schaden ist oft unsichtbar und zeigt sich erst im Betrieb als erhöhter Leckstrom oder Totalausfall.

## ESD-Empfindlichkeit

| Klasse | Empfindlichkeit |
|---|---|
| HBM Klasse 0 | unter 250 V |
| HBM Klasse 1 | 250 bis 500 V |
| HBM Klasse 2 | 500 bis 2000 V |
| HBM Klasse 3A | 2000 bis 4000 V |

HBM = Human Body Model (Modell für die Entladung durch einen Menschen).

## Heimtückisch: latente Schäden

ESD muss ein Bauteil nicht sofort zerstören. Latente Schäden schwächen es. Das Bauteil funktioniert zunächst, versagt aber nach einigen Stunden oder Wochen im Betrieb.

Das macht ESD-Schäden schwer zu diagnostizieren.

:::warning
ESD-Schäden sind in vielen Fällen nicht sichtbar. Ein vermeintlich funktionierendes Bauteil kann bereits beschädigt sein. Deshalb ESD-Schutz immer einhalten, auch wenn die Schaltung scheinbar noch funktioniert.
:::
