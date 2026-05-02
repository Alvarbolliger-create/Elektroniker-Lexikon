---
title: Vierleitermessung (Kelvin)
kategorie: MT
tags: [vierleitermessung, kelvin, widerstand, mΩ, messfehler, präzision, shunt, kontaktwiderstand, force-sense]
symbol: —
einheit: Ω
---

Die Vierleitermessung eliminiert den Einfluss der Messleitungswiderstände. Unverzichtbar für Widerstände unter ca. 10 Ω.

:::hbox
:::vbox
**Voraussetzungen**
- [[Innenwiderstand & Messfehler]]
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Schutzleiterwiderstand]]
:::
:::vbox
**Führt weiter zu**
- [[Schutzleiterwiderstand]]
:::
:::

---

## Das Problem bei zwei Leitungen

Bei der normalen Zweileitermessung fliesst der Messstrom durch dieselben Leitungen an denen auch die Spannung gemessen wird. Der Widerstand der Messleitungen (typisch 0.1 bis 1 Ω) addiert sich zum Messwert.

Bei einem 100 Ω Widerstand ist das vernachlässigbar. Bei 0.1 Ω Shunt ist der Leitungswiderstand grösser als der Messwert selbst.

## Die Lösung: vier Leitungen

Zwei Leitungen führen den Strom (Force+, Force-). Zwei separate Leitungen messen die Spannung direkt am Bauteil (Sense+, Sense-).

Da in die Spannungsleitungen kaum Strom fliesst (hochohmiger Voltmetereingang), erzeugen sie keinen Spannungsabfall. Die Messung ist fehlerfrei.

## Anwendungen

- Shunt-Widerstände (mΩ-Bereich)
- Kontaktwiderstände von Schaltern und Steckverbindern
- Schutzleiterwiderstand nach Norm (max. 0.3 Ω)
- Leiterbahnwiderstände auf Leiterplatten
- Batterie-Innenwiderstand

## Präzisions-Multimeter mit Vierleitermessung

Hochwertige Multimeter (z.B. Fluke 87V, Keithley 2100) bieten Vierleitermessung als eigene Funktion. Vier separate Buchsen, entsprechend beschriftet.

:::tip
Für Schutzleiterwiderstandsmessungen nach Norm (IEC 60364) ist die Vierleitermessung vorgeschrieben. Normale Zweileitermessung erfüllt die Anforderungen nicht.
:::
