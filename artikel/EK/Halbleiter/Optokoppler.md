---
title: Optokoppler
kategorie: EK
tags: [optokoppler, galvanische trennung, LED, fototransistor, CTR, isolation, PC817, 4N35, schaltnetzteil, SPS]
symbol: —
einheit: —
---

Ein Optokoppler überträgt Signale durch Licht. Elektrisch sind Eingang und Ausgang vollständig voneinander getrennt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[BJT Transistor]]
:::
:::vbox
**Verwandte Artikel**
- [[Relais und Schütze]]
- [[LED-Ansteuerung]]
:::
:::

---

## Aufbau

Im Gehäuse sitzt eine Infrarot-LED und ein Fototransistor oder Fotodiode einander gegenüber. Strom durch die LED erzeugt Licht, das den Transistor steuert.

Die Eingangseite (LED) und Ausgangseite (Transistor) sind galvanisch getrennt. Typische Isolationsspannung: 1000-5000 V.

## CTR (Current Transfer Ratio)

Der CTR gibt das Verhältnis von Kollektorstrom zu LED-Strom an:

```
CTR = I_C / I_LED × 100 %
```

Typischer CTR: 50-300 %. Hoher CTR: Ausgangs-Transistor kann viel Strom liefern. CTR sinkt mit Alter und Temperatur.

## Schaltbetrieb

Für digitale Signalübertragung: LED an mit Vorwiderstand, Transistor schaltet Last.

Vorwiderstand für die LED:
```
R = (U_in - U_F) / I_LED
```
Typisch: U_F = 1.2 V, I_LED = 5-20 mA.

Am Ausgang zieht ein Pull-up-Widerstand das Signal auf HIGH, der Transistor zieht es auf LOW.

## Geschwindigkeit

Optokoppler sind langsam. Standard-Typen (4N35, PC817): 10-50 kHz. Schnelle Typen (6N137, HCPL-2631): bis einige MHz. Für hohe Schaltfrequenzen den richtigen Typ wählen.

## Anwendungen

- Signaltrennung zwischen 230-V-Seite und Steuerschaltung
- SPS-Eingangskarten (24-V-Signal galvanisch getrennt einlesen)
- Schaltnetzteil-Rückkopplungskreis (Optokoppler überträgt Fehlersignal)
- CAN/RS485 Busabschluss mit Isolation

:::tip
PC817 ist das günstigste und am häufigsten verwendete Optokoppler-IC. Für einfache Anwendungen unter 10 kHz ist es ideal. Für Schaltregler-Feedback auf SNR und Phase achten.
:::
