---
title: Einheiten
kategorie: Grundlagen
---

# Einheiten

Alle Einheiten beginnen mit einem Unterstrich `_`. So weiß der Rechner sofort, dass es eine Einheit ist und keine Variable.

```
F := 2 * _kN          ▶  F := 2000 N
s := 5 * _m           ▶  s := 5 m
W := F * s            ▶  W := 10000 J
aprox(W)              ▶  10 kJ     (im ENG-Modus)
```

Der Rechner versucht automatisch, auf eine einzelne abgeleitete Einheit zurückzuführen: `_J/_m` wird zu `_N`, `_V/_A` zu `_Ω`, `_W/_V` zu `_A`, `_kWh * _Hz` wird zu `_W` usw. Ergebnisse aus `solve(...)` werden ebenfalls automatisch vereinfacht.

## Basiseinheiten

| Schreibweise | Bedeutung |
|---|---|
| `_m`   | Meter |
| `_kg`  | Kilogramm |
| `_s`   | Sekunde |
| `_A`   | Ampere |
| `_K`   | Kelvin |
| `_mol` | Mol |
| `_cd`  | Candela |

## Abgeleitete SI-Einheiten

| Schreibweise | Bedeutung |
|---|---|
| `_N`   | Newton (Kraft) |
| `_J`   | Joule (Energie) |
| `_W`   | Watt (Leistung) |
| `_Pa`  | Pascal (Druck) |
| `_Hz`  | Hertz (Frequenz) |
| `_V`   | Volt (Spannung) |
| `_Ohm` | Ohm (Widerstand, auch `_ohm`) |
| `_F`   | Farad (Kapazität) |
| `_C`   | Coulomb (Ladung) |
| `_T`   | Tesla (magn. Flussdichte) |
| `_H`   | Henry (Induktivität) |
| `_Wb`  | Weber (magn. Fluss) |
| `_S`   | Siemens (Leitwert) |

## Praktische Zusätze

| Schreibweise | Bedeutung |
|---|---|
| `_g`   | Gramm |
| `_L`   | Liter |
| `_min` | Minute |
| `_h`   | Stunde |
| `_Wh`  | Wattstunde (= 3 600 J) |
| `_kWh` | Kilowattstunde (= 3,6 MJ) |
| `_MWh` | Megawattstunde |

## SI-Präfixe

Alle üblichen Präfixe funktionieren direkt vor dem Einheitennamen:

| Präfix | Faktor | Beispiel |
|---|---|---|
| `Y` Yotta | 10²⁴ | |
| `Z` Zetta | 10²¹ | |
| `E` Exa   | 10¹⁸ | |
| `P` Peta  | 10¹⁵ | |
| `T` Tera  | 10¹² | `_THz` |
| `G` Giga  | 10⁹  | `_GW`, `_GHz` |
| `M` Mega  | 10⁶  | `_MHz`, `_MV` |
| `k` Kilo  | 10³  | `_km`, `_kN`, `_kOhm` |
| `h` Hecto | 10²  | `_hPa` |
| `da` Deka | 10¹  | |
| `d` Dezi  | 10⁻¹ | `_dL` |
| `c` Centi | 10⁻² | `_cm` |
| `m` Milli | 10⁻³ | `_mm`, `_mA`, `_ms` |
| `µ` / `u` Mikro | 10⁻⁶ | `_µm`, `_um`, `_µF` |
| `n` Nano  | 10⁻⁹ | `_nF`, `_ns` |
| `p` Pico  | 10⁻¹² | `_pF` |
| `f` Femto | 10⁻¹⁵ | `_fs` |
| `a` Atto  | 10⁻¹⁸ | |
| `z` Zepto | 10⁻²¹ | |
| `y` Yocto | 10⁻²⁴ | |

**Wichtig:** Basiseinheiten haben Vorrang vor Präfix-Kombinationen. `_m` ist immer Meter (nicht „Milli-irgendwas"), `_min` ist Minute (nicht „Milli-in"), `_h` ist Stunde.

## Wissenschaftliche Notation

Große oder kleine Zahlen kannst du mit `E` schreiben — SymPy versteht das direkt:

```
C := 1.5E-6 * _F      ▶  C := 3/2000000 F
aprox(C)              ▶  1.5 µF     (ENG-Modus)
```

Oder du schreibst es gleich in die Einheit: `1.5 * _µF` ist identisch mit `1.5E-6 * _F`.

## Umrechnungen mit `aprox`

Für ein hübsch formatiertes Ergebnis mit passendem Präfix verwendest du `aprox(...)` oder Ctrl+Enter. Siehe [[aprox]].

## Was geht (noch) nicht

- Nicht-SI-Einheiten wie Zoll, Fuß, PS, psi: bewusst weggelassen. Kann man bei Bedarf ergänzen.
- Temperatur-Offsets (°C ↔ K): nur als Kelvin. `0 _°C = 273.15 _K` muss von Hand gemacht werden.
- Prozent und Promille: keine eigenen Einheiten, einfach Faktor `0.01` bzw. `0.001` schreiben.
