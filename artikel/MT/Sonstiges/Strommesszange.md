---
title: Strommesszange
kategorie: MT
tags: [strommesszange, stromzange, hall, CT, berührungslos, AC, DC, differenzmessung, hallsensor, feldstärke]
symbol: —
einheit: A
---

Die Strommesszange misst Strom ohne den Leiter aufzutrennen. Sie umschliesst den Leiter und misst das Magnetfeld.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Strom-, Spannungs-, Widerstandsmessung]]
:::
:::vbox
**Verwandte Artikel**
- [[True RMS]]
- [[Vierleitermessung (Kelvin)]]
:::
:::

---

## Messprinzip

Ein Leiter mit Strom erzeugt ein Magnetfeld. Die Zange umschliesst den Leiter und misst dieses Feld.

**CT (Current Transformer)**: Funktioniert nur mit Wechselstrom. Der Leiter ist die Primärwicklung, im Kern sitzt die Sekundärwicklung. Einfach, günstig, genau. Typisch in Zangenammetern für Netzstrom.

**Hall-Sensor**: Misst Gleich- und Wechselstrom. Im Spalt des Kerns sitzt ein Hall-Element. Teurer, aber DC-fähig. Nötig bei Batterieüberwachung, Frequenzumrichtern.

## Handhabung

Nur einen Leiter in die Zange. Wenn Hin- und Rückleiter zusammen umschlossen werden, heben sich die Felder auf. Ergebnis: 0 A, egal welcher Strom fliesst.

Das ist manchmal nützlich: Differenzstrommessung durch Einführen aller Leiter eines Kabels prüft den Fehlerstrom.

## Genauigkeit

Zangenammmeter sind typisch auf 1-2 % genau. Bei sehr kleinen Strömen (unter 1 A) lässt die Genauigkeit nach. Trick: Leiter mehrfach durch die Zange wickeln (N Windungen), Messwert durch N teilen. Das erhöht die Auflösung.

## Aufsatz-Zangen

Günstiger Einstieg: Stromwandler-Aufsatz für normale Multimeter. Wandelt den Strom in eine Spannung um (z.B. 1 mV/A), die das Multimeter dann misst.

:::tip
Beim Messen von Strömen an Frequenzumrichtern immer True-RMS-Zangen verwenden. Die stark verzerrten Ströme ergeben mit einfachen Zangen falsche Werte.
:::
