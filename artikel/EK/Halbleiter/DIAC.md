---
title: DIAC
kategorie: EK
tags: [DIAC, trigger-diode, 4-schicht, symmetrisch, zündspannung, TRIAC, phasenanschnitt, bidirektional]
symbol: —
einheit: —
---

Ein DIAC ist eine bidirektionale Triggerdiode. Er leitet in beide Richtungen sobald die Spannung eine Zündspannung erreicht. Er hat kein Gate — er schaltet allein durch Spannungsüberschreitung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[Thyristor (SCR)]]
:::
:::vbox
**Verwandte Artikel**
- [[TRIAC]]
:::
:::vbox
**Führt weiter zu**
- [[TRIAC]]
:::
:::

---

## Schaltsymbol

:::schematic DIAC
/schaltplaene/symbole/D_DIAC.svg
:::

Zwei gegenläufige Dreiecke mit je einem Querbalken. Das Symbol zeigt die Symmetrie: Der DIAC leitet in beiden Richtungen.

## Aufbau

Der DIAC besteht aus **vier Halbleiterschichten** (PNPN / NPNP), symmetrisch aufgebaut. Er hat nur zwei Anschlüsse (A1 und A2) — kein Gate.

## Funktionsweise

Der DIAC sperrt in beiden Richtungen bis die angelegte Spannung die **Zündspannung U_BO** (Breakover Voltage) erreicht:

- Unterhalb U_BO: DIAC sperrt (hoher Widerstand)
- Bei U_BO: DIAC schaltet schlagartig durch, Widerstand sinkt stark
- Der Strom steigt sprunghaft — ideal um ein Gate-Zündsignal zu erzeugen

Typische Zündspannung: **28 bis 36 V** (z.B. DB3: 28–36 V)

## Anwendung: TRIAC-Zündung

Der DIAC wird fast ausschliesslich zusammen mit dem TRIAC für **Phasenanschnittsteuerung** verwendet:

1. Kondensator wird über Widerstand geladen
2. Sobald Kondensatorspannung U_BO erreicht, zündet der DIAC
3. DIAC entlädt den Kondensator schlagartig in das TRIAC-Gate
4. TRIAC zündet → Last wird eingeschaltet

Mit dem Ladewiderstand (Potentiometer) lässt sich der Zündzeitpunkt und damit die übertragene Leistung steuern.

:::tip
Ohne DIAC wäre die Zündung des TRIACs unsymmetrisch — die positive und negative Halbwelle würden unterschiedlich spät zünden. Der DIAC garantiert symmetrisches Zünden in beiden Halbwellen.
:::
