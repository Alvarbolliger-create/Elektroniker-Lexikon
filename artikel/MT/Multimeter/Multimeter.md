---
title: Strom-, Spannungs-, Widerstandsmessung
kategorie: MT
tags: [multimeter, messen, strom, spannung, widerstand, messfehler, durchgangsprüfung, effektivwert, innenwiderstand, AC, DC]
symbol: —
einheit: —
---

Das Multimeter ist das wichtigste Messinstrument in der Elektronik. Es misst Spannung, Strom, Widerstand und je nach Gerät noch mehr.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Innenwiderstand & Messfehler]]
:::
:::vbox
**Führt weiter zu**
- [[True RMS]]
- [[Vierleitermessung (Kelvin)]]
:::
:::

---

## Spannungsmessung

Messgerät parallel zur Messstelle. Das Gerät hat einen hohen Innenwiderstand (typisch 1 bis 10 MΩ), damit es die Schaltung kaum beeinflusst.

Achtung: Bei Wechselspannung zeigt das Multimeter den Effektivwert. Günstige Geräte sind nur für Sinus kalibriert.

## Strommessung

Messgerät in Reihe in den Stromkreis einschleifen. Der Stromkreis muss geöffnet werden. Das Gerät hat einen sehr tiefen Innenwiderstand.

:::warning
Strommessbereich nie direkt an eine Spannungsquelle halten. Das Gerät hat intern fast keinen Widerstand, es entsteht ein Kurzschluss. Sicherung im Gerät brennt durch oder Gerät wird zerstört.
:::

## Widerstandsmessung

Nur bei spannungsfreiem Bauteil messen. Das Gerät legt selbst eine kleine Messspannung an. Parallel liegende Bauteile verfälschen das Ergebnis.

Bauteile im Schaltkreis auslöten oder mindestens einen Anschluss abheben.

## Durchgangsprüfung

Niederohmige Verbindung ergibt einen Signalton. Nützlich für Kabelprüfung, Sicherungen und Lötverbindungen.

## Typische Spezifikationen

| Grösse | Typischer Messbereich | Auflösung |
|---|---|---|
| Gleichspannung | 0 bis 1000 V | 1 mV bis 1 V |
| Wechselspannung | 0 bis 750 V | 0.1 V |
| Gleichstrom | 0 bis 10 A | 0.01 mA |
| Widerstand | 0 bis 40 MΩ | 0.1 Ω |
