---
title: DC-DC-Wandler
kategorie: EK
kapitel: Stromversorgung
tags: [DC-DC, Schaltregler, Buck, Boost, Buck-Boost, Abwärtswandler, Aufwärtswandler, Inverswandler, Ladungspumpe, Tastverhältnis, PWM, Wirkungsgrad, MOSFET]
groessen: U_E|Eingangsspannung|V; U_A|Ausgangsspannung|V; D|Tastverhältnis|—; f_s|Schaltfrequenz|Hz; L|Induktivität|H; eta|Wirkungsgrad|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Spannungsstabilisierung]]
- [[MOSFET Anwendungen]]
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[Schaltregler Topologien]]
:::
:::vbox
**Führt weiter zu**
- [[Schaltregler Topologien]]
- [[Kühlkörper]]
:::
:::

---

DC-DC-Wandler wandeln eine Gleichspannung in eine andere Gleichspannung um — mit deutlich besserem Wirkungsgrad als Linearregler. Die Vorteile liegen im besseren Wirkungsgrad und geringerer Wärmeentwicklung (Spick S.46).

## Grundprinzip

Ein MOSFET schaltet mit Frequenz f_s und Tastverhältnis D = t_on / T. Die Induktivität L speichert Energie in der Ein-Phase und gibt sie in der Aus-Phase ab. Ein Siebkondensator am Ausgang glättet die Spannung.

:::formel
D = t_on / T = t_on * f_s    # Tastverhältnis (0 bis 1)
:::

## Topologien ohne galvanische Trennung

### Abwärtswandler — Buck Converter

:::schematic Buck Converter (Abwärtswandler): U_E links. MOSFET S (Schalter, high-side) nach unten. Wenn S ein: Strom durch L (Speicherdrossel) nach rechts zu Last R_L. Diode D (Freilaufdiode) von GND nach Ausgang (antiparallel zur Last, leitet wenn S aus). C am Ausgang parallel zu R_L. U_A = D × U_E. Eingezeichnet: Stromverlauf durch L (dreieckig), U_A glatt
/Diagramm/buck_converter.svg
:::

U_A ≤ U_E (Ausgangsspannung kleiner als Eingangsspannung). Schalter S in Reihe.

:::formel
U_A = D * U_E          # Ausgangsspannung
D   = U_A / U_E        # Tastverhältnis aus Spannungen
U_E = U_A / D          # Eingangsspannung
:::

### Aufwärtswandler — Boost Converter

:::schematic Boost Converter (Aufwärtswandler): U_E links. L (Speicherdrossel) in Reihe nach rechts zu Knoten A. MOSFET S von Knoten A nach GND (low-side Schalter). Diode D von Knoten A nach Ausgang (leitet wenn S aus, sperrt wenn S ein). C und R_L am Ausgang. U_A = U_E / (1−D). Wenn S ein: L lädt sich auf. Wenn S aus: L + U_E treiben Ausgang höher als U_E
/Diagramm/boost_converter.svg
:::

U_A ≥ U_E (Ausgangsspannung grösser als Eingangsspannung). Schalter S nach Masse.

:::formel
U_A = 1 / (1 - D) * U_E    # Ausgangsspannung
D   = 1 - U_E / U_A         # Tastverhältnis
U_E = U_A * (1 - D)         # Eingangsspannung
:::

### Inverswandler — Buck-Boost Converter

U_A ≤ 0 (Ausgangsspannung negativ, invertiert). Schalter S in Reihe, L nach Masse.

:::formel
U_A = -(D / (1 - D)) * U_E    # Ausgangsspannung (negativ!)
D   = U_A / (U_A - U_E)        # Tastverhältnis (U_A negativ einsetzen)
:::

### Ladungspumpe (Charge Pump)

Kein Schalter-L-System — nur Kondensatoren. Geeignet für kleine Leistungen.

| Typ | Spannungsbereich | Formel |
|---|---|---|
| Ladungspumpe positiv | U_E > 0, U_A > U_E | U_A ≈ 2 × U_E (Verdoppler) |
| Ladungspumpe negativ | U_E > 0, U_A < 0 | U_A ≈ −U_E (Inverter) |

## Weitere Topologien ohne Trennung (Spick 16.1)

| Wandlertyp | Formel | Elemente | Besonderheit |
|---|---|---|---|
| Synchronwandler | U_A = D · U_E | L | Bidirektional (Leistungsfluss wählbar) |
| SEPIC | U_A = D/(1−D) · U_E | 2L + C | U_E > 0, U_A positiv, hoch oder tief |
| Cuk | U_A = −D/(1−D) · U_E | 2L + C | U_A negativ, invertiert |
| Zeta | U_A = D/(1−D) · U_E | 2L + C | U_E > 0, U_A positiv |
| Doppelinverter | U_A = −D/(1−D) · U_E | 2L + C | U_A negativ |
| Split-Pi | Beliebig | 2L + C | Bidirektional |
| Kaskadierter Ab-/Aufwärtswandler | Beliebig | L | Kombiniert Buck- und Boost-Stufe (4 Schalter), nicht-invertierend, Leistungsfluss-Richtung wählbar |

## Wirkungsgrad

:::formel
eta = P_A / P_E = (U_A * I_A) / (U_E * I_E)    # Wirkungsgrad
:::

Typisch: η = 85–98 % (Schaltregler) vs. η = U_out/U_in (Linearregler, oft < 50 %).

| Wandlertyp | Typischer Wirkungsgrad |
|---|---|
| Linearregler (z.B. 7805 bei 12 V → 5 V) | ≈ 42 % |
| Buck Converter | 85 – 97 % |
| Boost Converter | 85 – 95 % |
| Buck-Boost | 80 – 92 % |

## Schutzfunktionen

Integrierte DC/DC-Wandler enthalten typisch vier Schutzfunktionen:

| Funktion | Abkürzung | Schutz vor |
|---|---|---|
| Überspannungsschutz | OVP (Over Voltage Protection) | U_A zu gross → Lasttrennung |
| Überstromschutz | OCP (Over Current Protection) | Kurzschluss, Überlast |
| Übertemperaturschutz | OTP (Over Temperature Protection) | Überhitzung des IC |
| Unterspannungsabschaltung | UVLO (Under Voltage Lockout) | U_E zu tief → Fehlfunktion |

:::warning
Schaltregler erzeugen HF-Störungen (EMV). Immer Eingangs- und Ausgangs-Entkoppelkondensatoren verwenden, Leiterbahnen möglichst kurz halten. Für rauscharme Anwendungen (Audio, Messtechnik) Linearregler bevorzugen oder zusätzlichen LC-Filter nachschalten.
:::
