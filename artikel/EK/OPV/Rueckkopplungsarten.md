---
title: Rückkopplungsarten beim OPV
kategorie: EK
tags: [Rückkopplung, Gegenkopplung, Serienrückkopplung, Parallelrückkopplung, Impedanz, OPV]
symbol: —
einheit: —
---

Die Art der Rückkopplung bestimmt, wie ein Verstärker mit Ein- und Ausgang interagiert. Vier Grundtypen ergeben sich aus der Kombination von Spannungs-/Strom-Abnahme am Ausgang und Spannungs-/Strom-Einspeisung am Eingang.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Aufbau]]
- [[OPV Invertierend]]
- [[OPV Nichtinvertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[Frequenzgang und Stabilität]]
- [[OPV Verstärker (Typen)]]
:::
:::

---

## Grundprinzip der Gegenkopplung

Gegenkopplung (negative Rückkopplung) verbessert:
- Stabilität der Verstärkung (weniger abhängig von Bauelementen)
- Linearität (weniger Verzerrung)
- Bandbreite (auf Kosten der Verstärkung)
- Ein- und Ausgangsimpedanz (je nach Rückkopplungstyp)

## Die vier Rückkopplungstypen

### 1. Spannungs-Serien-Rückkopplung

- Ausgang: Spannungsabnahme (parallel)
- Eingang: Serienrückkopplung (in Reihe mit Quelle)

**Wirkung**:
- Eingangsimpedanz ↑ (höher als ohne Rückkopplung)
- Ausgangsimpedanz ↓

**Typische Schaltung**: Nichtinvertierender OPV-Verstärker. Die Ausgangsspannung wird zurück auf den invertierenden Eingang gegeben (in Reihe mit dem Quellsignal am nicht-invertierenden Eingang).

### 2. Spannungs-Parallel-Rückkopplung

- Ausgang: Spannungsabnahme (parallel)
- Eingang: Parallelrückkopplung (parallel zur Quelle)

**Wirkung**:
- Eingangsimpedanz ↓
- Ausgangsimpedanz ↓

**Typische Schaltung**: Invertierender OPV-Verstärker. Der Rückkopplungswiderstand Rf liegt zwischen Ausgang und dem invertierenden Eingang, in den auch das Eingangssignal eingespeist wird.

### 3. Strom-Serien-Rückkopplung

- Ausgang: Strommessung (seriell im Lastkreis)
- Eingang: Serienrückkopplung

**Wirkung**:
- Eingangsimpedanz ↑
- Ausgangsimpedanz ↑ (die Schaltung wirkt als Stromquelle)

**Typische Schaltung**: Spannungs-Strom-Wandler (Transkonduktanzverstärker). Ausgangsstrom wird über einen Messwiderstand in eine Rückkopplungsspannung umgewandelt.

### 4. Strom-Parallel-Rückkopplung

- Ausgang: Strommessung (seriell)
- Eingang: Parallelrückkopplung

**Wirkung**:
- Eingangsimpedanz ↓
- Ausgangsimpedanz ↑

**Typische Schaltung**: Transimpedanzverstärker (TIA) in bestimmten Konfigurationen.

## Zusammenfassung

| Typ | Eingangsimpedanz | Ausgangsimpedanz |
|---|---|---|
| Spannungs-Serien | steigt | sinkt |
| Spannungs-Parallel | sinkt | sinkt |
| Strom-Serien | steigt | steigt |
| Strom-Parallel | sinkt | steigt |

**Merkhilfe**: 
- Spannungsrückkopplung am Ausgang → Ausgangsimpedanz sinkt (Schaltung wird zur Spannungsquelle)
- Stromrückkopplung am Ausgang → Ausgangsimpedanz steigt (Schaltung wird zur Stromquelle)
- Serienrückkopplung am Eingang → Eingangsimpedanz steigt
- Parallelrückkopplung am Eingang → Eingangsimpedanz sinkt

## Stabilitätsbedingung

Rückkopplung stabilisiert nur, wenn sie negativ (Gegenkopplung) ist. Positive Rückkopplung führt zur Instabilität oder Oszillation — das wird bei Komparatoren mit Hysterese und Oszillatoren bewusst eingesetzt.
