---
title: OPV Integrierer
kategorie: EK
kapitel: OPV
tags: [integrierer, integration, opv, kondensator, rampe, dreieckssignal, i-anteil, pid, tiefpass, offset-drift, reset]
groessen: U_A|Ausgangsspannung|V; R|Widerstand|Ω; C|Kapazität|F; τ|Zeitkonstante|s; Δt|Integrationszeit|s
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Invertierend]]
- [[Tiefpass]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Differenzierer]]
- [[Tiefpass]]
:::
:::vbox
**Führt weiter zu**
- [[PID-Regler]]
:::
:::

---

Der OPV-Integrierer integriert das Eingangssignal über die Zeit. Ein konstantes Eingangssignal erzeugt am Ausgang eine linear steigende Rampe. Er entspricht einem idealen Tiefpassfilter und bildet den I-Anteil im PID-Regler.

## Schaltung

:::schematic OPV Integrierer: OPV-Dreieck. U_E links → R → invertierender Eingang (−). Nichtinvertierender Eingang (+) auf GND. Kondensator C in der Rückkopplung (von Ausgang zurück auf −). Optional: R_Reset parallel zu C (begrenzt DC-Drift). Ausgang U_A steigt linear bei konstantem U_E
/Diagramm/opv_integrierer.svg
:::

Wie der invertierende Verstärker — aber statt R_R liegt ein **Kondensator C** in der Rückkopplung. Am Eingang liegt Widerstand R.

## Formeln

:::formel
U_A = -(1 / (R * C)) * integral(U_E * dt)    # kontinuierlich
U_A = -(Delta_t / (R * C)) * U_E             # diskret (bei konstantem U_E)
:::

Umgestellt:

:::formel
U_E  = -U_A * R * C / Delta_t     # Eingangsspannung
Delta_t = -U_A * R * C / U_E      # Integrationszeit
R    = -U_E * Delta_t / (U_A * C) # Widerstand
C    = -U_E * Delta_t / (U_A * R) # Kondensator
:::

## Berechnungsbeispiel

:::monospace
U_E = 1 V, R = 10 kΩ, C = 1 µF → τ = R·C = 10 ms
Nach 10 ms: U_A = -(1/(10k×1µ)) × 1 V × 10 ms = -1 V
Nach 20 ms: U_A = -2 V (linear steigende Rampe)

Gesucht: U_A = -5 V nach 50 ms bei U_E = 0.5 V, C = 10 µF
R = -U_E * Δt / (U_A * C) = -0.5 × 50e-3 / (-5 × 10e-6) = 500 Ω
:::

## Signalformen

:::schematic Integrierer Signalformen: Oben Rechteck-Eingangssignal (U_E alternierend +/−). Unten Dreieck-Ausgangssignal (U_A steigt bei positiver Halbwelle, fällt bei negativer). Zeitachse gemeinsam. Bei konstantem Gleichspannungs-Eingang: Rampe bis Sättigungsgrenze
/Diagramm/opv_integrierer_signal.svg
:::

- **Rechteck am Eingang → Dreieck am Ausgang**: Jede Halbwelle wird integriert, der Ausgang steigt/fällt linear.
- **Konstante Spannung am Eingang → Rampe am Ausgang**: Linear bis zur Sättigungsgrenze.

## Offset-Drift (Praktisches Problem)

Eine Offsetspannung U_off am OPV-Eingang wird ebenfalls integriert — der Ausgang driftet langsam gegen die Versorgungsschiene, auch ohne Eingangssignal.

**Lösung**: Widerstand R_Reset parallel zum Kondensator C (typisch 10× R). Er begrenzt die DC-Verstärkung auf –R_Reset/R und verhindert Auflaufen. Nachteil: kein idealer Integrierer mehr.

Für präzise Anwendungen: Kondensator mit elektronischem Schalter (FET) periodisch entladen.

## Anwendungen

**I-Anteil im PID-Regler**: Integriert den Regelfehler auf — solange Fehler vorhanden, steigt die Stellgrösse. → [[PID-Regler]]

**Dreieckgenerator**: Rechteck → Integrierer → Dreieck, kombiniert mit Schmitt-Trigger als Rücksetzer.

**Aktiver Tiefpass 1. Ordnung**: Übergangsfrequenz f_g = 1/(2π·R·C), Dämpfung –20 dB/Dekade.
