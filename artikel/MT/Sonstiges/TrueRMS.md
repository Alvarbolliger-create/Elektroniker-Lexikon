---
title: True RMS
kategorie: MT
tags: [truerms, effektivwert, multimeter, verzerrung, THD, crest-faktor, RMS, sinus, frequenzumrichter, schaltnetzteil]
symbol: —
einheit: V, A
---

Ein True-RMS-Messgerät misst den echten Effektivwert auch bei verzerrten Signalen. Ein normales Messgerät kann dabei 40 % daneben liegen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Sinuswellen]]
- [[Strom-, Spannungs-, Widerstandsmessung]]
:::
:::vbox
**Verwandte Artikel**
- [[Oberschwingungen und THD]]
- [[Strommesszange]]
:::
:::

---

## Was ist der Effektivwert?

Der Effektivwert (RMS = Root Mean Square) ist der Gleichspannungswert, der dieselbe Heizleistung erzeugen würde.

```
U_RMS = sqrt(1/T * integral(u(t)^2 dt))
```

Bei einem reinen Sinus: U_RMS = U_peak / sqrt(2) = U_peak × 0.707.

## Das Problem mit einfachen Messgeräten

Günstige Multimeter messen den Gleichrichtwert und rechnen ihn mit dem Faktor 1.11 auf RMS um. Das stimmt nur bei einem perfekten Sinus.

Bei einem verzerrten Signal (Schaltnetzteile, Frequenzumrichter) liefert diese Methode falsche Werte. Der Fehler kann 30-50 % betragen.

## True-RMS-Messung

Das Gerät berechnet den RMS-Wert direkt aus dem Messsignal: Quadrieren, Mitteln, Wurzel ziehen. Entweder analog mit einem RMS-Konverter-IC oder digital nach Abtastung.

Das Ergebnis ist korrekt unabhängig von der Signalform.

## Wann ist True RMS nötig?

- Spannungen an Schaltnetzteilen
- Strom an Frequenzumrichtern
- Netzstrom mit Oberschwingungen (THD > 5 %)
- Dimmer, Phasenanschnitt
- Beliebige nichtsinusförmige Signale

Bei reinen Sinussignalen aus dem Netz ist der Unterschied minimal.

## Crest-Faktor

True-RMS-Geräte haben eine Crest-Faktor-Spezifikation. Der Crest-Faktor ist das Verhältnis von Spitzenwert zu RMS-Wert.

Ein Sinus hat CF = 1.41. Impulse oder stark verzerrte Signale können CF > 5 haben. Wenn das Signal den spezifizierten CF überschreitet, ist auch die True-RMS-Messung ungenau.

:::tip
Für Netzstrommessungen mit Oberschwingungen immer True-RMS-Zangen verwenden. Der Aufdruck "True RMS" muss auf dem Gerät stehen, nicht bloss behauptet werden.
:::
