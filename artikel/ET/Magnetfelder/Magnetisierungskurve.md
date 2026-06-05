---
title: Magnetisierungskurve & Hysterese
kategorie: ET
tags: [hysterese, B-H-kurve, sättigung, remanenz, koerzitivfeldstärke, weichmagnetisch, hartmagnetisch, weißsche bezirke, neukurve, barkhausen, permeabilität]
groessen: B|Flussdichte|T; H|Feldstärke|A/m; B_r|Remanenz|T; H_c|Koerzitivfeldstärke|A/m; mu_r|Relative Permeabilität|—
_status: PORT+MERGE  # Merge aus: ET_alt/Magnetfelder/Hysteresekurve.md + Saettigung_Hysterese.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
:::
:::vbox
**Führt weiter zu**
- [[Transformator Aufbau]]
- [[Spule Typen]]
:::
:::

---

Ferromagnetische Materialien verhalten sich im Magnetfeld nichtlinear: Der Zusammenhang zwischen Feldstärke H und Flussdichte B hängt von der Geschichte des Materials ab. Wer Transformatoren, Drosseln oder Elektromagnete auslegt, muss dieses Verhalten kennen.

## Weißsche Bezirke

Ferromagnetische Materialien (Eisen, Kobalt, Nickel) bestehen auf mikroskopischer Ebene aus **Weißschen Bezirken** — kleinen Bereichen, in denen alle Elementarmagnete (Elektronenspins) gleichgerichtet sind.

:::schematic Weißsche Bezirke: links unmagnetisiert (zufällige Domänen), rechts magnetisiert (ausgerichtete Domänen)
/abbildungen/magnetfelder/weisssche_bezirke.svg
:::

Im **unmagnetisierten Zustand** sind die Bezirke zufällig orientiert und heben sich gegenseitig auf. Unter einem äusseren Feld richten sie sich aus — das Material wird magnetisch. Sind alle Bezirke ausgerichtet, ist das Material **gesättigt**.

## Materialklassen

| Klasse | Beispiele | mu_r | Verhalten |
|---|---|---|---|
| Ferromagnetisch | Eisen, Kobalt, Nickel | 100 bis 300 000 | Stark nichtlinear, sättigbar |
| Paramagnetisch | Aluminium, Chrom | ca. 1.000001 | Schwach, praktisch linear |
| Diamagnetisch | Kupfer, Wasser, Wismut | ca. 0.99999 | Leicht abstossend |

Für die Praxis relevant sind nur ferromagnetische Materialien.

## Neukurve und Sättigung

Beginnt man mit einem vollständig entmagnetisierten Material und erhöht H von 0, folgt B der **Neukurve**:

1. **Langsamer Anstieg**: Nur wenige Bezirke richten sich aus
2. **Steiler Anstieg**: Viele Bezirke kippen gleichzeitig (maximale Permeabilität)
3. **Abflachung**: Immer weniger Bezirke sind noch unausgerichtet
4. **Sättigung B_sat**: Alle Bezirke ausgerichtet — weiteres H bringt kaum noch mehr B

:::formel
B = mu_0 * mu_r * H
:::

Diese Formel gilt nur im **linearen Bereich** der Neukurve. Im gesättigten Bereich fällt mu_r auf nahezu 1 — die Formel gilt dort nicht mehr.

**Typische Sättigungswerte:**

| Material | B_sat | Bemerkung |
|---|---|---|
| Weicheisen | ca. 2.1 T | Hohe Flussdichte, für Trafokerne |
| Elektroblech (Si-Stahl) | ca. 1.7 T | Standard in Netz-Transformatoren |
| Ferrit (MnZn) | ca. 0.3–0.5 T | Für Schaltnetzteile, hohe Frequenz |
| Ferrit (NiZn) | ca. 0.1–0.3 T | HF-Anwendungen |

:::warning
Wird ein Kern gesättigt, bricht die Induktivität schlagartig ein — der Strom steigt unkontrolliert an. Ein häufiger Fehler bei schlecht ausgelegten Drosseln in Schaltnetzteilen. Der Arbeitspunkt muss im normalen Betrieb unter B_sat bleiben.
:::

### µr aus der Kennlinie bestimmen

Im nichtlinearen Bereich ist µr keine Konstante — er ändert sich mit dem Arbeitspunkt. Der aktuelle Wert muss direkt aus der Kennlinie berechnet werden:

1. Wertepaar (H, B) am gewünschten Arbeitspunkt aus der Kennlinie ablesen
2. µr berechnen:

:::formel
mu_r = B / (mu_0 * H)
:::

:::monospace
Beispiel: Aus Kennlinie abgelesen: H = 265 A/m, B = 0.3 T
mu_r = 0.3 / (1.257e-6 · 265) = 0.3 / 333e-6 ≈ 901
:::

:::warning
µr aus der Kennlinie gilt nur für diesen einen Arbeitspunkt. Bei anderem H-Wert muss µr neu abgelesen werden.
:::

## Hysteresekurve

Wird H nach der Sättigung wieder auf null reduziert, folgt B **nicht** der Neukurve zurück — das Material "erinnert sich" an seine magnetische Geschichte. Dieses Phänomen heisst **Hysterese**.

:::schematic B-H-Kurve mit vollständiger Hystereseschleife: Neukurve, Sättigungspunkt, Remanenz B_r (bei H=0), Koerzitivfeldstärke H_c (bei B=0)
/abbildungen/magnetfelder/hysteresekurve.svg
:::

**Remanenz B_r**: Bei H = 0 verbleibt eine Restmagnetisierung. Je grösser B_r, desto stärker der Dauermagnet.

**Koerzitivfeldstärke H_c**: Um B wieder auf null zu bringen, muss ein Gegenfeld angelegt werden. H_c ist die dafür nötige Feldstärke.

Der vollständige Umlauf — positive Sättigung → null → negative Sättigung → zurück — ergibt die geschlossene **Hystereseschleife**.

## Weich- vs. Hartmagnetisch

| Eigenschaft | Weichmagnetisch | Hartmagnetisch |
|---|---|---|
| Koerzitivfeldstärke H_c | Klein | Gross (> 100 kA/m) |
| Remanenz B_r | Klein bis mittel | Gross |
| Hysteresefläche | Schmal | Breit |
| Ummagnetisieren | Leicht | Schwer |
| Anwendung | Transformator, Drossel, Motor | Dauermagnet, Lautsprecher |
| Typische Materialien | Elektroblech, Ferrit (MnZn) | AlNiCo, Neodym (NdFeB) |

| Hartmagnet | B_r (T) | H_c (kA/m) |
|---|---|---|
| Alnico | 0.7–1.3 | 50–150 |
| Neodym (NdFeB) | 1.0–1.4 | 700–2000 |

## Hystereseverluste

Die Fläche innerhalb der Hystereseschleife entspricht der Energie, die bei **einem** vollständigen Ummagnetisierungszyklus als Wärme verloren geht. Die Verlustleistung steigt proportional mit der Frequenz.

:::formel
P_hyst = c * f * B_max^n
:::

- **c**: Materialabhängige Konstante (enthält Volumen, Materialeigenschaften)
- **n**: Steinmetz-Exponent — ein empirisch bestimmter Wert, der die Nichtlinearität des Materials beschreibt (typisch 1.6 bis 2). Für weiches Elektroblech liegt n nahe 2, für Ferritmaterialien eher bei 1.6.
- **B_max**: Maximale Flussdichte im Betrieb

Bei höherer Frequenz nehmen Hystereseverluste linear zu. Bei 50 Hz reicht Elektroblech; bei Schaltnetzteilen mit 50–500 kHz muss Ferrit verwendet werden (schmale Hystereseschleife = geringe Verluste pro Zyklus).

Neben Hystereseverlusten entstehen im Kern auch **Wirbelstromverluste** (induzierte Kurzschlussströme). Beide zusammen nennt man Kernverluste. Elektroblech wird deshalb aus dünnen, voneinander isolierten Lamellen aufgebaut — das unterbricht die Wirbelstrompfade.

## Barkhausen-Sprünge

Die Ausrichtung der Weißschen Bezirke erfolgt nicht kontinuierlich, sondern in kleinen, abrupten Sprüngen — **Barkhausen-Sprünge**. Stark vergrössert sieht die Neukurve nicht wie eine glatte Kurve aus, sondern wie eine Treppe aus vielen winzigen Stufen.

:::schematic Barkhausen-Sprünge: Zoom auf Neukurve — statt glatter Linie zeigen sich mikroskopische Stufen durch diskontinuierliche Domänenausrichtung
/abbildungen/magnetfelder/barkhausen_spruenge.svg
:::

Mit einer Spule um den Kern und einem empfindlichen Verstärker sind diese Sprünge als Knistern hörbar. Sie zeigen, dass Magnetisierung auf mikroskopischer Ebene ein diskontinuierlicher Prozess ist.

## Praxis-Hinweise

- **Gleichstromanteil** in einer Trafowicklung verschiebt den Arbeitspunkt und kann zu einseitiger Sättigung führen → Kern muss grösser ausgelegt werden
- **Entmagnetisierung**: Ein Kern kann durch ein langsam ausgeschlichenes Wechselfeld entmagnetisiert werden (Degaussing)
- **Frequenzgrenze Elektroblech**: Elektroblech (Si-Stahl) ist nur bis ca. 400 Hz sinnvoll einsetzbar — darüber werden die Wirbelstromverluste zu hoch
