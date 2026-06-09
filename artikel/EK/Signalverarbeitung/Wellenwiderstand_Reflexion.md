---
title: Wellenwiderstand & Reflexion
kategorie: EK
kapitel: Signalverarbeitung
tags: [wellenwiderstand, reflexion, reflexionskoeffizient, koaxialkabel, abschluss, impedanzanpassung, z0, leitung, laufzeit]
groessen: Z0|Wellenwiderstand|Ω; Γ|Reflexionskoeffizient|—; Z_L|Lastimpedanz|Ω; t_lauf|Laufzeit|s
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
:::
:::vbox
**Verwandte Artikel**
- [[Verstärkung & Dämpfung]]
:::
:::vbox
**Führt weiter zu**
- [[EMV Grundlagen]]
:::
:::

---

Jede Leitung hat einen charakteristischen **Wellenwiderstand Z0**. Trifft ein Signal am Ende auf eine falsche Last, wird ein Teil des Signals reflektiert und läuft zurück zur Quelle.

## Wellenwiderstand Z0

Der Wellenwiderstand ist eine Eigenschaft der Leitung selbst — er hängt von Geometrie und Material ab, aber **nicht** von der Länge:

| Leitungstyp | Z0 |
|---|---|
| Koaxialkabel (RG58, Messtechnik) | 50 Ω |
| Koaxialkabel (TV, RG59) | 75 Ω |
| PCB Microstrip | 50–100 Ω |
| Twisted Pair (Ethernet, differenziell) | 100 Ω |

## Reflexionskoeffizient Γ

Trifft eine laufende Welle auf eine Lastimpedanz Z_L, wird ein Teil reflektiert:

:::formel
Γ = (Z_L - Z0) / (Z_L + Z0)    # Reflexionskoeffizient; Bereich: −1 ≤ Γ ≤ +1
:::

| Abschluss | Z_L | Γ | Wirkung |
|---|---|---|---|
| Perfekter Abschluss | Z0 | 0 | **Keine Reflexion** — Welle wird vollständig absorbiert |
| Offen (nicht abgeschlossen) | ∞ | +1 | Volle Reflexion, Spannung verdoppelt sich am Ende |
| Kurzschluss | 0 Ω | −1 | Volle Reflexion, Spannung invertiert zurück |

:::info
**Merksatz:** Wenn Z_L = Z0, ist Γ = 0 — keine Reflexion. Das ist der Normalfall in der Messtechnik und Hochfrequenztechnik: Koaxialkabel werden immer mit einem 50-Ω- (oder 75-Ω-)Abschluss terminiert.
:::

## Laufzeit des reflektierten Impulses

Der Impuls durchläuft das Kabel zweimal (hin und zurück):

:::formel
t_lauf = 2 * l / v_p    # l = Kabellänge in m, v_p = Ausbreitungsgeschwindigkeit
:::

Bei Koaxialkabel gilt typisch v_p ≈ 2/3 × c ≈ 2×10⁸ m/s:

:::monospace
Beispiel: Koaxialkabel 100 m, v_p = 2×10⁸ m/s
t_lauf = 2 × 100 / (2×10⁸) = 1 µs

→ Der reflektierte Impuls trifft nach 1 µs wieder an der Quelle ein.
:::

## Praktische Fälle (Prüfungsrelevant)

Ein Impulsgenerator sendet in ein 100-m-Koaxialkabel mit Z0 = 50 Ω. Am Ende ist R_L angeschlossen:

| R_L | Γ | Was misst das Oszilloskop an der Quelle? |
|---|---|---|
| 50 Ω | 0 | Kein reflektierter Impuls |
| 0 Ω (Kurzschluss) | −1 | Invertierter Impuls nach Laufzeit |
| ∞ Ω (offen) | +1 | Gleicher Impuls nach Laufzeit — Spannung kurz doppelt so hoch |

:::warning
Reflexionen überlagern das Nutzsignal. Bei schnellen digitalen Signalen (USB, Ethernet, DDR-RAM) können Reflexionen Übertragungsfehler verursachen. Beim Messen mit dem Oszilloskop immer korrekten Eingangsabschluss prüfen (1 MΩ vs. 50 Ω).
:::
