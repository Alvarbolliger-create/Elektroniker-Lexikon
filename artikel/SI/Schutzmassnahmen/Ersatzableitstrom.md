---
title: Ersatzableitstrom
kategorie: SI
tags: [ableitstrom, ersatzableitstrom, schutzleiterstrom, VDE 0701, prüfung, Y-kondensator, FI, IEC 60990, 30mA]
symbol: I_A
einheit: mA
---

Der Ableitstrom fliesst über den Schutzleiter zur Erde, auch wenn kein Fehler vorliegt. Er entsteht durch Y-Kondensatoren, Filterbeschaltungen und parasitäre Kapazitäten.

:::hbox
:::vbox
**Voraussetzungen**
- [[Schutzklassen I, II, III]]
- [[Fehlerschutz (FI/RCD)]]
:::
:::vbox
**Verwandte Artikel**
- [[Isolationsmessung]]
- [[Schutzleiterwiderstand]]
:::
:::

---

## Warum Ableitstrom?

Schaltnetzteile und EMV-Filter enthalten Y-Kondensatoren zwischen Phase und PE sowie Neutral und PE. Diese Kondensatoren leiten bei 50 Hz einen kleinen Strom zur Erde.

Das ist erwünscht für die EMV-Funktion, aber der Strom muss begrenzt sein.

## Grenzwerte

Nach IEC 60990 und IEC 60335:

| Gerätetyp | Max. Ableitstrom |
|---|---|
| Haushaltsgeräte | 0.75 mA (3.5 mA mit FI) |
| Ortsfeste IT-Geräte | 3.5 mA |
| Industrieanlagen | bis 10 mA (bei guter PE-Verbindung) |

## FI-Schalter und Ableitstrom

FI-Schalter lösen bei 30 mA aus. Wenn mehrere Geräte mit je 3 mA Ableitstrom parallel laufen, addieren sich die Ableitströme. Bei 10 Geräten = 30 mA: FI kann unerwünscht auslösen.

In Industrieinstallationen werden deshalb FI-Schutzschalter mit höherem Ansprechstrom (100-300 mA) verwendet. Das setzt aber voraus dass der PE-Anschluss sicher und niederohmig ist.

## Messung: Ersatzableitstrom

Da die direkte Messung bei angeschlossenem Gerät gefährlich wäre, misst man den Ersatzableitstrom nach DIN VDE 0701-0702 mit einem definierten Netzwerk.

Das Messgerät simuliert den menschlichen Körperwiderstand und misst den Strom der bei einem PE-Unterbruch flösse.

:::warning
Bei Geräten mit hohem Ableitstrom (Servos, Frequenzumrichter) muss der Schutzleiter besonders sicher angeschlossen sein. Ein PE-Unterbruch führt zu einer gefährlichen Berührungsspannung am Gehäuse.
:::
