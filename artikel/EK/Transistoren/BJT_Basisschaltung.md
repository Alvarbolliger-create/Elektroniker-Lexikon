---
title: BJT Basisschaltung
kategorie: EK
kapitel: Transistoren
tags: [basisschaltung, hf-verstärker, gleichphasig, kleiner eingangswiderstand, grosser ausgangswiderstand, transitfrequenz, stromverstärkung kleiner 1]
groessen: v_u|Spannungsverstärkung|—; R_ein|Eingangswiderstand|Ω; R_aus|Ausgangswiderstand|kΩ; f_T|Transitfrequenz|Hz
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BJT Grundlagen]]
- [[BJT Arbeitspunkt]]
:::
:::vbox
**Verwandte Artikel**
- [[BJT Emitterschaltung]]
- [[BJT Kollektorschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[Verstärkung & Dämpfung]]
:::
:::

---

Die Basisschaltung hat einen kleinen Eingangswiderstand, einen grossen Ausgangswiderstand und dreht die Phase **nicht**. Sie ist die schnellste BJT-Schaltung und wird für HF-Verstärker eingesetzt — im Audiobereich kaum verwendet.

## Schaltungsprinzip

:::schematic BJT Basisschaltung (NPN): Basis über C_B an GND (AC-Masse). Signal u_ein am Emitter (über R_E). Ausgang u_aus am Kollektor (über R_C nach U_B). Kleiner Eingangswiderstand am Emitter, grosser Ausgangswiderstand am Kollektor. Phasenlage 0°
/Diagramm/bjt_basisschaltung.svg
:::

:::schematic Kaskodeschaltung: Emitterschaltung (unten, T1: Signal am Gate) in Reihe mit Basisschaltung (oben, T2: Basis auf AC-Masse). Eingang bei T1-Basis, Ausgang bei T2-Kollektor. Kombination aus hoher Verstärkung und hoher Bandbreite
/Diagramm/bjt_kaskodeschaltung.svg
:::

Die Basis ist für Wechselspannung mit GND verbunden (Kondensator). Das Signal kommt am Emitter rein, der Ausgang liegt am Kollektor. Der Emitter ist der niederohmige Eingang, der Kollektor der hochohmige Ausgang.

## Spannungsverstärkung

:::formel
v_u = u_aus / u_ein ≈ g_m * R_C = (I_C / U_T) * R_C    # gleichphasig, kein Minuszeichen
:::

Die Spannungsverstärkung ist ähnlich gross wie bei der Emitterschaltung, jedoch **ohne Phasenumkehr** (gleichphasig). Die Stromverstärkung ist kleiner als 1 — der Kollektorstrom ist etwas kleiner als der Emitterstrom (I_E = I_B + I_C).

## Eingangs- und Ausgangswiderstand

:::formel
R_ein = r_BE / B = U_T / I_C    # sehr klein, typisch 10–50 Ω
R_aus = r_CE || R_C              # sehr gross, typisch 50 kΩ – 1 MΩ
:::

| Kenngrösse | Emitterschaltung | Basisschaltung |
|---|---|---|
| Spannungsverstärkung | gross | gross |
| Stromverstärkung | gross (≈ B) | < 1 (≈ α ≈ 0.99) |
| Eingangswiderstand | mittel (kΩ) | sehr klein (10–50 Ω) |
| Ausgangswiderstand | mittel (kΩ) | sehr gross (50 kΩ+) |
| Phasenlage | 180° | 0° |

## Frequenzverhalten

Die Basisschaltung ist deutlich schneller als die Emitterschaltung. In der Emitterschaltung begrenzt die Miller-Kapazität (C_CB zurückgespiegelt auf den Eingang) die Bandbreite. In der Basisschaltung gibt es keinen Miller-Effekt — die obere Grenzfrequenz ist die **Transitfrequenz f_T** des Transistors selbst.

:::info
**Warum kein Miller-Effekt?** Der Miller-Effekt vergrössert die Rückkopplungskapazität zwischen Eingang und Ausgang um den Verstärkungsfaktor. Bei der Basisschaltung ist die Basis auf AC-Masse — die Kapazität zwischen Kollektor und Basis erscheint am Eingang nicht vergrössert.
:::

## Anwendung

**HF-Verstärker (UKW, UHF)**: In Hochfrequenzanwendungen ist die Basisschaltung der Standard, weil sie keine Rückkopplung hat und bis f_T stabil verstärkt.

**Kaskodeschaltung**: Emitterschaltung (gute Verstärkung) + Basisschaltung (verhindert Miller-Effekt) in Reihe kombiniert. Ergibt grosse Verstärkung bei hoher Bandbreite.

**Stromkopier-Schaltungen (Current Mirror)**: Basisschaltung als präziser Stromkopierer — der Emitterstrom fliesst fast vollständig als Kollektorstrom durch.
