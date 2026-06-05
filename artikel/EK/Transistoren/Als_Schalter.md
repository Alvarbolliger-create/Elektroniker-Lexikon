---
title: Transistor als Schalter
kategorie: EK
tags: [transistor, schalter, BJT, MOSFET, sättigung, sperrung, basiswiderstand, freilaufdiode, bootstrap, high-side, low-side, gate-treiber]
symbol: —
einheit: —
---

Ein Transistor kann wie ein elektronischer Schalter arbeiten. Er schaltet grosse Ströme oder Spannungen mit einem kleinen Steuersignal, schnell und ohne bewegliche Teile.

:::hbox
:::vbox
**Voraussetzungen**
- [[Bipolartransistor (BJT)]]
- [[FET / MOSFET]]
:::
:::vbox
**Verwandte Artikel**
- [[Relais & Schütze]]
:::
:::vbox
**Führt weiter zu**
- [[Buck (Step-down)]]
- [[Frequenzumrichter]]
:::
:::

---

## Zwei Zustände

**Gesperrt**: Kein Strom durch den Lastzweig. Beim BJT kein Basisstrom. Beim MOSFET Gate unter Schwellspannung.

**Gesättigt / leitend**: Maximaler Strom. Beim BJT Basis übersteuert. Beim MOSFET Gate weit über Schwellspannung.

Dazwischen (linearer Betrieb) wird vermieden. Der Transistor würde viel Verlustleistung in Wärme umwandeln.

## BJT als Schalter

:::schematic NPN-Schalter Grundschaltung
/schaltplaene/npn_schalter.svg
:::

:::formel
R_B = (U_in - U_BE) / I_B        # Basiswiderstand berechnen
I_B_min = I_C / h_FE             # Mindestsbasistrom für Sättigung
I_B = 5 * I_B_min                # Übersteuern: sicherer Sättigungsbetrieb
:::
U_BE ≈ 0.7 V, U_CE_sat ≈ 0.2 V im Betrieb.

## MOSFET als Schalter

Gate mit ausreichend Spannung über U_GS_th ansteuern (typisch 4 bis 10 V über Source). Kein Steuerstrom nötig, nur Ladung für die Gate-Kapazität.

Gate-Treiber-IC verwenden wenn der Mikrocontroller nicht genug Strom für schnelles Schalten liefert.

## Praxisbeispiel: µC-Pin schaltet Relais

**Aufgabe**: Mikrocontroller-Ausgangspin (3.3 V, max. 10 mA) soll ein Relais schalten (Spulenspannung 12 V, Spulenstrom 100 mA).

Das geht nicht direkt — der Pin liefert zu wenig Strom und die falsche Spannung. Lösung: NPN-Bipolartransistor als Schalter.

**Benötigte Bauteile**:
1. NPN-Transistor (z.B. BC547 oder 2N2222)
2. Basiswiderstand R_B (Strombegrenzung am Eingang)
3. Freilaufdiode parallel zur Relaisspule (z.B. 1N4148)

**Berechnung Basiswiderstand** (h_FE = 100 angenommen):

:::formel
I_C   = 100 mA          # Relaisstrom
I_B_min = I_C / h_FE = 100 mA / 100 = 1 mA    # Mindeststrom für Sättigung
I_B   = 5 * I_B_min = 5 mA    # Übersteuern für sicheres Schalten
R_B   = (U_pin - U_BE) / I_B = (3.3 V - 0.7 V) / 5 mA = 520 Ω → 470 Ω
:::
**Schaltungsaufbau**:
- Basiswiderstand (470 Ω) zwischen MC-Pin und Basis
- Kollektor über Relaisspule an +12 V
- Emitter an GND
- Freilaufdiode: Kathode an +12 V, Anode an Kollektor (antiparallel zur Spule)

**Warum Freilaufdiode zwingend**: Beim Abschalten der Spule erzeugt die Induktivität eine Gegenspannung (Lenz'sche Regel) von mehreren 100 V. Ohne Diode würde diese den Transistor sofort zerstören. Mit Diode fliesst der Strom in der Spule weiter über die Diode ab.

## MOSFET Gate-Ansteuerung

Das Gate verhält sich als Kapazität (C_iss = Eingangskapazität, typisch 1–10 nF). Zum Schalten muss diese Kapazität umgeladen werden.

**Gate-Ladung Q_g** (aus Datenblatt): Bestimmt, wie viel Ladung der Treiber liefern muss.

:::formel
t_ein = Q_g / I_Treiber     # Einschaltzeit; I_Treiber = Strom des Gate-Treibers
P_gate = Q_g × V_GS × f     # Schaltleistung (steigt mit Frequenz!)
:::
**Gate-Widerstand R_G**: In Reihe zum Gate begrenzter den Schaltstromanstieg. Kleiner R_G → schnelleres Schalten, mehr EMV. Grosser R_G → langsameres Schalten, weniger EMV.

**Low-Side vs. High-Side**:
- **Low-Side MOSFET** (Source auf GND): Einfach — U_GS = Gate-Spannung relativ zu GND.
- **High-Side MOSFET** (Source auf Schaltspannung): Source ist nicht GND. Das Gate muss höher als V_DD getrieben werden. Lösung: Bootstrap-Schaltung oder isolierter Gate-Treiber.

**Bootstrap-Kondensator** (für High-Side): Kleiner Kondensator lädt sich auf wenn Low-Side leitet (Source auf GND). Wenn High-Side schalten soll, wird Kondensatorspannung als floating Supply für den Gate-Treiber genutzt.

## Last: Induktiv oder ohmsch?

Bei ohmschen Lasten (Heizung, LED): kein Problem.

Bei induktiven Lasten (Motor, Relais, Spule): immer Freilaufdiode parallel zur Last. Sonst zerstört die Spannungsspitze beim Abschalten den Transistor.

:::warning
Nie den Strom im Lastzweig ohne Begrenzung wählen. Den maximalen Kollektorstrom (BJT) bzw. Drain-Strom (MOSFET) aus dem Datenblatt prüfen. Auch die Verlustleistung P = U_CE × I_C im Schaltzustand berechnen.
:::
