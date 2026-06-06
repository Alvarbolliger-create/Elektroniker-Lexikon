---
title: Fensterkomparator
kategorie: EK
kapitel: OPV
tags: [fensterkomparator, window comparator, obere schwelle, untere schwelle, spannungsüberwachung, band, wired-and, open-collector]
groessen: U_S_oben|Obere Schwelle|V; U_S_unten|Untere Schwelle|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Komparator]]
:::
:::vbox
**Verwandte Artikel**
- [[Komparator]]
- [[Schmitt-Trigger]]
:::
:::vbox
**Führt weiter zu**
- [[Regelkreis Grundlagen]]
:::
:::

---

Ein Fensterkomparator prüft ob eine Spannung innerhalb eines definierten Bereichs (Fensters) liegt. Er besteht aus zwei Komparatoren mit einem gemeinsamen Eingang und unterschiedlichen Referenzen.

## Aufbau und Funktion

:::schematic Fensterkomparator: Zwei Komparatoren (IC1A, IC1B) mit Open-Collector-Ausgang. Beide Eingangssignale U_in parallel an (−) beider Komparatoren. IC1A: (+) an U_S_oben. IC1B: (+) an U_S_unten. Beide Kollektor-Ausgänge zusammen am R_pullup (nach V_cc). Gemeinsamer Ausgangsknoten U_out. Spannungsteiler R1–R4 von V_cc nach GND für U_S_oben und U_S_unten. Wired-AND: HIGH nur wenn beide Transistoren sperren (U_in im Fenster)
/Diagramm/fensterkomparator.svg
:::

Zwei Komparatoren mit Open-Collector-Ausgang teilen sich einen Pullup:

- **Komparator IC1A** (obere Schwelle): schaltet wenn U_in > U_S_oben
- **Komparator IC1B** (untere Schwelle): schaltet wenn U_in < U_S_unten

Die Ausgänge sind über einen gemeinsamen Pullup zusammengeschaltet (Wired-AND). Der Ausgang ist nur dann HIGH (kein Transistor leitet), wenn U_in innerhalb des Fensters liegt.

## Wahrheitstabelle

| Eingangsspannung | IC1A | IC1B | U_Out |
|---|---|---|---|
| U_in < U_S_unten | sperrt | leitet | LOW (0.7 V) |
| U_S_unten ≤ U_in ≤ U_S_oben | sperrt | sperrt | HIGH (5 V) |
| U_in > U_S_oben | leitet | sperrt | LOW (0.7 V) |

## Schwellen einstellen

Die Schwellen werden mit einem Spannungsteiler aus R1, R2, R3, R4 an der Versorgungsspannung eingestellt:

:::formel
U_S_oben  = V_cc * R1 / (R1 + R2 + R3 + R4)    # obere Schwelle am (+) von IC1A
U_S_unten = V_cc * (R1 + R2) / (R1 + R2 + R3 + R4)    # untere Schwelle am (+) von IC1B
:::

## Anwendungen

**Batteriespannungsüberwachung**: Fenster zwischen 11 V und 13.5 V — ausserhalb leuchtet eine Warn-LED.

**Temperaturregelung mit Band**: NTC-Spannungsteiler im Fenster → Heizung bleibt aus. Ausserhalb → Heizung an.

**ADC-Überwachung**: Prüfen ob ein analoges Signal im gültigen Eingangsbereich liegt, bevor es gewandelt wird.

:::tip
Mit Open-Collector-Komparatoren (LM339) sind keine zusätzlichen Logikgatter nötig — die Wired-AND-Funktion entsteht durch einfaches Zusammenschalten der Ausgänge an einem Pullup-Widerstand.
:::
