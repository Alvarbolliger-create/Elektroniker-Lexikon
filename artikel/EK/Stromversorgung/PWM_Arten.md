---
title: PWM-Arten
kategorie: EK
tags: [PWM, pulsweitenmodulation, CCM, DCM, frequenz, tastverhältnis, H-brücke, FOC, totzeit, shoot-through, duty-cycle]
symbol: —
einheit: %, Hz
---

PWM (Pulsweitenmodulation) ist die häufigste Methode um analoge Grössen mit digitalen Schaltungen zu steuern. Das Tastverhältnis kodiert den gewünschten Wert.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale]]
- [[MOSFET]]
:::
:::vbox
**Verwandte Artikel**
- [[Buck Converter]]
- [[LED-Ansteuerung]]
- [[BLDC Motor]]
:::
:::

---

## Grundprinzip

Ein digitaler Ausgang schaltet periodisch zwischen HIGH und LOW. Das Verhältnis der HIGH-Zeit zur Gesamtperiode ist das Tastverhältnis (Duty Cycle):

```
D = t_ein / T     # 0 bis 1 (oder 0 bis 100 %)
```

Nach einem Tiefpass ergibt sich am Ausgang eine Gleichspannung proportional zum Duty Cycle.

## Einfache PWM

Feste Frequenz, variables Tastverhältnis. Einfachste Variante, von fast jedem Mikrocontroller-Timer erzeugt.

Einsatz: LED-Dimming, Servo-Ansteuerung, DAC-Ersatz.

## Komplementäre PWM (für H-Brücke)

Zwei komplementäre Ausgänge mit einstellbarer Totzeit (Dead Time). HIGH- und LOW-Seite schalten nie gleichzeitig, um Shootthrough zu verhindern.

Einsatz: DC-Motorsteuerung, BLDC, Halbbrücken-Schaltregler.

## Phasenkorrigierte (Phase-Correct) PWM

Zähler läuft hoch und dann runter statt überzulaufen. Das erzeugt eine symmetrische PWM mit halber Frequenz, aber der Schaltzeitpunkt liegt immer in der Mitte der Periode.

Vorteil: Geringere Oberschwingungen, besser für Motoransteuerung.

## Drei-Phasen-PWM (für BLDC/Servo)

Drei Halbbrücken mit 120° Phasenversatz zueinander. Erzeugt drei Spannungen für die drei Motorphasen. Notwendig für sinusförmige Kommutierung (FOC).

## Schaltregler: CCM und DCM

**CCM (Continuous Conduction Mode)**: Der Induktivitätsstrom fliesst immer. Stabil, gut regelbar, geringe Stromwelligkeit.

**DCM (Discontinuous Conduction Mode)**: Induktivitätsstrom fällt auf Null. Bei geringer Last automatisch. Andere Übertragungsfunktion als CCM, Regler muss das berücksichtigen.

## Frequenzwahl

Höhere Frequenz: kleinere Filterelemente, geringere Stromwelligkeit, aber mehr Schaltverluste. Typisch:
- Einfache Ansteuerung: 1-20 kHz
- Schaltregler: 100-500 kHz (Si-FET), bis einige MHz (GaN)
