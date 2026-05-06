---
title: Skineffekt & Proximity-Effekt
kategorie: ET
tags: [Skineffekt, Proximity-Effekt, Hochfrequenz, Eindringtiefe, Litzendraht, HF]
groessen: δ|Eindringtiefe|m; ρ|spezifische Widerstand|Ω*m; f|Frequenz|Hz; ω|Kreisfrequenz|2πf; µ|magnetische Permeabilität|H/m
---

Bei hohen Frequenzen fliesst der Strom nicht mehr gleichmässig über den Querschnitt eines Leiters. Er konzentriert sich an der Oberfläche das erhöht den effektiven Widerstand.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Selbstinduktion]]
:::
:::vbox
**Verwandte Artikel**
- [[Induktivität und Einheiten]]
- [[Wellenwiderstand]]
:::
:::vbox
**Führt weiter zu**
- [[HF-Transformatoren]]
- [[EMV Pre-Compliance]]
:::
:::

---

## Physikalische Ursache

Ein Wechselstrom erzeugt ein wechselndes Magnetfeld um den Leiter. Dieses Feld induziert im Leiterinnern Wirbelströme, die dem Hauptstrom entgegenwirken (Lenz'sche Regel). Das Ergebnis: Der Strom wird nach aussen in die Oberfläche verdrängt.

## Eindringtiefe (Skin Depth)

Die Eindringtiefe δ gibt an, ab welcher Tiefe die Stromdichte auf 1/e ≈ 37 % des Oberflächenwerts abgefallen ist:

:::formel
δ = sqrt(2 * ρ / (ω * µ_0 * µ_r))    # ρ = spez. Widerstand, ω = Kreisfrequenz, µ = Permeabilität
:::
Für Kupfer vereinfacht:

:::formel
δ_Cu ≈ 66 mm / sqrt(f)    # f in Hz, δ in mm
:::

Bei 1 MHz ist die Eindringtiefe nur noch 66 µm ein 1-mm-Draht nutzt dann nur noch die äusserste Schicht.

## Auswirkungen

**Erhöhter HF-Widerstand**: Ein runder Kupferleiter hat bei hohen Frequenzen einen viel höheren Widerstand als bei DC. Verluste in HF-Spulen und Übertragern steigen mit der Frequenz.

**Leiterdimensionierung**: Einen dickeren Draht zu nehmen bringt ab einer gewissen Frequenz kaum mehr Nutzen, weil das Innere nicht mehr genutzt wird.

## Gegenmasssnahmen

**Litzendraht**: Viele feine, gegeneinander isolierte Drähte, die verseilt sind. Jeder Einzeldraht ist dünner als die Eindringtiefe. Wird für HF-Spulen und Übertrager eingesetzt.

**Hohle Leiter**: Bei sehr hohen Frequenzen werden rohrförmige Leiter verwendet. Das Innere trägt ohnehin nichts bei.

**PCB-Leiterbahnen**: Bei HF-Leitungen muss die Leiterbahnbreite und -dicke auf die Frequenz abgestimmt sein.

## Proximity-Effekt

Wenn zwei Leiter eng nebeneinander verlaufen, beeinflusst das Magnetfeld des einen den Stromfluss im anderen. Der Strom konzentriert sich auf den einander zugewandten Seiten (oder der abgewandten Seite, je nach Stromrichtung).

Der Proximity-Effekt ist in mehrlagigen Spulen und Übertragern oft schlimmer als der Skineffekt allein. Litzendraht mindert ihn, aber nicht vollständig.

:::tip
Für HF-Spulen und Schaltnetzteile über 100 kHz immer Litzendraht oder flache Folienwicklung verwenden, um Kupferverluste zu minimieren.
:::
