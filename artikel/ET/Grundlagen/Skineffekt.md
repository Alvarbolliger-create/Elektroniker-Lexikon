---
title: Skin-Effekt
kategorie: ET
tags: [skineffekt, stromverdrängung, hochfrequenz, wechselstrom, eindringtiefe, HF, litzendraht]
groessen: delta|Eindringtiefe|m; rho|spez. Widerstand|Ohm·m; mu_r|relative Permeabilität|—; f|Frequenz|Hz
_status: PORT  # ET_alt/Grundlagen/Skineffekt.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Leiterwiderstand]]
- [[Sinuswellen & Effektivwert]]
:::
:::vbox
**Verwandte Artikel**
- [[Magnetfelder]]
:::
:::

---

Bei Wechselstrom verdrängt das eigene Magnetfeld des Leiters den Strom nach aussen — zum "Skin" (Haut) des Leiters. Mit steigender Frequenz fliesst der Strom in einer immer dünneren Randschicht, was den effektiven Widerstand erhöht.

## Ursache

Ein Wechselstromleiter erzeugt ein wechselndes Magnetfeld. Dieses induziert nach dem Lenzschen Gesetz im Leiter selbst eine Gegenspannung, die im Zentrum stärker ist als am Rand. Das Ergebnis: Der Strom weicht nach aussen aus.

Bei Gleichstrom gibt es keinen Skin-Effekt — der Strom verteilt sich gleichmässig über den gesamten Querschnitt.

## Eindringtiefe

Die Eindringtiefe delta gibt an, bis zu welcher Tiefe unter der Oberfläche der Strom noch merklich fliesst. Unterhalb von delta ist der Strom auf 1/e ≈ 37 % der Oberflächendichte abgefallen.

:::formel
delta = sqrt(rho / (pi * f * mu_0 * mu_r))
:::

| Frequenz | Eindringtiefe in Kupfer |
|---|---|
| 50 Hz (Netz) | ≈ 9,5 mm |
| 1 kHz | ≈ 2,1 mm |
| 10 kHz | ≈ 0,66 mm |
| 100 kHz | ≈ 0,21 mm |
| 1 MHz | ≈ 66 µm |
| 10 MHz | ≈ 21 µm |

Bei 50 Hz ist die Eindringtiefe grösser als der Radius der meisten Kupferleiter — der Skin-Effekt ist in der Energieverteilung noch vernachlässigbar. Bei HF-Leitern (MHz-Bereich) fliesst der Strom nur noch in einer hauchdünnen Oberflächenschicht.

## Konsequenzen

**Erhöhter Wechselstromwiderstand**: Da der Strom nur den äusseren Ring nutzt, ist die effektive Querschnittsfläche kleiner → R_AC > R_DC.

**Wärmeerzeugung an der Oberfläche**: HF-Heizung (Induktionshärten, Leiterplattenerwärmung) nutzt den Skin-Effekt gezielt.

**Koaxialkabel**: Das Innenleiter-Geflecht und die Abschirmung nutzen die Eindringtiefe aus. Bei GHz-Frequenzen reicht eine hauchdünne Silberschicht als Leiter.

## Massnahmen bei HF

Um den erhöhten Widerstand bei hohen Frequenzen zu reduzieren:

- **Litzendraht**: Viele dünne, gegenseitig isolierte Adern — jede Ader kleiner als delta. Damit wird die Gesamtoberfläche vergrössert.
- **Hohlleiter**: Ab GHz-Bereich sind Hohlleiter effizienter als Koaxialkabel.
- **Oberflächenvergoldung/-versilberung**: Bessere Leitfähigkeit an der Oberfläche.

:::tip
Für EFZ-Prüfungen: Der Skin-Effekt erklärt, warum HF-Leitungen anders dimensioniert werden als NF-Leitungen. Bei 50 Hz-Netzleitern ist er normalerweise nicht relevant.
:::
