---
title: Quarz-Oszillator
kategorie: EK
tags: [quarz, oszillator, piezo, frequenzstabilität, TCXO, OCXO, taktgenerator, pierce, lastkapazität, ppm, serienresonanz, parallelresonanz, atomuhr]
symbol: f_0
einheit: Hz
---

Ein Quarz-Oszillator nutzt die piezoelektrische Eigenschaft eines Quarzkristalls als hochpräzises Frequenzelement. Die Frequenzstabilität übertrifft LC- und RC-Oszillatoren um Grössenordnungen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszillatoren Grundlagen]]
- [[Schwingkreis LC]]
:::
:::vbox
**Verwandte Artikel**
- [[Colpitts-Oszillator]]
:::
:::vbox
**Führt weiter zu**
- [[PLL]]
:::
:::

---

## Piezoelektrischer Effekt

Ein Quarzkristall (SiO₂) verformt sich mechanisch wenn eine Spannung angelegt wird. Umgekehrt erzeugt eine mechanische Verformung eine Spannung (piezoelektrischer Effekt).

Dadurch hat der Quarz eine mechanische Resonanzfrequenz, die elektrisch anregbar ist. Diese Resonanzfrequenz ist extrem stabil gegenüber Temperatur und Alterung.

---

## Elektrisches Ersatzschaltbild

Der Quarz verhält sich elektrisch wie ein schmaler Serienschwingkreis parallel zu einer Kapazität C₀:

:::schematic
/Diagramm/quarz_oszillator_0.svg
:::
- **Ls**: Effektive Masse (grosse Induktivität, mehrere mH)
- **Cs**: Mechanische Federsteifigkeit (sehr kleine Kapazität, fF-Bereich)
- **Rs**: Verluste (meist 5–100 Ω)
- **C₀**: Elektrische Kapazität des Gehäuses (pF-Bereich)

**Zwei Resonanzfrequenzen**:
- **Serienresonanz** (f_s): Ls und Cs in Resonanz, niedrige Impedanz
- **Parallelresonanz** (f_p): Mit C₀, etwas höher als f_s

---

## Schaltungsprinzip

Quarz typisch in Pierce-Konfiguration (häufig in Mikrocontrollern):

:::schematic
/Diagramm/quarz_oszillator_1.svg
:::
Der Quarz wird im Bereich zwischen Serien- und Parallelresonanz betrieben (kapazitiv), wo die Phase stimmt für Schwingbedingung.

---

## Frequenzstabilität

| Typ | Stabilität | Beschreibung |
|---|---|---|
| Einfacher Quarz | ±50 ppm | Keine Temperaturkompensation |
| TCXO (Temp. Comp.) | ±0.5–2 ppm | Kompensationsnetzwerk |
| OCXO (Oven Controlled) | ±0.01–0.1 ppb | Quarz in Ofen auf konstanter Temperatur |
| Atomuhr (Rubidium) | ±0.001 ppb | Nur für Labors und Referenzzwecke |

**ppm = parts per million**: 1 ppm bei 10 MHz = 10 Hz Abweichung.

---

## Lastkapazität

Die Resonanzfrequenz des Quarzes hängt von der externen Lastkapazität C_L ab. Im Datenblatt steht die nominale Lastkapazität (typisch 8–20 pF). Mit dieser muss der Quarz betrieben werden:

:::monospace
C_L = (C1 × C2) / (C1 + C2) + C_stray    # Lastkapazität bestimmt f₀
:::
Falsche Lastkapazität → Frequenzabweichung.

---

## Taktgeneratoren (Fertige Module)

Fertige Quarzoszillatoren (XO-Module) enthalten Quarz, Verstärker und oft Temperaturkompensation in einem Gehäuse. Einfach anzuwenden: Spannung anlegen, Takt kommt am Ausgang.

Typische Frequenzen: 8 MHz, 10 MHz, 12 MHz, 25 MHz, 48 MHz (abhängig von USB/Ethernet-Standard).

:::tip
Für Mikrocontroller ist die XTAL-Beschaltung im Datenblatt exakt vorgegeben. Lastkapazitäten (C1, C2) und maximale Serienwiderstände sind einzuhalten — sonst schwingt der Quarz nicht sicher an oder schwingt auf falscher Frequenz.
:::
