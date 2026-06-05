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

:::formel
SR = dU_out / dt_max    # z.B. 0.5 V/µs bei LM741, 13 V/µs bei TL071
:::
**Physikalische Ursache**: Im internen Aufbau eines OPVs gibt es einen Kompensationskondensator C_c (typisch einige Picofarad) am Eingangs-Differenzverstärker. Er verhindert Schwingungen (stabiler Betrieb mit Gegenkopplung). Dieser Kondensator muss umgeladen werden wenn der Ausgang springt. Der maximale Ladestrom I_bias begrenzt wie schnell das geht:

:::formel
SR = I_bias / C_c    # physikalisches Limit
:::
**Konsequenz**: Wenn das Eingangssignal sich schneller ändert als die Slew Rate erlaubt, verzerrt der Ausgang. Ein Sinus mit grosser Amplitude und hoher Frequenz kann "verclippt" werden.

:::formel
U_max_unverzerrung = SR / (2π × f)    # maximale unverzerrte Amplitude
:::
## Rail-to-Rail

Standard-OPVs können den Ausgang nur bis etwa 1–2 V an die Versorgungsschiene heranfahren. Bei ±15 V Versorgung fällt das kaum auf. Bei 3.3 V oder 5 V Single-Supply geht damit ein grosser Teil des nutzbaren Aussteuerbereichs verloren.

**Rail-to-Rail-Ausgang (RRO)**: Der Ausgang kommt bis auf wenige mV an +V und GND heran. Nötig bei Batterie- und Mikrocontroller-Systemen.

**Rail-to-Rail-Eingang (RRI)**: Auch die Eingänge können bis zu den Schienen ausgesteuert werden. Wichtig für Komparatoren und Puffer, die das volle Eingangssignal verarbeiten müssen.

Im Datenblatt erkennbar am Kürzel **RRIO** (Rail-to-Rail Input/Output) oder an der Ausgangsspannungs-Tabelle: steht dort z.B. V_out_max = V+ − 10 mV, ist es Rail-to-Rail.

## Häufige Typen

| Typ | Merkmal | Rail-to-Rail | Einsatz |
|---|---|---|---|
| LM741 | Klassiker | Nein (±15 V) | Lehre, alte Schaltungen |
| LM358 | Single-Supply, 3–32 V | Ausgang annähernd | Einfache Anwendungen |
| TL071 | FET-Eingang, wenig Strom | Nein | Audio, Präzision |
| MCP6001 | 1.8–6 V, RRIO | Ja | Batteriebetrieb, µC |
| OPA2134 | Audio-Qualität | Nein | Hi-Fi |
| LT1028 | Sehr tiefes Rauschen | Nein | Präzisionsmessung |
