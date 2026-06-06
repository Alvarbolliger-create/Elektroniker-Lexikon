---
title: TRIAC
kategorie: EK
kapitel: Halbleiter
tags: [triac, bidirektional, phasenanschnitt, dimmer, wechselstromsteuerung, leistungssteuerung, zündquadranten, bt136, bt138, moc3020]
groessen: U_GT|Gatterspannung|V; I_GT|Gatterstrom|mA; I_T|Nennstrom|A; U_DRM|max. Sperrspannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Thyristor (SCR)]]
- [[DIAC]]
:::
:::vbox
**Verwandte Artikel**
- [[DIAC]]
- [[Thyristor (SCR)]]
:::
:::vbox
**Führt weiter zu**
- [[Leistungselektronik]]
:::
:::

---

Ein TRIAC ist zwei antiparallel geschaltete Thyristoren in einem Gehäuse. Er leitet in **beiden Richtungen** und lässt sich durch einen Gate-Impuls in beiden Halbwellen zünden. Er ist das Standardbauteil für Wechselstrom-Leistungssteuerung.

## Schaltsymbol

:::schematic TRIAC
/schaltplaene/symbole/TRIAC.svg
:::

Drei Anschlüsse: **A1 (MT1)**, **A2 (MT2)** und **Gate (G)**. Das Symbol zeigt zwei antiparallele Thyristoren.

:::schematic TRIAC-Schichtenaufbau: fünf Schichten n-p-n-p-n, A1 unten, A2 oben, Gate seitlich an der mittleren n-Schicht. Beide SCR-Hälften teilen die inneren Schichten
/Diagramm/triac_schichtenaufbau.svg
:::

:::schematic TRIAC-Ersatzschaltbild: zwei antiparallele Thyristoren (SCR) mit gemeinsam verbundenem Gate G. Linker SCR leitet positive Halbwelle, rechter SCR leitet negative Halbwelle
/Diagramm/triac_ersatzschaltbild.svg
:::

## Zündquadranten

Der TRIAC kann in vier Quadranten gezündet werden, abhängig von der Polarität der Hauptspannung (A2-A1) und des Gate-Impulses:

| Quadrant | A2-A1 | Gate | Gate-Empfindlichkeit |
|---|---|---|---|
| I+ | positiv | positiv | hoch |
| I– | positiv | negativ | mittel |
| III– | negativ | negativ | hoch |
| III+ | negativ | positiv | gering (vermeiden!) |

**Empfehlung**: Quadrant I+ und III– verwenden (hohe Empfindlichkeit). Gate-Impuls immer mit dem gleichen Vorzeichen wie A2-A1 oder negativ.

## Kennlinie

:::schematic TRIAC-Kennlinie: symmetrische Thyristor-Kennlinie für beide Halbwellen. Im ersten Quadranten (+U, +I) und dritten Quadranten (–U, –I) je ein Vorwärts-Blockierbereich und ein Durchlassbereich. Kippvorgang in beiden Richtungen bei ±U_S durch Gate-Impuls auslösbar
/Diagramm/triac_kennlinie.svg
:::

## Ausschalten

Wie beim Thyristor: **kein aktives Ausschalten über Gate**. Der TRIAC löscht beim Nulldurchgang des Stroms. Das macht ihn ideal für 50/60-Hz-Netze.

## Phasenanschnitt-Schaltung mit DIAC

:::schematic TRIAC-Phasenanschnitt-Grundschaltung: Netz → Last → TRIAC (A2–A1). Parallelpfad: Netz → R (Potentiometer) → C → DIAC → Gate des TRIACs. U_C steigt bis U_BO des DIAC, dann Zündimpuls ans Gate
/Diagramm/triac_phasenanschnitt.svg
:::

Typische Grundschaltung für Dimmer und Motoranlasser:

1. R (Potentiometer) und C bilden ein RC-Glied, das die Netzspannung verzögert
2. Wenn U_C die DIAC-Kippspannung erreicht, zündet der DIAC und lädt die Gate-Ladung des TRIACs um
3. Der TRIAC zündet und verbindet Last mit Netz
4. Beim nächsten Nulldurchgang löscht der TRIAC — Zyklus beginnt neu

Je grösser R, desto länger dauert das Laden → später Zündzeitpunkt α → weniger Leistung.

:::warning
Bei **induktiven Lasten** (Motoren, Transformatoren) ist Phasenanschnitt problematisch: Der Strom-Nulldurchgang kommt nach dem Spannungs-Nulldurchgang. Der TRIAC löscht nicht zuverlässig. Zusätzlich entstehen Spannungsspitzen. → Snubber-Netzwerk (RC ≈ 100 Ω / 10 nF) parallel zum TRIAC einbauen.
:::

## Optokoppler-Ansteuerung

Für galvanische Trennung (Mikrocontroller → Netz) gibt es **TRIAC-Optokoppler** (z. B. MOC3020, MOC3041):
- Eingang: LED-Seite (5 V Logik)
- Ausgang: integrierter DIAC-Trigger zum Gate des Haupt-TRIACs

Der MOC3041 hat zusätzlich eine **Nulldurchgangserkennung** — er zündet nur beim Nulldurchgang (sanfteres Schalten, weniger EMV).

## Typische Bauteile

| Typ | I_T | U_DRM | Besonderheit |
|---|---|---|---|
| BT136 | 4 A | 600 V | Kleiner Heizstrahler, Dimmer |
| BT138 | 12 A | 800 V | Motoranlasser |
| BTA16 | 16 A | 600 V | Mit Snubber intern |
| T2550 | 25 A | 800 V | Industrielle Steuerungen |
