---
title: OPV Grundlagen
kategorie: EK
kapitel: OPV
tags: [operationsverstärker, opv, differenzverstärker, open loop, gegenkopplung, golden rules, virtueller nullpunkt, slew rate, offsetspannung, gbw, rail-to-rail, lm741, tl071]
groessen: A_ol|Leerlaufverstärkung|dB; GBW|Gain-Bandwidth-Product|Hz; SR|Slew Rate|V/µs; U_off|Offsetspannung|mV; CMRR|Gleichtaktunterdrückung|dB
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BJT Emitterschaltung]]
- [[Verstärkung & Dämpfung]]
:::
:::vbox
**Verwandte Artikel**
- [[Komparator]]
- [[Schmitt-Trigger Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[OPV Invertierender Verstärker]]
- [[OPV Nichtinvertierender Verstärker]]
- [[OPV Spannungsfolger]]
:::
:::

---

Der Operationsverstärker (OPV) ist der vielseitigste analoge Baustein. Intern ist er ein galvanisch gekoppelter Differenzverstärker mit sehr hoher Leerlaufverstärkung. Mit externer Beschaltung lässt sich fast jede analoge Funktion realisieren.

## Eigenschaften des idealen OPV

- **Unendliche Leerlaufverstärkung** A_ol → Schaltungsverstärkung wird nur durch externe Widerstände bestimmt
- **Unendliche Eingangsimpedanz** → kein Strom fliesst in die Eingänge
- **Ausgangswiderstand null** → Ausgang kann beliebige Last treiben
- **Zwei symmetrische Versorgungsspannungen** gleichen Betrags (+V und -V)
- **Eingänge**: invertierend (–) und nichtinvertierend (+)

Für die Praxis reichen diese Näherungen in fast allen Fällen.

## Grundprinzip

:::schematic OPV-Schaltsymbol: Dreieck mit invertierendem Eingang (−) oben links, nichtinvertierendem Eingang (+) unten links, Ausgang U_a rechts. Versorgungsanschlüsse V+ und V− am Dreieck. Differenzspannung U_d = U_+ − U_−
/schaltplaene/symbole/OPV.svg
:::

Der OPV verstärkt die Differenz der beiden Eingänge:

:::formel
U_a = A_ol * (U_+ - U_-)    # ohne Gegenkopplung: Ausgang schlägt sofort an Schiene
:::

Bei A_ol = 100 000 genügen 0.1 mV Differenz um den Ausgang voll auszusteuern. Ohne Gegenkopplung ist der OPV als Komparator verwendbar — mit Gegenkopplung als präziser Verstärker.

## Goldene Regeln (mit Gegenkopplung)

Aus der unendlichen Verstärkung folgen die Goldenen Regeln für Berechnungen:

1. **Kein Strom in die Eingänge** (unendliche Eingangsimpedanz)
2. **U_+ = U_–** (virtuelle Kurzschluss — der OPV regelt seinen Ausgang so, dass die Differenz null wird)

Diese Regeln gelten nur solange die Gegenkopplung aktiv ist und der Ausgang nicht sättigt.

## Wichtige Kennwerte

| Kenngrösse | Symbol | Typischer Wert | Bedeutung |
|---|---|---|---|
| Leerlaufverstärkung | A_ol | 100 dB (10⁵) | Ohne Gegenkopplung |
| Gain-Bandwidth-Product | GBW | 1–10 MHz | f_3dB × Verstärkung = const |
| Slew Rate | SR | 0.5–13 V/µs | Max. Ausgangsänderung/Zeit |
| Offsetspannung | U_off | 0.1–5 mV | Fehler am Ausgang ohne Signal |
| Eingangs-Bias-Strom | I_B | 1 nA – 100 nA | Strom in die Eingänge |
| CMRR | — | 70–100 dB | Gleichtaktunterdrückung |

## Slew Rate

Die Slew Rate (SR) begrenzt wie schnell der Ausgang reagieren kann:

:::formel
SR = dU_a / dt_max          # Einheit: V/µs
U_max = SR / (2 * pi * f)   # maximale unverzerrte Amplitude bei Frequenz f
:::

:::monospace
Beispiel: SR = 0.5 V/µs (LM741), f = 10 kHz
U_max = 0.5e6 / (2π × 10e3) = 8 V_peak → darüber verzerrt das Signal
:::

## GBW — Bandbreite bei Verstärkung

Das GBW-Produkt ist für jeden OPV-Typ konstant:

:::formel
f_3dB = GBW / |A|    # Nutzbare Bandbreite bei gewählter Verstärkung
:::

:::monospace
OPV mit GBW = 1 MHz, Verstärkung 10× → f_3dB = 100 kHz
OPV mit GBW = 1 MHz, Verstärkung 100× → f_3dB = 10 kHz
:::

## Rail-to-Rail

Standard-OPVs erreichen den Ausgang nur bis 1–2 V vor der Versorgungsschiene. Bei ±15 V fällt das kaum auf. Bei 3.3 V Single-Supply fehlt ein grosser Teil des Aussteuerbereichs.

**RRIO** (Rail-to-Rail Input/Output): Ausgang und Eingang reichen bis auf wenige mV an die Schienen. Pflicht bei Batterie- und Mikrocontrollersystemen.

## Häufige Typen

| Typ | GBW | SR | Merkmal |
|---|---|---|---|
| LM741 | 1 MHz | 0.5 V/µs | Klassiker, ±15 V |
| LM358 | 1 MHz | 0.6 V/µs | Single-Supply, günstig |
| TL071 | 3 MHz | 13 V/µs | FET-Eingang, wenig Strom |
| MCP6001 | 1 MHz | 0.6 V/µs | RRIO, 1.8–6 V |
| OPA2134 | 8 MHz | 20 V/µs | Audio-Qualität |
