---
title: Zweikanalige Abschaltung
kategorie: SI
tags: [zweikanalig, redundanz, kategorie 3, kategorie 4, SIL, diagnose, CCF, diversitär, 1oo2, ISO 13849]
symbol: —
einheit: —
---

Zweikanalige Abschaltung bedeutet: zwei unabhängige Pfade schalten ab. Fällt einer aus, übernimmt der andere. Das ist die Grundlage für hohe Sicherheitsklassen.

:::hbox
:::vbox
**Voraussetzungen**
- [[SIL und PL]]
- [[Sicherheitsrelais]]
:::
:::vbox
**Verwandte Artikel**
- [[Not-Halt]]
- [[Sicherheitsrelais]]
:::
:::

---

## Grundprinzip

Ein einzelner Kanal kann versagen ohne erkannt zu werden (unerkannter Fehler). Zwei Kanäle, die unabhängig voneinander dasselbe Ergebnis liefern müssen, machen einen Einzelfehler sichtbar.

## Kategorie 3 vs. 4

**Kategorie 3**: Zweikanalig, ein Fehler darf nicht zum Verlust der Sicherheitsfunktion führen. Der Fehler muss spätestens beim nächsten Anlauf erkannt werden.

**Kategorie 4**: Wie Kategorie 3, aber auch ein zweiter Fehler darf die Sicherheitsfunktion nicht aufheben. Hohe Diagnosedeckung (DCavg > 99 %) gefordert.

## Kanaltypen

**Identische Kanäle (1oo2)**: Beide Kanäle sind gleich aufgebaut. Einfach, aber anfällig für gleiche Ausfallursache (Common Cause Failure).

**Diversitäre Kanäle**: Unterschiedliche Technologie (z.B. Hardware + Software, zwei verschiedene µC). Reduziert Common Cause Failures.

## Common Cause Failure (CCF)

Ein Fehler der beide Kanäle gleichzeitig trifft: Überspannung, falsche Verdrahtung, Temperatur. ISO 13849 fordert Massnahmen gegen CCF:

- Physische Trennung der Leitungen
- Unterschiedliche Bauteile (Diversität)
- Schutz gegen Umwelteinflüsse
- Prüfung der unabhängigen Funktion

## Verifikation

Die Unabhängigkeit beider Kanäle muss nachgewiesen werden. Bei der Inbetriebnahme: Kanal 1 manuell unterbrechen, prüfen ob die Maschine stoppt. Dann Kanal 2, gleiche Prüfung.
