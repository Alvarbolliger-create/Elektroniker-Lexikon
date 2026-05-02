---
title: Fehlerschutz (FI/RCD)
kategorie: SI
tags: [FI, RCD, RCCB, RCBO, fehlerstromschutzschalter, differenzstromschutzschalter, fehlerschutz, differenzstrom, personenschutz, summenstromtransformator, auslösestrom, typ A, typ B, typ AC, IEC 62423, brandschutz]
symbol: —
einheit: —
---

Der FI-Schalter (Fehlerstromschutzschalter, RCD) erkennt wenn Strom nicht auf dem erwarteten Weg zurückfliesst. Das passiert wenn er durch einen Menschen oder einen Isolationsfehler fliesst. Er löst in Millisekunden aus.

:::hbox
:::vbox
**Voraussetzungen**
- [[Gefahren des Stroms]]
- [[Schutzklassen I, II, III]]
:::
:::vbox
**Verwandte Artikel**
- [[Schutzklassen I, II, III]]
:::
:::vbox
**Führt weiter zu**
- [[Leitungsauslegung]]
:::
:::

---

## Funktionsprinzip

Hin- und Rückleiter (L und N) werden gemeinsam durch einen Ringkern geführt — einen **Summenstromtransformator**. Im Normalfall erzeugen ihre entgegengesetzten Ströme gleich starke, sich aufhebende Magnetfelder. Der Kern misst null.

Fliesst Strom über einen Fehlerweg ab (Körperkontakt, Isolationsdefekt), ist der Hinstrom grösser als der Rückstrom. Die Differenz erzeugt einen Netto-Magnetfluss im Kern. Eine Auslösespule erkennt diesen Fluss und trennt den Schalter in unter 40 ms.

30 mA als Auslöseschwelle liegt über den normalen Ableitströmen von Filterkondensatoren moderner Geräte (typisch unter 1 mA), aber unterhalb der Grenze für Herzkammerflimmern. Der FI schützt vor tödlichem Schlag.

## Auslösestrom

| Typ | Auslösestrom | Einsatz |
|---|---|---|
| 10 mA | 10 mA | Erhöhter Personenschutz, Badezimmer |
| 30 mA | 30 mA | Standard Personenschutz |
| 100 mA | 100 mA | Brandschutz |
| 300 mA | 300 mA | Anlagenschutz |

## Typen

**Typ AC**: Reagiert nur auf sinusförmigen Wechselfehlerstrom. Standard in älteren Installationen.

**Typ A**: Zusätzlich für gepulsten Gleichfehlerstrom. Pflicht bei Anlagen mit Frequenzumrichtern, Ladestationen und modernen Elektronikgeräten.

**Typ B**: Auch für glatten Gleichfehlerstrom. Für Wallboxen und bestimmte Industrieanlagen.

## Was schützt er nicht?

Der FI schützt nicht vor Stromschlag zwischen Aussen- und Neutralleiter, wenn der Strom auf dem korrekten Rückweg fliesst. Und er schützt nicht vor Überstrom (das ist Aufgabe der Sicherung).

:::warning
FI-Schalter monatlich testen. Taste drücken, FI soll auslösen. Ein FI der nicht auslöst gibt falsche Sicherheit. Testintervall ist normiert und sollte eingehalten werden.
:::
