---
title: Magnetische Flussdichte
kategorie: ET
tags: [magnetische flussdichte, tesla, gauss, halleffekt, permanentmagnet, sättigung, luftspalt]
groessen: B|Flussdichte|T; H|Feldstärke|A/m; mu_r|relative Permeabilität|—; mu_0|Feldkonstante|H/m
_status: PORT  # ET_alt/Netzqualitaet/Magnetische_Flussdichte.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::

---

Die magnetische Flussdichte B beschreibt, wie konzentriert das Magnetfeld an einem bestimmten Ort ist. Sie ist die massgebliche Grösse für Kräfte auf Ladungen, Leiterkräfte und die Sättigung von Kernmaterialien.

## Definition und Einheit

Die Flussdichte B hängt von der Feldstärke H und dem Material ab:

:::formel
B = mu_0 * mu_r * H
:::

**Einheit:** Tesla (T). 1 T = 1 Vs/m² = 1 Wb/m².

Ältere Einheit: 1 Gauss = 10⁻⁴ T (noch in der Werkstattpraxis zu finden).

## Typische Flussdichten

| Quelle | B |
|---|---|
| Erdmagnetfeld | ≈ 50 µT |
| Kühlschrankmagnet | ≈ 50 mT |
| Lautsprecher-Dauermagnet | 0,5–2 T |
| Trafokern (Sättigungsgrenze Si-Stahl) | 1,5–2 T |
| Ferritkern (Sättigungsgrenze) | 0,3–0,5 T |
| MRT-Scanner | 1,5–7 T |
| Stärkste Labor-Magnete | > 40 T |

## Flussdichte und Sättigung

In Eisenkernen kann B nicht beliebig erhöht werden — bei Überschreitung der **Sättigungs-Flussdichte B_sat** bricht die Permeabilität mu_r zusammen. Der Kern verhält sich wie Luft.

:::warning
Bei Überschreitung von B_sat verliert eine Drossel oder ein Transformator seine Induktivität. Für Wechselstromkerne wird deshalb B_max < B_sat/2 angestrebt. Bei Gleichstromanteilen im Kern (Schaltnetzteile) muss der Worst-Case-Strom berücksichtigt werden.
:::

## Kraftwirkung

Die Lorentzkraft auf einen Leiter der Länge l mit Strom I im Feld B ist F = I · l · B. Die Flussdichte B ist damit die direkte Ursache für die Motorwirkung (→ [[Lorentzkraft]]).

## Messung

**Hall-Effekt-Sensor**: Ein Halbleiterelement im Magnetfeld erzeugt eine Querspannung proportional zu B. Einfache, berührungslose Messung — in Hall-Gauss-Metern und als Stromsensor (Strom → Feld → Hall-Spannung).

**Induktive Messspule**: Ändert sich B, wird in einer Testspule eine Spannung induziert (u = −N · dPhi/dt). Durch Integration lässt sich B bestimmen.
