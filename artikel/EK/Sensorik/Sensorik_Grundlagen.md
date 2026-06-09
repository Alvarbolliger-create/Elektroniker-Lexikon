---
title: Sensorik Grundlagen
kategorie: EK
kapitel: Sensorik
tags: [sensor, wandler, messbereich, auflösung, genauigkeit, linearität, empfindlichkeit, kennlinie, offset, drift, resistiv, kapazitiv, wheatstone]
groessen: E|Empfindlichkeit|—; U_off|Offset|V; delta_x|Auflösung|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[NTC & PTC Thermistoren]]
- [[Hall-Sensor]]
- [[Lichtsensor]]
:::
:::vbox
**Führt weiter zu**
- [[NTC & PTC Thermistoren]]
- [[Hall-Sensor]]
- [[Lichtsensor]]
- [[Regelkreis Grundlagen]]
:::
:::

---

Ein Sensor wandelt eine **physikalische Grösse** (Temperatur, Licht, Kraft, Magnetfeld …) in ein **elektrisches Signal** (Spannung, Strom, Widerstand) um, das sich weiterverarbeiten lässt.

## Sensortypen nach Ausgangssignal

| Sensorprinzip | Ausgangssignal | Beispiele |
|---|---|---|
| Resistiv | Widerstandsänderung | NTC, PTC, LDR, DMS, PT100 |
| Kapazitiv | Kapazitätsänderung | Feuchte, Füllstand, Beschleunigung |
| Induktiv | Induktivitätsänderung durch Wirbelströme | Näherungsschalter, LVDT — **erkennt ausschliesslich metallische Objekte** |
| Halleffekt | Spannung (analog/digital) | Hall-Sensor, Stromsensor |
| Fotovoltaisch | Strom / Spannung | Fotodiode, Fototransistor |
| Thermoelektrisch | Thermospannung (µV) | Thermoelement (Typ K, J …) |
| Digital | Frequenz / Puls | Encoder, Ultraschall |

### Induktiver Sensor — Metallerfassung

Ein induktiver Sensor erzeugt ein hochfrequentes Magnetfeld an seiner Spitze. Nähert sich ein **Metall**, entstehen im Metall **Wirbelströme** — diese entziehen dem Schwingkreis Energie, die Amplitude sinkt und der Sensor schaltet.

:::info
Induktive Sensoren erkennen **nur Metall** (leitfähige Werkstoffe). Kunststoff, Holz, Glas und andere Nichtleiter werden nicht erkannt. Für Kunststoff: kapazitiver Sensor.
:::

| Merkmal | Wert |
|---|---|
| Detektiertes Material | Metall (Eisen, Alu, Kupfer, …) |
| Schaltabstand | typisch 1–50 mm |
| Ausgang | PNP oder NPN Schalter (Digital) |
| Typische Anwendung | Endlagenerkennung, Zählen von Metallteilen |

## Wichtige Kenngrössen

**Empfindlichkeit** — Ausgangssignal pro Einheit der Eingangsgrösse:

:::formel
E = Delta_U_aus / Delta_x_ein    # z.B. mV/°C oder mV/T
:::

**Messbereich** — der Bereich der Eingangsgrösse, in dem der Sensor spezifiziert ist.

**Auflösung** — kleinste Änderung der Eingangsgrösse, die der Sensor noch erkennt.

**Genauigkeit** — maximale Abweichung vom wahren Wert (absolut oder in % vom Messbereich).

**Linearität** — Mass dafür, wie gut die Kennlinie einer Geraden folgt. Angabe: maximale Abweichung in % FSR (Full Scale Range).

**Offset** — Ausgangssignal ohne Eingangsgrösse (Nullpunktfehler). Kompensierbar durch Kalibrierung.

**Drift** — langsame Verschiebung des Nullpunkts oder der Empfindlichkeit über Zeit oder Temperatur.

**Hysterese** — unterschiedliche Ausgangswerte bei steigender vs. fallender Eingangsgrösse. Mechanisch bedingt (z. B. Kontaktierung, Reibung).

## Signalaufbereitung

:::schematic Wheatstone-Brücke mit Instrumentenverstärker: Brückenspannung U_B oben, GND unten. Linker Zweig: R1 (oben) und R_Sensor (unten). Rechter Zweig: R2 (oben) und R3 (unten). Differenzspannung U_diff zwischen Mittelabgriffen (je zwischen R1/R_Sensor und R2/R3). Instrumentenverstärker (IA) nimmt U_diff als Eingang und verstärkt → U_aus. Im Abgleich (kein Messwert): U_diff = 0. Bei Widerstandsänderung von R_Sensor: U_diff ≠ 0, proportional zur Änderung
/Diagramm/wheatstone_bruecke.svg
:::

Resistive Sensoren (NTC, DMS, PT100) werden häufig in einer **Wheatstone-Brücke** betrieben, um kleine Widerstandsänderungen als Differenzspannung zu gewinnen:

:::formel
U_diff = U_B * (R_Sensor / (R_Sensor + R_ref) - R3 / (R3 + R4))    # Brückenspannung
:::

Die kleine Differenzspannung wird anschliessend mit einem **Instrumentenverstärker** oder OPV verstärkt.

## Sensor-Auswahl: Entscheidungskriterien

| Kriterium | Frage |
|---|---|
| Messbereich | Welcher physikalische Bereich? |
| Genauigkeit | Wie viel Fehler ist tolerierbar? |
| Umgebung | Temperatur, Feuchtigkeit, EMV? |
| Schnittstelle | Analog (0–10 V, 4–20 mA) oder Digital (I²C, SPI)? |
| Kosten | Massenmarkt (NTC) vs. Präzision (PT100)? |
| Reaktionszeit | Schnell (µs, Fotodiode) oder langsam (s, NTC)? |

## Übersicht: Häufige Sensoren EFZ-Niveau

| Grösse | Sensor | Prinzip |
|---|---|---|
| Temperatur | NTC, PTC, PT100, LM35 | Resistiv / Spannung |
| Licht | LDR, Fotodiode, Fototransistor | Resistiv / Fotovoltaisch |
| Magnetfeld / Strom | Hall-Sensor | Halleffekt |
| Kraft / Druck | DMS (Dehnmessstreifen) | Resistiv (Brücke) |
| Abstand | Ultraschall, IR-Reflex | Laufzeit / Intensität |
| Winkel / Drehzahl | Encoder, Hall-Sensor | Digital / Halleffekt |

:::tip
Die meisten Sensoren liefern sehr kleine Signale (mV-Bereich). Immer auf die Signalaufbereitung achten: Verstärker, Tiefpass gegen Rauschen, und ggf. Kalibrierung gegen einen bekannten Referenzpunkt.
:::
