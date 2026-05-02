---
title: TRIAC
kategorie: EK
tags: [TRIAC, triode alternating current switch, bidirektional, phasenanschnitt, wechselstromsteuerung, gate, zündwinkel, DIAC, leistungssteuerung, dimmer]
symbol: —
einheit: —
---

Ein TRIAC (Triode Alternating Current Switch) ist ein bidirektionaler steuerbarer Halbleiter. Er leitet in beide Richtungen und eignet sich zur Leistungssteuerung in Wechselstromkreisen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Thyristor (SCR)]]
- [[DIAC]]
:::
:::vbox
**Verwandte Artikel**
- [[DIAC]]
- [[Thyristor (SCR)]]
:::
:::

---

## Schaltsymbol

:::schematic TRIAC
/schaltplaene/symbole/TRIAC.svg
:::

Zwei gegenläufige Thyristoren mit gemeinsamen Gate (G). Anschlüsse: A1, A2, G (Gate).

## Aufbau und Prinzip

Der TRIAC besteht aus **zwei antiparallelen Thyristoren** in einem gemeinsamen Gehäuse. Er leitet:
- In der **positiven Halbwelle** (A1 positiver als A2)
- In der **negativen Halbwelle** (A2 positiver als A1)

Ein kurzer Zündimpuls am Gate reicht um den TRIAC in der jeweiligen Halbwelle zu zünden. Er erlischt automatisch beim nächsten Nulldurchgang des Stroms.

## Unterschied Thyristor / TRIAC

| Eigenschaft | Thyristor (SCR) | TRIAC |
|---|---|---|
| Leitrichtungen | 1 (unidirektional) | 2 (bidirektional) |
| Typische Anwendung | DC, Gleichrichter | AC, Dimmer |
| Abschalten | Nur bei Nulldurchgang | Nur bei Nulldurchgang |

## Phasenanschnittsteuerung

Die häufigste Anwendung: Leistung regeln durch Verzögerung des Zündzeitpunkts.

Der **Zündwinkel α** bestimmt wann in der Halbwelle der TRIAC zündet:
- α = 0°: TRIAC zündet sofort → volle Leistung
- α = 90°: TRIAC zündet in der Mitte → halbe Leistung
- α = 180°: TRIAC zündet nie → keine Leistung

:::plot
var: t
range: 0, 12.56
xlabel: Zeit
ylabel: Spannung (normiert)
Netzspannung:       sin(t)
Phasenanschnitt α=90°: (sin(t) > 0 && t % 6.28 > 1.57) ? sin(t) : (sin(t) < 0 && t % 6.28 > 4.71) ? sin(t) : 0
:::

## DIAC-TRIAC-Kombination

Typische Standardschaltung für einen Dimmer oder Heizungsregler:

```
Netz ──── R (Potentiometer) ──┬──── TRIAC (A1) ──── Last ──── Netz
                               │
                               C ──── DIAC ──── TRIAC (Gate)
```

1. R und C bilden ein RC-Glied, das die Phase verschiebt
2. Wenn U_C die DIAC-Zündspannung (≈30 V) erreicht, zündet der DIAC
3. DIAC schickt einen Stromimpuls ans TRIAC-Gate
4. TRIAC zündet und bleibt bis Nulldurchgang leitend
5. Mit R (Potentiometer) lässt sich α einstellen

:::warning
Phasenanschnitt erzeugt Oberwellen im Netz und kann bei induktiven Lasten (Motoren, Transformatoren) zu starken Spannungsspitzen führen. Für moderne Schaltnetzteile und dimmbare LEDs oft nicht geeignet — hier besser Nullpunkt-Schaltung (Burst-Firing) verwenden.
:::
