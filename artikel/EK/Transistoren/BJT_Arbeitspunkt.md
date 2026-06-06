---
title: BJT Arbeitspunkt
kategorie: EK
kapitel: Transistoren
tags: [arbeitspunkt, q-punkt, querstrom, spannungsteiler, vorspannung, arbeitsgerade, thermische stabilität, emitterwiderstand, vier-widerstands-netzwerk]
groessen: I_C|Kollektorstrom im AP|A; U_CE|Kollektor-Emitter-Spannung im AP|V; I_q|Querstrom|A; U_BE|Basis-Emitter-Spannung|V; U_E|Emitterspannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BJT Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[BJT Emitterschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[BJT Emitterschaltung]]
- [[BJT Kollektorschaltung]]
:::
:::

---

Der Arbeitspunkt (Q-Punkt) legt fest, wo auf der Kennlinie der Transistor im Ruhezustand arbeitet. Er muss so gewählt werden, dass das Wechselsignal verstärkt wird ohne zu verzerren — der Transistor darf weder sättigen noch sperren.

## Warum ein Arbeitspunkt?

Ein Transistor im Verstärkerbetrieb braucht einen definierten Gleichstrom-Ruhezustand. Liegt der Q-Punkt zu hoch, sättigt der Transistor bei positiven Halbwellen. Liegt er zu tief, sperrt er bei negativen. Beides schneidet das Signal ab.

**Optimaler Arbeitspunkt** für maximale Aussteuerung:

:::formel
U_CE = U_B / 2    # Arbeitspunkt in der Mitte des linearen Bereichs
:::

## Arbeitsgerade (Lastgerade)

Die Arbeitsgerade beschreibt, welche Kombinationen von U_CE und I_C die Beschaltung zulässt — unabhängig vom Transistor selbst. Sie wird in das **Ausgangskennlinienfeld** eingetragen. Der Q-Punkt liegt dort, wo die Arbeitsgerade die Ausgangskennlinie für den eingestellten I_B schneidet.

:::formel
I_C = (U_B - U_CE) / R_C    # Arbeitsgerade; zwei Endpunkte:
                              #   U_CE = U_B  →  I_C = 0 (gesperrt)
                              #   U_CE = 0    →  I_C = U_B / R_C (gesättigt)
:::

:::schematic Arbeitsgerade im Ausgangskennlinienfeld: Gerade von (U_B, 0) nach (0, U_B/R_C). Kennlinien für I_B = 0, 20, 40, 60 µA eingezeichnet. Q-Punkt markiert in der Mitte der Geraden bei U_CE = U_B/2
/Diagramm/bjt_arbeitsgerade.svg
:::

## Schaltung: Vier-Widerstands-Netzwerk (Spannungsteiler-Vorspannung)

:::schematic Vier-Widerstands-Netzwerk: U_B oben, R_C nach Kollektor, R_E nach Emitter-GND. R1 von U_B nach Basis, R2 von Basis nach GND. Koppelkondensatoren C_ein (Eingang), C_aus (Ausgang), C_E (parallel R_E)
/Diagramm/bjt_arbeitspunkt_netzwerk.svg
:::

Die stabilste Methode: R1, R2, R_C und R_E. Der Querstrom I_q durch R1/R2 stabilisiert den Arbeitspunkt gegen B-Streuungen und Temperaturänderungen.

## Dimensionierung Schritt für Schritt

Die Dimensionierung des Emitterschaltungs-Arbeitspunkts erfolgt in einer festen Reihenfolge. Ausgangspunkt sind I_C und U_B (Versorgungsspannung):

**1. Kollektorspannung und Kollektorwiderstand:**
:::formel
U_C = U_B - U_CE - U_E    # Spannung über R_C
R_C = U_C / I_C            # Kollektorwiderstand
:::

**2. Emitterwiderstand:**
:::formel
U_E = U_B - U_C - U_CE             # Emitterspannung (ca. 1/5 von U_B wählen)
R_E = U_E / (I_C + I_B)            # Emitterwiderstand; I_B = I_C / B
I_E = I_C + I_B = U_E / R_E        # Emitterstrom (Probe)
:::

**3. Basisspannungsteiler (Arbeitspunkt einstellen):**
:::formel
U_R2 = U_E + U_BE               # Spannung über R2; U_BE = 0.7 V
I_q  = I_B * (2..10)            # Querstrom: 2–10× Basisstrom (Faustregel)
R_2  = U_R2 / I_q               # Unterer Spannungsteiler-Widerstand
U_R1 = U_B - U_R2               # Spannung über R1
R_1  = U_R1 / (I_B + I_q)       # Oberer Spannungsteiler-Widerstand
I_B  = I_C / B                  # Basisstrom
:::

## Durchgerechnetes Beispiel

Gegeben: U_B = 12 V, I_C = 2 mA, B = 200, U_CE = 4 V

:::monospace
Schritt 1 — Spannungsaufteilung wählen (U_CE = 4 V, U_E = 2 V, U_C = 6 V):
  R_C = U_C / I_C = 6 V / 2 mA = 3 kΩ → Normwert 2.7 kΩ oder 3.3 kΩ

Schritt 2 — Emitter:
  I_B  = I_C / B = 2 mA / 200 = 10 µA
  R_E  = U_E / (I_C + I_B) = 2 V / 2.01 mA ≈ 995 Ω → 1 kΩ

Schritt 3 — Spannungsteiler (I_q = 5 × I_B = 50 µA):
  U_R2 = U_E + U_BE = 2 V + 0.7 V = 2.7 V
  R_2  = U_R2 / I_q = 2.7 V / 50 µA = 54 kΩ → 56 kΩ
  U_R1 = U_B - U_R2 = 12 V - 2.7 V = 9.3 V
  R_1  = U_R1 / (I_B + I_q) = 9.3 V / 60 µA = 155 kΩ → 150 kΩ

Probe: U_R2 = 12 V × 56k/(56k+150k) = 3.27 V → leichte Abweichung durch Normwerte — OK
:::

## Thermische Stabilität

Der Emitterwiderstand R_E ist entscheidend für die Stabilität:
- Steigt I_C durch Temperaturerhöhung, steigt U_E = R_E · I_C
- Damit steigt U_BE (da U_R2 durch den Spannungsteiler fest gehalten wird) → I_B sinkt → I_C sinkt wieder

**R_E ist eine Gegenkopplung** für den Gleichstrombetrieb — er stabilisiert den Arbeitspunkt. Für Wechselspannungsbetrieb wird R_E mit einem Kondensator C_E überbrückt, damit die Wechselverstärkung nicht leidet.

:::tip
Faustregeln für die Spannungsaufteilung: U_CE ≈ U_B/3, U_E ≈ U_B/5 bis U_B/6. Das gibt gute Aussteuerung und ausreichend Gegenkopplung.
:::
