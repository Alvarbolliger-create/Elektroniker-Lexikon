---
title: OPV Invertierender Verstärker
kategorie: EK
kapitel: OPV
tags: [invertierend, invertierender verstärker, opv, phasenumkehr, 180 grad, virtuelle masse, gegenkopplung, gbw, gain-bandwidth-product]
groessen: v_u|Verstärkung|—; U_A|Ausgangsspannung|V; U_E|Eingangsspannung|V; R_R|Gegenkopplungswiderstand|Ω; R1|Eingangswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Nichtinvertierender Verstärker]]
- [[OPV Summierender Verstärker]]
:::
:::vbox
**Führt weiter zu**
- [[OPV Summierender Verstärker]]
- [[OPV Integrierer]]
- [[OPV Differenzierer]]
:::
:::

---

Der invertierende Verstärker dreht das Signal um 180° und verstärkt es. Verstärkung und Eingangswiderstand werden durch zwei Widerstände exakt definiert — unabhängig vom OPV-Typ.

## Schaltung

:::schematic Invertierender Verstärker
/schaltplaene/OPV/Verstärker/opv_invertierender_verstaerker.svg
:::

Signal über R1 an den invertierenden Eingang (–). R_R von Ausgang zurück auf (–). Nichtinvertierender Eingang (+) liegt auf GND (oder Referenz).

## Formeln

:::formel
U_A = -U_E * R_R / R1      # Ausgangsspannung; Minuszeichen = 180° Phasenumkehr
v_u = -R_R / R1            # Verstärkung; negativ = Phasenumkehr
:::

## Virtuelle Masse

Die Gegenkopplung zwingt den OPV seinen Ausgang nachzuregeln bis U_– = U_+ = 0 V (da + auf GND). Der Knoten am invertierenden Eingang (–) bleibt auf 0 V — die **virtuelle Masse**.

Der gesamte Strom aus U_E fliesst durch R1 in die virtuelle Masse, dann weiter durch R_R in den Ausgang. Nichts davon geht in den OPV-Eingang.

:::info
Virtuelle Masse gilt nur solange der Ausgang nicht sättigt. Wenn U_A die Versorgungsgrenze erreicht, bricht die virtuelle Masse zusammen.
:::

## Berechnungsbeispiel

:::monospace
Gesucht: U_A = -5 V aus U_E = 0.5 V (Verstärkung -10)
R1 = 10 kΩ (frei wählbar)
R_R = |v_u| × R1 = 10 × 10 kΩ = 100 kΩ

Probe: U_A = -0.5 × 100k/10k = -5 V ✓
:::

## Referenzspannung am (+)-Eingang (angehobene virtuelle Masse)

Liegt der (+)-Eingang nicht auf GND, sondern auf einer Referenzspannung **V_ref**, verschiebt sich die virtuelle Masse auf dieses Potential. Die Formel erweitert sich:

:::formel
U_A = V_ref * (1 + R_R / R1) - U_E * R_R / R1    # mit Referenz V_ref am (+)-Eingang
:::

Die **Wechselspannungsverstärkung** (AC-Anteil) bleibt unverändert –R_R/R1. Nur der **DC-Arbeitspunkt** des Ausgangs verschiebt sich:

- Ohne Referenz (V_ref = 0): U_A schwingt um 0 V
- Mit Referenz (V_ref > 0): U_A schwingt um V_ref × (1 + R_R/R1) — der Ausgang ist nach oben verschoben

:::monospace
Beispiel: R1 = 1 kΩ, R_R = 2 kΩ, V_ref = +6 V, U_E = 1 V Sinus
  DC-Arbeitspunkt: 6 × (1 + 2/1) = 18 V
  AC-Anteil: –2 × 1 V = –2 V Amplitude, invertiert
  → Ausgang: Invertierter Sinus (2 V Amplitude) zentriert um +18 V
:::

:::tip
Anwendung: Der Offset V_ref × (1 + R_R/R1) dient als DC-Verschiebung des Ausgangssignals — z.B. um ein bipolares Signal in einen einseitig versorgten ADC-Eingang zu verschieben.
:::

## GBW und Bandbreite

Das Gain-Bandwidth-Product (GBW) ist für jeden OPV-Typ konstant — die nutzbare Bandbreite f_3dB ergibt sich aus f_3dB = GBW / |v_u|: bei LM741 (GBW = 1 MHz) und v_u = 10 bleiben 100 kHz.

| OPV | GBW | v_u = 1 | v_u = 10 | v_u = 100 |
|---|---|---|---|---|
| LM741 | 1 MHz | 1 MHz | 100 kHz | 10 kHz |
| TL071 | 3 MHz | 3 MHz | 300 kHz | 30 kHz |
| OPA2134 | 8 MHz | 8 MHz | 800 kHz | 80 kHz |

:::warning
Hohe Verstärkung = kleine Bandbreite. Bei A = –100 und GBW = 1 MHz ist die Bandbreite nur 10 kHz. Immer GBW prüfen bevor ein OPV-Typ gewählt wird.
:::
