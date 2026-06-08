---
title: Sukzessive Approximation (Wägeverfahren)
kategorie: SH
kapitel: Wandler
tags: [sukzessive approximation, waegeverfahren, sar-adc, binaere suche]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[AD-Wandler (Verfahren im Überblick)]]
:::
:::

---

Im → [[AD-Wandler (Verfahren im Überblick)|Überblick der AD-Wandler-Verfahren]] zeigte sich ein Zielkonflikt: Das Parallelverfahren ist rasend schnell, verschlingt dabei aber unverhältnismässig viel Hardware; die Zählverfahren kommen mit wenig Aufwand aus, sind dafür aber träge. Das **Wägeverfahren** — auch **Sukzessive Approximation** genannt — verspricht den goldenen Mittelweg: schnelle Wandlungszeiten im Mikrosekundenbereich bei überschaubarem Schaltungsaufwand.

## Das Grundprinzip: Bit für Bit "wägen"

:::merke
Ein **Successive Approximation Register (SAR)** vergleicht die — von der → [[Sample & Hold-Schaltung|Sample & Hold-Schaltung]] bereitgestellte — Eingangsspannung U_e fortlaufend mit der Ausgangsspannung U(Z) eines internen → [[DA-Wandler (Digital-Analog-Umsetzer)|DA-Wandlers]]. Zu Beginn wird die Zahl Z auf null gesetzt. Anschliessend wird **Bit für Bit, beginnend beim höchstwertigen (MSB)**, probeweise auf 1 gesetzt: Ist die resultierende DA-Wandlerspannung U(Z) kleiner als U_e, bleibt das Bit gesetzt — das Bit wurde "richtig gewogen". Ist U(Z) grösser als U_e, wird das Bit wieder auf 0 zurückgesetzt. Dieser Wäge-Schritt wird für jedes weitere Bit wiederholt, bis schliesslich auch das niederwertigste Bit (LSB) geprüft ist. Am Ende steht im Register exakt jene Binärzahl, die der analogen Eingangsspannung am nächsten kommt.
:::

## Ein Beispiel: 12 Bit, Schritt für Schritt

Ein 12-Bit-Wandler mit Eingangsbereich 0…10 V soll die Spannung 7,347 V digitalisieren. Bit 11 (Wertigkeit 2048, entspricht 5,000 V) wird zuerst probiert: 5,000 V < 7,347 V → Bit bleibt 1. Bit 10 (1024, +2,5 V) ergibt 7,500 V > 7,347 V → Bit wird wieder 0. So geht es weiter, jedes Mal mit der "Restspannung" als neuem Vergleichsmassstab:

| Schritt | Bit | Wertigkeit | Vergleichswert | Ergebnis | Bitwert |
|---|---|---|---|---|---|
| 1 | 11 | 2048 | 5,000 | kleiner | 1 |
| 2 | 10 | 1024 | 5,000 + 2,5 | grösser | 0 |
| 3 | 9 | 512 | 5,000 + 1,25 | kleiner | 1 |
| … | … | … | … | … | … |
| 12 | 0 | 1 | 7,34375 + 0,00244 | kleiner | 1 |

:::tip
Das Ergebnis lautet `1011 1100 0001` (binär) bzw. 3009 (dezimal). Die Kontrollrechnung U_e = (10 V / 4096) · 3009 ≈ 7,346 V bestätigt: Das Resultat trifft den ursprünglichen Wert von 7,347 V bis auf die durch die Auflösung U_LSB = 10 V / 4096 ≈ 2,44 mV vorgegebene Genauigkeitsgrenze. Genau **zwölf** solcher Wäge-Schritte genügen also, um aus 4096 möglichen Werten den passenden herauszufiltern — eine binäre Suche, die mit jedem Schritt den Suchraum halbiert.
:::

![Wägediagramm der Sukzessiven Approximation: Bit für Bit wird vom MSB zum LSB probeweise auf 1 gesetzt und mit dem DA-Wandlerergebnis verglichen — bleibt das Bit gesetzt oder wird es zurückgenommen, konvergiert die Annäherungsspannung schrittweise auf die Eingangsspannung U_e](abbildungen/sukzessive_approximation_waegediagramm.png)

## Warum Sample & Hold unverzichtbar ist

:::warning
Während der gesamten Wäge-Prozedur — bei einem 12-Bit-Wandler also über zwölf aufeinanderfolgende Vergleichsschritte hinweg — muss die Eingangsspannung **absolut stabil** bleiben. Würde sie sich zwischen zwei Wäge-Schritten ändern, bezöge sich die zweite Hälfte der Entscheidungen auf einen anderen Wert als die erste — das Ergebnis wäre in sich widersprüchlich und unbrauchbar. Genau deshalb ist die → [[Sample & Hold-Schaltung|Sample & Hold-Schaltung]] beim Wägeverfahren keine Option, sondern zwingende Voraussetzung.
:::

## Vorteile und Grenzen

Das Wägeverfahren benötigt nur einen einzigen DA-Wandler als Vergleichsreferenz und eine vergleichsweise schlanke "Wäge-Logik" (das SAR) — ein guter Kompromiss zwischen Geschwindigkeit (Wandlungszeiten im Mikrosekundenbereich) und Hardwareaufwand. Es ist deshalb bis heute eines der am weitesten verbreiteten Verfahren in industriellen Anwendungen — etwa im LTC1410, einem 12-Bit-SAR-Wandler mit 1,25 Millionen Wandlungen pro Sekunde (entsprechend einer Wandlungszeit von nur 0,8 µs) bei lediglich 160 mW Leistungsaufnahme.

Während die Sukzessive Approximation also Schritt für Schritt "wägt", verfolgt ein anderes modernes Wandlerprinzip einen gänzlich anderen Ansatz: Es verzichtet fast vollständig auf einen präzisen Analogteil und verlagert die eigentliche Arbeit in die digitale Signalverarbeitung — der → [[Sigma-Delta-Wandler|Sigma-Delta-Wandler]].
