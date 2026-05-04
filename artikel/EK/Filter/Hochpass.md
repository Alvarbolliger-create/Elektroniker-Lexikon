---
title: Hochpass (HP)
kategorie: EK
tags: [hochpass, HP, grenzfrequenz, dämpfung, RC, sallen-key, aktiv, passiv, wechselstromkopplung, gleichanteil, filterordnung, 20dB]
symbol: —
einheit: —
---

Ein Hochpass (HP) lässt hohe Frequenzen ungehindert durch und dämpft tiefe Frequenzen. Gleichspannung (0 Hz) wird vollständig gesperrt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Filter Grundlagen]]
- [[RC-Filter]]
:::
:::vbox
**Verwandte Artikel**
- [[Tiefpass (TP)]]
- [[Bandpass (BP)]]
- [[Aktive Filter]]
:::
:::vbox
**Führt weiter zu**
- [[Filtercharakteristik]]
:::
:::

---

## Anwendungen

- Wechselstromkopplung: Gleichanteil aus einem Signal entfernen (z.B. DC-Offset eines Sensors)
- Rundsteuerempfänger: 50-Hz-Netzfrequenz durchlassen, tiefe Störungen sperren
- Audioanwendungen: Tieffrequentes Brummen unterdrücken
- Hochpassfilter nach dem Mikrofon: Windgeräusche (unter 100 Hz) dämpfen

## Frequenzgang

:::plot
var: f
range: 0.01, 100
xlabel: Frequenz (normiert)
ylabel: Amplitude (normiert)
Hochpass 1. Ordnung: f / sqrt(1 + f*f)
Hochpass 2. Ordnung: f*f / sqrt(1 + f^4)
:::

Unterhalb der Grenzfrequenz f_g: Dämpfung mit 20 dB/Dekade pro Ordnung. Oberhalb: volle Amplitude.

## Grenzfrequenz

Die **Grenzfrequenz f_g** ist die Frequenz, bei der die Ausgangsamplitude auf **70.7 %** des Eingangs abgefallen ist (= −3 dB):

:::monospace
f_g = 1 / (2 · π · R · C)     # Passiver RC-Hochpass 1. Ordnung
:::
## Passiver RC-Hochpass (1. Ordnung)

C in Reihe, R parallel zur Last. Tiefe Frequenzen: C hat hohen Widerstand → fast keine Spannung an R. Hohe Frequenzen: C hat niedrigen Widerstand → Spannung fällt hauptsächlich an R ab.

- Steilheit: **20 dB/Dekade**
- Sperrt Gleichspannung vollständig

## Aktiver Hochpass — Sallen-Key (2. Ordnung)

Gleiche Topologie wie beim aktiven Tiefpass, aber R und C vertauscht. Steilheit: **40 dB/Dekade**.

:::monospace
f_g = 1 / (2 · π · R · C)     # für R1 = R2 = R und C1 = C2 = C
:::
## Steilheit und Ordnung

| Ordnung | Steilheit |
|---|---|
| 1 | 20 dB/Dek |
| 2 | 40 dB/Dek |
| 4 | 80 dB/Dek |

:::warning
Ein Hochpass sperrt zwar den Gleichanteil, erzeugt aber beim Einschalten einen Einschwingvorgang. Das Ausgangssignal springt kurz auf und klingt dann ab. Bei Audioverstärkern kann das zu einem unerwünschten Knackgeräusch führen.
:::
