---
title: CMRR & Differentielle Messung
kategorie: MT
tags: [CMRR, gleichtaktunterdrückung, differentielle messung, single-ended, high-side, shunt, instrumentenverstärker, OPV, common mode]
symbol: CMRR
einheit: dB
---

Die Gleichtaktunterdrückung (CMRR) beschreibt die Fähigkeit eines Verstärkers oder Messgeräts, ein gemeinsames Signal auf beiden Eingängen zu unterdrücken und nur die Differenz zu messen.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV: Aufbau & Kennwerte]]
- [[Oszilloskop: Aufbau & Bedienung]]
:::
:::vbox
**Verwandte Artikel**
- [[Tastkopf 1:1 vs. 10:1]]
- [[DMS (Dehnungsmessstreifen)]]
:::
:::

---

## Single-Ended vs. Differentielle Messung

**Single-Ended**: Ein Signal, gemessen gegen GND. Einfach, aber Störungen auf der GND-Leitung verfälschen das Ergebnis.

:::formel
U_meas = U_signal (plus alle Störungen auf GND)
:::
**Differentiell**: Zwei Signale, die Differenz wird gemessen. Störungen die auf beide Leitungen gleich einwirken (Gleichtakt) werden unterdrückt.

:::formel
U_meas = U+ - U-    # Störungen die auf U+ und U- gleich wirken, heben sich auf
:::
## Gleichtaktspannung (Common Mode Voltage)

:::formel
U_CM = (U+ + U-) / 2    # Mittelwert beider Eingänge
U_diff = U+ - U-         # Nutzsignal
:::
Der Verstärker soll U_diff verstärken und U_CM ignorieren.

## CMRR (Common Mode Rejection Ratio)

:::formel
CMRR = 20 × log10(A_diff / A_CM)    # in dB
:::
- A_diff = Differenzverstärkung (gewollt)
- A_CM = Gleichtaktverstärkung (ungewollt, sollte 0 sein)

| CMRR | Bedeutung |
|---|---|
| 60 dB | Gleichtakt wird 1000-fach unterdrückt |
| 80 dB | 10'000-fach unterdrückt (typisch guter OPV) |
| 100 dB | 100'000-fach (Instrumentenverstärker) |
| 120 dB | 1'000'000-fach (Präzisions-INA) |

## Warum CMRR kritisch ist: High-Side-Shunt

Ein Shunt im High-Side-Zweig (zwischen Plus-Pol der Versorgung und Last) hat typisch eine Spannung von 24 V + 10 mV (Shuntspannung). 

Ein Verstärker mit schlechtem CMRR "sieht" die 24 V Gleichtakt und gibt eine Fehlspannung am Ausgang. Bei CMRR = 60 dB und 24 V Gleichtakt:

:::formel
U_Fehler = U_CM / CMRR = 24 V / 1000 = 24 mV    # Fehler gleich gross wie Nutzsignal!
:::
Ein Instrumentenverstärker mit CMRR = 100 dB löst das:
:::formel
U_Fehler = 24 V / 100'000 = 0.24 mV    # vertretbar
:::
## Differentielle Oszilloskop-Messung

**Single-Ended Tastkopf am Netzmessgerät**: Der Erdungsclip des Tastkopfs ist mit Schutzerde (PE) verbunden. Misst man an einem Netz-bezogenen Punkt, entsteht ein Kurzschluss über die Schutzerde.

**Lösungen**:
1. **Differentieller Tastteiler**: Zwei Tastköpfe, Scope im Differenz-Math-Modus (A–B). Ungenau da beide Kanäle nicht perfekt gleich sind.
2. **Differentieller Tastkopf**: Integrierter Differenzverstärker im Tastkopf. CMRR typisch 80–100 dB. Für Netzspannungsmessungen geeignet.
3. **Isolierter Tastkopf / Trenntrafo**: Galvanische Trennung.

:::danger
Nie mit dem Standard-Erdungsclip eines Tastkopfs an einem netzpotenzial-bezogenen Punkt messen, wenn das Oszilloskop geerdet ist. Der Clip zieht diesen Punkt auf Erdpotenzial — das ist ein Kurzschluss und lebensgefährlich.
:::
