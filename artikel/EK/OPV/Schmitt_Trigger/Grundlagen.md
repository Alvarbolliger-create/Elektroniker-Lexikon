---
title: Schmitt-Trigger Grundlagen
kategorie: EK
kapitel: OPV
tags: [schmitt-trigger, hysterese, mitkopplung, schaltschwelle, schaltsymbol, invertierend, nichtinvertierend, positive rückkopplung, kennlinie, prüfung]
groessen: U_hys|Hysterese|V; U_e_ein|Einschaltschwelle|V; U_e_aus|Ausschaltschwelle|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Komparator]]
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Komparator]]
- [[Fensterkomparator]]
:::
:::vbox
**Führt weiter zu**
- [[Schmitt-Trigger nicht invertierend symmetrisch]]
- [[Schmitt-Trigger invertierend symmetrisch]]
- [[Schmitt-Trigger nicht invertierend unsymmetrisch]]
- [[Schmitt-Trigger invertierend unsymmetrisch]]
:::
:::

---

Ein Schmitt-Trigger ist ein Komparator mit **Hysterese**: Er hat zwei verschiedene Schaltschwellen — eine zum Einschalten, eine zum Ausschalten. Dazwischen reagiert er auf nichts. Das verhindert Mehrfachschalten bei verrauschten oder langsam steigenden Signalen.

## Mitkopplung: der Mechanismus

Ein gewöhnlicher Komparator hat keine Rückkopplung. Der Schmitt-Trigger führt den Ausgang über einen Widerstand auf den **nichtinvertierenden Eingang (+)** zurück — **positive Rückkopplung (Mitkopplung)**.

Sobald der Ausgang auf HIGH schaltet, hebt die Mitkopplung das Potential an (+) an. Der Eingang muss nun stärker sinken, um wieder LOW zu erzwingen. Diese Verschiebung der Schwelle ist die Hysterese.

## Hysteresekennlinie

:::schematic Schmitt-Trigger Hysteresekennlinie: U_a (vertikal) über U_e (horizontal). Ausgang HIGH: oberes Band. Ausgang LOW: unteres Band. Pfeil rechts: U_e steigt, Umschalten bei U_e_ein (obere Schwelle) von LOW auf HIGH. Pfeil links: U_e fällt, Umschalten bei U_e_aus (untere Schwelle) von HIGH auf LOW. Hysterese-Band U_hys zwischen U_e_aus und U_e_ein eingezeichnet
/Diagramm/schmitt_trigger_kennlinie.svg
:::

:::formel
U_hys = U_e_ein - U_e_aus    # Hysterese; U_e_ein > U_e_aus (immer > 0)
:::

Im Hysterese-Band (U_e_aus < U_e < U_e_ein) ändert der Ausgang seinen Zustand **nicht** — er bleibt in dem Zustand, in dem er zuletzt war. Kein Rauschen in diesem Bereich kann den Ausgang kippen.

## Schaltsymbole (Prüfungsrelevant)

:::hbox
:::vbox
**Nicht invertierend**
:::schematic Symbol nicht invertierender Schmitt-Trigger: Dreieck (Buffer, Spitze rechts). Innen eine kleine Hysteresekurve (σ-Form, öffnet nach rechts: steigende Kennlinie). Eingang links, Ausgang rechts — kein Kreis. Ausgang folgt dem Eingang (gleichphasig)
/Diagramm/st_symbol_nichtinv.svg
:::
:::
:::vbox
**Invertierend**
:::schematic Symbol invertierender Schmitt-Trigger: Dreieck (Spitze rechts) mit Hysteresekurve inside (gespiegelte Kennlinie oder σ-Form). Kreis (Negationspunkt) am Ausgang rechts. Ausgang ist zum Eingang invertiert (180° Phasenumkehr)
/Diagramm/st_symbol_inv.svg
:::
:::
:::

### Symbolerkennung

| Merkmal | Nicht invertierend | Invertierend |
|---|---|---|
| Kreis am Ausgang | Nein | **Ja** |
| Hysteresekurve im Symbol | öffnet nach rechts | gespiegelt oder Kreis |
| Phasenlage | 0° (gleichphasig) | 180° (invertiert) |
| Signal an OPV-Eingang | (+) | (−) |

**Faustregel**: Der Kreis am Ausgang bedeutet immer Inversion — genau wie beim NOT-Gatter, NAND, NOR.

Das "gedrehte" oder "gespiegelte" Symbol: Manche Hersteller drehen die Hysteresekurve um 180°. Das signalisiert ebenfalls den invertierenden Betrieb. Kommt das Symbol ohne Kreis, aber mit einer nach links öffnenden Kurve vor → invertierend.

## Schaltschwellen: was passiert beim Umschalten

Der OPV schaltet, wenn **U_+ = U_−** — genau an der Schwelle zwischen den zwei stabilen Zuständen. Die Schwelle selbst hängt vom aktuellen Ausgangszustand ab (wegen Mitkopplung):

- Ausgang aktuell LOW → (+) liegt tiefer → Eingang muss stärker steigen → **obere Schwelle U_e_ein**
- Ausgang aktuell HIGH → (+) liegt höher → Eingang muss stärker sinken → **untere Schwelle U_e_aus**

Die Herleitung der konkreten Schwellenwerte erfolgt über **KCL am (+)-Knoten** — separat für jede Variante.

## Varianten

| Variante | Signal | (−)-Eingang | Schwellen |
|---|---|---|---|
| [[Nicht invertierend, symmetrisch]] | → (+) | GND | symmetrisch um 0 |
| [[Invertierend, symmetrisch]] | → (−) | Signal | symmetrisch um 0 |
| [[Nicht invertierend, unsymmetrisch]] | → (+) | U_ref | verschoben um U_ref |
| [[Invertierend, unsymmetrisch]] | → (−) | Signal | verschoben um U_ref |

## Anwendungen

**Entprellung von Tastern**: Prellimpulse (Bouncing) beim Schaltvorgang liegen im Hysterese-Band — der Ausgang schaltet nur einmal.

**Signal-Aufbereitung**: Verrauschtes Sensorsignal (NTC, LDR) → sauberes Rechtecksignal.

**Rechteckgenerator**: Schmitt-Trigger + RC-Netzwerk schwingt selbst. → [[Oszillatoren Grundlagen]]
