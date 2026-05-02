---
title: Batterietechnik
kategorie: EK
tags: [batterie, Li-Ion, LiPo, NiMH, kapazität, laden, entladen, LiFePO4, SOC, CC-CV, tiefentladung, memory-effekt, energiedichte]
symbol: —
einheit: Ah, Wh
---

Batterien speichern elektrische Energie chemisch. Jede Technologie hat andere Spannung, Kapazität, Ladecharakteristik und Lebensdauer.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[BMS Balancing]]
:::
:::vbox
**Führt weiter zu**
- [[SOC (State of Charge)]]
- [[Schutzbeschaltung]]
:::
:::

---

## Kapazität und Energie

```
E = U * Q       # Energie in Wh; U = Nennspannung, Q = Kapazität in Ah
```

Eine 3.7 V Zelle mit 2000 mAh speichert 7.4 Wh.

## Lithium-Ionen (Li-Ion / LiPo)

Höchste Energiedichte, leicht, kein Memory-Effekt. Standard in Mobilgeräten, E-Bikes und Elektroautos.

Zellenspannung: 3.0 V (entladen) bis 4.2 V (voll). Nennspannung 3.6 bis 3.7 V.

LiPo (Lithium-Polymer): Flexibles Gehäuse, leichter, aber empfindlicher gegen mechanische Beschädigung.

:::warning
Li-Zellen nie unter 2.5 V entladen (Tiefentladung) und nie über 4.25 V laden. Beides verkürzt die Lebensdauer stark oder macht die Zelle gefährlich. Immer BMS verwenden.
:::

## NiMH (Nickel-Metallhydrid)

Günstig, robust, kein Gedächtniseffekt (gering). Zellenspannung 1.2 V. Geringere Energiedichte als Li-Ion.

Einsatz: Werkzeugbatterien, Haushalt (AA/AAA).

## Ladeverfahren Li-Ion (CC/CV)

Zuerst konstanter Strom (CC) bis Maximalspannung. Dann konstante Spannung (CV) bis Strom auf ca. 10 % des Nennstroms gesunken. Dann abschalten.

## Lebensdauer

| Technologie | Zyklen (bis 80 % Kapazität) | Lagerung |
|---|---|---|
| Li-Ion | 500 bis 1000 | bei 50 % SOC, kühl |
| LiPo | 300 bis 500 | bei 50 % SOC, kühl |
| NiMH | 500 bis 1000 | entladen |
| LiFePO4 | 2000 bis 5000 | robust |
