---
title: Spule Typen
kategorie: ET
tags: [spule, drossel, ferrit, luftspule, ringkern, bauform, toroid, DCR, EMV, sättigungsstrom, stromkompensationsdrossel, eisenpulver]
symbol: L
einheit: H
---

Spulen gibt es in vielen Ausführungen. Material und Aufbau des Kerns bestimmen Induktivität, Verluste, Sättigungsgrenze und Frequenzbereich.

:::hbox
:::vbox
**Voraussetzungen**
- [[Induktivität & Einheiten]]
:::
:::vbox
**Verwandte Artikel**
- [[Kondensator Typen]]
:::
:::vbox
**Führt weiter zu**
- [[Bauteilauswahl]]
:::
:::

---

## Luftspule

Kein Kern. Stabile Induktivität, kein Sättigungseffekt, keine Kernverluste. Nachteil: Sehr gross für hohe Induktivitäten.

Typisch für HF-Anwendungen, Filter bei hohen Frequenzen und Präzisionsanwendungen.

## Ferritkern

Ferritmaterial (Eisenoxid-Keramik) konzentriert das Feld. Hohe Induktivität auf kleinem Raum. Verluste steigen bei hohen Frequenzen.

Ferrit sättigt bei relativ kleinen Strömen. Für Schaltnetzteile nur bis zum Sättigungsstrom belastbar.

## Eisenpulverkern

Körner aus Eisenpulver in einem Bindemittel. Höhere Sättigungsgrenze als Ferrit. Gut für DC-Überlagerte Induktivitäten (Buck/Boost-Wandler).

## Ringkern (Toroid)

Das Feld bleibt grösstenteils im Kern. Wenig Streufeld, EMV-freundlich. Aufwendiger zu wickeln, aber magnetisch ideal.

Typisch für Netzfilter, Transformatoren und Stromkompensationsdrosseln.

## Stromkompensationsdrossel

Zwei gegensinnige Wicklungen auf demselben Kern. Der Nutzsignal-Strom (Gegentakt) fliesst in entgegengesetzten Richtungen — die Magnetfelder heben sich auf, die Spule wirkt transparent. Gleichtakt-Störströme dagegen fliessen in dieselbe Richtung und werden durch die volle Induktivität gebremst.

Eingesetzt in Netzfiltern am Eingang von Schaltnetzteilen um leitungsgebundene Störungen zu dämpfen. Mehr dazu unter [[EMV-Grundlagen]].

## SMD-Spulen

Aufgedruckte oder gewickelte Spulen auf einem Keramikträger. Kompakt, für Reflow-Bestückung. Typisch in Schaltnetzteilen auf Leiterplatten.

## Vergleich

| Typ | Kernmaterial | Induktivitätsbereich | Max. Frequenz | Sättigung | DCR |
|---|---|---|---|---|---|
| Luftspule | — | nH bis µH | GHz | keine | sehr niedrig |
| Ferritkern | Ferrit | µH bis H | MHz | niedrig | niedrig |
| Eisenpulver | Fe-Pulver | µH bis mH | kHz bis MHz | mittel | niedrig |
| Ringkern | Ferrit/Fe | µH bis H | kHz bis MHz | mittel | niedrig |
| SMD-Induktivität | Ferrit | 1 nH bis 100 µH | MHz | niedrig bis mittel | mittel bis hoch |

DCR (DC-Widerstand) ist der ohmsche Widerstand der Wicklung. Er verursacht Verluste und einen Spannungsabfall bei Gleichstrom. Im Datenblatt unter "DCR" oder "R_DC" angegeben.
