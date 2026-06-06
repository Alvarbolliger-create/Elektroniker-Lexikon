---
title: Optokoppler
kategorie: EK
kapitel: Halbleiter
tags: [optokoppler, galvanische trennung, isolation, led, fototransistor, ctr, stromübertragungsverhältnis, potentialfrei, 4n25, pc817]
groessen: CTR|Stromübertragungsverhältnis|%; I_F|LED-Strom|mA; I_C|Ausgangsstrom|mA; U_iso|Isolationsspannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[LED]]
- [[Fotodiode]]
- [[BJT Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Schaltregler Topologien]]
:::
:::vbox
**Führt weiter zu**
- [[Schaltregler Topologien]]
:::
:::

---

Ein Optokoppler überträgt ein Signal optisch — per Lichtstrahlung — von einem Stromkreis in einen anderen, ohne elektrische Verbindung. Er trennt zwei Schaltungsteile galvanisch und schützt gleichzeitig empfindliche Steuerkreise vor gefährlichen Spannungen.

## Aufbau

:::schematic Optokoppler-Aufbau: Eingangseite (LED mit Vorwiderstand) → Lichtstrahl durch isolierendes Medium → Ausgangseite (Fototransistor mit Lastwiderstand), galvanische Trennstrecke markiert
/Diagramm/optokoppler_aufbau.svg
:::

Ein Optokoppler besteht aus:
- **Eingangseite**: LED (meist infrarot, 950 nm)
- **Ausgangseite**: Fotoempfänger (Fotodiode, Fototransistor oder Fototriac)
- **Dazwischen**: Optisch transparentes, elektrisch isolierendes Material

Beide Seiten sind in einem gemeinsamen IC-Gehäuse untergebracht, aber elektrisch vollständig getrennt.

## Wichtigste Kenngrösse: CTR

Das **Current Transfer Ratio (CTR)** gibt das Verhältnis von Ausgangsstrom zu Eingangsstrom an:

:::formel
CTR = I_C / I_F * 100    # in Prozent; I_C = Kollektorstrom Ausgang, I_F = LED-Strom
:::

Typische CTR-Werte: 20 % bis 300 % (je nach Typ und Alterung).

:::warning
Der CTR sinkt mit der Lebensdauer der LED (Degradation) und mit steigender Temperatur. Schaltungen müssen so ausgelegt sein, dass sie auch mit dem minimalen CTR-Wert aus dem Datenblatt noch funktionieren.
:::

## Grundschaltung (Fototransistor-Ausgang)

**Eingang**: LED mit Vorwiderstand R1 nach +V_in.
**Ausgang**: Kollektor an +V_out über Lastwiderstand R2, Emitter nach GND.

:::formel
R1 = (V_in - U_F_LED) / I_F    # Vorwiderstand LED-Seite (I_F typisch 5–20 mA)
R2 = (V_out - U_CE(sat)) / I_C  # Lastwiderstand; I_C = CTR_min * I_F
:::

:::monospace
Beispiel: V_in = 5 V, U_F = 1.2 V, I_F = 10 mA, CTR_min = 50 %, V_out = 5 V
R1 = (5 - 1.2) / 10e-3 = 380 Ω → 390 Ω
I_C_min = 0.5 * 10e-3 = 5 mA
R2 = (5 - 0.2) / 5e-3 = 960 Ω → 1 kΩ
:::

## Isolationsspannung

Die Isolationsspannung U_iso gibt an, welche Spannung zwischen Ein- und Ausgang dauerhaft (oder kurzzeitig) anstehen darf:

| Klasse | U_iso | Anwendung |
|---|---|---|
| Standard | 1 kV | Logik-Trennung, Rückmeldungen |
| Reinforced | 3.75 kV | Netzspannungstrennung (EN 60950) |
| High-Voltage | 5–7 kV | Medizintechnik, Industrie |

## Typen nach Ausgang

| Ausgangstyp | CTR | Geschwindigkeit | Einsatz |
|---|---|---|---|
| Fototransistor (4N25, PC817) | 20–300 % | langsam (10 µs) | Digitale Signale, Relaisansteuerung |
| Darlington-Ausgang (4N29) | 300–1000 % | sehr langsam | Hohe Lasten |
| Fototriac (MOC3020) | — | 1/2-Welle | TRIAC-Ansteuerung aus Netz |
| Schneller Ausgang (6N136) | 19 % | < 1 µs | SPI, UART-Trennung |

## Anwendungen

**Steuerung aus dem Netz**: Mikrocontroller (3.3 V/5 V) steuert einen TRIAC an 230 V AC. Optokoppler trennt die Potentiale.

**Rückmeldung im Schaltregler**: Ausgangs-Spannung wird über Optokoppler zurück zur Primärseite gemeldet (galvanische Trennung bei Flyback-Wandler). → [[Schaltregler Topologien]]

**RS-485 / CAN Isolation**: Busknoten werden galvanisch getrennt, um Masseschleifen zu vermeiden und Überspannungsschäden zu verhindern.

:::tip
Bei hochfrequenten Signalen (> 100 kHz) auf schnelle Optokoppler (HCPL-2531, Si8621) achten. Standard-Typen wie der PC817 sind für Schaltfrequenzen > 50 kHz nicht mehr geeignet.
:::
