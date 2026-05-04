---
title: Frequenzumrichter
kategorie: EK
tags: [frequenzumrichter, VFD, drehstrom, drehzahlregelung, IGBT, PWM, zwischenkreis, U-f-kennlinie, oberschwingungen, sanftanlauf, rückspeisung]
symbol: —
einheit: Hz
---

Ein Frequenzumrichter (FU) stellt Frequenz und Spannung einer Drehstromversorgung variabel ein. Damit lässt sich die Drehzahl eines Asynchronmotors stufenlos regeln.

:::hbox
:::vbox
**Voraussetzungen**
- [[IGBT]]
- [[Drehstrom: Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[PWM-Arten]]
- [[Encoder & Resolver]]
:::
:::vbox
**Führt weiter zu**
- [[Motorenansteuerung]]
:::
:::

---

## Aufbau

**Gleichrichter**: Netz-Wechselspannung auf Zwischenkreis-Gleichspannung. Typisch 565 V DC aus 400 V AC.

**Zwischenkreis**: Grosser Kondensator glättet die Spannung. Puffer für Lastspitzen.

**Wechselrichter (Inverter)**: Sechs IGBTs schalten den Zwischenkreis mit PWM auf drei Ausgangsphasen. Frequenz und Spannung einstellbar.

## U/f-Kennlinie

Spannung und Frequenz werden proportional geändert. Bei halber Frequenz auch halbe Spannung. So bleibt das Motordrehmoment konstant.

:::monospace
U / f = const.      # U/f-Verhältnis konstant halten für konstantes Drehmoment
:::
## Vorteile

Sanftanlauf: kein Anlaufstrom-Spikes. Energiesparen bei Pumpen und Lüftern (Drehzahl bei halber Last senken, Leistung sinkt auf ⅛). Rückspeisung ins Netz möglich (Bremsenergie).

## Oberschwingungen

Frequenzumrichter erzeugen Oberschwingungen im Netz. Das belastet andere Geräte. Eingangsfilter oder aktive Frontend-Einheiten reduzieren die Rückwirkung.

:::warning
Motorleitungen bei Frequenzumrichtern geschirmt ausführen und so kurz wie möglich halten. Der schnelle PWM erzeugt starke hochfrequente Störungen. Ungeschirmte Leitungen wirken als Antenne.
:::

## Typische Kenndaten

| Grösse | Wert |
|---|---|
| Eingangsfrequenz | 50/60 Hz |
| Ausgangsfrequenz | 0 bis 400 Hz |
| Zwischenkreisspannung | 565 V DC (bei 400 V) |
| Schaltfrequenz IGBT | 2 bis 16 kHz |
| Wirkungsgrad | 95 bis 98 % |
