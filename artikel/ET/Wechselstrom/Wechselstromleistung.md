---
title: Wechselstromleistung
kategorie: ET
tags: [wirkleistung, blindleistung, scheinleistung, leistungsfaktor, cos phi, kompensation, leistungsdreieck]
groessen: P|Wirkleistung|W; Q_L|Blindleistung|var; S|Scheinleistung|VA; lambda|Leistungsfaktor|—; phi|Phasenwinkel|°; U|Spannung|V; I|Strom|A
_status: PORT+ZUSAMMENFASSEN  # ET_alt/Leistung/Wirkleistung.md, Blindleistung.md, Scheinleistung.md, Leistungsfaktor.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen & Effektivwert]]
- [[Impedanz]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektrische Leistung]]
:::
:::vbox
**Führt weiter zu**
- [[Blindleistungskompensation]]
:::
:::

---

Im Wechselstromkreis unterscheidet man drei Leistungsarten: **Wirkleistung** (wird verbraucht), **Blindleistung** (wird nur hin- und hertransportiert) und **Scheinleistung** (das Produkt aus Effektivwerten). Nur die Wirkleistung verrichtet nützliche Arbeit — Blindleistung belastet Leitungen und Transformatoren zusätzlich.

## Leistungsdreieck (S, P, Q)

Die drei Leistungsarten bilden ein rechtwinkliges Dreieck, analog zum Impedanzdreieck:

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Scheinleistung | S | VA | Produkt U·I (Effektivwerte) |
| Wirkleistung | P | W | Tatsächlich umgesetzte Leistung |
| Blindleistung | Q_L | var | Reaktiver Anteil (kapazitiv oder induktiv) |

:::formel
S = sqrt(P^2 + Q_L^2)
:::

## Wirkleistung

Die Wirkleistung ist der Anteil, der tatsächlich in Arbeit oder Wärme umgewandelt wird. Sie hängt vom Phasenwinkel phi zwischen Spannung und Strom ab.

:::formel
P = U * I * cos(phi)    # Wirkleistung
:::

Bei rein ohmscher Last (phi = 0°): P = U·I (alles ist Wirkleistung).
Bei rein induktiver oder kapazitiver Last (phi = 90°): P = 0 (keine Wirkleistung).

## Blindleistung

Blindleistung entsteht durch Energie, die zwischen Quelle und Reaktanz (L oder C) hin- und herpendelt. Sie verrichtet keine Arbeit, aber sie belastet die Leitungen mit Strom.

:::formel
Q_L = U * I * sin(phi)    # Blindleistung
:::

**Vorzeichen:** Induktive Blindleistung ist positiv (Q > 0), kapazitive negativ (Q < 0). Eine Kompensationsanlage nutzt das: kapazitive Blindleistung hebt induktive auf.

## Scheinleistung

Die Scheinleistung ist das, was der Erzeuger "liefern" muss — also den vollen Strom, unabhängig davon ob er Wirk- oder Blindstrom ist.

:::formel
S = U * I    # nur Effektivwerte, ohne Berücksichtigung der Phase
:::

Scheinleistung steht auf dem Typenschild von Transformatoren und Generatoren (in VA oder kVA), weil diese durch den Gesamtstrom begrenzt werden — nicht nur durch die Wirkleistung.

## Leistungsfaktor lambda = cos phi

Der Leistungsfaktor gibt an, welcher Anteil der Scheinleistung als Wirkleistung nutzbar ist.

:::formel
lambda = P / S
:::

Bei sinusförmigen Grössen gilt lambda = cos(phi). Bei nichtsinusförmigen Strömen (Schaltnetzteile, Dimmer) weicht lambda von cos phi ab.

| cos phi | Leistungsfaktor | Bedeutung |
|---|---|---|
| 1,0 | Ideal | Rein ohmsch, keine Blindleistung |
| 0,9 | Gut | Motoren mit guter Kompensation |
| 0,7 | Schlecht | Starke Blindleistungsbelastung |
| 0 | Rein reaktiv | Keine Wirkleistung |

:::warning
In der Schweiz schreiben Netzanschlussbedingungen oft cos phi ≥ 0,9 für grössere Anlagen vor. Wird dieser Wert unterschritten, können die Energieversorger Zusatzgebühren erheben. Grosse Industrie-Motoren werden deshalb durch Kondensatoren kompensiert → [[Blindleistungskompensation]].
:::

:::monospace
Beispiel Motor: U = 400 V, I = 10 A, cos phi = 0.8
S = 400 * 10 = 4000 VA = 4 kVA
P = 4000 * 0.8 = 3200 W = 3.2 kW  (Wirkleistung)
Q = sqrt(4000^2 - 3200^2) = 2400 var  (Blindleistung)
:::
