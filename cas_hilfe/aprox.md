---
title: aprox
kategorie: Funktionen
---

# `aprox` — numerisch auswerten

Mit `aprox(...)` zwingst du den Rechner, das Ergebnis **numerisch** darzustellen — als Dezimalzahl (Standard), in wissenschaftlicher Notation (SIC) oder in Ingenieurs-Notation (ENG). Ohne `aprox` bleibt das Ergebnis als exakter Bruch oder symbolischer Ausdruck stehen.

## Zwei Wege zum numerischen Ergebnis

### Variante 1: `aprox(...)` als Funktion

Einfach `aprox(...)` um den Ausdruck schreiben:

```
1/3 + 1/7             ▶  10/21
aprox(1/3 + 1/7)      ▶  0.47619
aprox(sqrt(2))        ▶  1.414214
aprox(π^2)            ▶  9.869604
```

`aprox` funktioniert auch auf der rechten Seite einer Zuweisung:

```
x := aprox(U/I)       ▶  x := 1200.0 Ω
```

### Variante 2: Ctrl+Enter

Setze den Cursor in eine Zeile und drück **Ctrl+Enter**. Der Rechner zeigt dann das aktuelle Ergebnis als Näherung — **ohne den Text zu verändern**. Das ist ein einmaliger „zeig's mir numerisch" — die Zeile bleibt inhaltlich unverändert.

Zum exakten Ergebnis zurück: **Backspace** (löscht das angezeigte Ergebnis) und dann **Enter** (wertet neu aus). So pendelst du ohne Textänderung zwischen exakt und numerisch.

## Mit Einheiten

`aprox` glänzt bei Einheiten: Die Zahl wird numerisch, und je nach Zahlenformat wird eine passende Präfix-Darstellung gewählt (nur im ENG-Modus).

```
R := 2200 * _Ohm
C := 470 * _nF
tau := R * C              ▶  tau := 517/500000 s
aprox(tau)                ▶  1.034 ms      (ENG)
                          ▶  1.034·10⁻³ s  (SIC)
                          ▶  0.001034 s    (Standard)
```

Welche Formatierung benutzt wird, stellst du im Einstellungen-Dialog ein (siehe [[Einstellungen]]).

## Mit freien Variablen

Wenn der Ausdruck noch freie Symbole enthält, werden die unverändert mitgenommen; nur die Zahlen werden numerisch:

```
aprox(π * r^2)        ▶  3.141593*r^2
```

## Wann `aprox`, wann nicht?

| Du willst … | Benutze |
|---|---|
| Exakten Bruch, symbolisches Ergebnis | nichts Besonderes |
| Eine konkrete Zahl zum Ablesen | `aprox(...)` oder Ctrl+Enter |
| Zahl mit passendem Einheiten-Präfix | `aprox(...)` + ENG-Modus |
| Wissenschaftliche Notation | `aprox(...)` + SIC-Modus |

## Was `aprox` nicht tut

- Es ändert keine globalen Zuweisungen — wenn `R := 220` exakt ist, bleibt `R` weiterhin exakt. Nur *die Zeile, in der `aprox` steht*, zeigt das numerische Ergebnis.
- Es verändert die Genauigkeit nicht über die eingestellten Nachkommastellen hinaus.
- Es umgeht keine Fehler: Ein undefiniertes Symbol bleibt ein Fehler, auch mit `aprox` drumrum.

## Unterschied zwischen den beiden Varianten

| Aspekt | `aprox(...)` im Text | Ctrl+Enter |
|---|---|---|
| Zeileninhalt wird geändert? | ja, `aprox(...)` steht im Text | nein, Text bleibt unverändert |
| Persistent? | ja — auch nach Neuladen noch da | nein — nur für diese eine Anzeige |
| Rückgängig? | Backspace löscht auch den Text | Backspace löscht nur das Ergebnis |
