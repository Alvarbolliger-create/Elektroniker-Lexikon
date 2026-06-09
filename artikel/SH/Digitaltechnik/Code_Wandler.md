---
title: Code-Wandler (BCD-zu-7-Segment)
kategorie: SH
kapitel: Digitaltechnik
tags: [codewandler, code-umsetzer, bcd, 7-segment-anzeige, decoder, wahrheitstabelle]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Digitale Codes (BCD, Gray, Hamming, ASCII)]]
- [[Karnaugh-Veitch-Diagramme (KV-Diagramme)]]
:::
:::vbox
**Führt weiter zu**
- [[Demultiplexer & Decoder]]
:::
:::

---

Ein **Code-Wandler** (auch Code-Umsetzer genannt) hat die Aufgabe, Informationen, die in einem gegebenen Code verschlüsselt sind, in einen anderen Code umzusetzen. Das alltäglichste Beispiel begegnet praktisch jedem: die Umwandlung einer BCD-verschlüsselten Ziffer in die Ansteuersignale einer 7-Segment-Anzeige.

## Die Aufgabenstellung: BCD auf 7-Segment

Eine 7-Segment-Anzeige soll zur Darstellung der im → [[Digitale Codes (BCD, Gray, Hamming, ASCII)|BCD-Code]] verschlüsselten Dezimalziffern 0…9 verwendet werden. Am Eingang des Code-Wandlers liegt die Ziffer als 4-Bit-Wort (D, C, B, A) an, am Ausgang werden die sieben Segmente a…g so angesteuert, dass die jeweilige Ziffer als Leuchtmuster erscheint:

| D | C | B | A | a | b | c | d | e | f | g | Ziffer |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 2 |
| 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 3 |
| 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 4 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 5 |
| 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 6 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 7 |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 |
| 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 9 |

:::merke
Ein Code-Wandler ist im Kern nichts anderes als eine kombinatorische Schaltung mit vier Eingangsvariablen (Eingangscode) und sieben Ausgangsvariablen (Ausgangscode). Jede Ausgangsvariable lässt sich einzeln über ein → [[Karnaugh-Veitch-Diagramme (KV-Diagramme)|Karnaugh-Veitch-Diagramm]] minimieren — das Ergebnis ist eine Schaltung, die für jedes Segment eine eigene Verknüpfungsgleichung aus A, B, C, D bildet (z. B. ergibt sich für Segment a der Term A∧B ∨ A∧C ∨ ¬A∧¬C ∨ ¬A∧¬B ∨ D).
:::

## Vom Gatternetz zum fertigen IC

Realisiert man die sieben Verknüpfungsgleichungen mit diskreten Gattern, entsteht ein Netz aus UND-, ODER- und Inverter-Bausteinen — pro Ziffer eine eigene "Spalte" aus Termen wie A∧B, ¬A∧¬C oder A∧¬B∧C, die anschliessend pro Segment passend mit ODER-Gattern zusammengeführt werden. In der Praxis übernimmt diese komplette Logik ein fertiger **BCD-zu-7-Segment-Decoder/Treiber-IC** wie der **74LS48** — er erspart den kompletten Gatteraufbau und liefert die Segmentsignale direkt aus dem BCD-Eingangswort.

## Mehrere Anzeigen zusammenschalten

Sollen mehrere Ziffern gleichzeitig dargestellt werden — etwa eine 4-stellige Dezimalzahl —, so erhält jede Stelle (10⁰, 10¹, 10², 10³) ihren eigenen 74LS48 mit eigener 7-Segment-Anzeige. Dabei treten zwei zusätzliche Anforderungen auf:

:::tip
**Nullenunterdrückung**: Bei einer mehrstelligen Anzeige sollen führende Nullen nicht dargestellt werden (aus "0042" soll "  42" werden). Der 74LS48 bringt dafür die Eingänge **RBI** (Ripple Blanking Input) und **RBO** (Ripple Blanking Output) mit: Ist eine Stelle "0" UND erhält sie über RBI das Signal, dass bereits eine höherwertige Stelle ausgeblendet wurde, so blendet sie sich selbst aus und reicht dieses Signal über RBO an die nächst niedrigere Stelle weiter. Die wertniedrigste Stelle (10⁰) wird dabei bewusst **nicht** in diese Kette eingebunden — eine "0" soll dort immer angezeigt werden.

**Lampentest**: Über den Eingang **LT** (Lamp Test) lassen sich mit einer einzigen Taste alle Segmente aller Anzeigen gleichzeitig auf "leuchtend" schalten — ein einfacher Funktionstest der kompletten Anzeigeneinheit, ohne jede Stelle einzeln prüfen zu müssen.
:::

Damit ist der Code-Wandler ein anschauliches Beispiel dafür, wie aus einer Wahrheitstabelle über eine kombinatorische Schaltung ein praktisches, alltägliches Bauteil entsteht — ein Funktionsprinzip, das sich in abgewandelter Form auch im → [[Demultiplexer & Decoder|Decoder]] und im → [[Encoder & Prioritätsencoder|Encoder]] wiederfindet.
