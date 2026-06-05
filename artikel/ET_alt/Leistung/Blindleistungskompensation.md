---
title: Blindleistungskompensation
kategorie: ET
tags: [Blindleistung, Kompensation, Leistungsfaktor, cos phi, Kondensator, PFC, Industrie]
symbol: Q_C
einheit: var
---

Induktive Lasten (Motoren, Transformatoren) belasten das Netz mit Blindleistung. Kondensatoren erzeugen kapazitive Blindleistung und gleichen sie aus. Das entlastet das Netz und senkt die Stromrechnung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Blindleistung]]
- [[Leistungsfaktor]]
- [[Scheinleistung]]
:::
:::vbox
**Verwandte Artikel**
- [[Oberschwingungen]]
- [[Drehstrom Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[Aktive PFC]]
- [[Frequenzumrichter]]
:::
:::

---

## Warum Kompensation?

Induktive Lasten (Asynchronmotoren, Schweissgeräte, Leuchtstofflampen) nehmen Blindleistung aus dem Netz. Diese Blindleistung ist nicht "verbraucht" — sie pendelt hin und her zwischen Quelle und Verbraucher.

Trotzdem belastet sie das Netz:
- Höhere Ströme in Kabeln, Transformatoren, Schaltern
- Höhere Verluste (P = I² × R)
- Spannungsabfall
- Netzgesellschaften verrechnen Blindleistung in der Industrie (Blindleistungstarif)

Ein schlechter Leistungsfaktor von cos φ = 0.7 bedeutet: Der Strom ist 43 % höher als nötig für die gleiche Wirkleistung.

## Wie Kondensatoren kompensieren

Ein Kondensator entnimmt dem Netz kapazitive Blindleistung (voreilender Strom). Die induktive Blindleistung der Last und die kapazitive Blindleistung des Kondensators heben sich (teilweise) auf.

Das Netz "sieht" danach eine Gesamtlast mit kleinerem Blindleistungsanteil und damit besserem Leistungsfaktor.

## Berechnung der Kompensationskapazität

Gegeben: Wirkleistung P, bestehender Leistungsfaktor cos φ1, Zielleistungsfaktor cos φ2.

:::formel
Q_L = P × tan(φ1)           # bestehende induktive Blindleistung
Q_C = P × tan(φ2)           # verbleibende Blindleistung nach Kompensation
ΔQ = Q_L - Q_C              # benötigte kapazitive Kompensationsleistung
C = ΔQ / (2π × f × U²)     # Kompensationskondensator
:::
**Beispiel**: Motor 10 kW, cos φ1 = 0.7, Ziel cos φ2 = 0.95, 400 V Drehstromnetz, 50 Hz:
:::formel
Q_L = 10 kW × tan(45.6°) = 10.2 kvar
Q_C_ziel = 10 kW × tan(18.2°) = 3.3 kvar
ΔQ = 10.2 - 3.3 = 6.9 kvar
C = 6900 / (2π × 50 × 400²) = 136 µF    # pro Phase im Dreieck
:::
## Kompensationsarten

**Einzelkompensation**: Kondensator direkt am Verbraucher. Optimal — Blindstrom fliesst nicht durch interne Leitungen.

**Gruppenkompensation**: Kondensatorbank für mehrere Verbraucher zusammen. Günstiger aber weniger präzise.

**Zentralkompensation**: Eine grosse Kondensatorbank für die gesamte Anlage. Am einfachsten zu installieren, kompensiert aber nichts im internen Netz.

**Automatische Kompensationsanlage (Blindleistungsregler)**: Misst cos φ kontinuierlich und schaltet Kondensatorstufen zu oder ab. Angepasst an schwankende Lasten.

## Überkompensation

Werden zu viele Kondensatoren geschaltet, dreht das Vorzeichen: die Last wird kapazitiv. Spannung steigt, Strom eilt nun vor. Das kann Transformatoren und Leitungen ebenfalls belasten.

:::warning
Vor der Blindleistungskompensation immer den Oberschwingungsanteil prüfen. Kondensatoren und Netzdrosseln können bei hohem Oberschwingungsgehalt (Frequenzumrichter, Gleichrichter) gefährliche Resonanzen bilden.
:::
