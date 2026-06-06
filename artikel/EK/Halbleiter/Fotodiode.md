---
title: Fotodiode
kategorie: EK
kapitel: Halbleiter
tags: [fotodiode, photodiode, lichtempfindlich, photostrom, sperrstrom, photoeffekt, photoelektrischer effekt, sensor, umgebungslicht]
groessen: I_ph|Photostrom|µA; η|Quanteneffizienz|%; C_j|Sperrschichtkapazität|pF; U_R|Sperrspannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[pn-Übergang]]
:::
:::vbox
**Verwandte Artikel**
- [[Optokoppler]]
- [[Lichtsensor]]
:::
:::vbox
**Führt weiter zu**
- [[Optokoppler]]
:::
:::

---

Eine Fotodiode erzeugt bei Lichteinfall einen messbaren Strom. Je mehr Licht, desto mehr Strom. Sie arbeitet normalerweise in **Sperrrichtung** — das Licht erzeugt den Sperrstrom.

## Funktionsprinzip

Photonen mit ausreichend Energie (E = h·f > E_g) können Elektronen aus dem Valenzband in das Leitungsband heben und damit Elektron-Loch-Paare erzeugen. In der Raumladungszone der Diode werden diese Träger durch das interne elektrische Feld sofort getrennt und als **Photostrom I_ph** abgeführt.

:::formel
I_ph = η * (P_opt * q) / (h * f)    # Photostrom (vereinfacht)
:::

Der Photostrom ist **proportional zur Beleuchtungsstärke** — das ist der wichtigste Unterschied zu anderen Lichtdetektoren.

## Schaltsymbol

:::schematic Fotodiode
/schaltplaene/symbole/D_Foto.svg
:::

Wie eine Diode, aber mit zwei eingehenden Pfeilen (Licht).

## Betriebsmodi

### Photovoltaischer Modus (ohne externe Spannung)
Die Diode arbeitet wie eine Solarzelle — sie erzeugt selbst eine Spannung. Nachteil: langsam (grosse Sperrschichtkapazität muss umladen).

### Sperrbetrieb / Photokonduktiver Modus (mit externer Sperrspannung)
Die externe Sperrspannung verbreitert die Raumladungszone → kleinere Kapazität → **schnellere Reaktion**. Die Diode wird mit umgekehrter Polung betrieben, der Photostrom fliesst als Sperrstrom.

:::formel
I_gesamt = I_ph - I_S * (exp(U / U_T) - 1)    # U negativ im Sperrbetrieb
:::

Im Sperrbetrieb dominiert I_ph. Die Schaltung ist einfach: Widerstand in Serie, Spannung über Widerstand messen.

## Dunkelstrom

Ohne Licht fliesst auch im Sperrbetrieb ein kleiner Strom — der **Dunkelstrom**. Er entspricht dem normalen Sperrstrom der Diode und steigt mit Temperatur stark an. Bei Präzisionsmessungen muss er abgezogen oder kompensiert werden.

## Kennwerte

| Kenngrösse | Bedeutung | Typischer Wert |
|---|---|---|
| I_ph | Photostrom bei 1 mW/cm² | 10–100 µA |
| I_dark | Dunkelstrom | 1 nA – 10 nA |
| λ_peak | Empfindlichkeitspeak | 850–950 nm (Si) |
| t_rise | Anstiegszeit | 2 ns – 1 µs |
| C_j | Sperrschichtkapazität | 2 pF – 100 pF |

## Anwendungen

**Lichtsensor** im Sperrbetrieb mit Transimpedanzverstärker (OPV) → genaue Strommessung.

**Optokoppler**: LED + Fotodiode/Fototransistor in einem Gehäuse für galvanische Trennung → [[Optokoppler]].

**Barcode-Scanner, Laserempfänger, Lichtschranken**: Schnelle Fotodioden (< 10 ns) erkennen Signale im MHz-Bereich.

**Strahlungsmessung**: UV- oder Röntgenlicht (bei geeignetem Material oder Szintillator).

:::tip
Für schnelle Anwendungen (> 1 MHz) immer im Sperrbetrieb mit kleinem Lastwiderstand betreiben und die Sperrschichtkapazität aus dem Datenblatt berücksichtigen. Die Bandbreite ist f = 1/(2π·R·C_j).
:::
