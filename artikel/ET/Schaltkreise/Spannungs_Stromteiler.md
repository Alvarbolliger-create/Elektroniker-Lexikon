---
title: Spannungs- & Stromteiler
kategorie: ET
tags: [spannungsteiler, stromteiler, widerstand, belasteter spannungsteiler, unbelastet, reihenschaltung, parallelschaltung, pegelwandler]
symbol: —
einheit: —
---

Zwei grundlegende Schaltungen: Der Spannungsteiler gibt eine Teilspannung aus. Der Stromteiler verteilt einen Strom auf zwei Zweige.

:::hbox
:::vbox
**Voraussetzungen**
- [[Kirchhoffsche Gesetze]]
:::
:::vbox
**Verwandte Artikel**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[Wheatstone-Brücke]]
:::
:::

---

## Spannungsteiler

R1 und R2 in Reihe an U_ein. Am Verbindungspunkt liegt U_aus.

```
U_aus = U_ein * R2 / (R1 + R2)
```

Die Spannung teilt sich proportional zu den Widerständen auf. Ein Potentiometer ist ein einstellbarer Spannungsteiler.

**Typische Anwendungen:** Pegelanpassung, Sensor-Vorspannung, Referenzspannung für ADC-Eingänge.

### Belasteter Teiler

Sobald eine Last R_L parallel zu R2 liegt, sinkt U_aus. Die Parallelschaltung aus R2 und R_L ersetzt R2 in der Formel:

```
U_aus = U_ein * (R2 || R_L) / (R1 + (R2 || R_L))
R2 || R_L = (R2 * R_L) / (R2 + R_L)
```

Faustregel: Der Teiler-Ruhestrom sollte mindestens zehnmal grösser sein als der Laststrom.

| R1 | R2 | U_aus bei 12 V |
|---|---|---|
| 1.4 kΩ | 1 kΩ | 5.0 V |
| 14 kΩ | 10 kΩ | 5.0 V |

Beide Teiler geben dieselbe Spannung, aber der erste zieht zehnmal mehr Ruhestrom und ist damit unempfindlicher gegenüber einer Last.

---

## Stromteiler

R1 und R2 parallel an einer Stromquelle I_ges. Der Strom verteilt sich umgekehrt proportional zu den Widerständen.

```
I_1 = I_ges * R2 / (R1 + R2)
I_2 = I_ges * R1 / (R1 + R2)
```

**Typische Anwendungen:** Strommessung mit Shunt-Widerstand, Parallelschalten von Bauteilen.

### Beispiel

100 mA, R1 = 100 Ω, R2 = 300 Ω:

| Grösse | Berechnung | Ergebnis |
|---|---|---|
| I_1 | 100 mA × 300 / (100 + 300) | 75 mA |
| I_2 | 100 mA × 100 / (100 + 300) | 25 mA |
