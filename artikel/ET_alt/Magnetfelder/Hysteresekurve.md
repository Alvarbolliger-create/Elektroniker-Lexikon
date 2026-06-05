---
title: Hysteresekurve (B-H-Kurve)
kategorie: ET
tags: [Hysterese, B-H-Kurve, Remanenz, Koerzitivfeldstärke, Ferromagnet, Sättigung]
symbol: B, H
einheit: T, A/m
---

Die Hysteresekurve beschreibt das magnetische Verhalten ferromagnetischer Materialien. Sie zeigt, wie B auf H reagiert — und dass die Geschichte des Materials eine Rolle spielt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Magnetische Flussdichte]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
- [[Transformator Aufbau]]
- [[Transformator Typen]]
:::
:::

---

## Warum Hysterese?

In einem nicht-ferromagnetischen Material (Luft, Kupfer) gilt: B = µ0 × H. Linearer Zusammenhang, keine Hysterese.

In Eisen, Ferrit und anderen ferromagnetischen Materialien richten sich magnetische Domänen (Weisssche Bezirke) im äusseren Feld aus. Wenn das Feld abgeschaltet wird, bleiben viele Domänen ausgerichtet. Das Material "erinnert sich".

## Verlauf der Hysteresekurve

**Erstmagnetisierungskurve**: Unmagnetisiertes Material, H wird von 0 erhöht. B steigt zuerst langsam, dann steil, dann flacht die Kurve ab (Sättigung).

**Sättigungspunkt (Bsat)**: Alle Domänen ausgerichtet, weitere Erhöhung von H bringt kaum mehr B-Zunahme.

**Remanenz (Br)**: H wird auf 0 zurückgesetzt. B fällt nicht auf 0 — ein Teil der Magnetisierung bleibt erhalten. Das ist die Remanenzflussdichte.

:::formel
Br = Flussdichte bei H = 0    # nach vorangegangener Sättigung
:::
**Koerzitivfeldstärke (Hc)**: Um B auf 0 zu bringen, muss ein Gegenfeld angelegt werden. Hc ist das dafür nötige Gegenfeld.

:::formel
Hc = Feldstärke bei B = 0    # "Koerzitivkraft"
:::
**Gegensättigung**: H wird negativ erhöht bis zur negativen Sättigung. Dann wieder positiv — die Schleife schliesst sich.

## Kennwerte verschiedener Materialien

| Material | Br (T) | Hc (kA/m) | Typ |
|---|---|---|---|
| Elektroblech (Si-Stahl) | 1.0–1.5 | 0.05–0.1 | Weichmagnetisch |
| Ferrit (MnZn) | 0.3–0.5 | 0.01–0.05 | Weichmagnetisch |
| Alnico | 0.7–1.3 | 50–150 | Hartmagnetisch |
| Neodym (NdFeB) | 1.0–1.4 | 700–2000 | Hartmagnetisch |

## Weich- vs. Hartmagnetisch

**Weichmagnete** (kleine Hc): Schmale Hystereseschleife. Leicht umzumagnetisieren. Geringer Energieverbrauch pro Zyklus. Geeignet für Transformatoren, Motoren, Drosseln.

**Hartmagnete** (grosse Hc): Breite Hystereseschleife. Schwer umzumagnetisieren. Bleiben dauerhaft magnetisiert. Geeignet für Permanentmagnete, Lautsprecher, Sensoren.

## Hystereseverluste

Jedes Durchlaufen der Hystereseschleife kostet Energie — proportional zur eingeschlossenen Fläche. Diese Energie wird in Wärme umgewandelt.

:::formel
P_hyst ∝ f × Bmax^n × V    # n ≈ 1.6–2 (Steinmetz-Exponent)
:::
In Transformatoren und Motoren sind Hystereseverluste neben Wirbelstromverlusten die Hauptquelle der Kernverluste. Siliziumzusatz im Elektroblech verringert beide.

## Bedeutung für die Praxis

- Transformatorkern nie in die Sättigung treiben (B unter Bsat halten)
- Gleichstromanteil in der Wicklung verschiebt den Arbeitspunkt und kann zur einseitigen Sättigung führen
- Bei Ummagnetisierungsfrequenz > 1 kHz: Ferrit statt Elektroblech wählen (Elektroblech hat bei hohen Frequenzen zu hohe Wirbelstromverluste)
