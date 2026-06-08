---
title: H-Brücke
kategorie: EK
kapitel: Aktorik
tags: [h-brücke, mosfet, bjt, pwm, drehrichtung, drehzahl, shoot-through, totzeit, freilaufdiode, bootstrap, high-side, motor-treiber-ic]
groessen: D|Duty Cycle|—; U_eff|Effektive Motorspannung|V; t_dead|Totzeit|s
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Aktorik Grundlagen]]
- [[MOSFET Anwendungen]]
- [[Modulation]]
:::
:::vbox
**Verwandte Artikel**
- [[Relais]]
- [[DC-Motor]]
- [[Schrittmotor]]
:::
:::vbox
**Führt weiter zu**
- [[DC-Motor]]
- [[BLDC-Motor]]
- [[Frequenzumrichter]]
:::
:::

---

Die H-Brücke ist eine Schaltung aus vier Schaltern (typisch N-Kanal-MOSFETs), die eine Last mit **umkehrbarer Polarität** betreiben kann. Sie ist die Standardschaltung für Drehrichtungssteuerung und Drehzahlregelung von Gleichstrommotoren.

## Aufbau

Vier Schalter sind paarweise zwischen Versorgungsspannung und GND angeordnet. Der Motor liegt als Last in der Mitte — das ergibt die charakteristische H-Form:

:::schematic H-Brücke: Vier N-Kanal-MOSFETs. S1 (High-Side links) von +U_B nach Knoten A. S3 (High-Side rechts) von +U_B nach Knoten B. S2 (Low-Side links) von Knoten A nach GND. S4 (Low-Side rechts) von Knoten B nach GND. Motor M zwischen Knoten A und B. Vorwärts: S1+S4 ein, S2+S3 aus. Rückwärts: S2+S3 ein, S1+S4 aus. Body-Dioden je Transistor als Freilauf
/Diagramm/h_bruecke.svg
:::

S1/S3 = High-Side (zwischen +U_B und Motor), S2/S4 = Low-Side (zwischen Motor und GND).

## Wahrheitstabelle

| S1 | S2 | S3 | S4 | Motorverhalten |
|---|---|---|---|---|
| EIN | AUS | AUS | EIN | Vorwärts |
| AUS | EIN | EIN | AUS | Rückwärts |
| AUS | EIN | AUS | EIN | Bremsen (Motor kurzgeschlossen über GND) |
| EIN | AUS | EIN | AUS | Bremsen (Motor kurzgeschlossen über +U_B) |
| AUS | AUS | AUS | AUS | Freilauf (Motor dreht aus) |

## Drehzahlsteuerung per PWM

PWM auf einem Schalterpaar regelt die effektive Motorspannung und damit die Drehzahl:

:::formel
U_eff = U_B * D        # effektive Motorspannung
D     = t_on / T       # Duty Cycle 0..1
n     ~ U_eff          # Drehzahl proportional zur Spannung
:::

Typische PWM-Frequenz: **10–50 kHz** — oberhalb des Hörbereichs, damit der Motor nicht pfeift.

## Freilaufdioden

Ein Motor ist induktiv. Beim Abschalten jedes Transistors entsteht eine induktive Spannungsspitze. Freilaufdioden (auch Flyback-Dioden) parallel zu jedem Schalter leiten diesen Strom ab.

:::warning
Ohne Freilaufdioden zerstören induktive Spannungsspitzen die Transistoren. Bei N-Kanal-MOSFETs übernimmt die integrierte Body-Diode diese Aufgabe — vorausgesetzt sie ist schnell genug (Schottky besser als langsame Body-Diode).
:::

## Shoot-Through — grösste Gefahr

:::warning
**Shoot-Through (Querstrom)**: Leiten S1 und S2 (oder S3 und S4) gleichzeitig, entsteht ein direkter Kurzschluss von +U_B nach GND. Die Schalter und die Versorgung werden sofort zerstört.
:::

**Ursache**: MOSFETs schalten nicht ideal: Beim Umschalten kann der noch leitende Transistor kurz gleichzeitig mit dem einschaltenden Transistor leiten.

**Lösung: Totzeit (Dead Time)**

:::formel
t_dead >= t_off_max + t_on_max    # Totzeit mindestens so gross wie Schaltzeiten
:::

Zwischen Ausschalten des High-Side-FETs und Einschalten des Low-Side-FETs eine Pause einfügen (typisch 100 ns–5 µs). Die meisten Gate-Treiber-ICs erzeugen die Totzeit automatisch.

:::monospace
S1 (HS): ___/‾‾‾‾‾‾\___________________
                    |← t_dead →|
S2 (LS): ___________________/‾‾‾‾‾‾\___
:::

## High-Side-Problem bei N-Kanal-MOSFETs

Ein N-Kanal-MOSFET schaltet durch wenn U_GS > U_GS_th. Auf der High-Side liegt die Source am Motoranschluss (nicht GND) — die Gate-Spannung muss höher als +U_B sein.

**Lösungen:**
- **Bootstrap-Kondensator**: C lädt sich über Diode auf U_B auf, wenn Low-Side leitet. Beim Einschalten des High-Side-FETs liefert C die nötige Überspan­nung. Standard in Gate-Treiber-ICs.
- **P-Kanal-MOSFET** für High-Side: Einfachere Ansteuerung (Gate auf GND zum Einschalten), aber höherer R_DS(on) als N-Kanal.
- **Ladungspumpe** im IC: DC-DC-Konverter erzeugt U > U_B.

## MOSFET-Auswahlkriterien

| Parameter | Anforderung |
|---|---|
| U_DS | > U_B × 1.5 (Sicherheitsmarge für Spannungsspitzen) |
| I_D | > I_Motor_max |
| R_DS(on) | Möglichst klein → niedrige Verluste P = I² × R_DS |
| Schaltzeit (t_r, t_f) | Klein genug für PWM-Frequenz |

## Fertige Motor-Treiber-ICs

Für die meisten Anwendungen sind fertige ICs die bessere Wahl — Freilaufdioden, Totzeit und Gate-Treiber sind integriert:

| IC | Spannung | Strom | Besonderheit |
|---|---|---|---|
| L298N | 5–46 V | 2 A | Veraltet, hohe Verluste |
| DRV8833 | 2.7–10.8 V | 1.5 A | Integrierte Freilaufdioden, kompakt |
| TB6612FNG | 2.5–13.5 V | 1.2 A | 2× H-Brücke, effizient |
| DRV8876 | 4.5–37 V | 3.5 A | Integrierter Stromsensor |

:::tip
Für Prototypen immer fertigen H-Brücken-IC einsetzen. Diskrete Aufbauten lohnen sich erst bei hohen Strömen (> 10 A) oder besonderen Spannungsbereichen.
:::
