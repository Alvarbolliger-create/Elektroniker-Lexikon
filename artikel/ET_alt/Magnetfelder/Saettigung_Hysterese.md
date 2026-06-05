---
title: Sättigung und Hysterese
kategorie: ET
tags: [sättigung, hysterese, remanenz, koerzitivfeldstärke, ferromagnetismus, weißsche bezirke, neukurve]
symbol: B
einheit: T
---

Ferromagnetische Materialien verhalten sich nichtlinear: Ab einer bestimmten Feldstärke sättigt das Material. Das B-H-Kurvenverhalten bestimmt die Auslegung von Transformatoren, Drosseln und Elektromagneten.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Magnetische Flussdichte]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
- [[Induktivität & Einheiten]]
:::
:::vbox
**Führt weiter zu**
- [[Transformator Aufbau]]
- [[Spule Typen]]
:::
:::

---

## Weißsche Bezirke

Ferromagnetische Materialien (Eisen, Kobalt, Nickel) bestehen aus mikroskopischen Bereichen, den **Weißschen Bezirken**, in denen alle Elementarmagnete (Elektronenspins) gleichgerichtet sind. Im unmagnetisierten Zustand sind diese Bezirke ungeordnet und heben sich gegenseitig auf.

Unter dem Einfluss eines äusseren Magnetfeldes richten sich die Bezirke aus — das Material wird zum Magneten. Sind alle Bezirke ausgerichtet, ist das Material **magnetisch gesättigt**.

## Materialklassen

| Klasse | Beispiele | µr | Verhalten |
|---|---|---|---|
| Ferromagnetisch | Eisen, Kobalt, Nickel | 100 bis 300.000 | Stark nichtlinear, sättigbar |
| Paramagnetisch | Aluminium, Chrom, Sauerstoff | ≈ 1.000001 | Schwach, linear |
| Diamagnetisch | Kupfer, Wasser, Wismut | < 1 (≈ 0.999990) | Leicht abstoßend |

Für die Praxis relevant sind nur ferromagnetische Materialien. Para- und Diamagnetismus sind in der Elektrotechnik vernachlässigbar.

## Die B-H-Kurve (Magnetisierungskennlinie)

### Neukurve

Beginnt man mit einem unmagnetisierten Material und erhöht H, folgt B der **Neukurve**: Zuerst langsamer Anstieg, dann starker Anstieg (maximale Permeabilität), dann flacher Verlauf zur Sättigung.

:::formel
B = µ0 * µr * H     # gilt nur im linearen Bereich
:::
Im gesättigten Bereich ist µr nicht mehr konstant — die Formel gilt nicht mehr.

### Sättigung

Ab der **Sättigungsflussdichte** B_sat steigt B trotz steigendem H kaum noch. Die Permeabilität µr sinkt auf nahezu 1.

Typische Sättigungswerte:
| Material | B_sat |
|---|---|
| Elektroblech (Si-Stahl) | ca. 1.7 T |
| Weicheisen | ca. 2.1 T |
| Ferrit (MnZn) | ca. 0.3 T |
| Ferrit (NiZn) | ca. 0.15 T |

:::warning
Wird ein Transformator- oder Drosselkern gesättigt, bricht die Induktivität ein. Der Strom steigt schlagartig an — ein typischer Fehler bei schlecht ausgelegten Spulen.
:::

## Hysterese

Wird H nach der Sättigung wieder auf null verringert, folgt B nicht der Neukurve zurück. Es bleibt eine **Remanenz** B_R übrig.

Um B auf null zu bringen, muss H umgepolt werden — bis zur **Koerzitivfeldstärke** H_C.

Wird das Feld weiter gesteigert, entsteht die negative Sättigung. Der vollständige Umlauf ergibt die geschlossene **Hysteresekurve**.

:::formel
B_R   # Remanenz: Restmagnetismus ohne äusseres Feld
H_C   # Koerzitivfeldstärke: H nötig um B = 0 zu erzwingen
:::
### Hartmagnetisch vs. Weichmagnetisch

| Eigenschaft | Weichmagnetisch | Hartmagnetisch |
|---|---|---|
| H_C | Klein | Gross |
| B_R | Klein–mittel | Gross |
| Hysteresefläche | Klein | Gross |
| Anwendung | Transformator, Drossel | Dauermagnet |
| Beispiel | Elektroblech, Ferrit | AlNiCo, Neodym |

Für Transformatoren und Drosseln wird weichmagnetisches Material verwendet: kleine Hysteresefläche bedeutet geringe Ummagnetisierungsverluste.

## Hystereseverluste

Die Fläche innerhalb der Hysteresekurve ist proportional zur Energie, die bei jedem Ummagnetisierungszyklus als Wärme verloren geht.

:::formel
P_hyst ~ f * B_max^n     # n ≈ 1.6 bis 2 (Steinmetz-Exponent)
:::
Bei höherer Frequenz (Schaltnetzteile) nehmen Hystereseverluste proportional zu — ein Grund warum Ferritmaterialien für HF verwendet werden (kleine Hysteresefläche).

## Barkhausen-Sprünge

Die Ausrichtung der Weißschen Bezirke erfolgt nicht kontinuierlich, sondern in kleinen Sprüngen (**Barkhausen-Sprünge**). Mit einem empfindlichen Verstärker und einer Spule um den Kern hörbar als Knistern.
