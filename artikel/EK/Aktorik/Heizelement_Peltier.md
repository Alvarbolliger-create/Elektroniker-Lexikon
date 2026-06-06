---
title: Heizelement & Peltier
kategorie: EK
kapitel: Aktorik
tags: [heizelement, peltier, thermoelektrisch, pwm, pid, cop, seebeck, kühlleistung, ptc, nichrom, phasenanschnitt, wärmeaktor]
groessen: P|Verlustleistung|W; Q_K|Kühlleistung|W; COP|Leistungszahl|—; D|Duty Cycle|—; alpha|Seebeck-Koeffizient|V/K
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Aktorik Grundlagen]]
- [[Wärmewiderstand]]
- [[Kühlkörper]]
:::
:::vbox
**Verwandte Artikel**
- [[NTC & PTC Thermistoren]]
- [[PID Regler]]
:::
:::vbox
**Führt weiter zu**
- [[PID Regler]]
- [[Regelkreis Grundlagen]]
:::
:::

---

## Heizelement

Ein Heizelement ist ein ohmscher Widerstand, der elektrische Energie vollständig in Wärme umwandelt. Der elektrische Wirkungsgrad ist per Definition 100 % (alle Energie wird zu Wärme).

:::formel
P = U * I = U^2 / R = I^2 * R    # Heizleistung
:::

**Leistungsregelung** geschieht durch:
- **PWM** (Pulsweitenmodulation): Einfach, digitale Steuerung, für DC-Versorgung
- **Phasenanschnittsteuerung**: Bei 50-Hz-Netzspannung (Triac), erzeugt HF-Störungen

:::formel
P_mittel = P_max * D    # D = Duty Cycle 0..1 (bei PWM-Regelung)
:::

### Heizelementtypen

| Typ | Merkmal | Einsatz |
|---|---|---|
| Nichrom-Heizdraht | Hohe Temp. möglich (> 1000 °C), günstig | Industrieöfen, 3D-Drucker-Hotend |
| PTC-Keramik | Selbstlimitierend (R steigt mit T) | Innenraumheizung, Luftvorwärmer |
| Silikon-Heizmatte | Flexibel, flächig | Rohre, Behälter, Frostschutz |
| Quarzstrahler | Infrarotstrahlung direkt | Industrietrockner, Heizstrahler |
| Heizpatrone | Kompakt, hohe Leistungsdichte | Spritzgiessmaschinen, Industrieöfen |

:::warning
Immer eine thermische Sicherung oder Thermoschutzschalter einplanen. Ein festgezogener Transistor (Shoot-Through, Gatedefekt) führt zu Dauerheizbetrieb und Brandgefahr.
:::

## Peltier-Element (Thermoelektrisches Modul, TEC)

:::schematic Peltier-Element Querschnitt: Zwei Keramikplatten (oben = Kaltseite, unten = Warmseite). Dazwischen: Thermoelektrische Paare aus N-Typ (dunkel) und P-Typ (hell) Halbleitern, abwechselnd in Reihe elektrisch geschaltet, thermisch parallel. Strom fliesst durch N→P (elektrisch in Serie). Peltier-Effekt: Kaltseite absorbiert Wärme Q_K, Warmseite gibt Q_K + P_el ab. Umpolung → Seiten tauschen
/Diagramm/peltier_querschnitt.svg
:::

Ein Peltier-Element basiert auf dem **Peltier-Effekt**: Fliesst Strom durch die Verbindung zweier unterschiedlicher Halbleitermaterialien (N-Typ und P-Typ), wird auf einer Seite Wärme absorbiert (Kaltseite) und auf der anderen Seite abgegeben (Warmseite).

**Durch Umpolung wechseln Kalt- und Warmseite** — dasselbe Bauteil kann heizen oder kühlen.

### Kühlleistungs-Formel

:::formel
Q_K = alpha * T_K * I - 0.5 * I^2 * R_TEC - K * Delta_T
:::

| Grösse | Bedeutung |
|---|---|
| Q_K | Kühlleistung [W] |
| alpha | Seebeck-Koeffizient [V/K] (aus Datenblatt) |
| T_K | Temperatur Kaltseite [K] |
| I | Steuerstrom [A] |
| R_TEC | Elektrischer Widerstand des Moduls [Ω] |
| K | Wärmeleitwert des Moduls [W/K] |
| Delta_T | T_warm − T_kalt [K] |

### Wirkungsgrad (COP)

Der COP (Coefficient of Performance) ist gering:

:::formel
COP = Q_K / P_el    # Kühlleistung / elektrische Eingangsleistung
:::

| Methode | COP typisch |
|---|---|
| Kompressionskältemaschine | 2–4 |
| Peltier-Element | 0.2–0.5 |

Für 1 W Kühlleistung werden typisch 3–8 W elektrische Leistung benötigt. Die überschüssige Wärme auf der **Warmseite muss abgeführt werden** (Kühlkörper + Lüfter oder Wasserkühlung) — sonst steigt die Warmseiten-Temperatur, Delta_T wächst und die Kühlleistung bricht ein.

### Ansteuerung des Peltier-Elements

Peltier-Elemente können mit einer H-Brücke angesteuert werden (Polaritätswechsel = Richtungswechsel). Für reine Kühlung genügt ein einfacher PWM-Schalter.

:::formel
I_Peltier_opt ~ I_max / sqrt(2)    # Optimaler Strom für max. COP (ca. 70 % von I_max)
:::

## Temperaturregelung

Beide Komponenten werden typisch über einen **PID-Regler** geregelt:

| Element | Sensor | Stellgrösse | Regelgrösse |
|---|---|---|---|
| Heizelement | NTC / PT100 | PWM-Duty-Cycle | Temperatur [°C] |
| Peltier | NTC / PT100 | PWM (+ Richtung) | Temperatur [°C] |

:::tip
Für einfache Anwendungen (Ein/Aus-Thermostat mit Hysterese) reicht ein Zweipunkt-Regler mit Schmitt-Trigger. Für genaue Temperaturstabilisierung (Laserdiode auf ±0.01 °C, Kalibriergerät) wird ein PID-Regler mit präzisem PT1000-Sensor benötigt.
:::

## Anwendungen

| Komponente | Einsatz |
|---|---|
| Heizelement (Nichrom) | Industrieöfen, 3D-Drucker-Hotend |
| Heizelement (PTC) | Selbstregelnde Raumheizung |
| Peltier (Kühlmodus) | Laserdiodenkühlung, Weinkühlschrank |
| Peltier (Heizbetrieb) | Temperaturstabilisierte Messkammern |
| Peltier (beides) | Laborinstrumente mit engem Regelband |
