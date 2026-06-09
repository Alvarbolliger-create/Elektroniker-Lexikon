---
title: Schaltregler Topologien
kategorie: EK
kapitel: Stromversorgung
tags: [schaltregler, Sperrwandler, Flusswandler, Flyback, Forward, Gegentakt, Halbbrücke, Vollbrücke, galvanische-Trennung, Transformator, Resonanzwandler, PFC, SNT]
groessen: U_E|Eingangsspannung|V; U_A|Ausgangsspannung|V; D|Tastverhältnis|—; P|Leistung|W
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[DC-DC-Wandler]]
- [[MOSFET Anwendungen]]
- [[Thyristor (SCR)]]
:::
:::vbox
**Verwandte Artikel**
- [[DC-DC-Wandler]]
- [[Kühlkörper]]
:::
:::vbox
**Führt weiter zu**
- [[Kühlkörper]]
:::
:::

---

Schaltnetzteil-Topologien unterscheiden sich in Leistungsbereich, galvanischer Trennung und Schaltungsaufwand. Der Spick unterscheidet Wandler ohne und mit galvanischer Trennung.

## Topologien ohne galvanische Trennung — Übersicht

Buck und Boost sind bereits in [[DC-DC-Wandler]] mit Schaltbild und Rechenbeispiel behandelt — hier die Kurzreferenz, alle weiteren Topologien folgen mit eigenem Schaltbild:

| Wandler | Richtung | Formel U_A | Spannungsbereich |
|---|---|---|---|
| Buck (Abwärts) | nur abwärts | D · U_E | 0 ≤ U_A ≤ U_E |
| Boost (Aufwärts) | nur aufwärts | U_E / (1−D) | U_A ≥ U_E |

**Richtung aus D bestimmen:** Bei Topologien mit der Formel U_A = D/(1−D) · U_E (Buck-Boost, SEPIC, Cuk, Zeta, Doppelinverter) entscheidet allein das Tastverhältnis D, ob auf- oder abwärts gewandelt wird — der Betrag |U_A| wird mit U_E verglichen:

:::formel
D < 0.5  → |U_A| < U_E   # Wandler arbeitet abwärts
D = 0.5  → |U_A| = U_E   # Übergangspunkt
D > 0.5  → |U_A| > U_E   # Wandler arbeitet aufwärts
:::

Reine Buck- und Boost-Wandler sind dagegen durch ihre Schaltungstopologie fest auf eine Richtung festgelegt: Beim Buck liegt der Schalter in Serie zur Last (Spannungsteiler-Wirkung → immer abwärts), beim Boost liegt die Speicherdrossel vor dem Schalter und lädt sich auf, bevor sie die Energie zusätzlich zu U_E an den Ausgang abgibt (→ immer aufwärts). Die Berechnung von U_A bzw. D erfolgt in jedem Fall durch Umstellen der jeweiligen Formel — siehe Beispiele in [[DC-DC-Wandler]].

### Ladungspumpe — Charge Pump

Die Ladungspumpe wandelt **ohne Spule**, nur mit Kondensatoren, Dioden und einem **Umschalter S** — geeignet für kleine Leistungen, da die übertragbare Energie pro Schaltzyklus durch die Kapazität von C1 begrenzt ist. Der Umschalter S legt den unteren Anschluss des Pumpkondensators C1 abwechselnd auf U_E+ oder auf U_E− (GND) und „pumpt" dadurch Ladung über die Dioden Richtung Ausgang. Je nachdem, wie D1, D2 und C1 verschaltet sind, entsteht entweder ein **Spannungsverdoppler** (Ausgang positiv, Faktor 2) oder ein **Inverter** (Ausgang negativ, Faktor −1):

#### Spannungsverdoppler (positiv)

:::schematic Ladungspumpe (Spannungsverdoppler, positiv): Schalter S legt C1 abwechselnd auf U_E+/GND, D1 klemmt Knoten A, D2 lädt C2 auf den Spitzenwert
/schaltplaene/Stromversorgung/ladungspumpe_verdoppler.svg
:::

Der Umschalter S wechselt periodisch zwischen zwei Stellungen — dadurch wird C1 abwechselnd **mit umgekehrter Polung** auf- bzw. umgeladen:

- **S in Stellung „+":** Der untere Anschluss von C1 liegt auf U_E+. D1 klemmt Knoten A (oberer Anschluss von C1) auf ≈ 0 V — C1 lädt sich mit ≈ U_E auf, **oberer Anschluss negativ gegenüber dem unteren**.
- **S in Stellung „−" (GND):** Der untere Anschluss von C1 springt auf 0 V. Da die Spannung über C1 erhalten bleibt, „schiebt" sich Knoten A auf ≈ +2 · U_E nach oben — C1 ist jetzt **mit vertauschter Polarität** geladen (oberer Anschluss positiv). D1 sperrt, D2 leitet und lädt den Speicherkondensator C2 auf diesen Spitzenwert.

C1 wird also bei jedem Umschaltvorgang mit **wechselnder Polung (+ / −)** be- und umgeladen — genau dieser Polaritätswechsel ist der „Pump"-Mechanismus, der die Spannung anhebt:

:::formel
U_A ≈ 2 * U_E    # Verdoppler: C1 wird umgepolt geladen, D2 gibt den Spitzenwert ≈ 2·U_E an C2/R_L weiter
:::

#### Inverter (negativ)

:::schematic Ladungspumpe (Inverter, negativ): Schalter S legt C1 abwechselnd auf U_E+/GND, D1 klemmt Knoten M nach GND, D2 (umgekehrt gepolt) lädt C2 negativ
/schaltplaene/Stromversorgung/ladungspumpe_inverter.svg
:::

Der Inverter nutzt denselben Umschalt-Mechanismus, jedoch sind **D1 und D2 anders gepolt** als beim Verdoppler — D1 leitet von Knoten M nach GND, D2 leitet von Knoten O (Ausgang) zurück nach M (also „rückwärts" verglichen mit der Stromrichtung im Verdoppler):

- **S in Stellung „+":** Der linke Anschluss von C1 liegt auf U_E+. D1 klemmt Knoten M auf ≈ 0 V — C1 lädt sich auf ≈ U_E (linker Anschluss positiv, rechter ≈ 0 V).
- **S in Stellung „−" (GND):** Der linke Anschluss von C1 springt auf 0 V. Die Spannung über C1 bleibt erhalten — Knoten M „rutscht" auf ≈ −U_E. D1 sperrt; D2 leitet jetzt von O nach M und zieht Ladung aus C2/R_L ab, wodurch sich der Ausgang auf ≈ −U_E gegenüber GND auflädt.

Auch hier wird C1 bei jedem Takt **mit wechselnder Polarität** umgeladen — der Unterschied zum Verdoppler liegt allein in der Dioden-Orientierung, die bestimmt, ob die gepumpte Ladung den Ausgang anhebt (Verdoppler) oder ihm Ladung entzieht und ihn so unter GND zieht (Inverter). Beachte auch die vertauschte Polaritätsbeschriftung der Klemmen: Der Ausgang „+" liegt hier auf GND-Potential, „−" führt die negative Spannung:

:::formel
U_A ≈ -U_E       # Inverter: D1/D2 umgekehrt gepolt → Ausgang wird auf negatives Potential gepumpt
:::

:::tip
Real liegt |U_A| wegen der Diodenflussspannungen (≈ 2 × 0.6 V) etwas unter dem theoretischen Wert: U_A ≈ 2·U_E − 2·U_F (Verdoppler) bzw. U_A ≈ −(U_E − 2·U_F) (Inverter). Für höhere Faktoren (×3, ×4, …) werden mehrere Pumpstufen kaskadiert (Dickson-Ladungspumpe). In integrierten Bausteinen (z. B. MAX232, ICL7660) übernehmen MOSFETs die Funktion von S und takten im MHz-Bereich.
:::

### Synchronwandler — Synchronous Buck Converter

:::schematic Synchronwandler: High-Side-Schalter S1 und Low-Side-Schalter S2 ersetzen Schalter und Freilaufdiode des Buck-Wandlers
/schaltplaene/Stromversorgung/synchronwandler.svg
:::

Der Synchronwandler ist ein Buck-Wandler, bei dem die **Freilaufdiode durch einen zweiten, aktiv angesteuerten Schalter S2** (i. d. R. MOSFET) ersetzt ist. S1 und S2 schalten gegenphasig (synchron, mit kurzer Totzeit gegen Querströme):

- **S1 leitet, S2 sperrt:** Strom fliesst von U_E über S1 und L zur Last — wie beim klassischen Buck.
- **S1 sperrt, S2 leitet:** L treibt den Strom über S2 (statt über die Freilaufdiode) weiter — der Schaltknoten SW wird aktiv auf GND gezogen.

Da ein leitender MOSFET (R_DS(on) im mΩ-Bereich) deutlich weniger Verlustleistung erzeugt als eine Diode (U_F ≈ 0.3–0.7 V), steigt der Wirkungsgrad spürbar — besonders bei niedrigen Ausgangsspannungen, wo die Diodenflussspannung sonst einen grossen Anteil von U_A ausmachen würde. Zusätzlich ermöglicht die aktive Ansteuerung beider Schalter einen **bidirektionalen Leistungsfluss** (Energie kann auch von der Last zurück in die Quelle fliessen, z. B. beim Bremsen eines Motors).

Die Spannungsformel ist identisch zum klassischen Buck-Wandler — nur die Verluste sind geringer:

:::formel
U_A = D * U_E    # Ausgangsspannung — gleiche Formel wie beim Buck Converter
D   = U_A / U_E  # Tastverhältnis aus Spannungen
:::

### Buck-Boost — Inverswandler

:::schematic Buck-Boost-Wandler (Inverswandler): Schalter S lädt L gegen GND auf, Diode D überträgt die Energie invertiert an den Ausgang
/schaltplaene/Stromversorgung/buck_boost_invers.svg
:::

Der Inverswandler kombiniert Buck und Boost in einer Schaltung — Schalter S, Speicherdrossel L und Diode D liegen so verschaltet, dass die Ausgangsspannung **invertiert** (negativ gegenüber GND) entsteht:

- **S leitet:** L wird über S gegen GND geladen — Strom steigt linear an, D sperrt (Ausgang vom Eingang getrennt).
- **S sperrt:** Das Magnetfeld in L bricht zusammen, der Strom fliesst über D weiter — und zwar in Richtung Ausgang/GND, wodurch sich am Ausgangskondensator eine **negative** Spannung gegenüber GND aufbaut.

Da die Spule zwischen den Phasen vollständig entladen werden kann oder nicht, ergibt sich je nach Tastverhältnis D ein Auf- oder Abwärtswandeln — siehe „Richtung aus D bestimmen" oben:

:::formel
U_A = -D / (1 - D) * U_E   # Ausgangsspannung — invertiert (U_A ≤ 0)
:::

:::warning
Wegen der Invertierung ist U_A **immer negativ** (bzw. ≤ 0), unabhängig vom Tastverhältnis — geeignet z. B. für negative Hilfsspannungen in Mehrfach-Versorgungen (OPV-Schaltungen, Displays).
:::

### SEPIC-Wandler — Single-Ended Primary-Inductor Converter

:::schematic SEPIC-Wandler: L1/S laden vor, Koppelkondensator C1 überträgt die Energie über L2/D nicht-invertierend an den Ausgang
/schaltplaene/Stromversorgung/sepic_wandler.svg
:::

Der SEPIC-Wandler wandelt **nicht-invertierend** sowohl auf- als auch abwärts — ein Vorteil gegenüber dem Inverswandler, wenn die Ausgangsspannung das gleiche Vorzeichen wie die Eingangsspannung haben muss, ihr Betrag aber über oder unter U_E liegen kann (z. B. Akkuspannung, die je nach Ladezustand über oder unter der benötigten U_A liegt):

- **S leitet:** L1 lädt sich über S gegen GND auf, gleichzeitig entlädt sich der Koppelkondensator C1 über S in L2 — D sperrt.
- **S sperrt:** L1 lädt C1 über D nach, während L2 ihre gespeicherte Energie ebenfalls über D an den Ausgang abgibt. Beide Spulenströme summieren sich am Ausgang.

Der in Serie liegende Koppelkondensator C1 entkoppelt Ein- und Ausgang galvanisch für Gleichspannung und verhindert, dass im Fehlerfall (S dauerhaft leitend) die volle Eingangsspannung am Ausgang anliegt:

:::formel
U_A = D / (1 - D) * U_E   # Ausgangsspannung — nicht invertierend, auf- und abwärts
:::

:::tip
Der **Zeta-Wandler** ist die strukturelle Variante des SEPIC mit vertauschter Lage von Schalter und Koppelkondensator (S am Ausgang, C1 am Eingang) — er liefert die gleiche Formel und Eigenschaften, eignet sich aber besser für Anwendungen mit niedriger Eingangs-Restwelligkeit.
:::

### Ćuk-Wandler

:::schematic Ćuk-Wandler: L1/S laden vor, Koppelkondensator C1 überträgt die Energie über D/L2 invertiert an den Ausgang
/schaltplaene/Stromversorgung/cuk_wandler.svg
:::

Der Ćuk-Wandler ist die **invertierende Variante** des SEPIC — gleicher Grundaufbau mit Energieübertragung über einen Koppelkondensator C1, jedoch sind Diode D und Speicherdrossel L2 vertauscht angeordnet, sodass die Ausgangsspannung negativ gegenüber GND wird:

- **S leitet:** L1 lädt sich über S gegen GND auf; C1 entlädt sich über S und liefert Energie an L2 — D sperrt.
- **S sperrt:** L1 lädt C1 über D nach; L2 gibt ihre Energie über D an den Ausgang ab. Der Ausgang liegt dabei auf negativem Potential gegenüber GND.

Wie beim SEPIC sorgt C1 für eine kontinuierliche Energieübertragung mit geringer Stromwelligkeit auf beiden Seiten — ein Vorteil bei EMV-kritischen Anwendungen:

:::formel
U_A = -D / (1 - D) * U_E   # Ausgangsspannung — invertiert, auf- und abwärts (U_A ≤ 0)
:::

:::tip
Der **Doppelinverter (Inverting SEPIC)** ist eine alternative invertierende Topologie mit ähnlicher Formel — die genaue Schaltungsanordnung unterscheidet sich, das Funktionsprinzip „auf-/abwärts wandeln und invertieren über D bestimmt durch das Tastverhältnis" bleibt gleich.
:::

### Split-Pi-Wandler — Boost-Buck Converter

:::schematic Split-Pi-Wandler: zwei Halbbrücken (S1/S3 und S2/S4) mit gemeinsamem Zwischenkreiskondensator C2 in der Mitte, je eine Speicherdrossel L1/L2 und Filterkondensator C1/C3 aussen an den Anschlüssen U1/U2
/schaltplaene/Stromversorgung/split_pi_wandler.svg
:::

Der Split-Pi-Wandler verbindet zwei Spannungsebenen U1 und U2 **bidirektional**. Anders als der Name "Speicherdrossel in der Mitte" vermuten liesse, sitzt das verbindende Element zwischen den beiden Halbbrücken nicht eine Spule, sondern der **Zwischenkreiskondensator C2** — die Spulen L1 und L2 liegen jeweils **aussen**, direkt an den Anschlüssen U1 bzw. U2:

- **Linke Stufe** (C1 – L1 – Halbbrücke S1/S3): ein synchroner Tiefsetzsteller zwischen der gemeinsamen Zwischenkreisspannung U_C2 (an C2) und U1.
- **Rechte Stufe** (Halbbrücke S2/S4 – L2 – C3): ein synchroner Tiefsetzsteller zwischen U_C2 und U2.
- **C2** in der Mitte bildet den gemeinsamen Spannungs-Zwischenkreis, an den beide Halbbrücken parallel angeschlossen sind und über den die Energie ausgetauscht wird.

Da beide Stufen mit aktiv angesteuerten Schaltern (statt Dioden) arbeiten, kann die Energie **in beide Richtungen** fliessen — je nachdem, welche Seite die Zwischenkreisspannung "treibt" und welche sie "abnimmt":

- **Energiefluss U1 → U2:** Die linke Halbbrücke speist C2 (arbeitet bezogen auf U1 als Hochsetzsteller), die rechte Halbbrücke entnimmt die Energie aus C2 und versorgt U2 (Tiefsetzsteller-Betrieb).
- **Energiefluss U2 → U1:** Die Rollen tauschen entsprechend.

Diese Topologie wird eingesetzt, wo Energie in beide Richtungen fliessen muss, z. B. zwischen Batterie und Zwischenkreis in Energiespeichersystemen (Laden **und** Entladen über denselben Wandler):

:::formel
U_C2 = U1 / D1 = U2 / D2     also     U2 = U1 * (D2 / D1)
:::

:::tip
Da beide Halbbrücken aktiv angesteuerte Schalter (statt Dioden) verwenden — wie beim Synchronwandler — ist der Wirkungsgrad hoch und der Leistungsfluss in beide Richtungen verlustarm möglich. Über das Verhältnis der Tastgrade D1/D2 lässt sich U2 frei über oder unter U1 einstellen.
:::

### Kaskadierter Ab-/Aufwärtswandler — Buck-Boost Cascade

:::schematic Kaskadierter Ab-/Aufwärtswandler: Buck-Stufe (S1, S2) und Boost-Stufe (S3, S4) teilen sich eine gemeinsame Speicherdrossel L
/schaltplaene/Stromversorgung/kaskadierter_buck_boost.svg
:::

Diese Topologie reiht eine Buck- und eine Boost-Stufe hintereinander, die sich eine gemeinsame Speicherdrossel L teilen — im Gegensatz zum Inverswandler bleibt die Ausgangsspannung dabei **nicht-invertierend** (gleiches Vorzeichen wie U_E), kann aber sowohl über als auch unter U_E liegen:

- **U_A < U_E gewünscht:** Die Buck-Stufe (S1, S2) regelt aktiv ab, die Boost-Stufe bleibt durchgeschaltet (S4 dauerhaft leitend, S3 dauerhaft sperrend) — die Schaltung verhält sich wie ein reiner Buck-Wandler.
- **U_A > U_E gewünscht:** Die Buck-Stufe bleibt durchgeschaltet (S1 dauerhaft leitend), die Boost-Stufe (S3, S4) übernimmt die Regelung — die Schaltung verhält sich wie ein reiner Boost-Wandler.
- **U_A ≈ U_E:** Beide Stufen takten gemeinsam (Vier-Schalter-Betrieb) — die Regelung wechselt nahtlos zwischen Buck- und Boost-Modus.

Diese Umschaltung macht die Topologie ideal für Anwendungen mit stark schwankender Eingangsspannung, die mal über und mal unter der gewünschten Ausgangsspannung liegt (z. B. Solarpanel- oder Batterie-Eingänge):

:::formel
U_A = D * U_E              # Buck-Modus aktiv (Boost-Stufe durchgeschaltet)
U_A = U_E / (1 - D)        # Boost-Modus aktiv (Buck-Stufe durchgeschaltet)
:::

## Topologien mit galvanischer Trennung

Ein Transformator trennt Ein- und Ausgangsseite elektrisch. Pflicht für Netzteile nach Sicherheitsvorschriften.

### Sperrwandler — Fly-Back Converter

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | < 250 W |
| Energieübertragende Elemente | Gekoppelte Speicherdrossel mit Luftspalt |
| Besonderheit | Aufbau wie Transformator, aber mit Luftspalt zur Energiespeicherung (kein gleichzeitiger Energie-Fluss) |

Einfachste Topologie mit galvanischer Trennung. Weit verbreitet in Ladegeräten und kleinen Netzteilen (Handy-Ladegerät, USB-Netzteil).

### Eintaktflusswandler — Forward Converter

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | < 500 W |
| Energieübertragende Elemente | Transformator + zusätzliche Speicherdrossel |
| Besonderheit | Energie fliesst direkt (gleichzeitig) durch Transformator |

### Gegentaktflusswandler — Push-Pull Converter

Zwei Varianten mit unterschiedlichem Leistungsbereich:

| Variante | Leistungsbereich | Schalter |
|---|---|---|
| Halbbrückenflusswandler | 100 W bis 2 kW | S1, S2 (Halbbrücke) |
| Vollbrückenflusswandler | > 300 W bis kW-Bereich | S1–S4 (H-Brücke) |

Transformator überträgt die Energie. Typisch für PC-Netzteile, Industrienetzteile, Motorendstufen.

### Resonanzwandler

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | Einige 10 W bis kW-Bereich |
| Besonderheit | Resonanzkreis (C_R, L_R) ermöglicht ZVS/ZCS (Zero Voltage/Current Switching) → sehr hoher Wirkungsgrad, geringe EMV |

Mit galvanischer Trennung durch zusätzlichen Transformator T_r erweiterbar.

### Brückenloser PFC-Wandler

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | 10 W bis unterer kW-Bereich |
| Besonderheit | Resonanzkreis aus zwei Kondensatoren und zwei magnetisch gekoppelten Drosseln und Übertrager |

PFC = Power Factor Correction — verbessert den Leistungsfaktor der Netzaufnahme.

## Zerhacker

Der **Zerhacker** ist eine elektromechanische Vorrichtung, die eine Gleichspannung in eine rechteckförmige Wechselspannung umwandelt — damit kann ein Transformator die Spannung transformieren. Historisch vor Halbleiter-Schaltreglern verwendet.

## Topologien-Vergleich

| Topologie | Leistung | Trennung | Aufwand | Typischer Einsatz |
|---|---|---|---|---|
| Buck | bis kW | nein | gering | Punkt-zu-Punkt-Versorgung (MCU, µC) |
| Boost | bis kW | nein | gering | LED-Treiber, PFC-Vorstufe |
| Flyback | < 250 W | ja | mittel | Handy-Ladegerät, USB-Netzteil |
| Forward | < 500 W | ja | mittel | Industrienetzteil |
| Halbbrücke | 100 W – 2 kW | ja | hoch | PC-Netzteil, Servoantrieb |
| Vollbrücke | > 300 W | ja | hoch | Grosse Netzteile, Frequenzumrichter |
| Resonanz | 10 W – kW | ja | sehr hoch | Hochleistungs-Netzteile, ZVS-Schaltungen |

:::tip
Für EFZ-Niveau: Buck und Boost berechnen, Flyback und Forward konzeptuell verstehen. Die galvanisch getrennten Topologien sind hauptsächlich für die Auswahl und das Verständnis von Fertigmodulen relevant.
:::
