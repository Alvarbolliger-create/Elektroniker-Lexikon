---
title: Derating
kategorie: EN
tags: [derating, belastungsminderung, MTBF, zuverlässigkeit, temperatur, lebensdauer, arrhenius, DC-Bias, MIL-HDBK-217, kondensator, widerstand]
symbol: —
einheit: %
---

Derating bedeutet, ein Bauteil mit weniger als der maximal zulässigen Belastung zu betreiben. Das verlängert die Lebensdauer erheblich und erhöht die Zuverlässigkeit (MTBF).

:::hbox
:::vbox
**Voraussetzungen**
- [[Datenblatt-Analyse]]
- [[Widerstand]]
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Verwandte Artikel**
- [[FMEA]]
- [[Lifecycle & Obsolescence]]
- [[Kühlkörperberechnung]]
:::
:::

---

## Warum Derating?

Jedes Bauteil hat eine Ausfallrate, die stark von Stress abhängt: Temperatur, Spannung, Strom und mechanische Beanspruchung. Die Ausfallrate steigt nicht linear, sondern exponentiell mit dem Stressniveau.

**Arrhenius-Gleichung** (vereinfacht für Temperaturstress):

:::monospace
λ(T) = λ0 × e^(Ea / (k × T))    # Ausfallrate steigt exponentiell mit Temperatur
:::
Faustregel: Jede 10 °C Temperaturerhöhung verdoppelt die Ausfallrate (bei manchen Bauteilen gilt sogar die Regel für 6 °C).

## Typische Derating-Regeln

### Widerstände
- Leistung: max. 50 % der Nennleistung im Betrieb
- Spannung: max. 80 % der maximalen Betriebsspannung

:::monospace
P_betrieb ≤ 0.5 × P_nenn    # 50 % Derating
:::
### Kondensatoren
- Betriebsspannung: max. 80 % der Nennspannung (Keramik) oder 50 % (Elektrolyt)
- Keramik: Kapazität sinkt stark bei hoher DC-Spannung (DC-Bias-Effekt) → tatsächliche Kapazität im Betrieb prüfen

:::monospace
U_betrieb ≤ 0.5 × U_nenn    # Elektrolyt: 50 % für lange Lebensdauer
:::
### Halbleiter
- Sperrspannung (Diode, Transistor): max. 70 % der Nennspannung
- Strom: max. 80 % des Nennstroms
- Temperatur: max. 25 °C unter max. Sperrschichttemperatur

:::formel
I_betrieb ≤ 0.8 × I_max
T_junction ≤ T_j_max - 25°C
:::
### Elektrolytkondensatoren: Temperaturkritisch

Die Lebensdauer eines Elektrolyts hängt stark von der Betriebstemperatur ab:

:::monospace
L(T) = L_base × 2^((T_max - T_betrieb) / 10)    # Lebensdauer verdoppelt sich je 10 K kühler
:::
Beispiel: Kondensator mit 105 °C / 2000 h Nennlebensdauer, betrieben bei 75 °C:
:::monospace
L = 2000 h × 2^((105-75)/10) = 2000 × 8 = 16'000 h
:::
## Auswirkung auf MTBF

Der MTBF (Mean Time Between Failures) steigt mit gutem Derating stark:

| Auslastung | Relativer MTBF |
|---|---|
| 100 % (kein Derating) | 1× |
| 80 % | 2–3× |
| 60 % | 5–10× |
| 50 % | 10–20× |

## Derating in Normen

- **MIL-HDBK-217**: US-Militär Zuverlässigkeitsmodell, enthält Derating-Tabellen für alle Bauteiltypen
- **ECSS-Q-ST-30-11**: ESA-Standard für Raumfahrtanwendungen (sehr konservatives Derating)
- **IPC-9592**: Anforderungen für Netzteile und Leistungswandler

## Praktische Hinweise

1. Nennleistung von Widerständen bezieht sich meist auf 70 °C Umgebungstemperatur. Bei höherer Umgebungstemperatur muss die zulässige Leistung weiter reduziert werden (Derating-Kurve im Datenblatt).
2. Bei Kondensatoren immer den DC-Bias-Effekt bei Keramik prüfen — ein 100-µF-Kondensator kann bei 80 % seiner Nennspannung auf 20 µF zusammenbrechen.
3. Für sicherheitskritische Anwendungen: Derating-Tabellen aus dem Anforderungsdokument (FMEA, Zuverlässigkeitsanalyse) verwenden.
