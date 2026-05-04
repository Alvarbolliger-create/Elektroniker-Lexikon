---
title: FMEA
kategorie: EN
tags: [FMEA, risikoanalyse, fehleranalyse, RPZ, design, qualität, DFMEA, PFMEA, fehlerart, auswirkung, ursache, VDA, AIAG, risikoprioritätszahl, zuverlässigkeit, präventiv]
symbol: —
einheit: —
---

FMEA (Failure Mode and Effects Analysis) ist eine systematische Methode um mögliche Fehler eines Systems im Voraus zu identifizieren und zu bewerten.

:::hbox
:::vbox
**Voraussetzungen**
- [[DFM (Design for Manufacturing)]]
- [[DFT (Design for Testing)]]
:::
:::vbox
**Verwandte Artikel**
- [[DFM (Design for Manufacturing)]]
- [[IPC-Kriterien]]
:::
:::

---

## Wozu FMEA?

Fehler in der Entwicklung zu finden kostet wenig. Fehler nach dem Serienanlauf zu finden kostet sehr viel. Die FMEA verschiebt die Fehleranalyse früh in den Entwicklungsprozess.

## Ablauf

Für jede Komponente oder Funktion werden drei Fragen gestellt:

1. Wie kann sie versagen? (Fehlerart)
2. Was passiert wenn sie versagt? (Auswirkung)
3. Warum könnte sie versagen? (Ursache)

## RPZ (Risikoprioritätszahl)

Jede Fehlerart wird mit drei Faktoren bewertet, je 1-10:

- **B** (Bedeutung): Wie schwerwiegend ist die Auswirkung?
- **A** (Auftretenswahrscheinlichkeit): Wie wahrscheinlich ist die Ursache?
- **E** (Entdeckungswahrscheinlichkeit): Wie wahrscheinlich ist es, den Fehler vor dem Kunden zu entdecken?

:::formel
RPZ = B × A × E
:::
Hohe RPZ = hohe Priorität für Massnahmen. Schwellwert oft bei RPZ > 100 oder > 125.

## Design-FMEA vs. Prozess-FMEA

**Design-FMEA (DFMEA)**: Analysiert das Produkt selbst. Betrachtet Konstruktionsfehler.

**Prozess-FMEA (PFMEA)**: Analysiert den Herstellungsprozess. Betrachtet was bei der Fertigung schiefgehen kann.

## Massnahmen

Für Fehlerarten mit hohem RPZ werden Massnahmen definiert:
- Design ändern (B oder A senken)
- Prüfmethode verbessern (E senken)
- Redundanz einbauen

Nach der Massnahme wird der RPZ neu bewertet.

:::tip
Eine FMEA im Team machen, nicht allein. Verschiedene Perspektiven (Entwicklung, Fertigung, Service) decken mehr Fehlerarten auf.
:::

## Beispiel: Elektrolytkondensator in Spannungsversorgung

Ein ausgefüllter FMEA-Eintrag für einen häufigen Praxisfall:

| Feld | Eintrag |
|---|---|
| Bauteil / Funktion | Elektrolytkondensator 100 µF / 25 V (Ausgangsfilter 5-V-Versorgung) |
| Fehlerart | Kapazitätsverlust durch Alterung |
| Auswirkung | Erhöhter Spannungsripple → Instabilität der 5-V-Versorgung → Systemausfall |
| Ursache | Betriebstemperatur nahe Nenngrenze, kein Derating angewendet |
| **B** (Bedeutung) | **7** — Systemausfall, kein Datenverlust |
| **A** (Auftreten) | **5** — tritt nach mehreren Jahren im Feld auf |
| **E** (Entdeckung) | **4** — Ripple messbar, aber kein Alarmierungssystem vorhanden |
| **RPZ** | **140** → Massnahme erforderlich (Schwellwert 100) |

**Massnahme**: Kondensator durch 105°C-Type mit 80%-Derating ersetzen; Testpunkt für Ripple-Messung in Layout aufnehmen.

| Feld | Nach Massnahme |
|---|---|
| **B** | 7 (unverändert — Auswirkung bleibt gleich) |
| **A** | 2 — Ausfallwahrscheinlichkeit stark reduziert |
| **E** | 2 — Testpunkt ermöglicht schnelle Diagnose |
| **RPZ** | **28** ✓ |
