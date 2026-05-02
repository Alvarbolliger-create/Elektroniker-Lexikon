---
title: Buck (Step-down)
kategorie: EK
tags: [buck, step-down, schaltregler, MOSFET, spule, PWM, effizienz, tastverhältnis, wirkungsgrad, EMV, schaltnetzteil, abwärtswandler, spannungsregler]
symbol: —
einheit: —
---

Der Buck-Wandler setzt eine höhere Spannung auf eine niedrigere um. Anders als der lineare Regler macht er das durch schnelles Schalten, nicht durch Verbrennen der Differenz. Wirkungsgrad bis über 95 % möglich.

:::hbox
:::vbox
**Voraussetzungen**
- [[FET / MOSFET]]
- [[Selbstinduktion]]
:::
:::vbox
**Verwandte Artikel**
- [[Boost (Step-up)]]
- [[Lineare Regler]]
:::
:::vbox
**Führt weiter zu**
- [[Batterietechnik]]
:::
:::

---

## Funktionsprinzip

Ein MOSFET schaltet mit hoher Frequenz (typisch 100 kHz bis 2 MHz). Wenn er leitet, fliesst Energie in die Spule. Wenn er sperrt, gibt die Spule die gespeicherte Energie über die Freilaufdiode weiter.

Der Kondensator am Ausgang glättet die Spannung.

## Tastverhältnis

```
U_aus = U_ein * D       # D = Tastverhältnis (0 bis 1); gilt im Idealfall
D = t_on / T            # Einschaltzeit durch Periodendauer
```

Die Regelschleife stellt D so ein, dass U_aus konstant bleibt, auch wenn U_ein oder der Laststrom schwankt.

## Wirkungsgrad

Verluste entstehen durch Schaltverluste im MOSFET, Flussspannung der Diode und Wicklungswiderstand der Spule. Trotzdem deutlich besser als lineare Regler.

```
eta = U_aus * I_aus / (U_ein * I_ein)   # typisch 85 bis 97 %
```

## Bauteilauswahl

**Spule**: Zu klein: starkes Ripple, Sättigung. Zu gross: langsame Regelung und teuer. Typisch: L so wählen dass Ripple 20 bis 40 % des Laststroms ist.

**Kondensator**: Ausgangskapazität begrenzt Spannungsripple. ESR des Kondensators bestimmt den Ripple mit.

:::warning
EMV beachten: Schaltregler erzeugen Störungen. Schaltknoten (SW-Pin) mit kurzer Leiterbahn. Eingangskondensator direkt am IC. Massefläche unter dem IC nicht unterbrechen.
:::

## Typische IC-Lösungen

| IC | U_ein | I_max | f_sw | Bemerkung |
|---|---|---|---|---|
| LM2596 | 4 bis 40 V | 3 A | 150 kHz | Einfach, alt |
| MP2307 | 4.75 bis 23 V | 3 A | 340 kHz | Kompakt, SMD |
| TPS54340 | 4.5 bis 42 V | 3.4 A | 200 kHz bis 2.5 MHz | Einstellbar |
