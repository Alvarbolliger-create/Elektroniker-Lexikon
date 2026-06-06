---
title: NTC & PTC Thermistoren
kategorie: EK
kapitel: Sensorik
tags: [ntc, ptc, thermistor, heissleiter, kaltleiter, negativer temperaturkoeffizient, positiver temperaturkoeffizient, b-wert, spannungsteiler, einschaltstrombegrenzer, selbstrückstellend]
groessen: R_T|Widerstand bei Temperatur T|Ω; R_0|Nennwiderstand bei T_0|Ω; B|B-Wert|K; T|Temperatur|K; alpha|Temperaturkoeffizient|1/K
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sensorik Grundlagen]]
- [[Wärmewiderstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Lichtsensor]]
- [[Regelkreis Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[Regelkreis Grundlagen]]
- [[Kühlkörper]]
:::
:::

---

NTC und PTC sind **Thermistoren** — temperaturabhängige Widerstände aus Halbleitermaterial. Sie reagieren stark auf Temperaturänderungen und sind einfach auszuwerten.

## NTC — Negativer Temperaturkoeffizient (Heissleiter)

Der Widerstand **sinkt** mit steigender Temperatur — wie ein Halbleiter-PN-Übergang.

**Kennlinie-Formel (B-Wert-Modell):**

:::formel
R_T = R_0 * e^(B * (1/T - 1/T_0))    # T und T_0 in Kelvin! (°C + 273.15)
:::

| Grösse | Bedeutung | Typisch |
|---|---|---|
| R_0 | Nennwiderstand bei T_0 | z.B. 10 kΩ bei 25 °C |
| T_0 | Nenntemperatur (= 25 °C = 298.15 K) | 298.15 K |
| B | B-Wert (Materialkonstante) | 3000–5000 K |
| T | Messtemperatur | in Kelvin! |

**Temperaturkoeffizient** (lokal, am Arbeitspunkt):

:::formel
alpha = -B / T^2    # negativ → NTC; bei T = 298 K und B = 3977: alpha ≈ -4.5 %/K
:::

### Spannungsteiler-Schaltung

:::schematic NTC-Spannungsteiler: U_B (Versorgung) oben. R_V (Festwiderstand) von U_B nach Knoten A. NTC von Knoten A nach GND. U_aus am Knoten A (zu ADC oder Komparator). Kalt (niedrige T): R_NTC hoch → U_aus niedrig. Warm (hohe T): R_NTC niedrig → U_aus hoch. Optimum: R_V ≈ R_NTC bei Zieltemperatur
/Diagramm/ntc_spannungsteiler.svg
:::

NTC allein ist nichtlinear. Im Spannungsteiler mit einem Festwiderstand R_V entsteht eine Ausgangsspannung, die sich mit dem Schmitt-Trigger oder ADC auswerten lässt:

:::formel
U_aus = U_B * R_NTC / (R_V + R_NTC)
:::

**Optimaler Arbeitspunkt:** R_V ≈ R_NTC bei der Zieltemperatur → maximale Empfindlichkeit.

:::monospace
Beispiel: NTC 10 kΩ bei 25 °C, B = 3977, R_V = 10 kΩ, U_B = 5 V
Bei 25 °C: U_aus = 5 * 10k/(10k+10k) = 2.5 V
Bei 50 °C: R_NTC = 10k * e^(3977*(1/323-1/298)) = 10k * e^(-1.01) ≈ 3.64 kΩ
           U_aus = 5 * 3.64k/(10k+3.64k) = 1.33 V → Δ1.17 V für 25 K Änderung
:::

### NTC-Anwendungen

| Anwendung | Prinzip |
|---|---|
| Temperaturüberwachung | Spannungsteiler → Komparator/ADC |
| Einschaltstrombegrenzer | NTC kalt = hoher R, begrenzt Einschaltstrom; warm = niedrig |
| Akkuüberwachung | NTC im Akkupack misst Zelltemperatur für BMS |
| Lüftersteuerung | NTC → analoge Steuerspannung für Lüfterdrehzahl |

## PTC — Positiver Temperaturkoeffizient (Kaltleiter)

Der Widerstand **steigt** mit Temperatur. Zwei verschiedene Typen:

### Silistor-PTC (linear, aus Si)

Linearer Anstieg über grossen Bereich, ähnlich wie Metall (PT100). Wird als Temperatursensor eingesetzt.

### Keramik-PTC (Sprung, aus BaTiO₃)

Unterhalb der Curie-Temperatur T_C ist R niedrig (Supraleiter-ähnlich). Oberhalb von T_C springt R um mehrere Dekaden innerhalb weniger Kelvin.

:::formel
alpha = +%/K    # positiv und gross (Keramik-PTC: +10 %/K bis +100 %/K im Sprungbereich)
:::

### PTC-Anwendungen

| Anwendung | Prinzip |
|---|---|
| Selbstrückstellende Sicherung (Polyswitch) | PTC-Polymer: Überstrom → Erwärmung → R↑ → Strom↓ → Schutz |
| Anlaufstrombegrenzer | PTC kalt = niedrig R, warm = hoch R |
| Motorschutz | PTC im Motorwickel: Übertemperatur → R↑ → Abschalten |
| Kaltlufttrockner-Heizung | Selbstregelnde Heizung: bei Nenntemperatur stabilisiert PTC den Strom |

:::warning
Keramik-PTC: Die Curie-Temperatur T_C ist keine absolute Grenze für den Sensor — sie ist der Arbeitspunkt für Schutzfunktionen. Wird der PTC als Temperatursensor eingesetzt, muss der Silistor-Typ gewählt werden.
:::

## Vergleich NTC / PTC / PT100

| Eigenschaft | NTC | Keramik-PTC | PT100 |
|---|---|---|---|
| Kennlinie | Exponentiell fallend | Sprung bei T_C | Linear steigend |
| Nennwiderstand | 1 kΩ – 100 kΩ | 10 Ω – 10 kΩ | 100 Ω (bei 0 °C) |
| Temperaturbereich | -50 bis +150 °C | -25 bis +125 °C | -200 bis +850 °C |
| Genauigkeit | ±1–5 % | Schaltpunkt ±2–5 K | ±0.1–0.5 °C |
| Hauptanwendung | Messen, Regeln | Schutzelement | Präzisionsmessung |
| Auswertungsaufwand | Einfach + Linearisierung | Sehr einfach (Schwelle) | Mittel (Verstärker) |
| Preis | Sehr günstig | Günstig | Mittel |

:::tip
Für einfache Temperaturüberwachung (z. B. Akku, Netzteil) ist der NTC ideal. Für Schutzabschaltungen der Keramik-PTC. Wenn Genauigkeit gefragt ist (Industriemessung, Kalibrierung), PT100 oder LM35/DS18B20.
:::
