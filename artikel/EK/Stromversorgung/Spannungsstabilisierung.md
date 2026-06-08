---
title: Spannungsstabilisierung
kategorie: EK
kapitel: Stromversorgung
tags: [spannungsstabilisierung, linearregler, zenerdiode, R_v, 7805, LM317, dropout, wirkungsgrad, festspannungsregler, einstellbar, IC-Regler]
groessen: U_0|Eingangsspannung|V; U_Z|Zenerspannung|V; U_a|Ausgangsspannung|V; R_v|Vorwiderstand|Ω; I_Z|Zenerstrom|A; I_L|Laststrom|A
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Gleichrichter]]
- [[Zener-Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[DC-DC-Wandler]]
:::
:::vbox
**Führt weiter zu**
- [[DC-DC-Wandler]]
- [[Schaltregler Topologien]]
:::
:::

---

Nach dem Gleichrichter und Siebkondensator ist die Gleichspannung noch lastabhängig und enthält Restwelligkeit. Spannungsstabilisierung sorgt für eine konstante, lastunabhängige Ausgangsspannung.

## Transistor-Zener-Regler (einfach, diskret)

Zenerdiode setzt Basisspannung. Transistor übernimmt den Laststrom und hält U_out konstant:

:::formel
U_out = U_Z - U_BE    # Ausgangsspannung (U_BE ≈ 0.6 V NPN)
:::

:::monospace
Beispiel: U_out = 15V → U_Z = 15V + 0.6V = 15.6V
:::

## OPV + Transistor Spannungsregler

Für höhere Lastströme oder einstellbare Ausgangsspannung: OPV als Fehlerverstärker, NPN-Transistor als Längsregler. Eine Referenzdiode D_ref setzt U_ref am (+)-Eingang. Ein Spannungsteiler am Ausgang (R_oben, R_unten) liegt am (−)-Eingang — OPV regelt so, dass U_minus = U_ref:

:::formel
U_out = U_ref * (1 + R_oben / R_unten)    # Ausgangsspannung
:::

:::monospace
Beispiel: U_ref=1V (Zener D1), R_oben=15kΩ, R_unten=R6+R2 (R6=1kΩ, R2=Poti 0–9kΩ)
  R_unten min = 1kΩ:  U_out_max = 1 × (1 + 15k/1k)  = 16V
  R_unten max = 10kΩ: U_out_min = 1 × (1 + 15k/10k) = 2.5V
  R_unten 50% = 5.5kΩ: U_out = 1 × (1 + 15k/5.5k)  = 3.73V
:::

## Strombegrenzung

Schutz vor Überstrom: Sense-Widerstand R_sense misst den Laststrom. Wenn U_R_sense > U_BE(Q2) ≈ 0.6V, leitet Q2 und reduziert I_B von Q1 (Längsregler) → Laststrom wird begrenzt.

:::formel
I_max = U_BE(Q2) / R_sense ≈ 0.6 V / R_sense    # maximaler Laststrom
R_sense = 0.6 V / I_max                           # Dimensionierung Sense-Widerstand
:::

Q1 (Längsregler) und Q2 + R_sense (Strombegrenzer) sind in Serie in den Ausgangspfad geschaltet.

## Zener-Spannungsstabilisierung

:::schematic Zener-Spannungsstabilisierung: Eingangsspannung U_0 links. R_v (Vorwiderstand) in Reihe nach rechts. Knotenpunkt A: Zenerdiode D_Z (Kathode oben an A, Anode nach GND). Last R_L parallel zu D_Z (von A nach GND). Ausgangsspannung U_a = U_Z über Last. R_v nimmt Spannungsdifferenz U_0 − U_Z auf. Strom: I_Rv = I_Z + I_L
/Diagramm/zener_stabilisierung.svg
:::

Eine Zenerdiode parallel zur Last hält die Ausgangsspannung auf U_Z konstant. R_v begrenzt den Strom.

**Bedingungen (aus dem Spick):**
- U_0 > U_a (Eingangsspannung muss grösser als Ausgangsspannung sein)
- Praxiswert: **U_0 ≈ 2 · U_a** (genug Reserve für Regelung und Verlust)

:::formel
R_v = (U_0 - U_Z) / (I_Z + I_L)    # Vorwiderstand
I_Z = (U_0 - U_Z) / R_v - I_L      # Zenerstrom aus Schaltung
P_Z = U_Z * I_Z_max                 # Verlustleistung Zenerdiode (I_L = 0, Worst Case)
P_v = (U_0 - U_Z)^2 / R_v          # Verlustleistung Vorwiderstand
:::

**Dimensionierung R_v:**
- Worst-Case für Zener: **I_L = 0** (kein Laststrom → gesamter Strom durch Zener)
- R_v so wählen, dass I_Z_max nicht überschritten wird

:::monospace
Beispiel: U_0 = 12 V, U_Z = 5.1 V, I_L_max = 50 mA, I_Z_min = 5 mA
R_v_max = (12 − 5.1) / (5 mA + 50 mA) = 6.9 / 0.055 = 125 Ω → 120 Ω (E12)
Probe bei I_L = 0: I_Z = 6.9 / 120 = 57.5 mA → Zener muss P_Z = 5.1 × 0.0575 = 293 mW aushalten
:::

:::warning
Bei Änderungen von U_0 und I_L verschiebt sich der Arbeitspunkt auf der Zener-Kennlinie. Der Regelbereich ist begrenzt — für präzise Anforderungen → IC-Linearregler.
:::

## Lineare IC-Regler

Integrierte Linearregler (z.B. 78xx, LM317) ersetzen die Zener-Schaltung. Sie enthalten intern eine Referenz und einen Regeltransistor.

| Typ | Beschreibung | U_out | I_max |
|---|---|---|---|
| 7805 | Festspannung positiv | +5 V | 1 A |
| 7812 | Festspannung positiv | +12 V | 1 A |
| 7905 | Festspannung negativ | −5 V | 1 A |
| LM317 | Einstellbar positiv | 1.25–37 V | 1.5 A |
| LM337 | Einstellbar negativ | −1.25–−37 V | 1.5 A |

**Dropout-Spannung (Headroom):** Lineare Regler benötigen eine Mindest-Spannungsdifferenz zwischen Eingang und Ausgang, um stabil zu regeln:

:::formel
U_dropout = U_in - U_out    # Headroom — minimale Differenz für stabile Regelung
:::

Für den LM317 werden ca. 3 V Headroom empfohlen (V_in − V_out), damit auch bei maximalem Strom und hoher Temperatur noch genug Reserve besteht.

**LM317 Einstellformel** (zwischen Vout und Adj herrschen immer 1.25V):

:::formel
U_out = 1.25 * (1 + R2 / R1)    # Ausgangsspannung (R1 typisch 100–240 Ω)
I_R1  = 1.25 / R1                # Strom durch R1 (= Strom durch R2)
U_R2  = U_out - 1.25             # Spannung an R2
R2    = U_R2 / I_R1              # Einstellwiderstand
:::

:::monospace
Beispiel: V_in=24V, U_out=5V, R1=100Ω
  I_R1 = 1.25/100 = 12.5mA  →  U_R2 = 5-1.25 = 3.75V  →  R2 = 3.75/12.5mA = 300Ω
:::

:::info
Schutzdiode D1 (z.B. 1N4007) zwischen Vout und Vin des LM317: Falls beim Abschalten C2 (Ausgang) grösser ist als C1 (Eingang), entlädt C2 langsamer — U_out kann kurzzeitig grösser als U_in sein. D1 leitet dann rückwärts und schützt den LM317 vor Rückwärtsspannung.
:::

**7805 Ausgangsspannung erhöhen (GND-Pin-Trick):**

Der 7805 hält 5V zwischen Output und GND-Pin. Liegt der GND-Pin auf einer erhöhten Spannung U_lift, ergibt sich U_out = 5V + U_lift:
- U_lift per Zener: U_out = 5V + U_Z
- U_lift per Spannungsteiler R1=R2: U_out = 5V + 5V = 10V (gleiche Widerstände)

## Verlustleistung und Wirkungsgrad

Der Linearregler "verbrennt" die Spannungsdifferenz als Wärme:

:::formel
P_verlust = (U_0 - U_out) * I_L    # Verlustleistung Linearregler
eta = U_out / U_0                   # Wirkungsgrad (theoretisch maximal)
:::

:::tip
Nachteil Linearregler: Schlechter Wirkungsgrad bei grossem U_0/U_out-Verhältnis (z.B. 12 V → 5 V: η ≤ 42 %). Vorteil: einfach, rauscharm, keine Störungen. Für hohe Effizienz → [[DC-DC-Wandler]].
:::
