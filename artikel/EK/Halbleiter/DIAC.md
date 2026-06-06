---
title: DIAC
kategorie: EK
kapitel: Halbleiter
tags: [diac, triggerdiode, bidirektional, kippspannung, breakover, triac-zündung, phasenanschnitt, db3, symmetrisch]
groessen: U_BO|Kippspannung|V; I_BO|Kippstrom|mA
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Thyristor (SCR)]]
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[TRIAC]]
- [[Thyristor (SCR)]]
:::
:::vbox
**Führt weiter zu**
- [[TRIAC]]
:::
:::

---

Ein DIAC ist eine bidirektionale Triggerdiode — er schaltet in **beiden Richtungen** durch, sobald die angelegte Spannung seine Kippspannung U_BO überschreitet. Er hat kein Gate, er zündet durch Spannungsüberschreitung allein.

## Schaltsymbol

:::schematic DIAC
/schaltplaene/symbole/D_DIAC.svg
:::

Zwei gegenläufige Dreiecke mit je einem Querbalken. Das Symbol zeigt die Symmetrie: Durchleitung in beiden Richtungen.

## Aufbau

:::schematic DIAC-Schichtaufbau: fünf Schichten p-n-p-n-p, Anschlüsse A1 und A2 an den äusseren p-Schichten
/Diagramm/diac_aufbau.svg
:::

Der DIAC besteht aus **fünf Halbleiterschichten (p-n-p-n-p)**, symmetrisch aufgebaut. Anders als der Thyristor (4 Schichten, p-n-p-n) hat er eine zusätzliche p-Schicht auf der anderen Seite — das ermöglicht das symmetrische Sperren und Schalten in beiden Richtungen. Er hat nur zwei Anschlüsse (A1 und A2) — kein Gate.

:::schematic DIAC-Ersatzschaltbild: zwei antiparallele Zener-Dioden (Kathode an Kathode). Positive Halbwelle zündet obere Zener, negative Halbwelle zündet untere Zener — symmetrisches Verhalten
/Diagramm/diac_ersatzschaltbild.svg
:::

## Funktionsweise

:::schematic DIAC-Kennlinie: symmetrische S-Kurve. Im Bereich –U_BO bis +U_BO hoher Widerstand (Sperrbereich). Bei ±U_BO schlagartige Umkehr in den Durchlassbereich (negativer Widerstand). Symmetrisch für beide Polaritäten
/Diagramm/diac_kennlinie.svg
:::

| Zustand | Beschreibung |
|---|---|
| U < U_BO | DIAC sperrt in beiden Richtungen (hoher Widerstand) |
| U = U_BO | DIAC schaltet schlagartig durch → Strom steigt sprunghaft |
| Strom fällt unter Haltestrom | DIAC sperrt wieder |

Die Kippspannung liegt typisch bei **28–36 V** (z. B. DB3: 32 V ±4 V). Das Zünden geschieht in beiden Halbwellen gleich — der DIAC ist vollständig symmetrisch.

## Anwendung: TRIAC-Phasenanschnitt

Der DIAC wird fast ausschliesslich für die **Phasenanschnittsteuerung** mit TRIAC eingesetzt:

1. Kondensator C wird über Potentiometer R geladen
2. Sobald C die Spannung U_BO erreicht, zündet der DIAC
3. DIAC entlädt C schlagartig in das TRIAC-Gate
4. TRIAC zündet → Last eingeschaltet

Mit dem Potentiometer lässt sich der Ladezeitraum und damit der **Zündzeitpunkt** (Phasenwinkel α) einstellen — von früh (volle Leistung) bis spät (minimale Leistung).

:::tip
Ohne DIAC wäre die TRIAC-Zündung **asymmetrisch**: Positive und negative Halbwelle würden zu unterschiedlichen Zeitpunkten zünden, weil Gate-Empfindlichkeit des TRIACs in verschiedenen Quadranten unterschiedlich ist. Der DIAC erzwingt symmetrisches Zünden in beiden Halbwellen und sorgt für gleichmässige Leistungsübertragung.
:::

## Typischer Baustein

**DB3** (häufigster DIAC): U_BO = 28–36 V, Gehäuse wie kleine Diode (DO-35). Wird in fast jedem Dimmer und Anlasser verbaut.
