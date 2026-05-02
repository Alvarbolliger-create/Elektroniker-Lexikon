---
title: Lineare Regler
kategorie: EK
tags: [linearregler, spannungsregler, 7805, LDO, verlustleistung, dropout, LM317, wirkungsgrad, rauscharm, kühlkörper, bandgap]
symbol: —
einheit: —
---

Ein linearer Spannungsregler hält die Ausgangsspannung konstant, indem er überschüssige Spannung als Wärme vernichtet. Einfach, rauscharm, aber ineffizient bei grosser Spannungsdifferenz.

:::hbox
:::vbox
**Voraussetzungen**
- [[Zener-Diode]]
- [[Bipolartransistor (BJT)]]
:::
:::vbox
**Verwandte Artikel**
- [[Buck (Step-down)]]
:::
:::vbox
**Führt weiter zu**
- [[Thermomanagement]]
:::
:::

---

## Funktionsprinzip

Ein Transistor im linearen Betrieb regelt den Spannungsabfall zwischen Ein- und Ausgang. Eine Regelschleife vergleicht die Ausgangsspannung mit einer Referenz und steuert den Transistor nach.

Die Verlustleistung fällt am Transistor ab:

```
P_verlust = (U_ein - U_aus) * I_last     # gesamte Verlustleistung als Wärme
```

## Typen

**Standard (z.B. 7805)**: Mindestens 2 bis 3 V Dropout-Spannung. Einfach, robust, günstig.

**LDO (Low Dropout)**: Funktioniert noch mit sehr kleiner Differenz (100 bis 300 mV). Besser für batteriegespeiste Geräte.

## Wirkungsgrad

```
eta = U_aus / U_ein     # Wirkungsgrad; stark lastabhängig
```

Beispiel: 12 V Eingang, 5 V Ausgang, 1 A Last. P_verlust = 7 W. Wirkungsgrad = 42 %. Der Regler braucht einen Kühlkörper.

## Wann sinnvoll?

Gute Wahl wenn: Eingangsspannung nur wenig über Ausgangsspannung, kleine Lasten, rauscharme Spannung benötigt (Audio, ADC-Referenz).

Schlechte Wahl wenn: grosse Spannungsdifferenz, hoher Strom. Dann besser [[Buck (Step-down)]].

## Typische ICs

| Typ | U_aus | I_max | Dropout | Bemerkung |
|---|---|---|---|---|
| 7805 | 5 V | 1.5 A | 2 V | Klassiker |
| 7812 | 12 V | 1.5 A | 2 V | Klassiker |
| LM317 | 1.25–37 V | 1.5 A | 1.5 V | Einstellbar über R1/R2 |
| LM1117-3.3 | 3.3 V | 0.8 A | 1.2 V | LDO, TO-220/SOT-223 |
| MCP1700 | einstellbar | 0.25 A | 0.18 V | LDO, sehr tief |

---

## OPV + Transistor Spannungsregler

Statt eines fertigen IC lässt sich ein Linearregler auch diskret aufbauen. Der OPV übernimmt die Regelung, ein externer Transistor den Laststrom:

```
U_ein ──[NPN-Transistor]──┬── U_aus
       (Emitterfolger)    |
                         [R1]
                          |
                     (+)──┤ OPV ──── Basis des NPN
                [R2]──(−)─┘
                          |
                         GND
```

**Funktion**:
- Spannungsteiler R1/R2 gibt einen Teil von U_aus an den (−)-Eingang des OPV
- Zener-Diode oder Referenz-IC an (+)-Eingang liefert U_ref
- OPV regelt Basis des NPN so, dass (−) = (+): U_aus = U_ref × (1 + R1/R2)
- NPN kann hohen Laststrom treiben; OPV liefert nur den kleinen Basisstrom

**LM317 als einstellbarer Regler**:

```
U_aus = 1.25 V × (1 + R2/R1)    # Formel für LM317
```

R1 = 240 Ω (typisch), R2 einstellbar. Wenn R2 = 2.16 kΩ → U_aus = 12.5 V.

:::info
Der LM317 hat intern denselben Aufbau: OPV als Fehlerverstärker, NPN als Stellglied. Die Referenzspannung zwischen Adjust und Ausgang beträgt 1.25 V (Bandgap-Referenz).
:::
