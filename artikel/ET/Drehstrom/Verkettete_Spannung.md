---
title: Verkettete Spannung
kategorie: ET
tags: [verkettete spannung, leiterspannung, strangspannung, sqrt3, drehstrom, zeiger]
groessen: U_str|Strangspannung|V; U_L|Leiterspannung|V; phi|Phasenwinkel|°
_status: PORT  # ET_alt/Drehstrom/Verkettete_Spannung.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Drehstrom Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Sternschaltung]]
- [[Dreieckschaltung]]
:::
:::

---

Die verkettete Spannung (Leiterspannung) ist die Spannung zwischen zwei Phasen — also "von Phase zu Phase". Sie ist sqrt(3) mal grösser als die Strangspannung (Phase gegen Neutral). Dieser Faktor sqrt(3) ≈ 1,732 taucht in allen Drehstromformeln auf.

## Herleitung

Die drei Phasenspannungen sind um 120° verschoben. Die Spannung zwischen L1 und L2 ist die **Differenz** der beiden Zeiger u1 und u2. Da beide dieselbe Amplitude und 120° Winkelabstand haben, ergibt die geometrische Differenz:

:::formel
U_L = U_str * sqrt(3)
:::

**Geometrische Begründung:** Im Zeigerdiagramm bilden die drei gleich langen, um 120° versetzten Zeiger ein gleichseitiges Dreieck. Die Verbindung zweier Zeigerspitzen (Differenz = Leiterspannung) ist um sqrt(3) länger als die Zeigeramplitude.

## Schweizer Netz (TN-S)

| Grösse | Wert |
|---|---|
| Strangspannung U_str (L–N) | 230 V |
| Leiterspannung U_L (L–L) | 400 V |
| Verhältnis | sqrt(3) = 1,732 |
| Frequenz f | 50 Hz |

Probe: 230 V · 1,732 = 398 V ≈ 400 V ✓

## Phasenwinkel

Die Leiterspannung eilt der niedrigeren Strangspannung um 30° vor (ergibt sich aus der Zeigergeometrie). Dieser Phasenunterschied ist wichtig bei Transformatoren und für die Beurteilung von Schaltgruppen.

:::tip
Im Alltag: **230 V** = Steckdose (Phase–Neutral, Einphasenstrom). **400 V** = Kraftsteckdose, Herd, Waschmaschine (Phase–Phase, Drehstrom). Beide sind dasselbe Netz — nur an unterschiedlichen Leitern abgegriffen.
:::

## Messung

Ein Voltmeter zeigt:
- Zwischen L und N: Strangspannung ≈ 230 V
- Zwischen L1 und L2 (oder L2–L3 oder L3–L1): Leiterspannung ≈ 400 V
- Zwischen N und PE: Idealerweise 0 V (PE und N sind an der Einspeisung verbunden)

:::warning
**Sicherheit:** 400 V zwischen zwei Phasen sind gefährlicher als 230 V Phase–Neutral — die Leiterspannung ist sqrt(3)-mal grösser. Beim Arbeiten an Drehstromanlagen müssen alle drei Phasen abgeschaltet und gesichert sein.
:::
