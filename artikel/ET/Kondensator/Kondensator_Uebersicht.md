---
title: Kondensator (Übersicht)
kategorie: ET
tags: [kondensator, bauteil, passiv, energie, ladung, kapazität, elko, keramikkondensator, folienkondensator, bypass, siebkondensator]
symbol: C
einheit: F
---

Ein Kondensator speichert elektrische Energie im elektrischen Feld. Er lässt Wechselstrom durch, blockiert Gleichstrom.

:::hbox
:::vbox
**Voraussetzungen**
- [[Elektrisches Feld]]
:::
:::vbox
**Verwandte Artikel**
- [[Spule (Übersicht)]]
:::
:::vbox
**Führt weiter zu**
- [[Kapazität & Einheiten]]
- [[Auf- und Entladung]]
- [[Kondensator Typen]]
:::
:::

---

## Schaltsymbol

Zwei parallele Linien mit je einem Anschluss. Bei polarisierten Kondensatoren (Elkos) ist das Plussymbol oder ein gebogener Bogen auf einer Seite.

:::hbox
:::schematic Kondensator (unpolarisiert)
/schaltplaene/symbole/C.svg
:::
:::schematic Elko (polarisiert)
/schaltplaene/symbole/C_pol.svg
:::
:::

## Aufbau

Zwei leitende Platten, getrennt durch ein Dielektrikum (Isolator). Wird Spannung angelegt, sammeln sich Ladungen auf den Platten. Das erzeugt ein elektrisches Feld zwischen ihnen.

## Grundgrössen

```
Q = C * U        # Ladung auf den Platten
Q = I * t        # Ladung aus Strom und Zeit
E = 0.5 * C * U^2   # gespeicherte Energie
```

| Grösse | Symbol | Einheit |
|---|---|---|
| Kapazität | C | F (Farad) |
| Ladung | Q | C (Coulomb) |
| Spannung | U | V |
| Strom | I | A |
| Energie | E | J |

## Bauformen

**Elektrolytkondensator (Elko)**: Grosse Kapazität auf kleinem Raum. Polarisiert, muss mit korrekter Polung eingebaut werden. Typisch für Siebung in Netzteilen.

**Keramikkondensator**: Klein, robust, unpolarisiert. Schnelles Ansprechen. Typisch als Bypass-Kondensator direkt am IC.

**Folienkondensator**: Genaue Kapazität, wenig Alterung. Typisch für Präzisionsanwendungen und Audio.

Mehr dazu unter [[Kondensator Typen]].

## Reihen- und Parallelschaltung

Bei der **Reihenschaltung** addieren sich die Kehrwerte — die Gesamtkapazität ist kleiner als die kleinste Einzelkapazität:

:::schematic Kondensatoren in Reihe
/schaltplaene/kondensator_reihe.svg
:::

```
1/C_ges = 1/C1 + 1/C2 + ... + 1/Cn
```

Bei der **Parallelschaltung** addieren sich die Kapazitäten direkt:

:::schematic Kondensatoren parallel
/schaltplaene/kondensator_parallel.svg
:::

```
C_ges = C1 + C2 + ... + Cn
```

:::tip
Parallel ist das Gegenteil von Widerständen: Kondensatoren in Reihe werden kleiner, Kondensatoren parallel werden grösser.
:::

## Verhalten

Ein leerer Kondensator verhält sich kurz wie ein Kurzschluss. Wenn er geladen ist, fliesst kein Gleichstrom mehr durch ihn. Im Wechselstromkreis ist er ein frequenzabhängiger Widerstand.

:::warning
Elkos haben eine maximale Betriebsspannung. Wird sie überschritten, können sie sich entladen, auslaufen oder bersten.
:::
