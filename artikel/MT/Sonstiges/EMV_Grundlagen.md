---
title: EMV-Grundlagen
kategorie: MT
tags: [EMV, elektromagnetische verträglichkeit, störung, kopplung, schirmung, abschirmung, faradayscher käfig, mu-metall, filter, gleichtakt, gegentakt, common mode, differential mode, netzfilter, EN 61000, IEC 61000, CE-kennzeichnung, EMV-richtlinie, surge, burst, ESD, leitungsgebunden, abgestrahlt]
symbol: —
einheit: —
---

Elektromagnetische Verträglichkeit (EMV) beschreibt die Fähigkeit eines Geräts, in seiner elektromagnetischen Umgebung störungsfrei zu funktionieren und andere Geräte nicht zu stören.

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
- [[Elektrisches Feld]]
:::
:::vbox
**Verwandte Artikel**
- [[EMV Pre-Compliance]]
- [[Signalintegrität]]
:::
:::vbox
**Führt weiter zu**
- [[CE-Kennzeichnung & Konformitätserklärung]]
:::
:::

---

## Kopplungsmechanismen

Störungen gelangen auf vier Wegen von einer Quelle zum Empfänger:

### 1. Galvanische Kopplung
Direkte leitende Verbindung zwischen Störquelle und Empfänger. Typisch über gemeinsame Masseleiter oder Versorgungsleitungen.

**Gegenmassnahmen:** Entkoppelkondensatoren (100 nF direkt am IC), getrennte Masseführung, Ferritperlen.

### 2. Kapazitive Kopplung
Störspannung koppelt über parasitäre Kapazität zwischen Leitern ein. Nimmt mit Frequenz und Leitungsabstand zu.

**Gegenmassnahmen:** Abstand vergrössern, Schirmung (geerdeter Schirm fängt das E-Feld ab), Leitungen verdrillen.

### 3. Induktive Kopplung
Wechselndes Magnetfeld induziert Störspannung in benachbarte Schleifen (Lenz'sches Gesetz). Wirkt über gemeinsame Induktivität (Gegeninduktivität M).

**Gegenmassnahmen:** Schleifflächen minimieren (Hin- und Rückleiter eng zusammenführen), Verdrillung, magnetische Schirmung (µ-Metall).

### 4. Strahlungskopplung
Elektromagnetische Wellen strahlen Energie in Leitungen und Gehäuse ein (oder werden von ihnen abgestrahlt). Relevant ab ca. 30 MHz.

**Gegenmassnahmen:** Metallgehäuse, Kabelschirmung, Filterung an Gehäusedurchführungen.

## Abschirmung — Faradayscher Käfig & Materialwahl

Ein **Faradayscher Käfig** ist eine geschlossene, elektrisch leitfähige Hülle, die das Innere vor äusseren elektromagnetischen Feldern abschirmt (und umgekehrt verhindert, dass innen erzeugte Felder nach aussen dringen). Jedes durchgehend leitfähige Metallgehäuse wirkt als Faradayscher Käfig — Lüftungsschlitze, Displayausschnitte und Kabeldurchführungen sind Schwachstellen und müssen zusätzlich gefiltert oder mit Dichtungen/Blenden versehen werden.

**Nicht jedes Material schirmt gleich gut — und gegen dieselbe Störung:**

| Material | Wirkprinzip | Schirmt wirksam gegen |
|---|---|---|
| Aluminium, Kupfer (gut leitfähig) | Wirbelströme im Metall bauen das eindringende Feld ab | Elektrische Felder & hochfrequente Wechselfelder (klassischer Faradayscher Käfig) |
| Eisen-Nickel-Legierung / **µ-Metall** (sehr hohes mu_r) | Feldlinien werden vom hochpermeablen Material "aufgesaugt" und um das Innere herumgeleitet | Niederfrequente Magnetfelder — genau dort, wo Aluminium kaum wirkt |
| Kunststoffe (Polyethylen, ABS, …) | Nichtleitend: keine Wirbelströme, kein magnetischer Pfad | **Nichts** — Kunststoffgehäuse bieten keinerlei Feldabschirmung |

:::tip
**Schirmung ≠ Filterung.** Ein Eingangsfilter (X-/Y-Kondensatoren, Gleichtaktdrossel, siehe unten) bekämpft **leitungsgebundene** Störungen auf den Versorgungsleitungen — er schützt das Gerät aber nicht vor von aussen einwirkenden elektromagnetischen Wechselfeldern. Gegen Felder hilft nur eine geschlossene, passend gewählte leitfähige bzw. hochpermeable Hülle (Schirmung/Faradayscher Käfig). Beides sind unabhängige EMV-Massnahmen gegen unterschiedliche Kopplungsmechanismen (→ oben: kapazitive/induktive/Strahlungskopplung vs. galvanische Kopplung).
:::

## Gleichtakt- und Gegentaktstörungen

| Art | Beschreibung | Gegenmassnahme |
|---|---|---|
| Gegentakt (DM) | Störung zwischen Hin- und Rückleiter | X-Kondensatoren, Gegentaktdrossel |
| Gleichtakt (CM) | Störung beider Leiter gegen Masse | Y-Kondensatoren, Gleichtaktdrossel (Common Mode Choke) |

## Netzfilter

Ein Netzfilter am Geräteeingang schützt vor Netzstörungen und verhindert, dass das Gerät selbst stört.

Typischer Aufbau:
- **X-Kondensatoren** (zwischen L und N): dämpfen Gegentaktstörungen
- **Y-Kondensatoren** (L/N gegen PE): dämpfen Gleichtaktstörungen
- **Common Mode Choke**: Drossel die Gleichtaktstörungen sperrt, Nutzsignal ungehindert lässt

:::warning
Y-Kondensatoren erzeugen einen Ableitstrom gegen PE. Bei medizinischen Geräten und IT-Schutzisolierten Netzen sind die zulässigen Ableitströme begrenzt.
:::

## EMV-Tests (nach EN 61000)

| Test | Kürzel | Beschreibung |
|---|---|---|
| Elektrostatische Entladung | ESD | Simuliert Entladung einer Person (2–8 kV) |
| Schnelle Transienten | Burst | Kurze Impulsketten auf Versorgung/Signalleitungen |
| Stossspannung | Surge | Langsame hochenergetische Spannungsspitzen (Blitzableitung) |
| HF-Einstrahlung | RS | Eingestrahltes HF-Feld von 80 MHz bis 1 GHz |
| Leitungsgebundene Störaussendung | CE | Störungen die über Leitungen abgegeben werden |
| Abgestrahlte Störaussendung | RE | Abstrahlung gemessen in der Antennenmesshalle |

## CE-Kennzeichnung und EMV

Jedes Gerät das in der EU verkauft wird, muss die EMV-Richtlinie (2014/30/EU) erfüllen. Der Hersteller erklärt die Konformität selbst (DoC). Vor der Zertifizierung empfiehlt sich eine **Pre-Compliance-Messung** im eigenen Labor.

Mehr dazu unter [[EMV Pre-Compliance]] und [[CE-Kennzeichnung & Konformitätserklärung]].
