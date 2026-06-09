---
title: Resonanz & Schwingkreise
kategorie: ET
tags: [resonanz, schwingkreis, resonanzfrequenz, güte, bandbreite, serieschwingkreis, parallelschwingkreis, LC, RLC]
groessen: f_r|Resonanzfrequenz|Hz; Q|Güte|—; b|Bandbreite|Hz
_status: PORT+ERWEITERN  # ET_alt/Wechselstrom/Resonanz.md — Übersichtsartikel
---

:::hbox
:::vbox
**Voraussetzungen**
- [[RLC-Reihenschaltung (Serieschwingkreis)]]
- [[RLC-Parallelschaltung (Parallelschwingkreis)]]
:::
:::vbox
**Führt weiter zu**
- [[LC-Filter]]
- [[Quarz-Oszillator]]
- [[Filtercharakteristik]]
:::
:::

---

Bei der Resonanzfrequenz heben sich induktiver und kapazitiver Blindwiderstand gegenseitig auf. Die Schaltung verhält sich wie ein reiner Widerstand — Strom und Spannung sind in Phase. Dieses Verhalten wird für Filter, Oszillatoren und Antennenkreise genutzt.

## Resonanzbedingung

Im **Reihenschwingkreis** gilt bei Resonanz X_L = X_C — die induktive und kapazitive Reaktanz heben sich auf, die Impedanz sinkt auf das Minimum (Z = R).

Im **Parallelschwingkreis** gilt B_L = B_C — die Blindleitwerte heben sich auf, die Impedanz steigt auf das Maximum.

Die Resonanzfrequenz f_r hängt nur von L und C ab. Der Widerstand R beeinflusst nicht, **wo** die Resonanz liegt — sondern nur, wie **scharf** oder **breit** sie ist.

Alle Formeln (f_r, Z, Q, b) sind in den Detail-Artikeln: → [[RLC-Reihenschaltung (Serieschwingkreis)]] / [[RLC-Parallelschaltung (Parallelschwingkreis)]]

## Güte Q

Die Güte Q beschreibt, wie verlustarm ein Schwingkreis ist — und damit wie scharf die Resonanzspitze ausfällt. Der Verlustwiderstand steckt hauptsächlich im Wicklungswiderstand der Spule.

| Güte Q | Charakter | Typische Anwendung |
|---|---|---|
| Q > 10 | Scharf, selektiv | Antennenfilter, Quarz |
| Q = 1 … 10 | Mittel | Audio-Filter, LC-Filter |
| Q < 1 | Schwach — Q → 0 entspricht einem reinen Widerstand ohne Resonanz | Aperiodischer Grenzfall |

## Serieschwingkreis vs. Parallelschwingkreis

| Merkmal | Reihenschwingkreis | Parallelschwingkreis |
|---|---|---|
| Impedanz bei f_r | **Minimum** (Z = R) | **Maximum** |
| Strom bei f_r | Maximum | Minimum |
| Spannung an L und C | Überhöhung um Faktor Q | — |
| Kreuzstrom in L und C | — | Überhöhung um Faktor Q |
| Wirkung als Filter | Kurzschluss bei f_r (Serienresonanz sperrt Frequenzen ausserhalb) | Sperrung bei f_r (Parallelresonanz sperrt f_r) |

:::warning
Im Reihenschwingkreis kann die Spannung über Spule und Kondensator auf das **Q-fache der Eingangsspannung** steigen. Bei Q = 50 und 10 V Eingang entstehen 500 V über dem Kondensator — gefährlich für nicht entsprechend ausgelegte Bauteile.
:::

## Anwendungen

**Quarz-Oszillator**: Mechanisch schwingender Kristall mit sehr hoher Güte (Q bis 100 000). Stabile Frequenzreferenz in Mikrocontrollern und Uhren. → [[Quarz-Oszillator]]

**LC-Filter**: Steilere Flanken als RC-Filter, geeignet für höhere Frequenzen. → [[LC-Filter]]

**Antennenkreis**: Abstimmbarer LC-Kreis wählt gezielt eine Empfangsfrequenz aus.

**LLC-Wandler**: Schaltnetzteile nutzen Resonanz, um Verluste beim Schalten zu minimieren.
