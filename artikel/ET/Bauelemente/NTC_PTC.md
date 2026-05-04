---
title: NTC und PTC
kategorie: ET
tags: [NTC, PTC, thermistor, temperatursensor, kaltleiter, heissleiter, einschaltstrombegrenzer, pt100, polyfuse, PPTC, steinhart-hart, B-parameter]
symbol: —
einheit: Ω
---

NTC und PTC sind Widerstände deren Widerstandswert sich stark mit der Temperatur ändert. Sie werden als Temperatursensoren, Schutzbauelemente und Anlaufstrombegrenzer eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Temperatursensoren]]
- [[Elektrische Leistung]]
:::
:::
---

## NTC — Heissleiter (Negative Temperature Coefficient)

Der Widerstand sinkt mit steigender Temperatur. Material: Halbleiterkeramik (Metalloxide wie MnO, NiO, CoO).

**R-T-Charakteristik:**

:::monospace
R(T) = R25 * e^(B * (1/T - 1/T25))     # Steinhart-Hart B-Parameter-Gleichung
:::
- R25: Nennwiderstand bei 25 °C
- B: Materialkonstante (typisch 3000–5000 K)
- T: Temperatur in Kelvin

| Anwendung | Typischer Wert |
|---|---|
| NTC als Sensor | 10 kΩ bei 25 °C, B = 3950 K |
| NTC als Einschaltstrombegrenzer | 5–47 Ω bei 25 °C |

**Nichtlineares Verhalten:** Die R-T-Kurve ist stark nichtlinear. Für präzise Temperaturmessungen wird die Steinhart-Hart-Gleichung oder eine Kennlinie aus dem Datenblatt verwendet.

## PTC — Kaltleiter (Positive Temperature Coefficient)

Der Widerstand steigt mit steigender Temperatur. Es gibt zwei Typen mit sehr unterschiedlichem Verhalten:

### Linearer PTC (Kaltleiter, z. B. Platin-Pt100)

Schwache, annähernd lineare Kennlinie. Wird ausschliesslich als Präzisionssensor eingesetzt.

:::monospace
R(T) = R0 * (1 + α * T)     # α ≈ 0.00385 /°C für Pt100
:::
Pt100: 100 Ω bei 0 °C. Pt1000: 1000 Ω bei 0 °C. Sehr stabile, reproduzierbare Kennlinie.

### Sprunghafter PTC (Polyfuse, PPTC)

Starker, nichtlinearer Widerstandsanstieg ab einer Schalttemperatur. Material: leitfähige Polymerkeramik (Barium-Titanat, BaTiO₃).

Unterhalb der Schalttemperatur: niedriger Widerstand (< 1 Ω).
Oberhalb: Widerstand steigt um Faktor 1000–10.000 innerhalb weniger Grad.

## Anwendungen

### NTC als Temperatursensor

Günstig, empfindlich, einfach auszulesen über Spannungsteiler. Für hohe Genauigkeit muss die nichtlineare Kennlinie in der Software kompensiert werden.

:::monospace
U_mess = U_vers * R_NTC / (R_fix + R_NTC)    # Spannungsteiler mit Festwiderstand
:::
Typisch: R_fix = R_NTC(25°C) für beste Auflösung im Arbeitsbereich.

### NTC als Einschaltstrombegrenzer

Beim Einschalten ist der NTC kalt → hoher Widerstand → begrenzt den Einschaltstrom von Netzteilen und Motoren. Im Betrieb erwärmt er sich → niedriger Widerstand → geringe Verlustleistung.

:::warning
NTC-Einschaltstrombegrenzer können nach dem Abschalten noch heiss sein. Kurze Wiedereinschaltungen bieten dann keinen Schutz mehr, da der NTC noch niederohmig ist.
:::

### PTC als Schutzbauelement (Polyfuse)

Selbstrückstellende Sicherung. Bei Überstromereignis erwärmt sich der PTC → hoher Widerstand → Strom sinkt auf Haltestrom → bleibt hochohmig solange Spannung anliegt → kehrt nach Abschalten auf niedrigen Widerstand zurück.

Typische Kennwerte aus dem Datenblatt:
- **I_hold**: Dauerstrom ohne Auslösung
- **I_trip**: Auslösestrom
- **V_max**: Maximale Betriebsspannung

### PTC als Motorschutz

In Motorwicklungen eingebaut. Löst bei Überhitzung aus und schaltet den Motor ab (über Auswerteschaltung).

## Kennzeichnung und Auswahl

| Kenngrösse | NTC | PTC (Polyfuse) | Pt100 |
|---|---|---|---|
| Kennlinie | Exponentiell fallend | Sprunghaft steigend | Linear steigend |
| Genauigkeit | Mittel | Gering | Hoch |
| Typische Anwendung | Sensor, Strombegrenzer | Schutzschalter | Präzisionssensor |
| Preis | Günstig | Günstig | Teurer |
