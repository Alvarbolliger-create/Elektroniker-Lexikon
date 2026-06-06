---
title: OPV Differenzierer
kategorie: EK
kapitel: OPV
tags: [differenzierer, ableitung, opv, kondensator, hochpass, d-anteil, pid, rauschempfindlich, flankenerkennung, begrenzung]
groessen: U_A|Ausgangsspannung|V; R|Widerstand|Ω; C|Kapazität|F; ΔU_E|Spannungsänderung|V; Δt|Zeit|s
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Invertierend]]
- [[Hochpass]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Integrierer]]
- [[Hochpass]]
:::
:::vbox
**Führt weiter zu**
- [[PID-Regler]]
:::
:::

---

Der OPV-Differenzierer gibt die Änderungsrate des Eingangssignals aus. Ein konstantes Signal ergibt null am Ausgang. Eine schnelle Flanke erzeugt einen grossen Impuls. Er bildet den D-Anteil im PID-Regler — ist aber rauschempfindlich.

## Schaltung

:::schematic OPV Differenzierer: OPV-Dreieck. U_E links → Kondensator C → invertierender Eingang (−). Optional R_S in Reihe zu C (Rauschbegrenzung). Nichtinvertierender Eingang (+) auf GND. Widerstand R in der Rückkopplung (von Ausgang zurück auf −). Ausgang U_A proportional zur Ableitung dU_E/dt
/Diagramm/opv_differenzierer.svg
:::

Wie der invertierende Verstärker — aber **Kondensator C am Eingang** und Widerstand R in der Rückkopplung.

## Formeln

:::formel
U_A = -R * C * (Delta_U_E / Delta_t)    # Ausgang proportional zur Änderungsrate
:::

Umgestellt:

:::formel
Delta_U_E = -U_A * Delta_t / (R * C)    # Eingangsspannungsänderung
Delta_t   = -R * C * Delta_U_E / U_A   # Zeit
R = -U_A * Delta_t / (Delta_U_E * C)   # Widerstand
C = -U_A * Delta_t / (Delta_U_E * R)   # Kondensator
:::

## Berechnungsbeispiel

:::monospace
C = 100 nF, R = 10 kΩ → τ = R·C = 1 ms
Eingangssignal: Dreieck, Anstieg 1 V in 1 ms → ΔU_E/Δt = 1000 V/s

U_A = -R·C · (ΔU_E/Δt) = -1e-3 × 1000 = -1 V (konstante Spannung während Flanke)
Bei Dreieck-Eingang → Rechteck am Ausgang
:::

## Signalformen

:::schematic Differenzierer Signalformen: Oben Dreieck-Eingangssignal (konstante Flankensteigung). Unten Rechteck-Ausgangssignal (konstanter Wert bei jeder Flanke, springt bei Umkehrung). Bei Rechteck-Eingang → schmale Impulse an den Flanken
/Diagramm/opv_differenzierer_signal.svg
:::

- **Dreieck am Eingang → Rechteck am Ausgang**: Konstante Flankensteigung → konstante Ausgangsspannung.
- **Sinus am Eingang → Cosinus am Ausgang**: Ableitung des Sinus ist der Cosinus (mit Verstärkung).
- **Rechteck am Eingang → Impulse am Ausgang**: Steile Flanken → grosse Ausgangsimpulse.

## Rauschproblem (Praktisches Problem)

Rauschen hat hohe Frequenzanteile — die Ableitung verstärkt hohe Frequenzen. Ein idealer Differenzierer würde Hochfrequenzrauschen massiv verstärken.

**Lösung**: Kleiner Widerstand R_S in Reihe zum Kondensator (typisch R_S = R/10). Er begrenzt die Hochfrequenzverstärkung auf –R/R_S und bändigt das Rauschen.

:::warning
Differenzierer ohne Hochfrequenzbegrenzung schwingen und rauschen stark. In der Praxis immer R_S vorsehen — sonst unbrauchbar.
:::

## Vergleich Integrierer vs. Differenzierer

| Eigenschaft | Integrierer | Differenzierer |
|---|---|---|
| C-Position | Rückkopplung | Eingang |
| R-Position | Eingang | Rückkopplung |
| Funktion | ∫ U_E dt | dU_E/dt |
| Problem | Offset-Drift | Rauschverstärkung |
| Tiefpass/Hochpass | Tiefpass | Hochpass |
| PID-Anteil | I | D |

## Anwendungen

**D-Anteil im PID-Regler**: Reagiert auf schnelle Änderungen der Regelabweichung. Dämpft Überschwingen. → [[PID-Regler]]

**Flankenerkennung**: Impulse bei Signalflanken, z. B. um Taktflanken zu detektieren.
