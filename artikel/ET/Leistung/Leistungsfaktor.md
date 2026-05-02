---
title: Leistungsfaktor cos φ
kategorie: ET
tags: [leistungsfaktor, cos phi, blindleistung, kompensation, wirkungsgrad, PFC, leistungsdreieck, scheinleistung]
symbol: cos φ
einheit: —
---

Der Leistungsfaktor gibt an, wie viel der Scheinleistung tatsächlich als Wirkleistung genutzt wird. Ein Wert von 1 ist ideal, alles darunter bedeutet unnötigen Strom in der Leitung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Scheinleistung]]
:::
:::vbox
**Verwandte Artikel**
- [[Blindleistung]]
:::
:::vbox
**Führt weiter zu**
- [[Oberschwingungen]]
:::
:::

---

## Definition

```
cos_phi = P / S     # Wirkleistungsfaktor
sin_phi = Q / S     # Blindleistungsfaktor
phi     = arctan(Q / P)
```

Bei cos φ = 1: gesamter Strom leistet Arbeit. Bei cos φ = 0.7: nur 70 % sind nutzbar, 30 % sind Blindstrom.

## Warum ist er wichtig?

Der Strom in der Leitung richtet sich nach der Scheinleistung, nicht nach der Wirkleistung. Eine Anlage mit 10 kW Bedarf und cos φ = 0.7 zieht 14.3 kVA aus dem Netz. Das bedeutet höhere Leitungsbelastung, grössere Transformatoren und mehr Verluste.

Energieversorger verrechnen Industriekunden bei schlechtem Leistungsfaktor eine Zusatzgebühr.

## Kompensation

Kondensatorbatterien parallel zur induktiven Last gleichen Blindleistung aus. Der Leistungsfaktor steigt. Der Leitungsstrom sinkt.

Aktive Leistungsfaktorkorrektur (PFC) in Schaltnetzteilen erreicht cos φ > 0.99.

| Last | Typischer cos φ |
|---|---|
| Heizung, Glühbirne | 1.0 |
| Motor ohne Kompensation | 0.7 bis 0.85 |
| Motor mit Kompensation | 0.95 bis 0.99 |
| Schaltnetzteil ohne PFC | 0.5 bis 0.7 |
| Schaltnetzteil mit PFC | 0.95 bis 0.99 |
