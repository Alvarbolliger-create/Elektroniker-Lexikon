---
title: NTC & PTC
kategorie: ET
tags: [ntc, ptc, thermistor, temperatursensor, kaltleiter, heissleiter, einschaltstrombegrenzer, pt100, polyfuse, pptc]
groessen: R|Widerstand|Ohm; T|Temperatur|°C; B|B-Parameter|K; alpha|Temperaturkoeffizient|1/K
_status: PORT  # ET_alt/Bauelemente/NTC_PTC.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Widerstand (Bauformen, Farbcode, E-Reihen)]]
:::
:::vbox
**Verwandte Artikel**
- [[Leiterwiderstand]]
- [[Elektrische Leistung]]
:::
:::

---

NTC und PTC sind Widerstände, deren Widerstandswert sich stark mit der Temperatur ändert. Sie werden als Temperatursensoren oder zum Schutz gegen Überstrom und Einschaltströme eingesetzt.

## Schaltsymbole

:::schematic
/schaltplaene/grundlagen/ntc_ptc_symbole.svg
:::

Beide Typen werden als Widerstandsrechteck dargestellt. Zwei schräge Pfeile zeigen die Wärmeeinwirkung an (wie beim Fototransistor das Licht). Der Buchstabe **Θ** (Theta) steht für Temperatur. Die Steigungsrichtung unterscheidet die Typen:

| Symbol | Bedeutung |
|---|---|
| −Θ oder NTC | Widerstand sinkt mit Temperatur (Heissleiter) |
| +Θ oder PTC | Widerstand steigt mit Temperatur (Kaltleiter) |

## NTC — Heissleiter (Negative Temperature Coefficient)

Der Widerstand des NTC **sinkt** mit steigender Temperatur. Das Verhalten ist nicht linear — der Widerstand hängt exponentiell von der Temperatur ab.

:::formel
R_NTC = R_25 * exp(B * (1/T - 1/T_25))    # T und T_25 in Kelvin (K = °C + 273)
:::

Der **B-Parameter** (typisch 2000–5000 K) beschreibt die Steilheit der Kennlinie.

| Kennwert | Bedeutung |
|---|---|
| R_25 | Nennwiderstand bei 25 °C |
| B-Parameter | Temperatursensitivität (Datenblatt) |

**Anwendungen:**
- Temperatursensor in Kühlkörpern, Batterien, Motoren
- Einschaltstrombegrenzer: Beim Einschalten ist NTC kalt → hoher Widerstand → begrenzt Einschaltstrom. Nach dem Aufwärmen sinkt R → kaum Verlust.

:::warning
NTC-Einschaltstrombegrenzer müssen vor jedem Einschalten wieder abkühlen können. Schnell hintereinander folgende Einschaltvorgänge (z. B. Notauslösung) können den Schutz unwirksam machen — der NTC ist noch heiss und hat kleinen Widerstand.
:::

## PTC — Kaltleiter (Positive Temperature Coefficient)

### Linearer PTC (Pt100)

Metallwiderstände (vor allem Platin) haben einen linearen positiven Temperaturkoeffizienten. Der Pt100 ist der Standard-Temperatursensor in der Messtechnik:

- **Pt100**: R_0 = 100 Ω bei 0 °C, alpha = 0,00385 /K (Platin)
- Messbereich: −200 °C bis +850 °C
- Sehr genau und langzeitstabil

:::formel
R_T = R_20 * (1 + alpha * (T - 20))    # lineare Näherung für kleinen T-Bereich
:::

### Sprunghafter PTC (Polyfuse / PPTC)

Aus Polymermaterial mit leitendem Russ. Bei Überschreitung einer Schwelltemperatur (verursacht durch zu hohen Strom → I²R → Erwärmung) dehnt sich das Polymer aus: Der Russ verliert den Kontakt → Widerstand steigt schlagartig um Faktor 1000.

- **Rückstellend**: Kühlt der PPTC ab, zieht sich das Polymer zusammen → Widerstand sinkt wieder → automatische Rückstellung
- Kein Austausch nötig wie bei Schmelzsicherungen

**Anwendungen:** USB-Ports (500 mA-Schutz), Lithium-Akkus, Platinen mit erhöhtem Kurzschlussrisiko.

## Anwendungen im Vergleich

| Typ | Anwendung | Prinzip |
|---|---|---|
| NTC Sensor | Temperaturmessung | Kalibrierte Kennlinie |
| NTC Begrenzer | Einschaltstrombegrenzer | Selbsterwärmung begrenzt Strom |
| Pt100/Pt1000 | Präzisions-Temperaturmessung | Linearer alpha-Wert |
| PPTC / Polyfuse | Rückstellende Sicherung | Selbst-Rückstellung nach Abkühlung |

## Kennzeichnung und Auswahl

| Parameter | NTC | PPTC |
|---|---|---|
| Nennwiderstand | R25 (bei 25 °C) | R_hold bei Nennstrom |
| Auslösestrom | — | I_trip |
| Haltestrom | — | I_hold |
| Rückstell | Nein (Sensor) / Ja (Begrenzer) | Ja (automatisch) |
