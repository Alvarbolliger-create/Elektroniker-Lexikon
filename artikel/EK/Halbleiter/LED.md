---
title: LED
kategorie: EK
kapitel: Halbleiter
tags: [led, leuchtdiode, vorwiderstand, farbspektrum, rgb, infrarot, uv, wirkungsgrad, rekombination, durchlassspannung, pwm-dimmung]
groessen: U_F|Durchlassspannung|V; I_F|Betriebsstrom|A; R_V|Vorwiderstand|Ω; P_V|Verlustleistung|W
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[Optokoppler]]
- [[Fotodiode]]
:::
:::vbox
**Führt weiter zu**
- [[Optokoppler]]
:::
:::

---

Eine LED (Light Emitting Diode) ist eine Diode, bei der die Rekombination von Elektronen und Löchern am pn-Übergang Licht erzeugt statt Wärme. Sie leuchtet, sobald Strom in Durchlassrichtung fliesst.

## Funktionsprinzip

In einer normalen Silizium-Diode gibt der Rekombinationsprozess Energie als Wärme ab. In speziellen Verbindungshalbleitern (GaAs, GaP, GaN, InGaN) geschieht die Rekombination strahlend — die Energie wird als **Photon** freigesetzt. Die Wellenlänge (Farbe) hängt vom Bandabstand des Materials ab:

:::formel
λ = h * c / E_g    # Wellenlänge; h = 6.63e-34 J·s, c = 3e8 m/s
:::

## Durchlassspannungen nach Farbe

| Farbe | λ (nm) | U_F typisch | Material |
|---|---|---|---|
| Infrarot | 850–940 | 1.2–1.5 V | GaAs |
| Rot | 620–680 | 1.8–2.2 V | GaAlAs |
| Orange | 590–620 | 2.0–2.2 V | GaAsP |
| Gelb | 570–590 | 2.0–2.2 V | GaP |
| Grün | 520–560 | 2.0–3.5 V | GaP, InGaN |
| Blau | 450–490 | 3.0–3.5 V | InGaN |
| Weiss | — | 3.0–3.5 V | InGaN + Phosphor |
| UV | 370–400 | 3.5–4.0 V | GaN |

## Schaltsymbol

:::schematic LED
/schaltplaene/symbole/D_LED.svg
:::

Wie eine Diode, aber mit zwei ausgehenden Pfeilen (Licht).

## Vorwiderstand berechnen

LEDs müssen strombegrenzt werden — niemals direkt an Spannung anschliessen. Der Vorwiderstand begrenzt den Strom auf den Nennstrom (typisch 10–20 mA für Standard-LEDs):

:::formel
R_V = (U_S - U_F) / I_F    # Vorwiderstand
P_RV = (U_S - U_F) * I_F   # Verlustleistung im Widerstand prüfen
:::

:::monospace
Beispiel: U_S = 5 V, U_F = 2.0 V (rote LED), I_F = 10 mA
R_V = (5 - 2.0) / 10e-3 = 300 Ω → Normwert: 270 Ω oder 330 Ω
P_RV = 3.0 * 10e-3 = 30 mW → 1/8 W Widerstand genügt
:::

:::warning
LEDs sind sehr nichtlinear. Ein kleiner Spannungsanstieg über U_F verdoppelt den Strom. Ohne Vorwiderstand (oder Konstantstromquelle) zerstört sich eine LED in Sekunden.
:::

## Mehrere LEDs

**Reihenschaltung**: Alle LEDs tragen den gleichen Strom — ein Vorwiderstand genügt. Die Spannungsabfälle addieren sich.

:::formel
R_V = (U_S - n * U_F) / I_F    # n = Anzahl LEDs in Reihe
:::

**Parallelschaltung**: Nicht empfohlen — durch Fertigungsstreuung von U_F nehmen einzelne LEDs zu viel Strom. Jede LED sollte einen eigenen Vorwiderstand haben.

## PWM-Dimmung

Statt den Strom zu reduzieren (verändert die Farbe), wird die LED schnell ein- und ausgeschaltet (Pulsweitenmodulation). Oberhalb von ~100 Hz sieht das menschliche Auge nur die mittlere Helligkeit:

:::formel
I_mittel = I_F * D    # D = Tastverhältnis (0–1)
:::

**Vorteil**: LED arbeitet immer am Nennstrom → konstante Farbe, gute Effizienz. **Anwendung**: Anzeigedimmung, RGB-Farbmischung.

## Power-LEDs

Für Beleuchtungsanwendungen existieren Power-LEDs mit I_F von 350 mA bis mehreren Ampere. Diese brauchen:
- Konstantstromquelle (kein einfacher Vorwiderstand)
- Kühlkörper (mehrere Watt Verlustleistung)
- Thermisches Management → [[Wärmewiderstand]]
