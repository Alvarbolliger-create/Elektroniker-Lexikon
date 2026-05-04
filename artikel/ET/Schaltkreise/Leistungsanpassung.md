---
title: Leistungsanpassung
kategorie: ET
tags: [leistungsanpassung, innenwiderstand, lastwiderstand, maximale leistung, anpassung, wirkungsgrad, impedanzanpassung, 50-ohm]
symbol: P_max
einheit: W
---

Eine Quelle gibt dann maximale Leistung an einen Verbraucher ab, wenn der Lastwiderstand gleich dem Innenwiderstand der Quelle ist.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Spannungs- & Stromteiler]]
:::
:::vbox
**Verwandte Artikel**
- [[Wirkleistung]]
- [[Reihenschaltung]]
:::
:::vbox
**Führt weiter zu**
- [[Impedanz]]
- [[Wellenwiderstand]]
:::
:::

---

## Grundmodell: Quelle mit Innenwiderstand

Jede reale Quelle hat einen Innenwiderstand Ri. Die Leerlaufspannung U0 teilt sich zwischen Ri und dem Lastwiderstand Ra auf.

:::monospace
I = U0 / (Ri + Ra)
P_a = I² × Ra = (U0 / (Ri + Ra))² × Ra
:::
## Bedingung für maximale Leistung

Die Ableitung von P_a nach Ra und Gleichsetzen mit null ergibt:

:::info
Maximale Leistungsübertragung tritt auf wenn Ra = Ri. Das ist die Leistungsanpassungsbedingung.
:::

:::monospace
Ra = Ri    # Leistungsanpassung: maximale Leistungsübertragung
:::
Im Anpassungsfall gilt:
:::monospace
P_max = U0² / (4 × Ri)    # maximale abgebbare Leistung
:::
Die Spannung an der Last beträgt dann genau die Hälfte der Leerlaufspannung:
:::monospace
U_a = U0 / 2    # bei Ra = Ri
:::
## Wirkungsgrad bei Leistungsanpassung

Bei Ra = Ri fällt die gleiche Leistung im Innenwiderstand ab wie an der Last. Der Wirkungsgrad beträgt nur 50 %.

:::monospace
η = P_a / P_gesamt = 50 %    # nur bei Leistungsanpassung
:::
Das ist kein Problem für Signalübertragung (Antenne, Audio), aber inakzeptabel für Energieübertragung (Stromversorgung).

## Wann wird Leistungsanpassung angestrebt?

**Ja, bei Signalübertragung**:
- Antennentechnik: 50-Ω-Anpassung für maximale Leistungsübertragung
- Audioschaltungen: Impedanzanpassung zwischen Endstufe und Lautsprecher
- HF-Messtechnik: 50-Ω-Kabel, Messgeräte, Antennen

**Nein, bei Energieversorgung**:
- Netzteil → Last: möglichst kleiner Innenwiderstand, Ra >> Ri
- Wirkungsgrad muss hoch sein, 50 % Verlust ist nicht akzeptabel
- Spannungsregler haben bewusst einen kleinen Ausgangswiderstand

## Grafische Darstellung

Die Leistung P_a als Funktion von Ra hat ein Maximum bei Ra = Ri. Links davon (Ra < Ri) steigt die Leistung mit Ra. Rechts davon (Ra > Ri) sinkt sie wieder.

| Ra / Ri | P_a / P_max | Wirkungsgrad |
|---|---|---|
| 0.25 | 64 % | 20 % |
| 0.5 | 89 % | 33 % |
| 1 (Anpassung) | 100 % | 50 % |
| 2 | 89 % | 67 % |
| 4 | 64 % | 80 % |
| 10 | 33 % | 91 % |
