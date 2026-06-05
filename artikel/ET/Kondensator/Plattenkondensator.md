---
title: Plattenkondensator & Influenz
kategorie: ET
tags: [plattenkondensator, kapazität, permittivität, influenz, faradayscher käfig, elektrisches feld, dielektrikum]
groessen: C|Kapazität|F; epsilon_0|Feldkonstante|F/m; epsilon_r|Permittivitätszahl|—; A|Plattenfläche|m²; d|Plattenabstand|m; E|Feldstärke|V/m
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Elektrisches Feld]]
- [[Kondensator (Übersicht)]]
:::
:::vbox
**Führt weiter zu**
- [[Kapazität & Einheiten]]
:::
:::

---

Der Plattenkondensator ist das einfachste und wichtigste Modell für Kondensatoren. Zwei parallele Platten, durch ein Dielektrikum getrennt — dazwischen ein homogenes elektrisches Feld.

## Kapazität des Plattenkondensators

:::formel
C = epsilon_0 * epsilon_r * A / d
:::

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Elektrische Feldkonstante | epsilon_0 | 8,854 · 10⁻¹² F/m | Vakuum |
| Relative Permittivität | epsilon_r | — | Materialeigenschaft des Dielektrikums |
| Plattenfläche | A | m² | Aktive Fläche |
| Plattenabstand | d | m | Abstand der Platten |

:::schematic Plattenkondensator
/abbildungen/kondensator/plattenkondensator_feld.svg
:::

## Einfluss von Plattenabstand und -fläche

| Massnahme | Wirkung auf C | Erklärung |
|---|---|---|
| A verdoppeln | C verdoppelt sich | Doppelte Fläche → doppelt so viel Ladung |
| d halbieren | C verdoppelt sich | Platten näher → stärkeres Feld bei gleicher Spannung |
| d verdoppeln | C halbiert sich | Platten weiter → schwächeres Feld |

:::monospace
Beispiel: A = 100 cm² = 0.01 m², d = 1 mm = 0.001 m, Luft (epsilon_r = 1)
C = 8.854e-12 * 1 * 0.01 / 0.001 = 88.5 pF
:::

Für grosse Kapazitäten in kleinem Volumen: grosse Fläche (gewickelte oder gestapelte Folien), kleiner Abstand, hohes epsilon_r.

## Dielektrikum & Permittivität

Das Dielektrikum erhöht die Kapazität um den Faktor epsilon_r (relative Permittivität). Ursache: Im elektrischen Feld polarisieren sich die Moleküle des Dielektrikums — das schwächt das Feld im Innern ab, was bei gleicher Ladung eine kleinere Spannung und damit grössere Kapazität bedeutet.

| Material | epsilon_r |
|---|---|
| Vakuum, Luft | 1 |
| Papier | 2–4 |
| Polyester (Folienkondensator) | 3–4 |
| Glas | 4–7 |
| Keramik (X7R) | 500–5000 |
| Keramik (Y5V) | 10 000–25 000 |

## Elektrische Influenz

Wird ein leitender Körper in ein elektrisches Feld gebracht, verschieben sich die freien Elektronen: Auf der feldnahen Seite sammeln sich negative Ladungen, auf der feldfernen positive. Der Körper bleibt insgesamt neutral, aber die Ladungen sind getrennt.

Ohne Erdung ändert das Aussenfeld den Körper nicht — er ist polarisiert, aber neutral. Mit Erdung fliessen Elektronen ab oder zu, und der Körper nimmt eine netto-Ladung an.

## Faradayscher Käfig

Ein geschlossenes leitendes Gehäuse (auch aus Gitter) schirmt das Innere vollständig vom äusseren elektrischen Feld ab. Das Feld im Innern ist exakt null (Superpositionsprinzip + Influenz).

**Anwendungen:**
- Abschirmgehäuse für empfindliche Elektronik (EMV)
- Mikrowellenherd (Metallgehäuse hält Mikrowellen innen)
- Schirm von Koaxialkabeln
- Schutzkäfige bei Hochspannungsanlagen

:::tip
Der Blitzschutz in Fahrzeugen funktioniert nach dem Prinzip des Faradayschen Käfigs: Die Metallkarosserie schirmt das Innere ab — Insassen im Fahrzeug sind bei Blitzeinschlag gut geschützt (der Blitz fliesst aussen ab).
:::
