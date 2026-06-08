---
title: DC-Motor
kategorie: EK
kapitel: Motoren
tags: [dc-motor, gleichstrommotor, kommutator, bürste, lorentzkraft, bemf, gegen-emk, anlaufstrom, pwm, h-brücke, drehzahl, drehmoment, verschleiss]
groessen: n|Drehzahl|U/min; M|Drehmoment|N·m; U_BEMF|Gegen-EMK|V; I_A|Ankerstrom|A; k_e|Spannungskonstante|V·min/U; k_t|Drehmomentkonstante|N·m/A
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[H-Brücke]]
- [[Aktorik Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Schrittmotor]]
- [[BLDC-Motor]]
:::
:::vbox
**Führt weiter zu**
- [[BLDC-Motor]]
- [[Regelkreis Grundlagen]]
:::
:::

---

Der DC-Motor (Gleichstrommotor) wandelt elektrische Energie in Drehbewegung um. Er ist einfach anzusteuern, gut regelbar und weit verbreitet in Robotik, Modellbau und Automatisierung.

## Funktionsprinzip

Strom durch die Ankerwicklung erzeugt ein Magnetfeld. Im Feld des Permanentmagneten entsteht eine **Lorentzkraft**, die den Anker dreht. Der **Kommutator** mit Kohlebürsten kehrt die Stromrichtung alle halbe Umdrehung um, sodass die Kraft immer in dieselbe Richtung wirkt.

## Gegen-EMK (BEMF)

Der rotierende Motor wirkt gleichzeitig als Generator — er erzeugt eine der Versorgungsspannung entgegengerichtete **Gegen-EMK** (Back-EMF):

:::formel
U_BEMF = k_e * n           # proportional zur Drehzahl
I_A    = (U - U_BEMF) / R_A    # Ankerstrom (U = angelegte Spannung)
M      = k_t * I_A         # Drehmoment proportional zum Ankerstrom
:::

| Grösse | Bedeutung |
|---|---|
| k_e | Spannungskonstante [V·min/U] — aus Datenblatt |
| k_t | Drehmomentkonstante [N·m/A] — aus Datenblatt |
| R_A | Ankerwiderstand [Ω] |

**Im Leerlauf**: BEMF ≈ U → I_A klein → wenig Verluste.  
**Unter Last**: Drehzahl sinkt → BEMF sinkt → I_A steigt → mehr Drehmoment.

## Anlaufstrom

Im Stillstand ist BEMF = 0. Der Anlaufstrom wird nur durch R_A begrenzt:

:::formel
I_anlauf = U / R_A    # kann 5–10× Nennstrom erreichen!
:::

:::warning
Anlaufstrom immer berücksichtigen: Netzteil, Treiber und Sicherung müssen den Anlaufstrom kurzzeitig liefern können. Bei grossen Motoren Sanftanlauf (Rampenfunktion über PWM) oder Strombegrenzung einsetzen.
:::

## Drehzahlregelung mit PWM

:::schematic DC-Motor mit H-Brücke und PWM-Steuerung: µC gibt PWM-Signal (10–50 kHz). Motor-Treiber-IC (z.B. DRV8833) enthält H-Brücke mit 4 N-Kanal-MOSFETs. Versorgung U_B → H-Brücke → DC-Motor M (Spule + BEMF-Quelle + R_A in Reihe). Vorwärts: S1+S4 PWM. Rückwärts: S2+S3 PWM. U_eff = D × U_B. Freilaufdioden parallel zu jedem MOSFET (Body-Dioden)
/Diagramm/dc_motor_hbruecke.svg
:::

:::formel
U_eff = U_B * D     # effektive Motorspannung
n ~ U_eff           # Drehzahl proportional zur Spannung
D = t_on / T        # Duty Cycle 0..1
:::

**Typische PWM-Frequenz**: 10–50 kHz (kein hörbares Pfeifen).

Drehrichtungsumkehr: **H-Brücke** (4 Transistoren / Motor-Treiber-IC) — der Motor kann mit beiden Polaritäten betrieben werden.

## Typische Kenndaten

| Grösse | Einheit | Bedeutung |
|---|---|---|
| Nennspannung | V | Betriebsspannung laut Datenblatt |
| Leerlaufdrehzahl | U/min | Drehzahl ohne Last |
| Nennstrom | A | Strom bei Nennlast |
| Anlaufmoment | N·m | Maximales Drehmoment im Stillstand |
| Wirkungsgrad | % | Typisch 60–80 % |
| Leerlaufstrom | mA | Strom für Reibungsverluste |

## Bürsten und Verschleiss

Kommutator und Kohlebürsten verschleissen mechanisch. Typische Lebensdauer: 500–3000 Betriebsstunden. Symptome: Funkenbildung am Kommutator, Geräusche, sinkende Drehzahl.

**Alternative**: Bürstenloser Motor (BLDC) — kein mechanischer Kommutator, kein Verschleiss, besserer Wirkungsgrad (85–95 %). Dafür komplexere elektronische Kommutierung nötig.

## Vergleich DC-Motor / BLDC

| Eigenschaft | DC-Motor (bürstenbehaftet) | BLDC |
|---|---|---|
| Kommutierung | Mechanisch (Bürsten) | Elektronisch (Hall / sensorlos) |
| Verschleiss | Ja (Bürsten, Kommutator) | Nein |
| Wirkungsgrad | 60–80 % | 85–95 % |
| Ansteuerung | Einfach (H-Brücke + PWM) | Komplex (3-Phasen-Treiber) |
| Kosten | Günstig | Höher |
| Wartung | Bürsten tauschen | Wartungsfrei |

:::tip
Für Prototypen und einfache Anwendungen: Motor-Treiber-ICs (DRV8833, TB6612FNG) integrieren H-Brücke, Freilaufdioden und Strombegrenzung. Kein diskreter Aufbau nötig.
:::
