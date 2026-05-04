---
title: Hard-Switching vs. Soft-Switching (ZVS / ZCS)
kategorie: EK
tags: [Soft-Switching, Hard-Switching, ZVS, ZCS, Schaltverluste, Resonanz, Schaltnetzteil]
symbol: —
einheit: —
---

Bei hohen Schaltfrequenzen entstehen erhebliche Verluste im Schaltmoment selbst. Soft-Switching-Techniken eliminieren diese Verluste, indem der Transistor nur dann schaltet, wenn Spannung oder Strom null ist.

:::hbox
:::vbox
**Voraussetzungen**
- [[Buck (Step-down)]]
- [[MOSFET]]
- [[PWM Arten]]
:::
:::vbox
**Verwandte Artikel**
- [[Flyback & Forward Converter]]
- [[Snubber-Netzwerk]]
:::
:::

---

## Hard-Switching: Das Problem

Beim konventionellen Schalten schaltet der Transistor, während gleichzeitig Spannung und Strom vorhanden sind. Im Schaltmoment entsteht ein Übergangsbereich, in dem beide Grössen nicht null sind.

**Einschaltvorgang**: Strom steigt, Spannung sinkt. Kurz trägt der Transistor gleichzeitig hohen Strom und hohe Spannung → Verlustleistung P = U × I.

**Ausschaltvorgang**: Strom sinkt, Spannung steigt. Dasselbe Problem.

Die Energie aus der parasitären Drain-Source-Kapazität (COSS) wird bei jedem Einschalten vernichtet:

:::monospace
P_COSS = 0.5 × C_OSS × U_DS² × f    # proportional zu Frequenz
:::
Bei 1 MHz und modernen GaN-Transistoren werden diese Verluste dominant.

## ZVS (Zero Voltage Switching)

Der Transistor schaltet ein, wenn die Spannung über ihm null (oder sehr klein) ist.

**Wie**: Vor dem Einschalten wird die Energie aus C_OSS durch eine Resonanzinduktivität "abgeleitet". Die Drain-Spannung schwingt auf null — dann schaltet der Transistor ein.

**Vorteile**:
- Keine COSS-Verluste beim Einschalten
- Kein EMV-Problem durch steile Spannungsflanken
- Geringere Gatewiderstände möglich

**Typisch**: In Halbbrücken-Topologien (LLC-Resonanzwandler, Phase-Shift Full Bridge).

## ZCS (Zero Current Switching)

Der Transistor schaltet aus, wenn der Strom durch ihn null ist.

**Wie**: Eine Resonanzschaltung sorgt dafür, dass der Strom vor dem Ausschalten auf null abklingt. Dann wird der Transistor ausgeschaltet, ohne den Strom zu unterbrechen.

**Vorteile**:
- Keine Ausschaltverluste (kein dI/dt-Problem)
- Gut für Thyristoren (können ohnehin nur beim Nulldurchgang gelöscht werden)

**Einsatz**: Thyristorschaltungen, Induktionserwärmung, bestimmte Resonanzwandler.

## LLC-Resonanzwandler

Der häufigste Soft-Switching-Wandler in der Praxis. Nutzt eine Resonanzschaltung aus Lr (Streuinduktivität des Übertragers) und Cr (Resonanzkondensator) plus Magnetisierungsinduktivität Lm.

Bei Betrieb nahe der Resonanzfrequenz erreicht der Wandler ZVS automatisch. Wirkungsgrade > 95 % bei hohen Frequenzen (100 kHz – 1 MHz) sind möglich.

**Typische Anwendung**: Server-Netzteile, Ladeinfrastruktur, LED-Treiber (hohe Effizienz gefordert).

## Vergleich

| Merkmal | Hard-Switching | Soft-Switching |
|---|---|---|
| Schaltverluste | Hoch | Sehr gering |
| Schaltfrequenz | 50–500 kHz typisch | 500 kHz – mehrere MHz möglich |
| EMV | Schlechter (steile Flanken) | Besser |
| Schaltungsaufwand | Einfach | Höher |
| Wirkungsgrad typisch | 87–92 % | 93–97 % |
