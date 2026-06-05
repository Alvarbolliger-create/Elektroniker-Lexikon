---
title: Aktor mit Rückmeldung
kategorie: EK
tags: [rückmeldung, encoder, potentiometer, regelkreis, closed-loop, feedback, inkremental, absolut, resolver]
symbol: —
einheit: —
---

Ein Aktor mit Rückmeldung meldet seine aktuelle Position, Drehzahl oder einen anderen Zustand an die Steuerung zurück. Damit entsteht ein geschlossener Regelkreis — die Grundlage für präzise Automatisierung und Robotik.

:::hbox
:::vbox
**Voraussetzungen**
- [[Aktorik]]
- [[Sensorik]]
- [[Regelkreis]]
:::
:::vbox
**Verwandte Artikel**
- [[Servomotor]]
- [[Schrittmotor]]
- [[PID Regler]]
:::
:::vbox
**Führt weiter zu**
- [[Stabilitaet]]
:::
:::

---

## Offener vs. geschlossener Regelkreis

| | Open Loop | Closed Loop |
|---|---|---|
| Rückmeldung | Keine | Sensor misst Istwert |
| Fehlerkorrektur | Keine | Automatisch durch Regler |
| Genauigkeit | Hängt vom Aktor ab | Hoch, unabhängig von Störungen |
| Beispiel | [[Schrittmotor]] ohne Encoder | [[Servomotor]], CNC-Achse |

Ein [[Schrittmotor]] ohne Encoder ist open loop: Er bewegt sich um die befohlenen Schritte, weiss aber nicht, ob er angekommen ist. Bei Überlastung verliert er Schritte, ohne dass die Steuerung es bemerkt.

---

## Rückmeldesensoren

| Sensor | Messgrösse | Prinzip | Auflösung |
|---|---|---|---|
| Inkremental-Encoder | Winkel, Weg | Lichtschranke oder Hall | 100–10 000 Inkremente/U |
| Absolut-Encoder | Winkel | Optisch (Gray-Code) | 12–24 Bit |
| Potentiometer | Winkel | Widerstandsteilung | ~0,1–1° |
| Resolver | Winkel | Induktiv | Sehr präzise, robust, hitzebeständig |
| Linearer Encoder | Weg | Optisch oder magnetisch | < 1 µm |
| Linearpotentiometer | Weg | Widerstandsteilung | 0,1–1 mm |

---

## Regelschleife

:::formel
Soll-Position
    ↓
  [Vergleich] ← Ist-Position (Encoder)
    ↓ Regelfehler
  [PID-Regler]
    ↓ Stellgrösse
  [Treiber / Verstärker]
    ↓
  [Motor / Aktor]
    ↓
  [Encoder] → Istwert zurück
:::

Typische Abtastraten: 10 ms für Positionsregelung, 1 ms für Drehzahlregelung, 100 µs für Stromregelung.

---

## Encoder-Typen im Detail

**Inkremental-Encoder** gibt Impulse pro Grad ab. Die Position wird durch Zählen der Impulse ermittelt. Nach Stromausfall ist die Position unbekannt — ein Referenzfahrt (Homing) ist nötig.

**Absolut-Encoder** kodiert jede Position als eindeutigen Binärwert (z.B. Gray-Code). Nach Stromausfall ist die Position sofort bekannt, kein Homing nötig.

:::formel
Inkremental: A-Kanal, B-Kanal (Richtungserkennung), Z-Kanal (Nullimpuls)
Absolut:     SSI, BiSS, EnDat oder parallele Binärausgabe
:::

---

## Echtzeitanforderungen

Mikrocontroller mit Hardware-Encoder-Interface (z.B. STM32 Timer im Encoder-Mode) lesen den Encoder ohne CPU-Last. Ohne Hardware-Support müssen Interrupts verwendet werden — bei hohen Drehzahlen wird das zum Engpass.

---

## Anwendungen

- CNC-Achsen (Linearencoder, < 10 µm Genauigkeit)
- Industrieroboter (Absolut-Encoder, 6 Freiheitsgrade)
- [[Servomotor|RC-Servos]] (Potentiometer als Feedback)
- Kamerastabilisierung (Gyro + Brushless-Motor)
- Medizintechnik (Chirurgieroboter, Infusionspumpen)
