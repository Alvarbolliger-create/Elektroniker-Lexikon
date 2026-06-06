---
title: BJT Emitterschaltung
kategorie: EK
kapitel: Transistoren
tags: [emitterschaltung, verstärker, spannungsverstärkung, phasenumkehr, 180-grad, arbeitspunkt, koppelkondensator, frequenzgang, eingangswiderstand, ausgangswiderstand, emitterwiderstand, ac-gegenkopplung]
groessen: v_u|Spannungsverstärkung|—; R_E|Emitterwiderstand|Ω; R_C|Kollektorwiderstand|Ω; R_ein|Eingangswiderstand|Ω; R_aus|Ausgangswiderstand|Ω; f_g|Grenzfrequenz|Hz
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BJT Grundlagen]]
- [[BJT Arbeitspunkt]]
:::
:::vbox
**Verwandte Artikel**
- [[BJT Kollektorschaltung]]
- [[BJT Basisschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[Verstärkung & Dämpfung]]
- [[OPV Grundlagen]]
:::
:::

---

Die Emitterschaltung ist die wichtigste BJT-Verstärkerschaltung. Sie hat grosse Spannungs- und Stromverstärkung und dreht die Phase um **180°** — positive Halbwelle am Eingang ergibt negative Halbwelle am Ausgang.

## Schaltungsprinzip

:::schematic BJT Emitterschaltung (NPN): U_B oben → R_C → Kollektor → Transistor → Emitter → R_E → GND. R1 (U_B nach Basis), R2 (Basis nach GND). C_ein am Eingang, C_aus am Ausgang (Kollektor). C_E parallel R_E. Signal u_ein an Basis, u_aus an Kollektor
/Diagramm/bjt_emitterschaltung.svg
:::

Der Emitter ist mit GND verbunden (über R_E), das Signal kommt an die Basis, der verstärkte Ausgang liegt am Kollektor. R1/R2 stellen den Arbeitspunkt ein, C_ein und C_aus entkoppeln Gleichspannungsanteil vom Signal.

## Gleichstromanalyse (Arbeitspunkt)

Alle Grössen beziehen sich auf den Gleichstromzustand (Wechselsignale = 0):

:::formel
B = I_C / I_B                           # Stromverstärkung

U_C = U_B - U_CE - U_E = R_C * I_C     # Kollektorspannung
R_C = U_C / I_C                        # Kollektorwiderstand

U_E = U_B - U_C - U_CE = R_E * (I_C + I_B)   # Emitterspannung
R_E = U_E / (I_C + I_B)                       # Emitterwiderstand
I_E = I_C + I_B = U_E / R_E            # Emitterstrom

U_R2 = U_E + U_BE                      # Spannung über R2
R_2  = U_R2 / I_q                      # Unterer Teiler
I_q  = I_B * (2..10) = U_R2 / R_2     # Querstrom

U_R1 = U_B - U_R2 = R_1 * (I_B + I_q) # Spannung über R1
R_1  = U_R1 / (I_B + I_q)             # Oberer Teiler
I_B  = I_C / (2..10) = I_C / B        # Basisstrom
:::

## Kleinsignalverstärkung (Wechselanteil)

Im Kleinsignalbetrieb (Wechselgrössen, Gleichspannung ausgeblendet) gilt:

:::formel
v_u = u_aus / u_ein ≈ -(R_C || R_Last) / (r_BE/B + R_Eac)
:::

- **R_Eac** = Wechsel-Emitterwiderstand (= 0 wenn C_E den R_E überbrückt)
- **r_BE** = differenzieller Eingangswiderstand der Basis-Emitter-Strecke ≈ B · U_T / I_C
- Das **Minuszeichen** = Phasenumkehr 180°

**v_u ist maximal wenn R_Eac = 0** (C_E brückt R_E kurz). Das geht auf Kosten der Linearität — ohne R_E gibt es keine Arbeitspunktgegenkopplung für Wechselgrössen.

:::info
Faustregel Kleinsignalverstärkung: v_u ≈ R_C / r_E mit r_E = U_T / I_C ≈ 26 mV / I_C. Bei I_C = 1 mA ist r_E = 26 Ω. Mit R_C = 4.7 kΩ ergibt sich v_u ≈ -180.
:::

## Eingangs- und Ausgangswiderstand

:::formel
R_Eingang = 1 / (1/R_1 + 1/R_2 + 1/(r_BE + R_E))    # Parallelschaltung der drei Widerstände
R_Ausgang = 1 / (1/(r_CE + R_E) + 1/R_C + 1/R_L)    # Parallelschaltung am Ausgang
:::

Der Eingangswiderstand ist **mittelgross** (typisch 1–10 kΩ). Der Ausgangswiderstand wird durch R_C dominiert (mittelgross, typisch 1–10 kΩ).

## Frequenzgang und kapazitive Kopplung

Koppelkondensatoren C_ein und C_aus sperren Gleichstrom, lassen aber Wechselstrom durch. Sie begrenzen jedoch die untere Grenzfrequenz:

:::formel
f_gEingang = 1 / (2 * pi * C_Eingang * R_Eingang)    # untere Grenzfrequenz Eingang
f_gAusgang = 1 / (2 * pi * C_Ausgang * R_Ausgang)    # untere Grenzfrequenz Ausgang
:::

**Frequenzgang**: Im Durchlassbereich konstante Verstärkung (ca. 18 dB im Spick-Beispiel). Unterhalb der Grenzfrequenz fällt die Verstärkung mit –20 dB/Dekade. Oben wird sie durch die Transitfrequenz des Transistors begrenzt (typisch 100 MHz für BC547).

:::monospace
Beispiel: R_Eingang = 2 kΩ, C_ein = 10 µF
f_g = 1 / (2π × 10e-6 × 2e3) = 8 Hz → Grenzfrequenz bei 8 Hz
:::

:::tip
Soll die Emitterschaltung bis 20 Hz (Audiobereich) arbeiten, die Grenzfrequenzen mit mindestens 0.5 × f_min ansetzen — also f_g < 10 Hz. Das erfordert grössere Koppelkondensatoren.
:::

## Vergleich mit Gegenphasigkeit

Die 180° Phasenumkehr ist charakteristisch. Sie entsteht weil ein steigender Basisstrom den Kollektorstrom erhöht — dadurch fällt mehr Spannung über R_C ab und die Kollektorspannung sinkt.
