---
title: Knotenpotenzialanalyse
kategorie: ET
tags: [knotenpotenzial, netzwerkanalyse, gleichungssystem, knotenregel, leitwert]
groessen: V|Knotenpotenzial|V; I|Strom|A; R|Widerstand|Ohm
_status: OK
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kirchhoffsche Gesetze]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Superposition (Mehrere Quellen)]]
- [[Erzeuger-Ersatzschaltung (Thévenin)]]
:::
:::

---

Wenn eine Schaltung mehrere Knoten hat die sich nicht schrittweise vereinfachen lassen, hilft die Knotenpotenzialanalyse: Statt Ströme sucht man die Spannungen (Potenziale) an den Knoten. Aus den Potenzialen folgen alle Ströme direkt mit I = U / R.

## Wann ist die Methode sinnvoll?

Bei gemischten Schaltungen die sich **nicht** in einfache Reihen- und Parallelgruppen zerlegen lassen — zum Beispiel Leiternetzwerke oder Brückenschaltungen. Statt viele Maschen mit KVL aufzuschreiben, braucht man nur **eine KCL-Gleichung pro unbekanntem Knoten**.

## Grundidee

Jedem Knoten wird ein Potenzial V zugewiesen. Der Strom durch einen Widerstand zwischen zwei Knoten folgt aus dem Potenzialunterschied:

:::formel
I = (V_von - V_nach) / R    # positiv wenn Strom von V_von nach V_nach fliesst
:::

Die Knotenregel (KCL) sagt: Die Summe aller **abfliessenden** Ströme an einem Knoten ist null.

## Vorgehen

1. **Referenzknoten wählen** — meist GND (Minuspol der Quelle) → V_GND = 0 V
2. **Bekannte Potenziale eintragen** — Pluspol einer Spannungsquelle = U_q
3. **Unbekannte Knoten benennen** — alle anderen Knoten: V_A, V_B ...
4. **KCL aufstellen** — an jedem unbekannten Knoten alle abfliessenden Ströme als (V_von − V_nach) / R addieren und gleich null setzen
5. **Gleichungssystem lösen** — eine Gleichung pro unbekanntem Knoten

## Beispiel: ein unbekannter Knoten

Schaltung: U_q = 12 V. R1 = 200 Ω von Plus nach Knoten A. R2 = 300 Ω von A nach GND. R3 = 600 Ω von A nach GND.

Bekannte Potenziale: V_+ = 12 V, V_GND = 0 V. Unbekannt: V_A.

KCL an Knoten A — alle drei Ströme fliessen von A weg:

:::formel
(V_A - 12) / 200 + V_A / 300 + V_A / 600 = 0
:::

Mit 600 (kleinstes gemeinsames Vielfaches) multiplizieren:

:::monospace
3*(V_A - 12) + 2*V_A + V_A = 0
3*V_A - 36 + 3*V_A = 0
6*V_A = 36
V_A = 6 V
:::

Aus V_A alle Ströme berechnen:

:::monospace
I_R1 = (12 - 6) / 200 = 30 mA  (fliesst von Plus nach A)
I_R2 =       6 / 300  = 20 mA
I_R3 =       6 / 600  = 10 mA
Probe: I_R2 + I_R3 = 30 mA = I_R1 ✓
:::

## Beispiel: zwei unbekannte Knoten

Schaltung: U_q = 12 V, alle Widerstände 100 Ω. R1 von Plus nach Knoten A, R2 von A nach GND, R3 von A nach Knoten B, R4 von B nach GND.

Unbekannte: V_A und V_B.

KCL an Knoten A:

:::formel
(V_A - 12) / 100 + V_A / 100 + (V_A - V_B) / 100 = 0
:::

KCL an Knoten B:

:::formel
(V_B - V_A) / 100 + V_B / 100 = 0
:::

Gleichungen vereinfachen (beide ×100):

:::monospace
Gleichung A:  (V_A - 12) + V_A + (V_A - V_B) = 0  →  3*V_A - V_B = 12
Gleichung B:  (V_B - V_A) + V_B = 0               →  2*V_B = V_A

Einsetzen (V_A = 2*V_B in Gleichung A):
3*(2*V_B) - V_B = 12  →  5*V_B = 12  →  V_B = 2.4 V
V_A = 2 * 2.4 = 4.8 V

Ströme:
I_R1 = (12 - 4.8) / 100  = 72 mA
I_R2 =        4.8 / 100  = 48 mA
I_R3 = (4.8 - 2.4) / 100 = 24 mA
I_R4 =        2.4 / 100  = 24 mA

Probe Knoten A: 72 = 48 + 24 ✓
Probe Knoten B: 24 = 24     ✓
:::

:::tip
Das CAS löst das Gleichungssystem automatisch mit `solve()`. Die eigentliche Arbeit ist das korrekte Aufstellen der KCL-Gleichungen — eine Gleichung pro unbekanntem Knoten.
:::
