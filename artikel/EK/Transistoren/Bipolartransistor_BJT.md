---
title: Bipolartransistor (BJT)
kategorie: EK
tags: [transistor, BJT, NPN, PNP, verstärker, schalter, halbleiter, h_FE, stromverstärkung, U_BE, sättigung, emitter, kollektor, basis]
symbol: T
einheit: —
---

Der Bipolartransistor steuert einen grossen Strom mit einem kleinen. Er wird als Schalter oder als Verstärker eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[p-n-Übergang]]
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[FET / MOSFET]]
:::
:::vbox
**Führt weiter zu**
- [[Als Schalter]]
- [[Als Verstärker]]
:::
:::

---

## Aufbau und Typen

Drei Schichten: Emitter, Basis, Kollektor.

**NPN**: Strom fliesst von Kollektor zu Emitter, wenn ein kleiner Strom in die Basis fliesst. Der häufigste Typ.

**PNP**: Umgekehrt. Strom fliesst, wenn die Basis gegen Emitter negativ gezogen wird.

## Schaltsymbol

:::hbox
:::schematic NPN-Transistor (Übersicht)
/schaltplaene/bjt_npn.svg
:::
:::schematic NPN (Symbol)
/schaltplaene/symbole/Q_NPN.svg
:::
:::schematic PNP (Symbol)
/schaltplaene/symbole/Q_PNP.svg
:::
:::

Drei Anschlüsse: B (Basis), C (Kollektor), E (Emitter). Beim NPN zeigt der Pfeil am Emitter nach aussen (weg vom Transistor). Beim PNP nach innen.

## Betrieb als Schalter

Die Basis steuert ob der Transistor leitend (gesättigt) oder gesperrt ist.

:::monospace
I_B = (U_ein - U_BE) / R_B   # Basisstrom; U_BE ca. 0.7 V
I_C = h_FE * I_B             # Kollektorstrom; h_FE = Stromverstärkung
:::
| Grösse | Symbol | Typischer Wert |
|---|---|---|
| Basis-Emitter-Spannung | U_BE | 0.6 bis 0.7 V |
| Stromverstärkung | h_FE | 50 bis 500 |
| Kollektor-Emitter-Sättigung | U_CE_sat | 0.1 bis 0.3 V |

## Betrieb als Verstärker

Im Arbeitspunkt wird der Transistor linear betrieben. Eine kleine Wechselspannung an der Basis ergibt eine verstärkte an Kollektor.

Details dazu unter [[Als Verstärker (Arbeitspunkt)]].

:::warning
Der Basiswiderstand ist zwingend. Ohne ihn fliesst zu viel Basisstrom, der Transistor wird zerstört. Immer den Arbeitsstrom berechnen.
:::
