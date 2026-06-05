---
title: Quarz-Oszillator
kategorie: ET
tags: [quarz, oszillator, schwingkreis, frequenzreferenz, güte, piezoeffekt, serienresonanz, parallelresonanz]
groessen: f_s|Serienresonanzfrequenz|Hz; f_p|Parallelresonanzfrequenz|Hz; Q|Güte|—
_status: PORT  # ET_alt/Wechselstrom/Quarz_Oszillator.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Resonanz & Schwingkreise]]
:::
:::

---

Ein Quarz-Oszillator nutzt den Piezoeffekt von Quarzkristallen, um eine extrem stabile Frequenz zu erzeugen. Quarze haben Güten von Q = 10 000 bis 1 000 000 — millionenfach höher als LC-Schwingkreise.

## Piezoeffekt und elektrisches Ersatzschaltbild

Quarzkristalle verformen sich, wenn eine Spannung angelegt wird (**inverser Piezoeffekt**). Umgekehrt erzeugen sie eine Spannung bei mechanischer Verformung (**direkter Piezoeffekt**). Bei einer bestimmten Frequenz gerät der Kristall in mechanische Resonanz — und hält diese Resonanz durch sein elektrisches Feld aufrecht.

Das **elektrische Ersatzschaltbild** des Quarzes zeigt zwei Resonanzstellen:
- **Serienresonanzfrequenz f_s**: L_m und C_m in Reihe → minimale Impedanz
- **Parallelresonanzfrequenz f_p**: Serienresonanz mit zusätzlicher Elektrodenkapazität C_0 in Parallel → maximale Impedanz

Zwischen f_s und f_p (Abstand typisch einige kHz) verhält sich der Quarz induktiv — dieser Bereich wird für Oszillatoren genutzt.

## Stabilität und Güte

| Kennwert | LC-Schwingkreis | Quarz |
|---|---|---|
| Güte Q | 50 – 500 | 10 000 – 1 000 000 |
| Frequenzgenauigkeit | ±1 % | ±20 ppm bis ±1 ppm |
| Temperaturdrift | Hoch | Gering (temperaturkompensiert: <1 ppm) |

Die hohe Güte erklärt die Stabilität: Der Quarz "akzeptiert" nur eine sehr enge Frequenz — kleine Abweichungen werden stark gedämpft.

## Typische Frequenzen und Anwendungen

| Frequenz | Anwendung |
|---|---|
| 32,768 kHz | Uhrenquarz (2¹⁵ Hz → einfache Teilung auf 1 Hz) |
| 4 – 25 MHz | Mikroprozessor-Takt |
| 12 MHz, 16 MHz | Arduino, Mikrocontroller |
| 27 MHz, 433 MHz | Fernsteuerungen (SAW-Resonator) |
| > 100 MHz | HF-Kommunikation (Oberwellenquarz) |

## Temperaturkompensierung (TCXO, OCXO)

Standard-Quarze driften mit der Temperatur um typisch ±50 ppm:
- **TCXO** (Temperature Compensated Crystal Oscillator): Elektronische Kompensation, ±0,5 ppm
- **OCXO** (Oven Controlled Crystal Oscillator): Quarz im Ofen auf konstante Temperatur gehalten, < 0,01 ppm. Verwendet in GPS, Messtechnik.

:::tip
Für Mikroprozessoren ist die absolute Frequenzgenauigkeit meist unkritisch — aber der Uhrenquarz (32,768 kHz) im RTC (Real Time Clock) muss über Jahre stabil sein: ±20 ppm bedeuten nur 10 Minuten Abweichung pro Jahr.
:::
