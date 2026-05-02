---
title: Schutzleiterwiderstand
kategorie: SI
tags: [schutzleiterwiderstand, PE, schutzleiter, vierleitermessung, VDE, 0.3 Ohm, kelvin, DIN VDE 0701, prüfstrom]
symbol: R_PE
einheit: Ω
---

Der Schutzleiterwiderstand ist der Widerstand zwischen dem PE-Anschluss eines Geräts und allen berührbaren leitfähigen Teilen. Ein hoher Widerstand bedeutet gefährliche Berührungsspannung im Fehlerfall.

:::hbox
:::vbox
**Voraussetzungen**
- [[Schutzklassen I, II, III]]
- [[Vierleitermessung (Kelvin)]]
:::
:::vbox
**Verwandte Artikel**
- [[Isolationsmessung]]
- [[Fehlerschutz (FI/RCD)]]
:::
:::

---

## Warum ist er wichtig?

Bei einem Isolationsfehler (Phase berührt Gehäuse) fliesst der Fehlerstrom über den Schutzleiter ab. Wenn der PE-Widerstand zu hoch ist, entsteht am Gehäuse eine gefährliche Spannung bevor die Sicherung auslöst.

Grenzwert nach IEC 60335 und IEC 60950: **0.1 Ohm** für Haushaltsgeräte, **0.3 Ohm** für ortsfeste Geräte der Informationstechnik.

## Messung

Die Messung erfolgt nach der Vierleitermethode (Kelvin-Messung). Zwei Leitungen führen den Prüfstrom, zwei separate Leitungen messen die Spannung direkt an den Messpunkten.

Prüfstrom: 10 A oder 25 A Wechselstrom nach DIN VDE 0701-0702. Der hohe Strom dient dazu auch Kontaktwiderstände sicher zu erfassen.

Messzeit: mindestens 5 Sekunden, typisch bis 10 Sekunden.

## Prüfpunkte

Der Widerstand wird gemessen zwischen dem PE-Steckerstift und:
- Dem Metallgehäuse
- Allen berührbaren leitfähigen Teilen (Schrauben, Griffe, Schienen)
- Dem Gehäuse von Anschlussklemmen

Jeder Punkt einzeln messen.

## Geräteprüfung nach DIN VDE 0701-0702

Bei der Wiederholungsprüfung elektrischer Geräte (z.B. Betriebsmittel nach BGV A3) ist die Schutzleitermessung Pflicht. Das Protokoll wird aufbewahrt.

:::tip
Für die Messung immer ein geeignetes Geräteprüfgerät verwenden (z.B. Metrel MI3000, Gossen Metrawatt Profitest). Normale Multimeter liefern keine normgerechten Ergebnisse.
:::
