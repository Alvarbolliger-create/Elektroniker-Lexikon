---
title: Schutzmassnahmen ESD
kategorie: FT
tags: [ESD, schutz, erdungsarmband, EPA, ableitend, arbeitsplatz, ionisator, antistatisch, leitfähig, 1 MOhm, verpackung]
symbol: —
einheit: —
---

ESD-Schutz beginnt bevor das Bauteil die Hand berührt. Ein strukturierter Ansatz schützt zuverlässig, ein halbherziger gar nicht.

:::hbox
:::vbox
**Voraussetzungen**
- [[Was ist ESD?]]
:::
:::vbox
**Verwandte Artikel**
- [[Erdungsarmband]]
:::
:::vbox
**Führt weiter zu**
- [[PCB Aufbau & Material]]
:::
:::

---

## ESD-Schutzzone (EPA)

EPA = Electrostatic Protected Area. Ein definierter Bereich mit kontrollierten Materialien und Erdungsanbindungen.

Was zur EPA gehört:
- Ableitfähige Arbeitsmatte (angeschlossen an PE)
- Erdungsarmband für die Person
- ESD-gerechte Verpackung für Bauteile
- Kein normaler Kunststoff auf dem Tisch

## Ableitfähige Materialien

ESD-Matten und -Boxen bestehen aus Materialien mit definiertem Widerstand:

| Typ | Widerstand |
|---|---|
| Leitfähig | 10^4 bis 10^6 Ω |
| Ableitfähig | 10^6 bis 10^9 Ω |
| Antistatisch | 10^9 bis 10^11 Ω |

Leitfähig ist nicht immer besser. Zu niederohmige Matten können bei Kurzschluss gefährlich werden.

## Erdungsarmband

Verbindet die Person über ca. 1 MOhm mit PE. Der 1-MOhm-Widerstand schützt bei versehentlichem Kontakt mit spannungsführenden Teilen.

Täglich prüfen. Ein defektes Armband bietet keinen Schutz.

## Verpackung

ESD-empfindliche Bauteile kommen in ableitfähige Beutel (metallisch glänzend, silber). Normale Plastikbeutel oder Schaumstoff (Styropor) sind ungeeignet und laden erst auf.

## Ionisatoren

Wenn ableitfähige Materialien nicht ausreichen (z.B. beim Reinigen mit Druckluft), baut ein Ionisator die statische Ladung aktiv ab. Erzeugt positive und negative Ionen in der Luft.

:::warning
Ein Erdungsarmband das nicht getragen wird schützt nicht. ESD-Massnahmen wirken nur wenn sie konsequent eingehalten werden.
:::
