---
title: Kühlkörperberechnung
kategorie: EK
tags: [kühlkörper, thermisch, widerstand, R_th, verlustleistung, temperatur, wärmeleitpaste, T_junction, derating, T_j_max, sperrschichttemperatur]
symbol: R_th
einheit: K/W
---

Verlustleistung erzeugt Wärme. Wärme muss abgeführt werden, sonst überhitzt das Bauteil. Der thermische Widerstand beschreibt wie gut Wärme abfliessen kann.

:::hbox
:::vbox
**Voraussetzungen**
- [[Wirkleistung]]
- [[Lineare Regler]]
:::
:::vbox
**Verwandte Artikel**
- [[Derating-Kurven]]
:::
:::vbox
**Führt weiter zu**
- [[Thermomanagement]]
:::
:::

---

## Thermisches Ersatzschaltbild

Wärme verhält sich analog zu Strom: Verlustleistung ist der Strom, Temperaturdifferenz ist die Spannung, thermischer Widerstand ist der Widerstand.

Thermische Widerstände addieren sich in Reihe: Chip → Gehäuse → Kühlkörper → Luft.

```
T_junction = T_ambient + P * (R_th_jc + R_th_cs + R_th_sa)
```

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Sperrschichttemperatur | T_j | °C | Temperatur im Chip |
| Umgebungstemperatur | T_amb | °C | Lufttemperatur |
| Verlustleistung | P | W | Abzuführende Wärme |
| R_th Chip-Gehäuse | R_th_jc | K/W | Aus Datenblatt |
| R_th Gehäuse-Kühlkörper | R_th_cs | K/W | Wärmeleitpaste ca. 0.5 K/W |
| R_th Kühlkörper-Luft | R_th_sa | K/W | Aus Kühlkörper-Datenblatt |

## Beispiel: Linearregler 7805

Eingang 12 V, Ausgang 5 V, Last 1 A. P_verlust = (12-5) × 1 = 7 W.

R_th_jc = 5 K/W (aus Datenblatt). T_j_max = 125 °C. T_amb = 25 °C.

Max. R_th gesamt = (125 - 25) / 7 = 14.3 K/W. Minus R_th_jc = 5: Kühlkörper muss R_th_sa < 9 K/W haben.

## Wärmeleitpaste

Zwischen Gehäuse und Kühlkörper gehört Wärmeleitpaste oder ein Wärmeleitpad. Ohne: R_th_cs steigt auf 2 bis 5 K/W. Mit Paste: ca. 0.5 K/W.

:::warning
T_j_max nie überschreiten. Für Langzeitbetrieb Derating einrechnen: T_j im Betrieb sollte mindestens 20 bis 30 °C unter dem Maximum liegen.
:::
