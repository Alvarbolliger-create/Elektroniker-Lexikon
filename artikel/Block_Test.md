---
title: NE555 Block-Test
kategorie: Test
tags: [test, NE555, timer, blöcke]
symbol: IC
einheit: —
---

Dieser Artikel testet alle verfügbaren Block-Typen anhand des **NE555 Timer-ICs** als Beispiel. Der NE555 ist eines der meistverkauften ICs der Geschichte und eignet sich hervorragend als Demonstrations-Thema.

## Einfache Blöcke (alt)

### Überschrift Ebene 3

Paragraph mit **Fettschrift**, `Inline-Code` und einem Wiki-Link auf [[Logikgatter]].

- Erster Listeneintrag mit `Code`
- Zweiter Eintrag mit **fett**
- Dritter Eintrag

| Parameter | Min | Typ | Max | Einheit |
|---|---|---|---|---|
| Versorgungsspannung Vcc | 4.5 | 5.0 | 15 | V |
| Ausgangsstrom | — | — | 200 | mA |
| Frequenz (astabil) | 0 | — | 500 | kHz |
| Temperaturbereich | -55 | 25 | 125 | °C |

### Formel-Block (CodeBlock → CAS)

```
f = 1.44 / ((R_A + 2*R_B) * C)
tau = 0.693 * (R_A + R_B) * C
D = (R_A + R_B) / (R_A + 2*R_B)
```

---

## Neue Blöcke

### Pinout

:::pinout NE555 DIP-8
1: GND | Masse (0 V)
2: TRIG | Trigger-Eingang (< 1/3 Vcc → setzt Ausgang)
3: OUT | Ausgang (Vcc − 1.7 V oder GND + 0.25 V)
4: RST | Reset, aktiv LOW — auf Vcc legen wenn ungenutzt
5: CV | Kontrollspannung (intern 2/3 Vcc, extern einstellbar)
6: THR | Schwellen-Eingang (> 2/3 Vcc → rücksetzt Ausgang)
7: DIS | Entladung (Open-Collector, verbunden mit internem Flip-Flop)
8: VCC | Versorgungsspannung (+5 … +15 V)
:::

### Wahrheitstabelle — Internes RS-Flip-Flop

Der NE555 enthält intern ein RS-Flip-Flop. Die Eingänge TRIG und THR steuern es:

:::truth TRIG<1/3,THR>2/3 | Q (OUT)
1,0 | 1
0,1 | 0
0,0 | 0
1,1 | 1
:::

### Signale — Astabiler Betrieb

Typisches PWM-Signal im astabilen Modus (50 % Duty Cycle mit R_A = R_B):

:::waveform
labels: t0,t1,t2,t3,t4,t5,t6,t7
OUT: 0,1,1,0,0,1,1,0
CAP: ~0.3,0.5,0.7,0.6,0.3,0.5,0.7,0.6
THR: ~0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7
:::

### Schaltplan

:::schematic NE555 Astabiler Oszillator
schaltplaene/ne555_astabil.svg
:::

### Hinweis-Blöcke

:::info
Der NE555 benötigt einen 100 nF Bypass-Kondensator zwischen Vcc (Pin 8) und GND (Pin 1), direkt am IC platziert.
:::

:::tip
Für genaue Frequenzen empfiehlt sich Pin 5 (CV) über 10 nF nach GND abzublocken — verhindert Störeinstreuung auf die Referenzspannung.
:::

:::warning
Der Ausgang (Pin 3) kann zwar 200 mA liefern, jedoch erhitzt sich der NE555 bei Dauerlast über 100 mA deutlich. Kühlkörper oder Strombegrenzung vorsehen.
:::

:::danger
Nie mehr als 15 V an Vcc anlegen! Oberhalb dieser Grenze wird das IC irreversibel zerstört — auch kurze Spannungsspitzen können genügen.
:::

### Layout-Blöcke — HBox / VBox

Vergleich Monostabiler vs. Astabiler Betrieb:

:::hbox
:::vbox
## Monostabil
**Einmalige Ausgabe** nach Trigger-Impuls.

- Nur ein Widerstand + ein Kondensator
- Pulsbreite: `t = 1.1 * R * C`
- OUT bleibt HIGH während der Entladung

:::warning
TRIG muss kürzer sein als die Pulsbreite, sonst bleibt OUT dauerhaft HIGH.
:::
:::
:::vbox
## Astabil
**Freilaufender Oszillator** ohne externe Trigger.

- Zwei Widerstände + ein Kondensator
- Frequenz: `f = 1.44 / ((R_A + 2*R_B) * C)`
- Duty Cycle > 50 % (R_A > 0)

:::tip
Mit einer Diode parallel zu R_B lässt sich 50 % Duty Cycle erreichen.
:::
:::
:::
