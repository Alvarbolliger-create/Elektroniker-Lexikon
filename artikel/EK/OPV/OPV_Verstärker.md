---
title: OPV als Verstärker
kategorie: EK
tags: [OPV, Verstärker, Instrumentenverstärker, Differenzverstärker, Gain]
symbol: A
einheit: —
---

OPVs sind die Grundlage für analoge Signalverarbeitung. Mit wenigen Widerständen wird aus einer Verstärkungsschaltung ein präzises Werkzeug.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Aufbau]]
- [[OPV Invertierend]]
- [[OPV Nichtinvertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[Frequenzgang und Verstärkungsfaktor]]
- [[Aktive Filter]]
:::
:::

---

## Differenzverstärker

Misst die Differenz zweier Signale. Unterdrückt Gleichtaktanteile (Common Mode).

Schaltung mit vier gleichen Widerständen R:

```
U_out = (U_2 - U_1) × R_f / R_in
```

Problem: Eingangsimpedanz abhängig von der Verstärkung, Widerstandsmatching kritisch.

## Instrumentenverstärker (INA)

Ein einfacher Differenzverstärker (ein OPV mit vier Widerständen) hat ein Problem: Die Eingangsimpedanz hängt von der Verstärkung ab, und Widerstandstoleranzen begrenzen den CMRR stark.

Der **3-OPV-Instrumentenverstärker** löst das:

**Aufbau**:
```
U_1 → [OPV A] ──┐
                  ├── [OPV C (Differenzverstärker)] → U_out
U_2 → [OPV B] ──┘
```

- OPV A und OPV B sind Pufferverstärker mit Gegenkopplung, zwischen deren invertierenden Eingängen ein einziger Widerstand R_G liegt
- Die beiden Ausgänge von A und B gehen auf einen klassischen Differenzverstärker (OPV C)

**Verstärkung**:
```
A = (1 + 2×R / R_G) × 1    # erste Stufe verstärkt, zweite subtrahiert
```
Die Verstärkung lässt sich mit einem einzigen Widerstand R_G einstellen.

**Entscheidender Vorteil gegenüber einfachem Differenzverstärker**:
- Die Eingänge gehen direkt auf die hochohmigen (+)-Eingänge der Pufferverstärker → nahezu unendliche Eingangsimpedanz
- Gleichtaktunterdrückung (CMRR) > 100 dB, unabhängig von Widerstandstoleranzen
- Keine Auswirkung der Verstärkungseinstellung auf die Eingangsimpedanz

CMRR (Common Mode Rejection Ratio) > 100 dB typisch.

Einsatz: DMS-Brücken, Thermoelemente, Bioelektronik, alles mit kleinen Differenzsignalen auf grossem Gleichtakt.

Typische ICs: INA128, INA333, AD8221.

## Transimpedanzverstärker (TIA)

Wandelt Strom in Spannung. Rückkopplung über Widerstand vom Ausgang zum invertierenden Eingang, Strom wird direkt in den Eingang eingespeist.

```
U_out = I_in × R_f
```

Einsatz: Fotodioden-Auswertung, Strommessung.

## Summerverstärker

Mehrere Eingangssignale werden über Widerstände addiert:

```
U_out = -R_f × (U_1/R_1 + U_2/R_2 + ...)
```

DAC-Aufbau, Audiomixer.

## Spannungs-Strom-Wandler (Howland-Strom)

Liefert einen definierten Strom unabhängig von der Last. Basis für Konstantstromquellen.

## Logarithmischer Verstärker (Log-Amp)

Der Logarithmische Verstärker erzeugt eine Ausgangsspannung proportional zum Logarithmus der Eingangsspannung. Dazu wird eine Diode oder ein BJT-Transistor in die Rückkopplungsschleife des OPV geschaltet:

```
Eingang → R_in → (−) → OPV → Ausgang
                         ↓
                   [Diode/BJT] in Rückkopplung
```

Das Verhalten basiert auf der exponentiellen Diodenkennlinie:

```
U_out = -U_T × ln(U_in / (I_S × R_in))    # U_T = 26 mV bei 25°C (Temperaturspannung)
```

**Vorteil**: Grosse Dynamikbereiche auf wenig Aussteuerbereich darstellen (z.B. Signale von 1 µV bis 1 V auf 0–1 V komprimieren).

**Nachteil**: Stark temperaturabhängig (U_T = k×T/q), Kalibration nötig. Nur für positive Eingangsspannungen.

**Antilog-Verstärker**: Diode/BJT am Eingang statt in der Rückkopplung — der Ausgang ist exponentiell zum Eingang.

Anwendungen: Dynamikkompression (Audio), dB-Messungen, Multiplikation zweier Signale (log + log = log(A×B)).

:::tip
Für schnelle Verstärkungen im µV-Bereich: Chopper-Stabilisierte OPVs (z.B. MAX4238) haben extrem niedriges Offset und Drift, aber begrenzte Bandbreite.
:::
