---
title: Auf- und Entladung (Kondensator)
kategorie: ET
tags: [kondensator, RC, zeitkonstante, tau, laden, entladen, exponentialkurve, transient, konstantstrom, ladung]
groessen: tau|Zeitkonstante|s; R|Widerstand|Ω; C|Kapazität|F; U_C|Kondensatorspannung|V; I|Strom|A; Q|Ladung|C
_status: PORT+ERWEITERN  # ET_alt/Kondensator/Auf_und_Entladung.md — Konstantstrom-Abschnitt neu
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kapazität & Einheiten]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Auf- und Entladung (RL)]]
:::
:::vbox
**Führt weiter zu**
- [[Energie im Kondensator]]
- [[Laden mit Konstantstrom]]
- [[RC-Reihenschaltung]]
:::
:::

---

Ein Kondensator kann auf zwei grundlegend verschiedene Arten geladen werden: über einen Widerstand (exponentieller Verlauf) oder mit einem konstanten Strom (linearer Verlauf). Beide Methoden haben unterschiedliche Eigenschaften und Anwendungen.

## Ladung und Spannung

Die Verbindung zwischen gespeicherter Ladung, Kapazität und Spannung ist die grundlegende Kondensatorformel:

:::formel
Q = C * U_C
:::

Dabei ist Q die elektrische Ladung in Coulomb (C = As). Diese Formel gilt immer — unabhängig davon, wie der Kondensator geladen wurde.

## Laden über Widerstand (RC)

:::schematic
/schaltplaene/C/rc_ladeschaltung.svg
:::

### Zeitkonstante tau = R · C

:::formel
tau = R * C
:::

Die Zeitkonstante bestimmt, wie schnell der Ladevorgang abläuft. Nach einer Zeitkonstante sind 63 % des Endwerts erreicht.

| Vielfaches von tau | Laden: U_C / U_0 | Entladen: U_C / U_0 |
|---|---|---|
| 1 × tau | 63 % | 37 % |
| 2 × tau | 86 % | 14 % |
| 3 × tau | 95 % | 5 % |
| 5 × tau | 99 % | 1 % |

**Faustregel**: Nach 5 · tau gilt der Kondensator als vollständig geladen oder entladen.

### Ladevorgang

Der Kondensator lädt sich über R auf die Quellspannung U_0 auf. Der Strom ist anfangs maximal und nimmt ab, weil die steigende Kondensatorspannung dem Strom entgegenwirkt — der Prozess verlangsamt sich selbst.

:::formel
U_C(t) = U_0 * (1 - e^(-t / tau))
:::

:::formel
I(t) = (U_0 / R) * e^(-t / tau)
:::

### Entladevorgang

Wird die Quelle getrennt, entlädt sich der Kondensator über R. Die gespeicherte Energie treibt den Strom, bis nichts mehr übrig ist.

:::formel
U_C(t) = U_0 * e^(-t / tau)
:::

## Laden mit Konstantstrom

:::schematic
/schaltplaene/C/konstantstrom_ladeschaltung.svg
:::

Fliesst ein konstanter Strom I in den Kondensator (z. B. von einer Stromquelle), dann wächst die Ladung Q linear mit der Zeit: Q = I · t. Da Q = C · U_C gilt, steigt auch die Spannung **linear**:

:::formel
U_C = (I * t) / C
:::

Die Steigung der Spannungskurve ist konstant: ΔU_C / Δt = I / C. Ein doppelt so grosser Strom lädt doppelt so schnell.

:::plot
var: t
range: 0, 5
colors: #0284c7, #16a34a
xlabel: Zeit (normiert)
ylabel: U_C (normiert)
RC-Laden (exponentiell):  1 - exp(-t)
Konstantstrom (linear):   t / 5
:::

Der direkte Vergleich zeigt den wesentlichen Unterschied: RC-Laden verlangsamt sich mit steigender Spannung, Konstantstrom-Laden bleibt gleichmässig.

:::tip
Konstantstrom-Laden wird gezielt eingesetzt, wenn eine lineare Spannungsrampe gebraucht wird — z. B. im Sägezahn-ADC (Zeit messen = Spannung messen) oder in Dreiecksgeneratoren. → [[Laden mit Konstantstrom]]
:::

## Rechenbeispiel

R = 22 kΩ, C = 47 µF, U_0 = 12 V

Zeitkonstante: tau = 22 000 · 47 · 10⁻⁶ = **1.03 s**

Spannung nach t = 2 s (Ladevorgang): U_C = 12 · (1 − e^(−2 / 1.03)) ≈ **10.3 V**

## Wofür braucht man das?

| Methode | Verlauf | Anwendung |
|---|---|---|
| RC (Widerstand) | Exponentiell | Zeitschaltung, Tiefpass-Filter, Entprellung, Netzteil-Glättung |
| Konstantstrom | Linear | Sägezahn-ADC, Dreieckgenerator, Präzisionslader |

:::warning
Grosse Kondensatoren (Elkos in Netzteilen, Frequenzumrichtern) können nach dem Ausschalten noch **Minuten lang** gefährliche Spannungen tragen. Vor Arbeiten im Gerät immer entladen und mit Messgerät prüfen.
:::
