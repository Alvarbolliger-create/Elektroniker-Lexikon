---
title: PID-Regler
kategorie: EK
kapitel: Regelungstechnik
tags: [PID-Regler, P-Anteil, I-Anteil, D-Anteil, integrierer, differenzierer, OPV, KP, KI, KD, stellgrösse, regeldifferenz, tiefpass, hochpass, ziegler-nichols, wind-up, rauschen]
groessen: K_P|Proportionalbeiwert|—; K_I|Integrierbeiwert|1/s; K_D|Differenzierbeiwert|s; e|Regeldifferenz|V; y|Stellgrösse|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Regelkreis Grundlagen]]
- [[Regelstrecke]]
- [[OPV Integrierer]]
- [[OPV Differenzierer]]
:::
:::vbox
**Verwandte Artikel**
- [[Regelstrecke]]
:::
:::vbox
**Führt weiter zu**
- [[Verstärkung & Dämpfung]]
:::
:::

---

Der PID-Regler kombiniert drei Regelanteile für schnelles, stabiles Ausregeln ohne bleibende Abweichung. In der Elektronik wird jeder Anteil durch einen OPV realisiert.

## Die drei Anteile

### P-Anteil — Proportional
Stellgrösse direkt proportional zur aktuellen Regeldifferenz. **Schnell**, aber hinterlässt **bleibende Abweichung**.

### I-Anteil — Integral
Stellgrösse proportional zur aufintegrierten Regeldifferenz. **Eliminiert bleibende Abweichung** (solange e ≠ 0, wächst y weiter). Macht Regelung träger.

### D-Anteil — Differential
Stellgrösse proportional zur **Änderungsrate** der Regeldifferenz. Reagiert auf de/dt — "vorausschauend", dämpft Überschwingen. Verstärkt aber Rauschen.

## PID-Stellgrösse (zeitkontinuierlich)

:::formel
y = K_P * e + K_I * integral(e, dt) + K_D * de/dt    # PID-Gesamtstellgrösse
:::

## OPV-Realisierung der Anteile

### I-Anteil = OPV-Integrierer (Aktiver Tiefpass)

:::formel
U_Aus = -(1 / (R * C)) * integral(U_Ein, dt)    # OPV-Integrierer
tau   = R * C                                     # Zeitkonstante
:::

**Vergleich Tiefpass ↔ Integrierer** (aus Spick S. 28):
- **Passiver Tiefpass** (R + C): dämpft ab f_g = 1/τ, Ausgangsspannung begrenzt
- **Aktiver Integrierer** (R + C + OPV): integriert ohne Grenze bis zum Aussteuerungsanschlag (Wind-Up!)

### D-Anteil = OPV-Differenzierer (Aktiver Hochpass)

:::formel
U_Aus = -R * C * dU_Ein/dt    # OPV-Differenzierer
:::

**Vergleich Hochpass ↔ Differenzierer** (aus Spick S. 28):
- **Passiver Hochpass** (C + R): sperrt bis f_g, dann konstant
- **Aktiver Differenzierer** (C + R + OPV): differenziert — verstärkt Hochfrequenz unbegrenzt → Rauschproblem!

## OPV-Realisierung des PID-Reglers

:::schematic PID-Regler aus OPVs: Eingang e (Regeldifferenz) links. Drei parallele Zweige: (1) P-Zweig: OPV invertierend mit R5/R6 → Yp. (2) I-Zweig: OPV-Integrierer (R8, C3) → Yi. (3) D-Zweig: OPV-Differenzierer (C4, C5, R10) mit Tiefpass-Schutz → Yd. Summierer (U4): alle drei Ausgänge über gleiche Widerstände R7/R9/R11 auf (−)-Eingang → Ausgang y = Yp+Yi+Yd. U1 (Subtrahierer) für e = w−x davor
/Diagramm/pid_regler_opv.svg
:::

## Schema PID-Regler (OPV-Realisierung, Spick S. 28)

| Block | OPV | Funktion | Bauteilwerte |
|---|---|---|---|
| U1 | Subtrahierer | Regeldifferenz e = x − w | R3, R4 = 100 kΩ |
| U2 | Verstärker | P-Anteil Yp = K_P · e | R5=1kΩ, R6=6% (Poti) |
| U3 | Integrierer | I-Anteil Yi = K_I · ∫e dt | R8=64% (Poti), C3=100 nF |
| U5/U6 | Differenzierer | D-Anteil Yd = K_D · de/dt | C4=1 µF, C5=50 nF, R10=65% |
| U4 | Summierer | Y = Yp + Yi + Yd | R7, R9, R11, R12 = 10 kΩ |

Ausgangstiefpass (R13=1 kΩ, C6=470 nF) glättet hochfrequente Anteile des D-Glieds.

:::warning
**Wind-Up (I-Anteil):** Wenn der Aktor in der Begrenzung ist (z.B. Heizung 100 %), läuft der Integrierer weiter auf. Nach dem Abschalten dauert es lange, bis Yi wieder normal ist → Regelung überschwingt stark. Abhilfe: Anti-Wind-Up Schaltung (Integrierer begrenzen).

**Rauschen (D-Anteil):** Der Differenzierer verstärkt Messrauschen. Immer mit Begrenzungskondensator (C5 im Spick-Schema) oder Tiefpass vor dem D-Eingang bändigen.
:::

## Wirkung der Anteile

| Anteil | Vergrössern bewirkt | Gefahr |
|---|---|---|
| K_P grösser | schnellere Reaktion, kleinere Abweichung | Schwingen, Instabilität |
| K_I grösser | kleinere bleibende Abweichung | Wind-Up, Überschwingen |
| K_D grösser | weniger Überschwingen, schnellere Dämpfung | Rauschverstärkung |

## Reglereinstellung nach Ziegler-Nichols

**Einschaltmethode** (empirisch, Sprungmethode):

:::monospace
1. Aus Sprungantwort: t_u (Verzugszeit), t_g (Ausgleichszeit), K_S ablesen

PID nach Ziegler-Nichols:
K_P = 1.2 / (K_S * t_u/t_g)
T_I = 2 * t_u    → K_I = K_P / T_I
T_D = 0.5 * t_u  → K_D = K_P * T_D
:::

**Schwingmethode** (nur K_P aktiv, aufdrehen bis Dauerschwingung):

:::monospace
K_krit: kritische Verstärkung (bei Dauerschwingung)
T_krit: Periodendauer der Dauerschwingung

PID: K_P = 0.6 × K_krit
     T_I = 0.5 × T_krit  → K_I = K_P / T_I
     T_D = 0.125 × T_krit → K_D = K_P × T_D
:::
