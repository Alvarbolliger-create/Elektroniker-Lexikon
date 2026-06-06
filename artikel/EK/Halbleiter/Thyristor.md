---
title: Thyristor (SCR)
kategorie: EK
kapitel: Halbleiter
tags: [thyristor, scr, silicon controlled rectifier, gate, zündung, haltestrom, kommutierung, leistungselektronik, phasenanschnitt, pnpn, vier-schichten]
groessen: U_T|Schleusenspannung|V; I_H|Haltestrom|mA; I_GT|Zündstrom|mA; U_DRM|max. Sperrspannung|V; I_T|Nennstrom|A
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[pn-Übergang]]
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[DIAC]]
- [[TRIAC]]
:::
:::vbox
**Führt weiter zu**
- [[TRIAC]]
- [[DIAC]]
:::
:::

---

Ein Thyristor (SCR = Silicon Controlled Rectifier) ist ein steuerbarer Gleichrichter. Er lässt sich durch einen kurzen Gate-Impuls einschalten und bleibt danach selbst leitend — auch ohne weiteres Gate-Signal. Ausschalten ist nur durch Stromunterbrechung möglich.

## Schaltsymbol und Aufbau

:::schematic Thyristor (SCR)
/schaltplaene/symbole/Thyristor.svg
:::

Drei Anschlüsse: **Anode (A)**, **Kathode (K)** und **Gate (G)**. Der Thyristor besteht aus vier abwechselnden Halbleiterschichten: **p-n-p-n**.

:::schematic Thyristor-Schichtenaufbau: vier Schichten p1–n1–p2–n2, Anode oben an p1, Gate seitlich an p2, Kathode unten an n2. Drei pn-Übergänge J1, J2, J3 eingezeichnet
/Diagramm/thyristor_schichtenaufbau.svg
:::

## Zwei-Transistor-Ersatzschaltbild

:::schematic Thyristor-Zwei-Transistor-Modell: PNP-Transistor T1 (Emitter = Anode, Kollektor → Basis von T2) und NPN-Transistor T2 (Emitter = Kathode, Kollektor → Basis von T1). Gate an Basis T2. Rückkopplungspfeil zeigt Selbsthaltung
/Diagramm/thyristor_zwei_transistor.svg
:::

Der Thyristor lässt sich als zwei rückgekoppelte Transistoren verstehen — ein PNP (T1, Anode-seitig) und ein NPN (T2, Gate-seitig):

**Einschaltvorgang Schritt für Schritt:**
1. Positive Spannung am Gate → T2 (NPN) leitet
2. Kollektorstrom von T2 fliesst in die Basis von T1 → T1 (PNP) leitet
3. Kollektorstrom von T1 liefert zusätzlichen Basisstrom an T2 → Rückkopplung vollständig
4. Gate-Signal kann wegfallen — die Rückkopplung hält beide Transistoren leitend (Selbsthaltung)

## Einschalten

Voraussetzung: Anode positiver als Kathode (Vorwärtsspannung). Dann:

1. Kurzer positiver Strompuls ans Gate (I_GT, typisch einige mA)
2. Der Thyristor schaltet durch — er wird leitend (U_T ≈ 1–2 V)
3. Das Gate-Signal kann wegfallen — der Thyristor bleibt leitend

Der Thyristor hält sich selbst leitend, solange der Strom über den **Haltestrom I_H** bleibt.

## Ausschalten (Kommutierung)

Das Gate hat **keine Abschaltwirkung**. Der Thyristor schaltet nur aus wenn:

**Natürliche Kommutierung**: In Wechselstromsystemen geht der Netzstrom beim Nulldurchgang durch null — der Thyristor löscht automatisch.

**Zwangskommutierung (Kondensator-Methode)**: Ein vorgeladener Kondensator C_K wird beim Betätigen des AUS-Tasters parallel zum Thyristor geschaltet. Er entlädt sich kurzzeitig in Gegenrichtung durch den Thyristor, drückt den Hauptstrom unter I_H, und der Thyristor erlischt. Danach lädt sich C_K wieder auf U_B auf und ist für den nächsten Ausschaltvorgang bereit. Diese Methode ist aufwändig — heute meist durch IGBTs oder GTOs ersetzt.

## Kennlinie

:::schematic Thyristor-Kennlinie (I über U_AK): Im negativen Bereich kleiner Sperrstrom bis –U_Rab. Im positiven Bereich Vorwärts-Blockierbereich (kleiner Strom) bis U_S, dann schlagartig Kippen in den Durchlassbereich (Diodenkennlinie ab U_H). Kennlinie zeigt S-Form. Pfeil markiert Kippvorgang bei Zündung
/Diagramm/thyristor_kennlinie.svg
:::

Die Thyristor-Kennlinie (Strom I_T über Spannung U_AK) hat vier Bereiche:

| Bereich | U_AK | Zustand |
|---|---|---|
| Rückwärtssperrbereich | negativ | Sperrt, kleiner Leckstrom; bei –U_Rab Durchbruch |
| Vorwärts-Blockierbereich | 0 … U_S | Sperrt vorwärts — Gate noch nicht gezündet |
| Übergangsbereich | bei U_S (nach Gate-Impuls) | Kippt schlagartig in Durchlass |
| Durchlassbereich | > U_H | Leitet; U_T ≈ 1–2 V, ähnlich einer Diode |

**Wichtige Kenngrösssen:**
- **U_S**: Zündspannung — bei Überschreitung ohne Gate-Impuls feuert der Thyristor selbst durch
- **U_H**: Haltespannung — Mindestspannung im Durchlassbetrieb
- **I_H**: Haltestrom — fällt der Strom darunter, erlischt der Thyristor
- **I_L** (Latching Current): Minimalstrom nach dem Zünden, damit der Thyristor einrastet
- **U_Rab**: Max. Rückwärtssperrspannung

## Phasenanschnittsteuerung

Typische Anwendung: Drehzahlsteuerung, Helligkeitsregelung. Der Zündzeitpunkt α wird gegenüber dem Nulldurchgang verzögert. Je später gezündet wird, desto weniger Leistung wird übertragen:

:::formel
P_aus = P_max * (1 - α/π + sin(2α)/(2π))    # Vereinfacht, ohmsche Last
:::

Je grösser α (0° = maximale Leistung, 180° = keine Leistung), desto weniger Energie fliesst zur Last.

## Phasenanschnitt vs. Phasenabschnitt

| | Phasenanschnitt | Phasenabschnitt |
|---|---|---|
| Zündung | nach dem Nulldurchgang | beim Nulldurchgang |
| Abschaltung | am Nulldurchgang | nach definiertem Winkel |
| Bauelement | Thyristor, TRIAC | GTO, IGBT, MOSFET |
| Geeignet für | ohmsche Lasten | kapazitive Lasten |
| EMV | schlecht (steile Flanken) | besser |

:::warning
Phasenanschnitt an induktiven Lasten (Motoren, Transformatoren) erzeugt starke Spannungsspitzen (di/dt beim Sperren). Ohne **Snubber-Beschaltung** (RC parallel zum Thyristor) können Thyristor oder TRIAC beschädigt werden.
:::

## Vergleich zu anderen Bauelementen

| Bauelement | Schalten | U_max | I_max | Frequenz |
|---|---|---|---|---|
| Thyristor | Gate ein, Nulldurchgang aus | 10 kV | 10 kA | 50–400 Hz |
| IGBT | Gate ein und aus | 6.5 kV | 3.6 kA | bis 100 kHz |
| MOSFET | Gate ein und aus | 900 V | 100 A | bis MHz |
| GTO | Gate ein und aus | 6 kV | 6 kA | bis 1 kHz |

Thyristoren dominieren bei sehr hohen Leistungen (HGÜ-Übertragung, grosse Gleichrichter). Für Frequenzumrichter und Schaltregler werden heute fast ausschliesslich IGBTs oder MOSFETs eingesetzt.
