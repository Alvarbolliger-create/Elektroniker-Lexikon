---
title: Energie im Kondensator
kategorie: ET
tags: [energie, kondensator, kapazität, ladung, joule, superkondensator, entladung]
groessen: W|Energie|J; C|Kapazität|F; U|Spannung|V; Q|Ladung|C
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kapazität & Einheiten]]
:::
:::vbox
**Verwandte Artikel**
- [[Spule (Übersicht)]]
:::
:::

---

Ein geladener Kondensator speichert elektrische Energie im elektrischen Feld zwischen den Platten. Diese Energie kann bei Bedarf wieder abgegeben werden — Kondensatoren sind kurzzeit-Energiespeicher.

## Formel

:::formel
W = C * U^2 / 2    # Energie W (J) im Kondensator
:::

Alternativ über die Ladung Q = C · U:

:::formel
W = Q^2 / (2 * C)
:::

**Einheit:** Joule (J) = Ws.

## Herleitung

:::schematic
/abbildungen/kondensator/energie_dreieck.svg
:::

Beim Laden steigt die Spannung von 0 auf U. Der Strom muss gegen die wachsende Kondensatorspannung arbeiten — die Energie ist das Integral der Momentanleistung. Da die Spannung linear ansteigt (bei Konstantstrom), ergibt sich der Faktor 1/2:

W = integral(u · i, dt) = C · integral(u, du, 0, U) = C · U²/2

Das ist halb so viel wie P·t bei konstantem U·I — weil die Spannung am Anfang null und am Ende U ist.

## Numerische Beispiele

:::monospace
Elko 10 mF (10 000 µF) auf 16 V geladen:
W = 10e-3 * 16^2 / 2 = 1.28 J

Kondensator 100 µF auf 400 V (Netzteile!):
W = 100e-6 * 400^2 / 2 = 8 J
:::

:::warning
8 Joule klingen harmlos — aber bei einem Ladezustand von 400 V kann die Entladung in Millisekunden ablaufen. Das entspricht einer Impulsstromstärke von hunderten Ampere. Grosse Netzteil-Elkos sind nach dem Ausschalten noch **lange gefährlich geladen** — immer prüfen und vor Arbeiten entladen!
:::

## Vergleich: Kondensator vs. Batterie

| Eigenschaft | Kondensator | Batterie (Li-Ion) |
|---|---|---|
| Energiedichte | 0,001–0,1 Wh/kg | 100–250 Wh/kg |
| Leistungsdichte | Sehr hoch (kW/kg) | Mittel |
| Ladevorgänge | >100 000 | 500–2000 |
| Ladezeit | Millisekunden bis Sekunden | Minuten bis Stunden |
| Selbstentladung | Hoch (Stunden bis Tage) | Niedrig (Monate) |

Kondensatoren können also sehr schnell Energie aufnehmen und abgeben — sie sind keine Langzeitspeicher, aber perfekte Kurzzeitpuffer.

**Superkondensatoren (Ultracaps)**: Elektrolytkondensatoren mit sehr grosser Kapazität (1–3000 F), aber niedriger Spannung (2–3 V). Energiedichte zwischen klassischem Kondensator und Batterie — wird in Hybridfahrzeugen für Bremsenergie-Rückgewinnung eingesetzt.
