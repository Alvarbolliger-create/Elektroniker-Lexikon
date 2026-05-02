---
title: Thermisches Rauschen (Johnson-Nyquist-Rauschen)
kategorie: EK
tags: [Rauschen, thermisches Rauschen, Johnson-Rauschen, Nyquist, Rauschspannung, SNR]
symbol: U_n
einheit: V/sqrt(Hz)
---

Jeder Widerstand erzeugt ein Rauschen durch die thermische Bewegung der Elektronen. Dieses Rauschen ist fundamental — es kann nicht durch bessere Schaltungstechnik eliminiert werden, nur durch Kühlung oder kleinere Widerstände reduziert werden.

:::hbox
:::vbox
**Voraussetzungen**
- [[Widerstand]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Verstärker (Typen)]]
- [[ADC/DAC Grundlagen]]
:::
:::

---

## Physikalische Ursache

Elektronen in einem Leiter führen zufällige thermische Bewegungen aus (Brownsche Bewegung). Diese Bewegungen erzeugen kleine, zufällige Spannungsfluktuationen. Die Energie dieser Schwingungen ist proportional zur absoluten Temperatur.

## Rauschspannung

```
U_n = sqrt(4 × k × T × R × B)    # k = 1.38e-23 J/K, T in Kelvin, R in Ohm, B = Bandbreite in Hz
```

Oder als Rauschspannungsdichte (unabhängig von der Bandbreite):

```
u_n = sqrt(4 × k × T × R)    # V/sqrt(Hz)
```

Bei Raumtemperatur (T = 300 K):
```
u_n ≈ 4 nV/sqrt(Hz) × sqrt(R/1kΩ)    # Näherung bei 300 K
```

## Typische Werte

| Widerstand | Rauschspannungsdichte (300 K) |
|---|---|
| 100 Ω | 1.3 nV/√Hz |
| 1 kΩ | 4.1 nV/√Hz |
| 10 kΩ | 13 nV/√Hz |
| 100 kΩ | 41 nV/√Hz |
| 1 MΩ | 130 nV/√Hz |

Über eine Bandbreite von 10 kHz (typisch Audio):

| Widerstand | Effektive Rauschspannung (10 kHz BW) |
|---|---|
| 1 kΩ | 0.41 µV |
| 10 kΩ | 1.3 µV |
| 100 kΩ | 4.1 µV |

## Charakteristika

**Weisses Rauschen**: Thermisches Rauschen ist "weiss" — die Leistungsdichte ist gleichmässig über alle Frequenzen verteilt (bis zur Plasma-Frequenz des Materials, praktisch unbegrenzt).

**Gaussche Verteilung**: Die Momentanwerte folgen einer Normalverteilung.

**Unkorreliert**: Die Rauschquellen verschiedener Widerstände sind statistisch unabhängig. Leistungen addieren sich (nicht Spannungen): `U_gesamt = sqrt(U1² + U2²)`.

## Einfluss auf Schaltungen

### Vorverstärker / rauscharme Verstärker (LNA)

Am Eingang eines Verstärkers erzeugt der Quellwiderstand Rauschspannung. Der Verstärker selbst erzeugt ebenfalls Rauschen (Rauschzahl NF).

Das Signal-zu-Rausch-Verhältnis (SNR) wird durch das erste Bauteil in der Signalkette dominiert — "Friis-Formel" für mehrstufige Systeme.

### Massnahmen

- Widerstände so klein wie möglich wählen (weniger Rauschen)
- Kühlung (Kryostat): Rauschen sinkt mit sqrt(T)
- Bandbreite begrenzen (Tiefpassfilter): Rauschen ∝ sqrt(B)
- Differentielle Schaltungen: Gleichtaktrauschen unterdrücken

:::info
Thermisches Rauschen ist das Grundlimit jeder Messung. In der Radioastronomie werden Empfänger auf wenige Kelvin gekühlt, um das Rauschen unter das Signal zu drücken. In normaler Elektronik ist es der Grund, warum Hochohmschaltungen immer rauschiger sind.
:::
