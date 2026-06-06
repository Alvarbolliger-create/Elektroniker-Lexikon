---
title: Zener-Diode
kategorie: EK
kapitel: Halbleiter
tags: [zener, zenerdiode, z-diode, spannungsreferenz, zenerspannung, zenereffekt, avalanche-effekt, spannungsstabilisierung, vorwiderstand, überspannungsschutz]
groessen: U_Z|Zenerspannung|V; I_Z|Zenerstrom|A; I_Zmax|max. Zenerstrom|A; R_V|Vorwiderstand|Ω; P_Z|Verlustleistung|W
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[pn-Übergang]]
:::
:::vbox
**Verwandte Artikel**
- [[Spannungsstabilisierung]]
- [[TVS-Diode & Varistor]]
:::
:::vbox
**Führt weiter zu**
- [[Spannungsstabilisierung]]
- [[TVS-Diode & Varistor]]
:::
:::

---

Die Zener-Diode wird absichtlich in **Sperrrichtung** betrieben. Sie bricht bei einer definierten Spannung (Zenerspannung U_Z) kontrolliert durch und hält diese Spannung aufrecht — egal wie viel Strom fliesst. Sie dient als einfache Spannungsreferenz und Überspannungsschutz.

## Schaltsymbol

:::hbox
:::schematic Diode (zum Vergleich)
/schaltplaene/symbole/D.svg
:::
:::schematic Zener-Diode
/schaltplaene/symbole/D_Z.svg
:::
:::

Wie eine normale Diode, aber die Kathoden-Linie hat beidseitig Knicke (Z-Form).

## Durchbruchmechanismen

### Zener-Effekt (U_Z < 5 V)
Bei tiefer Zenerspannung (starke Dotierung → enge Raumladungszone) ist das elektrische Feld in der Sperrschicht so stark, dass es Elektronen direkt aus den Valenzbindungen herausreisst. Dieser Tunnelprozess ist der eigentliche "Zener-Effekt". Er beginnt bei genau definierten Spannungen.

### Lawinendurchbruch / Avalanche-Effekt (U_Z > 7 V)
Beschleunigte Elektronen stossen mit dem Kristallgitter und schlagen weitere Elektronen heraus — eine Lawine entsteht. Etwas weniger stabil, aber in der Praxis ebenso gut kontrollierbar.

Zwischen 5 V und 7 V arbeiten beide Mechanismen — die Temperaturkoeffizienten heben sich auf, was diese Zener sehr stabil macht.

## Grundschaltung: Spannungsreferenz

Vorwiderstand R_V in Reihe, Zener-Diode parallel zur Last und nach GND. Die Ausgangsspannung bleibt auf U_Z, solange genügend Strom durch die Zener fliesst.

:::formel
R_V = (U_ein - U_Z) / (I_Z + I_L)    # Vorwiderstand; I_Z ≥ I_Zmin (5–10 mA typisch)
P_Z = U_Z * I_Zmax                    # max. Verlustleistung der Zener prüfen
:::

:::monospace
Beispiel: U_ein = 12 V, U_Z = 5.1 V, I_L = 20 mA, I_Z = 10 mA
R_V = (12 - 5.1) / (10e-3 + 20e-3) = 6.9 / 30e-3 = 230 Ω → nächster Normwert: 220 Ω
P_RV = (U_ein - U_Z)² / R_V = 6.9² / 220 = 216 mW → Widerstand 0.5 W wählen
:::

:::warning
Zener niemals ohne Vorwiderstand direkt an eine Spannungsquelle anschliessen — unbegrenzter Strom zerstört sie sofort.
:::

## Normierte Zenerspannungen

Typische Werte (E12-Reihe): 2.4 V · 2.7 V · 3.0 V · 3.3 V · 3.6 V · 3.9 V · 4.3 V · 4.7 V · 5.1 V · 5.6 V · 6.2 V · 6.8 V · 7.5 V · 8.2 V · 9.1 V · 10 V · 12 V · 15 V · 18 V · 22 V · 27 V · 33 V

## Bauteile im Vergleich

| Typ | U_Z | P_max | Toleranz | Gehäuse |
|---|---|---|---|---|
| BZX55C5V1 | 5.1 V | 500 mW | ±5 % | DO-35 |
| BZX84C3V3 | 3.3 V | 300 mW | ±5 % | SOT-23 |
| BZX85C12 | 12 V | 1.3 W | ±5 % | DO-41 |
| LM4040-5.0 | 5.0 V | 150 mW | ±0.1 % | SOT-23 |

## Anwendungen

**Spannungsreferenz**: Stabile Spannung für ADC-Referenz, Komparatoreingänge, einfache Versorgungen kleiner Lasten.

**Überspannungsschutz**: Zener parallel zum Eingang — bei Überspannung leitet sie ab. Günstige Alternative zur TVS bei langsamen Transienten.

**Pegelverschiebung**: Ein Signal um U_Z anheben, z. B. für Levelshifter-Schaltungen.

:::tip
Für genaue Referenzspannungen (< ±1 %) besser eine dedizierte Spannungsreferenz (z. B. LM4040, LM385) wählen. Zener-Dioden haben typisch ±5 % und einen Temperaturkoeffizienten von bis zu 100 ppm/K.
:::
