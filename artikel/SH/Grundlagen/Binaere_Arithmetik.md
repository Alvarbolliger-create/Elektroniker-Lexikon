---
title: Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)
kategorie: SH
kapitel: Grundlagen
tags: [binaere addition, binaere subtraktion, zweierkomplement, ueberlauf, binaere multiplikation, vorzeichen]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Zahlensysteme (Dual, Hexadezimal)]]
:::
:::vbox
**Führt weiter zu**
- [[Bitmanipulation in der Programmierung]]
- [[Addierer (Halbaddierer, Volladdierer)]]
:::
:::

---

Rechenoperationen im Dualsystem folgen denselben Prinzipien wie im Zehnersystem — nur mit der Basis 2. Da Subtraktion in Hardware aufwendiger zu realisieren ist als Addition, wird sie über das **Zweierkomplement** auf eine Addition zurückgeführt. So lässt sich mit ein und demselben Rechenwerk addieren *und* subtrahieren.

## Binäre Addition

Addiert wird stellenweise wie gewohnt — nur dass ein Übertrag (Carry) bereits ab 1 + 1 = 10₂ entsteht:

```
   1001   (9)
 + 1011  (11)
 ------
  10100  (20)
```

Für die niederwertigste Stufe (kein Übertrag von rechts) genügt ein **Halbaddierer (HA)**: Er bildet die Summe per EXOR und den Übertrag per AND.

Für alle weiteren Stufen braucht es einen **Volladdierer (VA)**, der zusätzlich den Übertrag der vorherigen Stufe (C_in) mit verarbeitet. Mehrere Volladdierer in Serie — der Übertragsausgang jeder Stufe gespeist in den Übertragseingang der nächsten — ergeben einen mehrstelligen **Addierer**, z. B. den 4-Bit-Addierer-Baustein 74283. → [[Addierer (Halbaddierer, Volladdierer)]]

:::merke
Halbaddierer = nur 2 Eingänge (A, B), kein Übertragseingang. Volladdierer = 3 Eingänge (A, B, C_in) — er kann an beliebiger Stelle einer Addiererkette stehen.
:::

## Das Zweierkomplement

Das **Zweierkomplement** einer Dualzahl entsteht durch zwei Schritte:

:::formel
**Zweierkomplement bilden**

1. Alle Bits invertieren (Einerkomplement)
2. Auf das Ergebnis +1 addieren

Beispiel: 0011 → invertieren → 1100 → +1 → 1101
:::

Das Zweierkomplement entspricht der "Ergänzung auf die nächste Zweierpotenz" — bei 4 Bit also der Ergänzung auf 16. Genau diese Eigenschaft macht es möglich, eine **Subtraktion als Addition** auszuführen:

:::tip
A − B = A + (Zweierkomplement von B), wobei die vorderste (überzählige) Stelle des Ergebnisses verworfen wird.

Beispiel: 1011 − 0011 → Zweierkomplement von 0011 ist 1101 → 1011 + 1101 = ~~1~~1000 → Ergebnis 1000
:::

In einer Schaltung lässt sich diese Umschaltung elegant mit **EXOR-Gattern** realisieren: Steuert man jedes Bit von B über ein EXOR mit einem gemeinsamen Steuersignal, wirkt das EXOR je nach Steuerpegel als Inverter (Subtraktion) oder als Durchleiter (Addition) — das EXOR wird so zum **steuerbaren Inverter**.

## Vorzeichenbehaftete Zahlen (signed)

Ohne Vorzeichen (**unsigned**) deckt ein 8-Bit-Wert den Bereich 0…255 ab. Mit Vorzeichen (**signed**) wird das MSB zum Vorzeichenbit: 0 = positiv, 1 = negativ — und negative Zahlen werden direkt im Zweierkomplement dargestellt.

| Bitmuster | unsigned | signed |
|---|---|---|
| 0000'0000 | 0 | 0 |
| 0111'1111 | 127 | +127 |
| 1000'0000 | 128 | −128 |
| 1111'1111 | 255 | −1 |

Damit lässt sich auch eine Subtraktion mit negativem Ergebnis korrekt als Addition rechnen — z. B. 5 − 7 = 5 + (Zweierkomplement von 7) = 0000'0101 + 1111'1001 = 1111'1110 = −2. ✓

## Überlauf (Overflow)

Reicht die Stellenzahl nicht aus, um das Ergebnis korrekt darzustellen, entsteht ein **Überlauf**: Das Resultat "rutscht" gedanklich über den Rand des Zahlenkreises hinaus und erscheint als völlig falscher Wert.

:::warning
Bei **unsigned**-Typen führt ein Überlauf "nur" dazu, dass das Ergebnis um die volle Wertespanne (z. B. 256) verschoben ist (129 + 128 = 257 → als 8-Bit-Wert 1). Bei **signed**-Typen ist ein Überlauf wesentlich tückischer: Selbst das Vorzeichen kippt, das Ergebnis ist komplett unbrauchbar (125 + 5 = 130 → als signed 8-Bit −126). Es liegt in der Verantwortung des Programmierers, solche Überläufe durch ausreichend grosse Datentypen zu vermeiden. → [[Datentypen]], [[Bitmanipulation in der Programmierung]]
:::

## Binäre Multiplikation

Die Multiplikation lässt sich auf wiederholte **Addition mit Stellenverschiebung** zurückführen — genau wie die schriftliche Multiplikation im Zehnersystem: Für jede 1 im Multiplikator wird der Multiplikand (um die entsprechende Stellenzahl nach links verschoben) addiert.

```
   101 × 1001
       1001
      0000
     0000
    1001
   ---------
    101101   (= 45)
```

In Hardware wird dies mit einer Matrix aus AND-Gattern (zur Bildung der Teilprodukte) und mehreren Addiererstufen realisiert.
