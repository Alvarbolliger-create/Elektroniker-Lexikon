---
title: OPV: Aufbau & Kennwerte
kategorie: EK
tags: [OPV, operationsverstärker, differenzverstärker, verstärkung, kennwerte, GBW, slew rate, offsetspannung, gegenkopplung, leerlaufverstärkung, LM741, TL071]
symbol: A
einheit: —
---

Der Operationsverstärker ist der vielseitigste analoge Baustein. Er verstärkt die Differenz seiner zwei Eingänge mit sehr hoher Verstärkung. Mit externer Beschaltung lässt sich fast jede analoge Funktion realisieren.

:::hbox
:::vbox
**Voraussetzungen**
- [[Als Verstärker (Arbeitspunkt)]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Invertierend]]
- [[OPV Nichtinvertierend]]
:::
:::vbox
**Führt weiter zu**
- [[OPV Invertierend]]
- [[OPV Nichtinvertierend]]
- [[OPV Komparator]]
:::
:::

---

## Grundprinzip

Zwei Eingänge: nichtinvertierend (+) und invertierend (-). Der OPV verstärkt die Differenz: U_aus = A × (U_+ - U_-).

Die Leerlaufverstärkung A ist sehr gross, typisch 100 000 bis 1 000 000. Ohne Gegenkopplung schlägt der Ausgang sofort an eine der Versorgungsschienen.

## Ideales Modell

Für Berechnungen mit Gegenkopplung gilt das ideale Modell:
- Unendliche Leerlaufverstärkung
- Unendlicher Eingangswiderstand (kein Strom in die Eingänge)
- Ausgangswiderstand null

Diese Annahmen vereinfachen die Berechnung stark und sind für die meisten praktischen Fälle ausreichend genau.

## Gegenkopplung

Durch Rückführung des Ausgangs auf den invertierenden Eingang entsteht ein stabiler, präzise definierbarer Verstärker. Die Schaltungsverstärkung hängt dann nur noch von äusseren Widerständen ab, nicht mehr von A.

## Wichtige Kennwerte

| Kennwert | Symbol | Typischer Wert | Bedeutung |
|---|---|---|---|
| Leerlaufverstärkung | A_OL | 100 dB | Verstärkung ohne Gegenkopplung |
| Einheitsverstärkungs-BW | GBW | 1 MHz | Grenzfrequenz bei Verstärkung 1 |
| Slew Rate | SR | 0.5 V/µs | Max. Ausgangsänderung pro Zeit |
| Offsetspannung | U_OS | 1 mV | Fehler am Ausgang ohne Signal |
| Versorgungsspannung | — | ±15 V, 3.3 V bis 36 V | Je nach Typ |

## Slew Rate

Die Slew Rate (SR) ist die maximale Änderungsgeschwindigkeit des Ausgangs:

```
SR = dU_out / dt_max    # z.B. 0.5 V/µs bei LM741, 13 V/µs bei TL071
```

**Physikalische Ursache**: Im internen Aufbau eines OPVs gibt es einen Kompensationskondensator C_c (typisch einige Picofarad) am Eingangs-Differenzverstärker. Er verhindert Schwingungen (stabiler Betrieb mit Gegenkopplung). Dieser Kondensator muss umgeladen werden wenn der Ausgang springt. Der maximale Ladestrom I_bias begrenzt wie schnell das geht:

```
SR = I_bias / C_c    # physikalisches Limit
```

**Konsequenz**: Wenn das Eingangssignal sich schneller ändert als die Slew Rate erlaubt, verzerrt der Ausgang. Ein Sinus mit grosser Amplitude und hoher Frequenz kann "verclippt" werden.

```
U_max_unverzerrung = SR / (2π × f)    # maximale unverzerrte Amplitude
```

## Häufige Typen

| Typ | Merkmal | Einsatz |
|---|---|---|
| LM741 | Klassiker, ±15 V | Lehre, alte Schaltungen |
| LM358 | Single-Supply, 3 V bis 32 V | Einfache Anwendungen |
| TL071 | FET-Eingang, wenig Strom | Audio, Präzision |
| OPA2134 | Audio-Qualität | Hi-Fi |
| LT1028 | Sehr tiefes Rauschen | Präzisionsmessung |
