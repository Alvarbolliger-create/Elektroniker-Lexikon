---
title: Elektrische Ladung & Elementarladung
kategorie: ET
tags: [ladung, coulomb, elementarladung, elektron, strom, zeit, ionisation]
groessen: Q|Ladung|C; I|Strom|A; t|Zeit|s; n|Elektronenanzahl|—; qe|Elementarladung|C
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Kapazität & Einheiten]]
:::
:::

---

Elektrische Ladung ist die fundamentalste Grösse der Elektrotechnik. Alle elektrischen Erscheinungen — Strom, Spannung, Felder — gehen auf die Eigenschaft zurück, dass Materie elektrisch geladen sein kann.

## Elektrische Ladung

Elektrische Ladung Q ist eine Eigenschaft von Teilchen:
- **Elektronen** tragen negative Ladung (−e)
- **Protonen** tragen positive Ladung (+e)
- **Neutrale Atome** haben gleich viele Elektronen und Protonen

Ladung ist eine **Erhaltungsgrösse** — sie kann weder erzeugt noch vernichtet werden, nur von einem Ort zum anderen verschoben.

**Einheit:** Coulomb (C). 1 C ist eine sehr grosse Ladungsmenge — sie entspricht etwa 6,24 · 10¹⁸ Elektronen.

## Zusammenhang mit Strom

Strom ist das zeitliche Fliessen von Ladung. Ein Strom von 1 A bedeutet: Pro Sekunde fliesst 1 C Ladung durch den Leiter.

:::formel
Q = I * t    # Ladung Q (C) = Strom I (A) mal Zeit t (s)
:::

Diese Formel ist direkt beim Kondensatorladen anwendbar: Lädt man einen Kondensator mit einem Konstantstrom I über die Zeit t, akkumuliert sich die Ladung Q = I · t auf den Platten (→ [[Auf- und Entladung (Kondensator)]]).

:::monospace
Beispiel: Ladevorgang mit I = 200 mA über t = 5 s
Q = 200e-3 * 5 = 1 C
:::

## Elementarladung

Die kleinste frei vorkommende Ladung ist die **Elementarladung** — die Ladung eines einzelnen Elektrons (negativ) oder Protons (positiv):

qe = 1,602176634 · 10⁻¹⁹ C  (exakter CODATA-Wert, seit 2019 festgelegt)

Jede messbare Ladung ist ein ganzzahliges Vielfaches von qe:

:::formel
Q = n * _qe    # n = Anzahl Elektronen (negative Ladungsträger)
:::

| Teilchen | Ladung |
|---|---|
| Elektron | −qe = −1,602 · 10⁻¹⁹ C |
| Proton | +qe = +1,602 · 10⁻¹⁹ C |
| Neutron | 0 C |

:::tip
Im CAS-Rechner ist die Elementarladung als Konstante `_qe` hinterlegt — kein Abtippen nötig:
:::
:::monospace
qe              → 1.602176634e-19 C
Q = 6.24e18 * _qe  → ≈ 1.00 C   (entspricht 1 Coulomb)
Q = 100 * _qe      → 1.602e-17 C (100 Elektronen)
:::

Der Name `_qe` steht für "charge of the electron" (q = Ladung, e = Elektron).

:::tip
In einem Kupferleiter bei 1 A fliessen rund **6,24 · 10¹⁸ Elektronen pro Sekunde** vorbei. Jedes einzelne Elektron bewegt sich dabei sehr langsam (Driftgeschwindigkeit ca. 0,1 mm/s) — die elektrische Wirkung breitet sich jedoch nahezu lichtschnell aus, weil das Feld sofort durch den ganzen Leiter wirkt.
:::
