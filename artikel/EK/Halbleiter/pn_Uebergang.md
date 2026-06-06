---
title: pn-Übergang
kategorie: EK
kapitel: Halbleiter
tags: [pn-übergang, sperrschicht, raumladungszone, diffusion, drift, kontaktspannung, durchlassrichtung, sperrrichtung, shockley, leckstrom, durchbruchspannung]
groessen: U_D|Diffusionsspannung|V; U_F|Flussspannung|V; I_S|Sättigungsstrom|A; U_T|Temperaturspannung|mV
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Halbleiter Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Diode]]
- [[BJT Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[Diode]]
- [[Zener-Diode]]
- [[BJT Grundlagen]]
:::
:::

---

Der pn-Übergang entsteht an der Grenzfläche zwischen p-dotiertem und n-dotiertem Halbleiter. Er ist das grundlegende Element aller Halbleiterbauelemente — jede Diode, jeder Transistor beruht darauf.

## Entstehung der Raumladungszone

:::schematic pn-Übergang im Gleichgewicht: p-Gebiet (–Ionen) | Raumladungszone | n-Gebiet (+Ionen), internes E-Feld von n nach p, Diffusions- und Driftstrom im Gleichgewicht
/Diagramm/pn_aufbau.svg
:::

Werden p- und n-dotiertes Silizium in Kontakt gebracht, diffundieren die Majoritätsträger über die Grenze: Elektronen vom n-Gebiet in das p-Gebiet, Löcher vom p-Gebiet in das n-Gebiet. Dabei hinterlassen sie ortsfeste Ionen zurück:

- Im n-Gebiet nahe der Grenze: positive Donatorionen (kein freies Elektron mehr)
- Im p-Gebiet nahe der Grenze: negative Akzeptorionen (kein freies Loch mehr)

Diese Schicht aus ortsfesten Ladungen ohne freie Träger heisst **Raumladungszone** (RLZ) oder **Sperrschicht**. Sie erzeugt ein internes elektrisches Feld, das der Diffusion entgegenwirkt. Im Gleichgewicht heben sich Diffusions- und Driftstrom auf — kein Nettostrom fliesst.

Die dabei entstehende **Diffusionsspannung** U_D beträgt für Silizium typisch 0.6 bis 0.7 V. Sie ist die interne Potentialbarriere, die Ladungsträger überwinden müssen.

## Durchlassrichtung (Plus auf p, Minus auf n)

:::schematic Durchlass- vs. Sperrrichtung: Links Durchlass (RLZ verkleinert, Strom fliesst), rechts Sperr (RLZ verbreitert, kein Strom)
/Diagramm/pn_richtungen.svg
:::

Die externe Spannung wirkt der Diffusionsspannung entgegen und verkleinert die Raumladungszone. Ab ca. **0.6 V (Si)** ist die Barriere so weit abgebaut, dass Majoritätsträger massenhaft über die Grenze fliessen. Der Strom steigt exponentiell.

:::formel
I = I_S * (exp(U / U_T) - 1)    # Shockley-Gleichung
:::

Dabei ist:
- **I_S** = Sättigungsstrom (typisch 10⁻¹² bis 10⁻⁹ A)
- **U_T** = Temperaturspannung = k·T/q ≈ 26 mV bei 25 °C

## Sperrrichtung (Minus auf p, Plus auf n)

Die externe Spannung verstärkt das interne Feld und verbreitert die Raumladungszone. Majoritätsträger werden von der Grenze weggedrängt — kein Strom fliesst, ausser dem kleinen **Sperrstrom (Leckstrom)** durch thermisch erzeugte Minoritätsträger.

Der Sperrstrom I_S ist sehr klein (nA bis µA) und steigt stark mit der Temperatur (verdoppelt sich ca. alle 10 K).

## Durchbruch

Wird die Sperrspannung zu gross, kommt es zum Durchbruch:

**Zener-Effekt** (< ~5 V): Das starke Feld reisst Elektronen direkt aus den Valenzbindungen heraus. Kontrolliert und reversibel — genutzt in Zener-Dioden.

**Lawinendurchbruch / Avalanche** (> ~7 V): Beschleunigte Ladungsträger erzeugen durch Stösse weitere Träger (Lawineneffekt). Ebenfalls reversibel, sofern die Verlustleistung begrenzt bleibt.

:::warning
Bei normalen Dioden (nicht Zener) ist der Durchbruch zerstörend, wenn der Strom nicht begrenzt wird. Die Raumladungszone hält die Energie nicht ab — sie heizt sich auf und schmilzt durch.
:::

## Temperaturspannung U_T

Die Shockley-Gleichung enthält den Faktor U_T = k·T/q:

:::formel
U_T = k * T / q    # k = 1.38e-23 J/K, q = 1.6e-19 C
:::

Bei Raumtemperatur (T = 298 K) ergibt das U_T ≈ 26 mV. Die Durchlassspannung einer Si-Diode nimmt um ca. **2 mV/K** ab — bei 75 °C Erwärmung liegt U_F rund 150 mV tiefer als bei Raumtemperatur.
