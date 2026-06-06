---
title: Halbleiter Grundlagen
kategorie: EK
kapitel: Halbleiter
tags: [halbleiter, dotierung, n-typ, p-typ, eigenleitung, silizium, germanium, leitungsband, valenzband, freie elektronen, löcher, majoritätsträger, minoritätsträger]
groessen: E_g|Bandabstand|eV; n|Elektronenkonzentration|cm⁻³; p|Löcherkonzentration|cm⁻³; σ|Leitfähigkeit|S/m
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Elektrisches Feld]]
:::
:::vbox
**Verwandte Artikel**
- [[pn-Übergang]]
:::
:::vbox
**Führt weiter zu**
- [[pn-Übergang]]
- [[BJT Grundlagen]]
- [[FET Grundlagen]]
:::
:::

---

Halbleiter leiten Strom schlechter als Metalle, aber besser als Isolatoren. Durch gezielte Beimischung von Fremdatomen (Dotierung) lässt sich ihre Leitfähigkeit um viele Grössenordnungen kontrolliert einstellen. Das ist die physikalische Grundlage aller Transistoren, Dioden und integrierten Schaltkreise.

## Bandstruktur und Eigenleitung

:::schematic Bändermodell: Valenzband (unten, voll) – verbotene Zone (Breite E_g) – Leitungsband (oben, leer). Vergleich Leiter / Halbleiter / Isolator
/Diagramm/halbleiter_baendermodell.svg
:::

Im Atommodell eines Kristalls entstehen zwei Energiebänder: das **Valenzband** (voll besetzt, keine freien Elektronen) und das **Leitungsband** (leer, Elektronen würden hier Strom tragen). Dazwischen liegt eine verbotene Zone — der **Bandabstand E_g**.

| Material | Bandabstand E_g | Eigenschaft |
|---|---|---|
| Silizium (Si) | 1.12 eV | Standard-Halbleiter |
| Germanium (Ge) | 0.67 eV | Tiefe Schwellenspannung, wärmeempfindlich |
| Galliumarsenid (GaAs) | 1.43 eV | HF, Leuchtdioden |
| Siliziumcarbid (SiC) | 3.26 eV | Hohe Temp./Spannungen |
| Galliumnitrid (GaN) | 3.40 eV | Leistungselektronik, HF |

Beim **reinen (intrinsischen) Halbleiter** werden durch Wärme einzelne Elektronen über den Bandabstand angehoben. Das frei gewordene Elektron hinterlässt eine Lücke im Valenzband — ein **Loch**. Löcher verhalten sich wie positive Ladungsträger: Sie wandern entgegen der Elektronen und tragen ebenfalls zum Strom bei.

:::info
Silizium ist bei Raumtemperatur fast ein Isolator (ca. 2300 Ω·m). Dotiertes Silizium kann bis auf 0.001 Ω·m gebracht werden — ein Faktor von über einer Million.
:::

## n-Dotierung (Elektronenleitung)

:::schematic n-dotiertes Silizium: Si-Gitter mit eingebautem Phosphoratom (5 Valenzelektronen), das fünfte Elektron ist frei beweglich (Donator)
/Diagramm/halbleiter_n_dotierung.svg
:::

Wird ein Phosphor- oder Arsenatom (5 Valenzelektronen) in den Si-Kristall eingebaut, passt das fünfte Elektron nicht in das Bindungsgitter — es bleibt frei und steht als Ladungsträger zur Verfügung. Solche Atome heissen **Donatoren**.

- Majoritätsträger: **Elektronen**
- Minoritätsträger: Löcher
- Leitfähigkeit steigt mit Dotierungskonzentration

## p-Dotierung (Löcherleitung)

:::schematic p-dotiertes Silizium: Si-Gitter mit eingebautem Boratom (3 Valenzelektronen), fehlende Bindung ergibt ein wanderndes Loch (Akzeptor)
/Diagramm/halbleiter_p_dotierung.svg
:::

Wird ein Boratom (3 Valenzelektronen) eingebaut, fehlt eine Bindung — es entsteht ein Loch. Dieses Loch kann von benachbarten Elektronen besetzt werden und wandert dadurch scheinbar durch den Kristall. Solche Atome heissen **Akzeptoren**.

- Majoritätsträger: **Löcher**
- Minoritätsträger: Elektronen
- Auch hier steigt die Leitfähigkeit mit der Dotierungskonzentration

## Temperaturabhängigkeit

Mehr Wärme → mehr Elektronen werden über den Bandabstand gehoben → mehr freie Ladungsträger → niedrigerer Widerstand. Halbleiter haben deshalb einen **negativen Temperaturkoeffizienten (NTC)** — der Widerstand sinkt mit steigender Temperatur. Das gilt für **undotierte** Halbleiter; stark dotierte verhalten sich eher wie Metalle.

:::warning
Transistoren und Dioden reagieren empfindlich auf Temperatur. Bei BJTs sinkt U_BE um ca. 2 mV pro Kelvin Temperaturanstieg — bei 50 °C mehr als bei Raumtemperatur verschiebt sich der Arbeitspunkt um 100 mV.
:::

## Verbindungshalbleiter

Während Silizium für Logik und Leistungselektronik dominiert, haben spezialisierte Materialien ihre Nischen:

**GaAs**: Höhere Elektronenbeweglichkeit → schnellere Transistoren. In HF-Verstärkern, Mobilfunk, Laserdiodensubstraten.

**SiC und GaN**: Grosser Bandabstand → hohe Durchbruchspannungen, Betrieb bei hohen Temperaturen. SiC-MOSFETs und GaN-HEMTs verdrängen Silizium in der Hochleistungselektronik.
