---
title: Lichtsensor
kategorie: EK
kapitel: Sensorik
tags: [lichtsensor, ldr, fotodiode, fototransistor, helligkeit, beleuchtungsstärke, photodetector, lux, sperrschicht, fotostrom, spannungsteiler, spektrum]
groessen: R_LDR|LDR-Widerstand|Ω; I_ph|Fotostrom|A; E_v|Beleuchtungsstärke|lx
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sensorik Grundlagen]]
- [[Diode]]
- [[BJT Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Optokoppler]]
- [[NTC & PTC Thermistoren]]
:::
:::vbox
**Führt weiter zu**
- [[Regelkreis Grundlagen]]
- [[Aktorik Grundlagen]]
:::
:::

---

Lichtsensoren wandeln **Lichtintensität** in ein elektrisches Signal um. Die drei gebräuchlichsten Typen auf EFZ-Niveau sind LDR, Fotodiode und Fototransistor.

## LDR — Lichtabhängiger Widerstand

Der LDR (Light Dependent Resistor, auch Fotowiderstand) ist ein Halbleiter (meist CdS), dessen Widerstand mit zunehmender Beleuchtung stark sinkt.

| Beleuchtung | Widerstand typisch |
|---|---|
| Dunkelheit | 1 MΩ – 10 MΩ |
| Raumbeleuchtung (100 lx) | 1 kΩ – 10 kΩ |
| Helles Sonnenlicht (10 klx) | 100 Ω – 1 kΩ |

**Kennlinie**: Stark nichtlinear (logarithmisch). Keine genaue Formel — Kennlinie aus Datenblatt ablesen.

**Reaktionszeit**: Langsam (10–200 ms). Nicht geeignet für schnelle Lichtimpulse.

**Spannungsteiler-Schaltung** (LDR als unterer Widerstand):

:::formel
U_aus = U_B * R_fest / (R_LDR + R_fest)    # heller → R_LDR kleiner → U_aus grösser
:::

R_fest ≈ R_LDR bei Sollbeleuchtung für maximale Empfindlichkeit wählen.

:::warning
CdS-LDRs enthalten Cadmium (RoHS-problematisch). In neuen Designs lieber Fotodiode oder Fototransistor einsetzen.
:::

## Fotodiode

Eine Fotodiode ist eine PN-Diode die im **Sperrbetrieb** betrieben wird. Einfallende Photonen erzeugen Elektronen-Loch-Paare in der Sperrschicht — der **Fotostrom I_ph** fliesst entgegen der Sperrichtung und ist proportional zur Lichtintensität.

:::formel
I_ph = E_v * S_lambda    # S_lambda = Empfindlichkeit in A/lx oder A/W (aus Datenblatt)
:::

**Betriebsarten:**

| Betriebsart | Beschreibung | Anwendung |
|---|---|---|
| Fotovoltaisch (U=0) | Kein Bias, erzeugt Spannung | Sonnenzelle, Präzisionsmessung |
| Fotodioden-Modus (U<0) | Rückwärtsbias, schnell | Lichtmessung, Kommunikation |

Im Fotodioden-Modus (Sperrbetrieb) ist der Fotostrom linear zur Beleuchtung und die Reaktionszeit sehr kurz (ns–µs).

**Transimpedanzverstärker** (Strom → Spannung):

:::schematic Fotodiode mit Transimpedanzverstärker: Fotodiode im Sperrbetrieb (Kathode an VCC, Anode am (−)-Eingang des OPV). OPV: (−) am Diodenknoten, (+) an GND. Rückkopplungswiderstand R_f von Ausgang nach (−). Licht → Fotostrom I_ph fliesst in (−)-Eingang. U_aus = −I_ph × R_f. OPV hält (−) auf 0 V (virtueller Kurzschluss) → linearster Betrieb der Diode
/Diagramm/fotodiode_transimpedanz.svg
:::

:::formel
U_aus = -I_ph * R_f    # OPV-Gegenkopplungs-Widerstand R_f
:::

Der OPV hält den Diodenknoten auf 0 V (virtueller Kurzschluss) — ideal für linearen Betrieb.

## Fototransistor

Ein Fototransistor ist ein BJT ohne Basisanschluss — das Licht erzeugt den Basisstrom. Die Kollektorstrom-Verstärkung β multipliziert den Fotostrom:

:::formel
I_C = beta * I_ph_Basis    # Verstärkter Fotostrom
:::

Einfacher auszuwerten als Fotodiode (grösseres Signal), aber langsamer (µs–ms) und weniger linear.

**Schaltung (als Schalter für Lichtschranke):**

:::schematic Fototransistor als Lichtschranken-Schalter: VCC oben. R_C (Kollektorwiderstand) von VCC nach Kollektor des Fototransistors. Kollektor auch an U_aus (Signalausgang). Emitter des Fototransistors nach GND. Licht trifft auf die Basis-Fläche (kein Basisanschluss). Dunkel: I_C = 0 → U_aus = VCC (HIGH). Hell: I_C steigt → Spannungsabfall an R_C → U_aus sinkt → LOW
/Diagramm/fototransistor_lichtschranke.svg
:::

Licht → I_C steigt → Spannungsabfall an R_C steigt → U_aus sinkt. Im Dunkeln: U_aus ≈ U_B.

## Vergleich LDR / Fotodiode / Fototransistor

| Eigenschaft | LDR | Fotodiode | Fototransistor |
|---|---|---|---|
| Ausgangssignal | Widerstand | Strom (nA–µA) | Strom (µA–mA) |
| Linearität | Nichtlinear (log) | Sehr linear | Mässig linear |
| Reaktionszeit | 10–200 ms | ns–µs | µs–ms |
| Empfindlichkeit | Hoch (aber ungenau) | Niedrig (braucht Verstärker) | Mittel |
| Spektrum | Sichtbares Licht | UV bis NIR (je nach Typ) | Sichtbar bis NIR |
| Signalaufbereitung | Spannungsteiler | Transimpedanzverstärker | Einfacher Widerstand |
| Typische Anwendung | Dämmerungsschalter | Optische Kommunikation, Präzisionsmessung | Lichtschranke, Zähler |

## Spektrale Empfindlichkeit

Nicht alle Sensoren sehen das gleiche Licht. Siliziumbauteile (Fotodiode, Fototransistor) sind am empfindlichsten im **Nahinfrarot (800–1000 nm)**, weniger im sichtbaren Blaubereich. CdS-LDRs passen besser zum menschlichen Auge.

:::tip
Für einfache Hell/Dunkel-Schaltungen genügt LDR + Schmitt-Trigger. Für Lichtschranken und schnelle Zähler ist der Fototransistor einfacher als die Fotodiode. Für genaue Lichtstärken-Messung (Lux-Meter, Kamera) gibt es dedizierte IC-Sensoren (z. B. BH1750, TSL2561) mit I²C-Ausgang.
:::
