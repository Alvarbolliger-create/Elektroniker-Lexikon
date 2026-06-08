---
title: RC-Reihenschaltung
kategorie: ET
tags: [RC, reihenschaltung, impedanz, phasenverschiebung, kondensator, widerstand, wechselstrom, tiefpass, hochpass, grenzfrequenz]
groessen: Z|Impedanz|Ohm; R|Wirkwiderstand|Ohm; X_C|kapazitive Reaktanz|Ohm; phi|Phasenwinkel|°; U|Spannung|V; I|Strom|A; f|Frequenz|Hz; C|Kapazität|F; omega|Kreisfrequenz|rad/s
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
- [[Kondensator im Wechselstrom]]
:::
:::vbox
**Verwandte Artikel**
- [[RL-Reihenschaltung]]
- [[Zeigerdiagramm]]
:::
:::vbox
**Führt weiter zu**
- [[RC-Parallelschaltung]]
- [[RLC-Reihenschaltung (Serieschwingkreis)]]
:::
:::

---

Die RC-Reihenschaltung ist das Gegenstück zur RL-Reihenschaltung: Widerstand R und Kondensator C in Serie. Der Kondensator erzeugt eine negative Phasenverschiebung — der Strom eilt der Spannung vor. Als Filter bildet die RC-Reihenschaltung den einfachsten Tiefpass oder Hochpass.

:::schematic RC-Reihenschaltung
/schaltplaene/Filter/rc_reihe.svg
:::

## Kapazitive Reaktanz

Der Kondensator hat eine frequenzabhängige Reaktanz, die mit der Frequenz sinkt:

:::formel
X_C = 1 / (omega * C)
:::

Bei hohen Frequenzen ist X_C klein — der Kondensator "lässt durch". Bei niedrigen Frequenzen und Gleichstrom (f → 0) wird X_C sehr gross — der Kondensator sperrt.

## Impedanz

R und X_C sind 90° phasenverschoben, deshalb gilt Pythagoras:

:::formel
Z = sqrt(R^2 + X_C^2)
:::

## Phasenverschiebung

Die Spannung am Kondensator eilt dem Strom um 90° nach. Die Gesamtspannung liegt zwischen U_R (in Phase) und U_C (90° nach) — der Phasenwinkel phi liegt zwischen 0° und −90°.

:::formel
phi = arctan(-X_C / R)    # negatives Vorzeichen: kapazitiv → phi < 0
:::

| Grenzfall | Bedingung | Verhalten |
|---|---|---|
| Rein ohmsch | X_C ≪ R | phi ≈ 0°, Z ≈ R |
| Rein kapazitiv | X_C ≫ R | phi ≈ −90°, Z ≈ X_C |

## Strom und Teilspannungen

:::formel
I = U_ges / Z
:::

:::hbox
:::formel
U_R = I * R
:::

:::formel
U_C = I * X_C
:::

:::formel
U_ges = sqrt(U_R^2 + U_C^2)
:::
:::

:::monospace
Beispiel: U = 10 V, f = 1 kHz, R = 1 kOhm, C = 100 nF
X_C = 1 / (2 * pi * 1000 * 100e-9) = 1592 Ohm
Z = sqrt(1000^2 + 1592^2) = 1882 Ohm
I = 10 / 1882 = 5.31 mA
U_R = 5.31e-3 * 1000 = 5.31 V  (Ausgang Hochpass)
U_C = 5.31e-3 * 1592 = 8.45 V  (Ausgang Tiefpass)
phi = arctan(-1592 / 1000) = -57.9°
:::

## Umgekehrte Berechnung

Wenn nur Teilgrössen bekannt sind, lassen sich die Formeln umstellen:

:::formel
U_C = sqrt(U_ges^2 - U_R^2)    # Blindspannung aus Gesamt- und Wirkspannung
X_C = sqrt(Z^2 - R^2)           # Reaktanz aus Impedanz und Wirkwiderstand
C   = 1 / (omega * X_C)         # Kapazität aus berechneter Reaktanz
:::

:::monospace
Beispiel: U = 230 V, U_R = 100 V, I = 0.3 A, f = 50 Hz
U_C = sqrt(230^2 - 100^2) = 207 V
X_C = 207 / 0.3 = 690 Ω
C   = 1 / (2*pi*50 * 690) = 4.6 µF
:::

## Filter-Anwendung

Die RC-Reihenschaltung ist der Grundbaustein für einfache Filter. Die **Grenzfrequenz** f_3dB ist die Frequenz, bei der X_C = R gilt — dort beträgt die Ausgangsspannung 1/sqrt(2) ≈ 70,7 % der Eingangsspannung:

:::formel
f_3dB = 1 / (2 * pi * R * C)
:::

| Ausgang an | Verhalten | Filtertyp |
|---|---|---|
| R (U_R) | Hohe Frequenzen passieren | Hochpass |
| C (U_C) | Tiefe Frequenzen passieren | Tiefpass |

:::tip
Die RC-Grenzfrequenzformel f = 1/(2·pi·R·C) ist dieselbe wie die Formel für die Zeitkonstante tau = R·C, denn f_3dB = 1/(2·pi·tau). Ein Tiefpass mit tau = 1 ms hat seine Grenzfrequenz bei f_3dB ≈ 159 Hz.
:::

## Antwort auf Rechtecksignale (Pulsformer/Differenzierglied)

Speist man die RC-Reihenschaltung statt mit Sinus mit einem **Rechtecksignal**, zeigt sich im Zeitbereich dasselbe Hochpass-/Tiefpass-Verhalten — nur als Lade-/Entladevorgang statt als Phasenverschiebung:

:::schematic Oszillogramm-Vergleich: oben das Rechteck-Eingangssignal U_in (Sprünge zwischen 0 V und U_max); darunter zwei Antwortkurven I und U_C übereinander gezeichnet (in Rot bzw. Blau). I zeigt bei jeder Flanke einen steilen Nadelimpuls (positiv bei steigender, negativ bei fallender Flanke), der exponentiell mit tau = R·C gegen 0 abklingt. U_C zeigt dazu komplementär abgerundete, exponentiell ansteigende bzw. abfallende Rampen zwischen den Pegeln — die typische Lade-/Entladekurve
/Diagramm/rc_hochpass_rechteck_antwort.svg
:::

**Strom I (Differenzierglied):** Bei jeder Flanke springt U_in sofort um U_max. Da sich die Kondensatorspannung U_C nicht sprunghaft ändern kann ([[Auf- und Entladung (Kondensator)]]), liegt im ersten Moment die gesamte Sprunghöhe am Widerstand — und damit auch am Strom I = U_R / R, der überall in der Reihenschaltung gleich ist. I "springt mit" und klingt anschliessend exponentiell mit tau = R·C auf 0 ab. Das Ergebnis: aus jeder Flanke wird ein **Nadelimpuls** (positiv bei steigender, negativ bei fallender Flanke) — die Schaltung "differenziert" das Rechtecksignal. (U_R = I·R zeigt exakt dieselbe Form wie I, nur skaliert.)

**Spannung U_C (Integrierglied):** U_C folgt trägheitsbehaftet dem Eingang — bei jedem Pegelwechsel lädt bzw. entlädt sich C exponentiell auf den neuen Wert. Aus dem Rechteck wird so ein "abgerundetes" Signal mit Lade-/Entladerampen.

| Verhältnis tau zu Pulsdauer T | Verhalten von I (Hochpass-Charakter) | Verhalten von U_C (Tiefpass-Charakter) |
|---|---|---|
| tau ≪ T (Grenzfrequenz hoch) | Scharfe, schnell abklingende Nadelimpulse — reines Differenzierglied | Fast vollständige Lade-/Entladerampen — folgt dem Rechteck mit Rundung |
| tau ≫ T (Grenzfrequenz tief) | I folgt dem Rechteck nahezu unverändert | C lädt sich kaum um — Ausgang bleibt nahezu konstant (glättet) |

:::tip
Dasselbe Prinzip mit vertauschten Rollen gilt für die [[RL-Reihenschaltung]]: dort übernimmt U_L die Differenzierfunktion (Spannungsspitzen bei den Flanken) und U_R die Integrierfunktion — denn bei der Spule ist es der **Strom**, der sich nicht sprunghaft ändern kann.
:::
