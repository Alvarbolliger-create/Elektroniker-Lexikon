---
title: Thyristor (SCR)
kategorie: EK
tags: [thyristor, SCR, TRIAC, phasenanschnitt, zündung, löschen, wechselstromsteuerung, kommutierung, haltestrom, phasenabschnitt]
symbol: T
einheit: —
---

Ein Thyristor ist ein steuerbarer Gleichrichter. Er lässt sich durch einen Zündimpuls einschalten, schaltet aber erst aus wenn der Strom durch Null geht.

:::hbox
:::vbox
**Voraussetzungen**
- [[p-n-Übergang]]
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[Gleichrichter]]
- [[DIAC]]
- [[TRIAC]]
:::
:::

---

## Schaltsymbol und Aufbau

:::schematic Thyristor (SCR)
/schaltplaene/symbole/Thyristor.svg
:::

Ein Thyristor hat drei Anschlüsse: Anode (A), Kathode (K) und Gate (G). Er besteht aus vier abwechselnden p-n-Schichten (PNPN).

## Einschalten und Halten

Wenn Anode positiver als Kathode ist (Vorwärtsspannung) und ein Strompuls ans Gate angelegt wird, schaltet der Thyristor durch. Er bleibt leitend solange der Strom grösser als der Haltestrom ist, auch wenn das Gate-Signal wegfällt.

## Ausschalten (Kommutierung)

Ein Thyristor kann nicht über das Gate ausgeschaltet werden. Er schaltet erst aus wenn:
- Der Strom unter den Haltestrom sinkt (natürliche Kommutierung)
- Der Strom zwangsweise auf Null gebracht wird (Zwangskommutierung)

In Wechselstromsystemen übernimmt die natürliche Nulldurchgang des Netzstroms das Löschen.

## DIAC und TRIAC

Für Wechselstrom-Leistungssteuerung wird der Thyristor ergänzt durch:
- **[[DIAC]]**: Bidirektionale Triggerdiode — erzeugt den Zündimpuls symmetrisch in beiden Halbwellen
- **[[TRIAC]]**: Zwei antiparallele Thyristoren in einem Gehäuse — leitet in beiden Richtungen

## Phasenanschnitt vs. Phasenabschnitt

Beide Verfahren steuern die Leistung über das Netz, aber auf unterschiedliche Weise:

**Phasenanschnitt (Phase-Angle Firing)**:
- Zündung erfolgt *nach* dem Spannungsnulldurchgang (verzögert um Winkel α)
- Thyristor/TRIAC leitet vom Zündzeitpunkt bis zum nächsten Nulldurchgang
- Je grösser α, desto kleiner die übertragene Leistung
- Geeignet für **ohmsche Lasten** (Heizung, Glühlampe)
- Bei **induktiven Lasten** (Motoren, Transformatoren): Phasenversatz zwischen Strom und Spannung führt zu Problemen — der Nulldurchgang der Spannung ist nicht gleich dem Nulldurchgang des Stroms

**Phasenabschnitt (Trailing-Edge Dimming)**:
- Zündung erfolgt beim Nulldurchgang (sofort), Abschalten nach einem definierten Winkel
- Wird durch abschaltbare Bauelemente (GTO, IGBT, MOSFET) realisiert, da Thyristoren nicht aktiv ausschaltbar sind
- Geeignet für **kapazitive Lasten** (elektronische Treiber, Schaltnetzteile)
- Erzeugt weniger Störungen im Netz bei modernen Netzteilen

:::warning
Phasenanschnitt an induktiven Lasten erzeugt starke Spannungsspitzen (di/dt beim Abschalten). Ohne Schutzbeschaltung (Snubber) werden Thyristor oder TRIAC beschädigt.
:::

## Vergleich IGBT / MOSFET

Thyristoren schalten sehr hohe Ströme und Spannungen (kA, kV) bei hohem Wirkungsgrad. Für Einphasennetz-Steuerung einfach. Nachteil: Kein aktives Ausschalten, daher für PWM ungeeignet.
