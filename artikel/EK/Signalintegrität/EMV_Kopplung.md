---
title: EMV-Koppelmechanismen
kategorie: EK
tags: [EMV, Kopplung, galvanisch, kapazitiv, induktiv, elektromagnetisch, Störung, PCB]
symbol: —
einheit: —
---

Elektromagnetische Störungen koppeln immer über einen von vier Mechanismen. Wer den Mechanismus kennt, weiss welche Gegenmassnahme wirkt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signalintegrität]]
- [[Magnetfelder]]
- [[Elektrisches Feld]]
:::
:::vbox
**Verwandte Artikel**
- [[Übersprechen (Crosstalk)]]
- [[Wellenwiderstand]]
- [[EMV Pre-Compliance]]
:::
:::

---

## Übersicht der vier Koppelmechanismen

| Mechanismus | Koppelmedium | Typische Frequenz |
|---|---|---|
| Galvanisch (leitungsgebunden) | Gemeinsame Impedanz | DC bis HF |
| Kapazitiv | Elektrisches Feld | NF bis HF |
| Induktiv | Magnetisches Feld | NF bis HF |
| Elektromagnetisch (Wellen) | Elektromagnetische Welle | HF (> 30 MHz) |

---

## 1. Galvanische Kopplung (leitungsgebunden)

**Ursache**: Zwei Schaltkreise teilen sich einen gemeinsamen Impedanzpfad (z.B. dieselbe Masseleitung, dasselbe Netzteil).

Ein Strompuls in Schaltkreis A erzeugt einen Spannungsabfall über die gemeinsame Impedanz Z_gemeinsam. Schaltkreis B "sieht" diesen Spannungsabfall als Störung.

```
U_Stoerung = I_A × Z_gemeinsam
```

**PCB-Gegenmassnahme**:
- Massefläche statt Massesternpunkt bei HF
- Getrennte Entkopplungskondensatoren pro IC
- Keine gemeinsamen Versorgungsleitungen für Leistungs- und Signalteil
- Ferrite in Versorgungsleitungen als HF-Trennstellen

---

## 2. Kapazitive Kopplung

**Ursache**: Das elektrische Feld zwischen zwei Leitungen koppelt Spannungsänderungen. Die Kopplungskapazität hängt vom Abstand, der Parallelläuflänge und der Dielektrizität ab.

```
I_koppel = C_koppel × dU/dt    # Störstrom proportional zu Spannungsänderung
```

**Typisch**: Schnelle Spannungsänderungen (PWM-Taktleitungen, Schalttransistoren) koppeln auf benachbarte Signalleitungen.

**PCB-Gegenmassnahme**:
- Abstand zwischen Leitungen vergrössern (Kapazität ∝ 1/d)
- Masseleitung zwischen aggressiver und empfindlicher Leitung
- Abschirmblech oder Abschirmkappe über HF-Quellen
- Kabel: geschirmtes Kabel, Schirm geerdet

---

## 3. Induktive Kopplung

**Ursache**: Ein sich ändernder Strom erzeugt ein magnetisches Wechselfeld, das in eine benachbarte Schleife eine Spannung induziert. Die Gegenseitigkeitsinduktivität M bestimmt die Kopplung.

```
U_koppel = M × dI/dt    # Störspannung proportional zu Stromänderung
```

**Typisch**: Hohe dI/dt bei Schalttransistoren, Motoren, Relais. Koppelt auf Messleitungen, Signalkabel.

**PCB-Gegenmassnahme**:
- Schleifenfläche minimieren (Hin- und Rückleiter eng beieinander)
- Twisted Pair: Magnetfeld des Hin- und Rückleiters hebt sich auf
- Massefläche: Rückstrom fliesst direkt unter der Signalleitung → minimale Schleife
- Ferritkern über Kabel: Dämpft induktive Einkopplung im HF-Bereich
- Abstand von Störquellen (Übertrager, Drosseln)

---

## 4. Elektromagnetische Kopplung (Strahlungskopplung)

**Ursache**: Bei hohen Frequenzen (typisch > 30 MHz) strahlen Leiterbahnen und Kabel als Antennen. Die Welle breitet sich im Raum aus und induziert in anderen Leitungen Spannungen/Ströme.

**Typisch**: Schaltnetzteile, Mikroprozessortakte, Hochgeschwindigkeitsdatenbusse.

**PCB-Gegenmassnahme**:
- Schirmgehäuse (Faraday'scher Käfig)
- Geschlossene Massefläche ohne Schlitze (Schlitze wirken wie Schlitzantennen)
- Impedanzkontrolliertes Layout (keine Antennenstrukturen)
- Via-Stitching an Schlitzkanten
- Filterkondensatoren und Ferrite an Kabeldurchführungen
- Leitungsgebundene Massnahmen: LISN, Ferrite, Mantelwellensperren

---

## Zusammenfassung: Massnahmen vs. Mechanismus

| Massnahme | Galv. | Kap. | Ind. | EM |
|---|---|---|---|---|
| Massefläche | ✓ | ✓ | ✓ | ✓ |
| Abstand | — | ✓ | ✓ | ✓ |
| Twisted Pair | — | — | ✓ | ✓ |
| Schirmung | — | ✓ | — | ✓ |
| Ferrit | ✓ | — | ✓ | ✓ |
| Entkopplungs-C | ✓ | — | — | — |
