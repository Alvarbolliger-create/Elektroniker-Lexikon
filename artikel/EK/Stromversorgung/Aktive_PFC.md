---
title: Aktive Leistungsfaktorkorrektur (PFC)
kategorie: EK
tags: [PFC, Leistungsfaktor, Oberschwingungen, Boost-PFC, IEC 61000-3-2, cos phi]
symbol: —
einheit: —
---

Aktive PFC formt den Eingangsstrom eines Netzgerätes so, dass er sinusförmig und phasengleich mit der Netzspannung ist. Das eliminiert Oberschwingungen und bringt den Leistungsfaktor nahe 1.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oberschwingungen]]
- [[Blindleistungskompensation]]
- [[Buck (Step-down)]]
:::
:::vbox
**Verwandte Artikel**
- [[Flyback & Forward Converter]]
- [[Boost (Step-up)]]
:::
:::

---

## Warum ist PFC nötig?

Einfache Netzgeräte (Gleichrichter + Ladekondensator) ziehen Strom nur in kurzen Spitzen um den Spannungsscheitel. Der Strom ist nicht sinusförmig sondern stark nichtlinear.

Das erzeugt:
- Hohe Oberschwingungen (3., 5., 7. Harmonische stark ausgeprägt)
- Schlechter Leistungsfaktor (cos φ ≈ 0.5–0.7 typisch)
- Netzrückwirkungen, die andere Verbraucher stören

**IEC 61000-3-2** schreibt Grenzwerte für Oberschwingungen vor:
- Klasse A: Haushaltsgeräte, Schaltnetzteile > 75 W
- Für Geräte über 75 W ist aktive PFC praktisch Pflicht

## Topologie: Boost-PFC

Die einfachste und häufigste aktive PFC-Schaltung ist ein Boost-Converter vor dem eigentlichen Schaltnetzteil.

**Aufbau**:
1. Brückengleichrichter (AC → pulsierender DC)
2. Boost-Converter mit geregeltem Tastverhältnis
3. Zwischenkreiskondensator (400 V DC)
4. Eigentlicher Schaltregler (z.B. Flyback, LLC)

**Regelung**:
- Innerer Regelkreis: Strom durch Boost-Drossel folgt dem (gleichgerichteten) Sinus der Netzspannung
- Äusserer Regelkreis: Zwischenkreisspannung wird auf 400 V gehalten

Das Ergebnis: Der Eingangsstrom ist nahezu sinusförmig, phasengleich mit der Netzspannung, THD < 5 %.

:::monospace
Leistungsfaktor cos φ ≈ 0.99    # mit aktiver PFC
THD < 5 %                       # statt 80-100 % ohne PFC
:::
## Betriebsmodi der Boost-PFC

**CCM (Continuous Conduction Mode)**: Drossel-Strom fliesst immer. Geringes EMV-Problem, niedriger THD. Für Leistungen > 300 W bevorzugt.

**BCM/CRM (Boundary/Critical Conduction Mode)**: Neues Einschalten genau wenn Strom auf null sinkt. Einfacheres ZVS, aber variable Schaltfrequenz. Für 75–300 W.

**DCM (Discontinuous Conduction Mode)**: Einfachster Regler, aber höherer THD. Nur für < 75 W oder wenn es die Norm noch erlaubt.

## Typische PFC-Controller-ICs

| IC | Bemerkung |
|---|---|
| L6561 / L6562 | ST, CCM/CRM PFC |
| UC3854 / UCC3854 | TI, klassischer CCM |
| NCP1654 | ON Semi, BCM |
| ICL7527x | Infineon, integrierter LLC+PFC |

## Aufbau Zwei-Stufen-Netzteil

:::monospace
AC-Netz → Gleichrichter → Boost-PFC (400 V DC) → LLC-Resonanzwandler → UOUT
:::
Diese Struktur findet man in PC-Netzteilen, Ladeinfrastruktur und Industrienetzteilen über 150 W.

## Einphasige vs. dreiphasige PFC

Bei dreiphasigen Systemen (Industrieanlagen) reicht oft eine Drossel im Zwischenkreis (passive PFC). Die drei Phasen kompensieren sich gegenseitig. Für sehr hohe Anforderungen: dreiphasiger aktiver Gleichrichter (PFC auf allen drei Phasen).
