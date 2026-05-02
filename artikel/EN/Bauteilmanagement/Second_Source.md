---
title: Second Source
kategorie: EN
tags: [second source, alternativ, verfügbarkeit, pin-kompatibel, EOL, BOM, BGA, QFN, qualifizierung, footprint, lieferengpass]
symbol: —
einheit: —
---

Eine Second Source ist ein alternatives Bauteil das denselben Footprint und dieselbe Funktion hat wie das Originalbauteil. Sie sichert die Produktion wenn das erste Bauteil nicht verfügbar ist.

:::hbox
:::vbox
**Voraussetzungen**
- [[Datenblatt-Analyse]]
- [[Lifecycle & Obsolescence]]
:::
:::vbox
**Verwandte Artikel**
- [[Lifecycle & Obsolescence]]
- [[DFM (Design for Manufacturing)]]
:::
:::

---

## Warum Second Source?

Lieferengpässe, End-of-Life, Preisspitzen: Wer nur eine Bezugsquelle für ein kritisches Bauteil hat, ist verwundbar. 2021/2022 hat die weltweite Chipkrise gezeigt wie schnell Produktionen stoppen wenn ein einzelnes IC fehlt.

## Anforderungen an eine Second Source

Eine echte Second Source muss:
- **Pin-kompatibel** sein (gleicher Footprint, gleiche Pinbelegung)
- **Elektrisch kompatibel** sein (gleiche Spannungen, Ströme, Protokolle)
- **Funktional äquivalent** sein (gleiche Funktion, gleiche Timing-Parameter)

Unterschiede in Timing, Startverhalten oder internen Zuständen können zu subtilen Fehlern führen.

## Qualifizierung

Bevor eine Second Source freigegeben wird, müssen Musterbauteile vollständig getestet werden. Testablauf:
- Elektrische Grundparameter prüfen
- Vollständiger Systemtest auf dem Zielsystem
- Thermal-Stress und Langzeittests wenn nötig

## Dokumentation

Second Sources werden im Schaltplan als erlaubte Alternativen dokumentiert. Entweder über eine Bauteilliste (BOM) mit mehreren Herstellereinträgen oder über interne Freigabelisten.

## Footprint-Kompatibilität

Bei ICs mit sehr kleinen Gehäusen (BGA, QFN) auf exakt gleiche Padgeometrie achten. Selbst kleine Unterschiede im thermischen Pad können Lötprobleme verursachen.

:::tip
Schon beim ersten Design nach Second Sources suchen. Wenn es keine gibt, dieses Bauteil wenn möglich durch ein mit mehr Alternativen ersetzen.
:::
