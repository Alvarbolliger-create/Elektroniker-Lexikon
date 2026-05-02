---
title: Isolationsmessung
kategorie: SI
tags: [isolationsmessung, megger, isolationswiderstand, IR, prüfspannung, polarisationsindex, DIN VDE 0100, feuchtigkeit]
symbol: —
einheit: MΩ
---

Die Isolationsmessung prüft ob die Isolation zwischen spannungsführenden Teilen und Gehäuse oder Erde intakt ist. Sie erkennt Feuchtigkeitsschäden, Alterung und mechanische Beschädigungen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Schutzklassen I, II, III]]
- [[Fehlerschutz (FI/RCD)]]
:::
:::vbox
**Verwandte Artikel**
- [[Schutzleiterwiderstand]]
- [[Die 5 Sicherheitsregeln]]
:::
:::

---

## Messprinzip

Ein Isolationsmessgerät (Megger) legt eine hohe Gleichspannung zwischen den zu prüfenden Punkten an und misst den fliessenden Strom. Daraus berechnet es den Widerstand.

```
R = U_prüf / I
```

Messspannungen: 250 V, 500 V, 1000 V, 2500 V je nach Nennspannung des Prüflings.

## Typische Prüfspannungen

| Gerätespannung | Prüfspannung |
|---|---|
| bis 50 V | 250 V |
| 51 bis 500 V | 500 V |
| 501 bis 1000 V | 1000 V |

## Grenzwerte

Nach IEC 60364 und DIN VDE 0100:
- Mindest-Isolationswiderstand: **1 MOhm** für Starkstromanlagen bis 500 V

Für neue Installationen sind Werte von 100 MOhm oder mehr normal. Unter 1 MOhm muss die Ursache gefunden und behoben werden.

## Vor der Messung

Das Gerät muss spannungslos und von der Versorgung getrennt sein. Elektronische Bauteile können durch die Prüfspannung beschädigt werden. Schutzkondensatoren (Y-Kondensatoren) vor der Messung abklemmen, sie verfälschen das Ergebnis.

## Polarisationsindex (PI)

Der PI ist das Verhältnis des Isolationswiderstands nach 10 Minuten zu dem nach 1 Minute. Ein Wert über 2 zeigt trockene, gute Isolation. Ein Wert unter 1 deutet auf Feuchtigkeit hin.

:::warning
Isolationsmessgeräte erzeugen gefährliche Spannungen. Vor der Messung sicherstellen dass keine Personen mit dem Prüfling in Berührung kommen können.
:::
