---
title: Wärmewiderstand
kategorie: EK
kapitel: Thermomanagement
tags: [wärmewiderstand, thermischer widerstand, r_th, verlustleistung, junction, sperrschichttemperatur, thermisches netzwerk, reihenschaltung, kühlkette]
groessen: R_th|Wärmewiderstand|K/W; P_v|Verlustleistung|W; theta_J|Sperrschichttemperatur|°C; theta_U|Umgebungstemperatur|°C; Delta_T|Temperaturdifferenz|K
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[MOSFET Anwendungen]]
- [[BJT Arbeitspunkt]]
:::
:::vbox
**Verwandte Artikel**
- [[Spannungsstabilisierung]]
- [[DC-DC-Wandler]]
:::
:::vbox
**Führt weiter zu**
- [[Kühlkörper]]
:::
:::

---

Jedes Halbleiterbauteil erzeugt beim Betrieb Verlustleistung. Diese Wärme muss abgeführt werden — sonst steigt die Sperrschichttemperatur θ_J über den erlaubten Maximalwert (typisch 125 °C oder 150 °C) und das Bauteil wird zerstört. Der **Wärmewiderstand R_th** beschreibt den Widerstand gegen Wärmefluss, analog zum elektrischen Widerstand.

## Grundformel (Spick Kap. 14)

Wärme verhält sich wie Strom: Verlustleistung ist die "Stromquelle", Temperaturdifferenz ist die "Spannung" und R_th ist der "Widerstand":

:::formel
Delta_T = P_v * R_th          # Temperaturdifferenz in K
P_v     = Delta_T / R_th      # Verlustleistung in W
R_th    = Delta_T / P_v       # Wärmewiderstand in K/W
:::

## Thermische Kühlkette (Reihenschaltung)

:::schematic Thermische Kühlkette (Analogie zu elektrischer Reihenschaltung): Wärmequelle P_v (Verlustleistung, analog Stromquelle) an theta_J (Sperrschichttemperatur). Thermische Widerstände in Serie: R_thJC (Junction→Gehäuse), R_thü (Gehäuse→Kühlkörper, Wärmeleitpaste), R_thK (Kühlkörper→Luft). Endpunkt theta_U (Umgebungstemperatur, analog GND). Jede Temperatur = Summe aller P_v × R_th davor
/Diagramm/thermische_kuehlkette.svg
:::

Wärme fliesst vom heissen Chip durch mehrere Schichten bis zur Umgebungsluft. Jede Schicht hat ihren eigenen R_th — sie addieren sich wie Widerstände in Reihe:

| Symbol | Bedeutung | Typischer Wert |
|---|---|---|
| theta_J | Sperrschichttemperatur (Junction) | max. 125–150 °C |
| R_thG | Wärme­widerstand Gehäuse (Junction–Gehäuse) | 1–5 K/W (aus Datenblatt) |
| theta_G | Gehäusetemperatur | — |
| R_thü | Übergangs­widerstand (Gehäuse–Kühlkörper) | 0.1–1 K/W |
| theta_K | Kühlkörpertemperatur | — |
| R_thK | Wärme­widerstand Kühlkörper (Kühlkörper–Luft) | aus Kühlkörper-Datenblatt |
| theta_U | Umgebungstemperatur | typisch 25 °C (Norm), 40–70 °C (Industrie) |

**Gesamte Sperrschichttemperatur:**

:::formel
theta_J = theta_U + P_v * (R_thG + R_thü + R_thK)
:::

**Erforderlicher Kühlkörper R_thK:**

:::formel
R_thK = (theta_J_max - theta_U) / P_v - R_thG - R_thü
:::

## Verlustleistung berechnen

Vor der Kühlkörperdimensionierung muss P_v bekannt sein:

| Bauteil | Formel | Hinweis |
|---|---|---|
| Linearregler (z. B. 7805) | P_v = (U_ein - U_aus) * I_L | Typisch mehrere Watt |
| Transistor (BJT/MOSFET) | P_v = U_CE * I_C (BJT) / R_DS_on * I_D² (MOSFET) | Im Linearbetrieb höher |
| Diode | P_v = U_F * I_F | ca. 0.7 V × Strom |
| Schaltregler | P_v = P_ein * (1 - eta) | Eta typisch 85–95 % |

## Berechnungsbeispiel

:::monospace
Linearregler 7805: U_ein=12 V, U_aus=5 V, I_L=1 A
P_v = (12-5) * 1 = 7 W

Aus Datenblatt: R_thG = 5 K/W, T_j_max = 125 °C
T_U = 25 °C, R_thü = 0.5 K/W (Wärmeleitpaste)

Erforderlich: R_thK = (125-25)/7 - 5 - 0.5 = 14.3 - 5.5 = 8.8 K/W

→ Kühlkörper mit R_thK ≤ 8.8 K/W wählen.

Probe: theta_J = 25 + 7*(5 + 0.5 + 8.8) = 25 + 7*14.3 = 25+100 = 125 °C ✓
:::

:::warning
Für Dauerbetrieb immer Derating einrechnen: θ_J im Betrieb mindestens 20–30 °C unter T_j_max halten. Im Beispiel also R_thK so wählen dass θ_J ≤ 100 °C.
:::

## Analogie Wärme ↔ Elektrizität

| Thermisch | Symbol | Elektrisch | Symbol |
|---|---|---|---|
| Verlustleistung | P_v [W] | Strom | I [A] |
| Temperaturdifferenz | ΔT [K] | Spannung | U [V] |
| Wärmewiderstand | R_th [K/W] | Widerstand | R [Ω] |
| Wärmekapazität | C_th [J/K] | Kapazität | C [F] |

:::tip
Faustregel: Bei einem TO-220-Gehäuse ohne Kühlkörper ist R_thG ≈ 5 K/W. Bei 25 °C Umgebung und T_j_max = 125 °C kann der Chip dann maximal (125-25)/5 = 20 W ohne Kühlkörper ab.
:::
