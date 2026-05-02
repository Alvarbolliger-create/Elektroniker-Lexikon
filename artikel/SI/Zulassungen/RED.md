---
title: RED (Radio Equipment Directive)
kategorie: SI
tags: [RED, funkanlagen, zulassung, 2014/53/EU, CE, funk, DoC, ESP32, nRF52, 2.4 GHz, harmonisierte normen]
symbol: —
einheit: —
---

Die RED (Radio Equipment Directive, 2014/53/EU) regelt das Inverkehrbringen von Funkanlagen in der EU. Betrifft alles was Funkwellen sendet oder empfängt.

:::hbox
:::vbox
**Voraussetzungen**
- [[CE-Kennzeichnung & Konformitätserklärung]]
:::
:::vbox
**Verwandte Artikel**
- [[CE-Kennzeichnung & Konformitätserklärung]]
- [[EMV Pre-Compliance]]
:::
:::

---

## Geltungsbereich

Die RED gilt für alle Funkanlagen: WLAN-Module, Bluetooth-Geräte, Mobiltelefone, Fernbedienungen, Funksensoren, LoRa-Geräte, DECT-Telefone.

Auch Empfänger ohne Sender können unter die RED fallen wenn sie Funkwellen verarbeiten.

## Wesentliche Anforderungen

1. **Gesundheit und Sicherheit**: Equivalent zur Niederspannungsrichtlinie
2. **EMV**: Equivalent zur EMV-Richtlinie
3. **Effiziente Nutzung des Funkfrequenzspektrums**: Keine unnötige Störung anderer Funksysteme

## Technische Unterlagen

Für die CE-Kennzeichnung nach RED braucht man:
- Konformitätsbewertungsverfahren (Richtlinie Anhang II oder III)
- Technische Unterlagen mit Testergebnissen
- DoC (Konformitätserklärung)
- Notifizierte Stelle nötig wenn harmonisierte Normen nicht vollständig angewendet werden

## WLAN und Bluetooth: vorkonforme Module

Wer ein vorzertifiziertes Funk-Modul (ESP32, nRF52, SARA-R4 etc.) in ein Produkt integriert, muss trotzdem die RED-Konformität für das Gesamtprodukt nachweisen.

Das Modul-Zertifikat deckt nur das Modul ab, nicht das Endprodukt. Änderungen am Antennendesign oder der RF-Umgebung können das ursprüngliche Modul-Zertifikat ungültig machen.

## Frequenzplan

Jedes EU-Land hat denselben Frequenzplan (dank Harmonisierung). Im Anhang der RED sind Frequenzbänder und Leistungsgrenzen definiert. Für 2.4-GHz-WLAN/Bluetooth: max. 100 mW EIRP.
