---
title: Multiplexer und Demultiplexer
kategorie: Auswahl-Schaltungen
tags: [Routing, Bus, Hardware]
---

# Signalsteuerung

Diese Bausteine fungieren als elektronische "Umschalter" für Datenströme.

## Multiplexer (MUX)
Ein Multiplexer hat mehrere Dateneingänge ($D_0, D_1...$), aber nur einen Ausgang ($Y$). Über **Adressleitungen** (Selekteingänge) wird bestimmt, welcher Eingang zum Ausgang durchgeschaltet wird.
- **Anwendung:** Umschalten zwischen verschiedenen Datenquellen auf einen gemeinsamen Bus.

## Demultiplexer (DEMUX)
Das Gegenstück zum MUX: Ein Eingang wird auf einen von vielen Ausgängen verteilt.
- **Anwendung:** Adressierung von Speicherbausteinen oder Verteilung von Signalen.

## Kaskadierung
Durch das Zusammenschalten mehrerer kleiner MUX-Bausteine (z.B. zwei 4-zu-1 MUX) lassen sich größere Einheiten (z.B. ein 8-zu-1 MUX) aufbauen.

---
**Siehe auch:**
- [[Codewandler und Anzeigen]]
- [[Computerarchitektur]]