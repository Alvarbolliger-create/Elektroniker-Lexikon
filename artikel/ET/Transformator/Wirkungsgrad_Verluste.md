---
title: Transformator: Wirkungsgrad & Verluste
kategorie: ET
tags: [transformator, wirkungsgrad, verluste, kupferverluste, eisenverluste, hystereseverluste, wirbelstromverluste, derating, leerlaufverluste, eta]
symbol: η
einheit: —
---

Kein Transformator ist verlustfrei. Die Verluste entstehen in den Wicklungen und im Kern. Gute Transformatoren erreichen 95 bis 99 % Wirkungsgrad.

:::hbox
:::vbox
**Voraussetzungen**
- [[Übersetzungsverhältnis]]
:::
:::vbox
**Verwandte Artikel**
- [[Thermomanagement]]
:::
:::vbox
**Führt weiter zu**
- [[Derating-Kurven]]
:::
:::

---

## Verlustarten

**Kupferverluste (I²R)**: Ohmsche Verluste in den Wicklungen. Steigen quadratisch mit dem Strom. Verursachen Erwärmung der Wicklung.

**Eisenverluste**: Entstehen im Kern, unabhängig vom Laststrom.
- *Hystereseverluste*: Energie geht bei jedem Ummagnetisierungszyklus verloren. Steigen mit Frequenz und Flussdichte.
- *Wirbelstromverluste*: Induzierte Ströme im Kern erzeugen Wärme. Werden durch geblätterten Kern (Lamellen) oder Ferrit minimiert.

## Wirkungsgrad

```
eta = P_aus / P_ein     # Wirkungsgrad; typisch 95 bis 99 % bei Netztransformatoren
P_verlust = P_ein - P_aus
```

## Leerlaufverluste

Auch ohne Last verbraucht ein Transformator Strom für die Magnetisierung des Kerns. Das sind die Leerlaufverluste. Bei schlecht ausgelegten Transformatoren können sie im Dauerbetrieb relevant sein.

## Derating

Bei erhöhter Umgebungstemperatur sinkt die maximal erlaubte Last. Ein 1 kVA Transformator bei 40 °C Umgebung darf vielleicht nur 85 % belastet werden.

:::tip
Effizienzklassen für Transformatoren in der EU: ErP-Richtlinie definiert Mindest-Wirkungsgrade. Beim Kauf auf die Effizienzklasse achten, besonders bei Dauerbetrieb.
:::

## Kenndaten Netztransformator

| Nennleistung | Typischer Wirkungsgrad | Leerlaufverluste |
|---|---|---|
| 50 VA | 90 bis 94 % | 2 bis 5 W |
| 500 VA | 95 bis 97 % | 5 bis 10 W |
| 5 kVA | 97 bis 99 % | 20 bis 50 W |
