---
title: Schaltalgebra
kategorie: Grundlagen
tags: [Mathe, Optimierung]
---

# Boolesche Algebra & Optimierung

Um Schaltungen mit so wenigen Gattern wie möglich zu bauen, nutzt man mathematische Regeln.

## Rechenregeln
- **Kommutativgesetz:** `A + B = B + A`
- **De Morgansche Gesetze:** Sehr wichtig für die Umwandlung von Logik.
  `!(A * B) = !A + !B`
  `!(A + B) = !A * !B`

## KV-Diagramm (Karnaugh-Veitch)
Ein grafisches Werkzeug zur Vereinfachung von Logikfunktionen.
- Man trägt die Wahrheitstabelle in eine Matrix ein.
- Man bildet 2er-, 4er- oder 8er-Blöcke (Einsen- oder Nuller-Schleifen).
- Variablen, die innerhalb eines Blocks ihren Zustand ändern, fallen weg.

## Don't Care Zustände (X)
In manchen Schaltungen treten bestimmte Eingangskombinationen niemals auf. Diese "Don't Cares" können im KV-Diagramm wahlweise als 0 oder 1 behandelt werden, um die Blöcke so groß wie möglich zu machen.

---
**Siehe auch:**
- [[Logikgatter]]
- [[Programmierbare Logik]]