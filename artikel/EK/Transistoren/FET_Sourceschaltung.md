---
title: FET Sourceschaltung
kategorie: EK
kapitel: Transistoren
tags: [sourceschaltung, fet-verstärker, steilheit, phasenumkehr, hoher eingangswiderstand, gate-vorspannung, selbstvorspannung, arbeitspunkt, analogverstärker]
groessen: v_u|Spannungsverstärkung|—; g_m|Steilheit|A/V; R_D|Drainwiderstand|Ω; R_ein|Eingangswiderstand|MΩ; R_aus|Ausgangswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[FET Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[BJT Emitterschaltung]]
- [[MOSFET Anwendungen]]
:::
:::vbox
**Führt weiter zu**
- [[MOSFET Anwendungen]]
:::
:::

---

Die Sourceschaltung ist das FET-Äquivalent zur BJT-Emitterschaltung. Sie hat eine grosse Spannungsverstärkung, hohen Eingangswiderstand und **180° Phasenumkehr**. Typisch für Signalverstärker, wo hohe Eingangsimpedanz gefordert ist.

## Schaltungsprinzip

:::schematic FET Sourceschaltung (N-Kanal Enhancement MOSFET): U_B oben → R_D → Drain → MOSFET → Source → R_S → GND. Gate-Spannungsteiler R_G1 (von U_B) und R_G2 (nach GND). C_ein am Gate-Eingang, C_aus am Drain-Ausgang. C_S parallel R_S. Signal u_ein an Gate, u_aus an Drain. Phasenlage 180°
/Diagramm/fet_sourceschaltung.svg
:::

Der Source-Anschluss liegt (für Wechselstrom) auf GND. Das Signal kommt am Gate, der verstärkte Ausgang liegt am Drain. R_D ist der Drainwiderstand, R_G der Gate-Widerstand zur Arbeitspunkt-Einstellung.

## Spannungsverstärkung

:::formel
v_u = u_aus / u_ein ≈ -(R_D || R_Last) / (1/g_m + R_Sac)
:::

Vereinfacht (ohne Source-Widerstand):

:::formel
v_u ≈ -g_m * (R_D || R_Last)    # Minuszeichen: Phasenumkehr 180°
:::

**v_u ist maximal wenn R_Sac = 0** (Source-Widerstand für Wechsel kurzgeschlossen durch C_S). Dies entspricht dem Überbrücken von R_E durch C_E bei der Emitterschaltung.

## Steilheit g_m

Die Steilheit ist der zentrale Kennwert für den FET-Verstärker:

:::formel
g_m = ΔI_D / ΔU_GS    # in A/V oder Siemens
:::

Im Sättigungsbereich (linearer Verstärkerbetrieb) gilt für Enhancement MOSFET näherungsweise:

:::formel
g_m = 2 * I_D / (U_GS - U_th)    # abhängig vom Arbeitspunkt
:::

Typische Werte: g_m = 1–10 mA/V für Kleinsignal-MOSFETs.

## Eingangs- und Ausgangswiderstand

:::formel
R_ein = R_G              # bestimmt nur durch Gate-Widerstand (Gate selbst: GΩ)
R_aus ≈ R_D || r_DS      # r_DS = differenzieller Drain-Source-Widerstand
:::

Der Eingangswiderstand R_ein = R_G ist frei wählbar (typisch 100 kΩ – 10 MΩ). Das Gate selbst zieht praktisch keinen Strom — der Gate-Widerstand legt nur das Gleichspannungspotential fest.

| Kenngrösse | BJT Emitterschaltung | FET Sourceschaltung |
|---|---|---|
| Eingangswiderstand | mittel (1–10 kΩ) | sehr hoch (100 kΩ – 10 MΩ) |
| Ausgangswiderstand | ≈ R_C | ≈ R_D |
| Verstärkung | –g_m · R_C (gross) | –g_m · R_D (kleiner, da g_m tiefer) |
| Steuerstrom | I_B (nötig) | praktisch 0 |
| Phasenlage | 180° | 180° |

## Arbeitspunkt-Einstellung

**Selbstvorspannung (für JFET / Depletion MOSFET)**:

R_S erzeugt eine negative U_GS durch den Drainstrom selbst (kein externer Spannungsteiler nötig):

:::formel
U_GS = -I_D * R_S    # negative Gate-Source-Spannung bei JFET
:::

**Spannungsteiler (für Enhancement MOSFET)**:

R_G1 und R_G2 teilen die Versorgungsspannung und stellen U_GS > U_th ein:

:::formel
U_GS = U_B * R_G2 / (R_G1 + R_G2)    # Gate-Potential; U_GS > U_th nötig
:::

## Anwendung

**Audiovorverstärker**: Hoher Eingangswiderstand belastet Mikrofon oder Tonabnehmer nicht.

**Rauscharme Eingangsstufe**: JFETs haben deutlich weniger Rauschen als BJTs — wichtig für Messverstärker, Audiotechnik.

**Transimpedanzverstärker (TIA)**: Fotodiodenstrom → Spannung. JFET/MOSFET als Eingangsstufe wegen geringem Strom-Rauschen.
