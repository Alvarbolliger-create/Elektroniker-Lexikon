---
title: Sinuswellen & Effektivwert
kategorie: ET
tags: [sinuswelle, effektivwert, scheitelwert, frequenz, periode, kreisfrequenz, PWM, dreieck, rechteck, RMS, bogenmass, phasenwinkel, phasenverschiebung, oszillogramm]
groessen: u(t)|Momentanspannung|V; U_peak|Scheitelwert|V; U_eff|Effektivwert|V; f|Frequenz|Hz; T|Periodendauer|s; omega|Kreisfrequenz|rad/s; phi|Phasenwinkel|°
_status: PORT+ERWEITERN  # ET_alt/Wechselstrom/Sinuswellen.md — Dreieck/Rechteck/PWM + Grad/Bogenmass ergänzt
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Zeigerdiagramm]]
:::
:::vbox
**Führt weiter zu**
- [[Impedanz]]
- [[Wellenlänge]]
- [[Wechselstromleistung]]
:::
:::

---

Wechselspannung im Stromnetz und in den meisten Signalen hat die Form einer Sinuswelle. Sie ist die einzige periodische Kurvenform, die bei Durchgang durch lineare Bauteile (R, L, C) ihre Form behält — nur Amplitude und Phase ändern sich.

:::plot
var: t
range: 0, 12.56
xlabel: Zeit (t)
ylabel: Spannung
Sinuswelle:  sin(t)
Effektivwert: 0.707
:::

## Allgemeine Gleichung

:::formel
u(t) = U_peak * sin(omega * t + phi)
omega = 2 * pi * f
T = 1 / f
:::

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Scheitelwert | U_peak | V | Maximaler Ausschlag |
| Kreisfrequenz | omega | rad/s | Winkelgeschwindigkeit der Zeigerdrehung |
| Frequenz | f | Hz | Schwingungen pro Sekunde |
| Periodendauer | T | s | Dauer einer vollständigen Schwingung |
| Phasenwinkel | phi | ° oder rad | Zeitlicher Versatz gegenüber dem Nullpunkt |

Die **Kreisfrequenz omega** taucht in allen Impedanzformeln auf (Z_C = 1/(omega·C), Z_L = omega·L) und ist deshalb die gebräuchlichere Grösse in der Wechselstromrechnung.

## Grad und Bogenmass

Der Phasenwinkel phi kann in Grad (°) oder Radiant (rad) angegeben werden. In Formeln wird Radiant erwartet.

:::formel
phi_rad = phi_deg * pi / 180
:::

| Grad | Radiant | Position auf der Sinuswelle |
|---|---|---|
| 0° | 0 | Nulldurchgang (aufsteigend) |
| 90° | pi/2 | Scheitel (Maximum) |
| 180° | pi | Nulldurchgang (absteigend) |
| 270° | 3*pi/2 | Negativer Scheitel |
| 360° | 2*pi | Ende einer Periode |

:::tip
Taschenrechner immer auf **RAD-Modus** stellen, wenn mit omega·t gerechnet wird. Im DEG-Modus liefert sin(omega·t) falsche Ergebnisse.
:::

## Phasenwinkel aus dem Oszillogramm ablesen

Sind zwei Kurven (z. B. u und i) im selben Diagramm gezeichnet, lässt sich der Phasenwinkel phi direkt aus der **zeitlichen Verschiebung Delta_t** zwischen zwei entsprechenden Punkten (z. B. beide Scheitelwerte oder beide Nulldurchgänge) bestimmen:

:::formel
phi = (Delta_t / T) * 360°    # Delta_t = Zeitverschiebung zwischen den Kurven, T = Periodendauer
:::

Eine volle Periode T entspricht 360°. Der Anteil, den Delta_t von T ausmacht, überträgt sich direkt auf den Winkel — daraus lässt sich z. B. der Leistungsfaktor cos(phi) berechnen → [[Wechselstromleistung]].

:::monospace
Beispiel: T = 20 ms, die Spitze von i folgt der Spitze von u um Delta_t ≈ 3,3 ms später
phi = (3.3 / 20) * 360° ≈ 60°
cos(phi) = cos(60°) = 0.5
:::

## Effektivwert – Grundprinzip

Der Effektivwert (RMS, Root Mean Square) ist der Gleichspannungswert, der an einem Widerstand **dieselbe Heizleistung** erzeugt wie das Wechselsignal. Das ist der Wert, den Multimeter anzeigen.

Das Grundprinzip: Signal **quadrieren** (macht alle Werte positiv), über die Zeit **mitteln**, **Wurzel** ziehen — daher Root Mean Square.

:::formel
U_eff = sqrt((1/T) * int(u(t)^2, t, 0, T))
:::

Für ein **stückweise konstantes Signal** — ein Signal, das bestimmte Spannungswerte für Anteile D1, D2, ... der Periode hält — vereinfacht sich das zu:

:::formel
U_eff = sqrt(U1^2 * D1 + U2^2 * D2)
:::

D1 und D2 sind die Zeitanteile (0 bis 1), also das Tastverhältnis jedes Pegels.

**Beispiel**: Ein Signal liegt 80 % der Zeit bei +15 V und 20 % der Zeit bei −5 V:

U_eff = sqrt(15² · 0.8 + (−5)² · 0.2) = sqrt(180 + 5) = sqrt(185) ≈ 13.6 V

Das **Vorzeichen** der Spannung spielt keine Rolle — durch das Quadrieren wird −5 V zu denselben 25 V² wie +5 V. Eine negative Spannung heizt genauso wie eine positive.

## Effektivwert – Kurvenformen

| Kurvenform | Herleitung | Formel |
|---|---|---|
| Rechteck (±U_peak, je 50 %) | sqrt(U_peak² · 0.5 + U_peak² · 0.5) | U_eff = U_peak |
| PWM (U_peak für D, 0 für 1−D) | sqrt(U_peak² · D + 0² · (1−D)) | U_eff = U_peak · sqrt(D) |
| Dreieck (kontinuierlich, 0 bis U_peak) | Integration nötig | U_eff = U_peak / sqrt(3) |
| Sinus | Integration nötig | U_eff = U_peak / sqrt(2) |

Rechteck und PWM lassen sich direkt aus der stückweise-Formel ableiten. Dreieck und Sinus verlaufen kontinuierlich — hier muss das Integral gebildet werden, das Ergebnis ist jeweils eine bekannte Formel.

:::warning
Einfache Multimeter (ohne True-RMS) messen den Gleichrichtwert und rechnen intern auf Sinus-Effektivwert um. Bei Dreieck-, Rechteck- oder PWM-Signalen liefern sie **falsche Werte**. Für nichtsinusförmige Signale immer ein True-RMS-Gerät verwenden.
:::

## Netzspannung Schweiz

Das Schweizer Netz liefert 230 V Effektivwert bei 50 Hz — dieser Wert steht auch auf Geräten.

| Grösse | Wert |
|---|---|
| Effektivwert U_eff | 230 V |
| Scheitelwert U_peak | 325 V |
| Periodendauer T | 20 ms |
| Frequenz f | 50 Hz |
| Kreisfrequenz omega | 314 rad/s |

:::tip
Das Netz hat **325 V Scheitelwert**, nicht 230 V. Kondensatoren in Netzteilen müssen mindestens 400 V aushalten — 325 V Scheitel plus Reserve für Spannungsschwankungen und Transienten.
:::
