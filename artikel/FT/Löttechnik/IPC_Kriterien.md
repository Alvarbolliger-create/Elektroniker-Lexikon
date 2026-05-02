---
title: IPC-Kriterien
kategorie: FT
tags: [IPC, IPC-A-610, löten, qualität, norm, akzeptanzkriterien, klasse 1, klasse 2, klasse 3, lötstelle, THT, SMD, CIS, CIT, zertifizierung, high-reliability, luft- und raumfahrt, medizintechnik]
symbol: —
einheit: —
---

IPC-A-610 ist die internationale Norm für akzeptable Elektronikbaugruppen. Sie definiert was eine gute Lötstelle ist, und was nicht, mit Fotos und Messwerten.

:::hbox
:::vbox
**Voraussetzungen**
- [[Weichlöten]]
- [[Bleifreies Lot]]
:::
:::vbox
**Verwandte Artikel**
- [[Fehlerbilder Löten]]
:::
:::vbox
**Führt weiter zu**
- [[DFM (Design for Manufacturing)]]
:::
:::

---

## Akzeptanzklassen

**Klasse 1** — Allgemeine Elektronik: Konsumprodukte, bei denen ein Ausfall keine schwerwiegenden Folgen hat. Günstige Konsumprodukte. Weit gefasste Kriterien.

**Klasse 2** — Standard-Industrie: Dedizierte Serviceprodukte, Industrieelektronik, Bürogeräte. Verlängerter Betrieb erwartet, aber keine Leben auf dem Spiel. Standard für die meisten professionellen Produkte.

**Klasse 3** — High-Reliability: Luft- und Raumfahrt, Medizintechnik, Militär. Ein Ausfall kann Leben gefährden oder ist ausserordentlich kostspielig. Engste Kriterien, keine Kompromisse.

### Klasse 2 vs. Klasse 3 — die wichtigsten Unterschiede

| Merkmal | Klasse 2 | Klasse 3 |
|---|---|---|
| Lotmenge THT (Durchstieg) | ≥ 75 % | ≥ 100 % (voll gefüllt) |
| Seitliche Lotfüllung SMD | ≥ 50 % | ≥ 75 % |
| Kürzeste Bauteilabstandsunterschreitung | Toleriert (Zielzustand) | Nicht akzeptiert |
| Bauteilneigung | bis 15° | bis 5° |
| Flussmittelrückstände | Akzeptiert wenn ionisch unbedenklich | Reinigung bevorzugt |
| Dokumentation & Rückverfolgbarkeit | Empfohlen | Zwingend |
| Prozessqualifikation | Nicht zwingend | Vollständige Qualifikation nötig |

**Konsequenz**: Ein Produkt nach Klasse 3 zu fertigen ist deutlich aufwändiger und teurer — mehr Kontrolle, engere Fertigungstoleranzen, vollständige Rückverfolgbarkeit jeder Baugruppe.

## Was beurteilt wird

Für jede Lötverbindung gibt es Kriterien für:
- Benetzungsgrad des Lots
- Füllstand im Pad und Durchstieg (THT)
- Seitliche Lotfüllung
- Lotmenge (zu wenig, zu viel)
- Position des Bauteils auf dem Pad

## Beispiel THT-Durchstecklötstelle (Klasse 2)

- Lot füllt mindestens 75 % des Durchstiegs
- Lot auf beiden Seiten sichtbar
- Kontaktwinkel: konkav, gut benetzt
- Kein Flussmittelrückstand der die Beurteilung verhindert

## Zertifizierung

IPC bietet Kurse und Zertifizierungen für Bediener (CIS) und Prüfer (CIT). In der Serienproduktion meist Pflicht. Zeigt dass die Qualitätsbeurteilung nach einheitlichem Standard erfolgt.

:::tip
Die IPC-A-610 Norm ist kostenpflichtig, aber viele Hersteller stellen Beispielbilder frei zur Verfügung. Ein Lötlehrkurs nach IPC ist eine gute Investition für jeden der professionell Elektronik fertigt.
:::
