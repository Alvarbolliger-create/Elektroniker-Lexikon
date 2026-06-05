---
title: Kondensator Typen
kategorie: ET
tags: [kondensator, elko, keramik, folie, typen, bauformen, ESR, ESL, tantalkondensator, MKP, NP0, X5R, Y5V]
symbol: C
einheit: F
---

Kondensatoren gibt es in vielen Ausführungen. Jeder Typ hat andere Stärken. Die Wahl des falschen Typs kann eine Schaltung zum Problem machen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Kapazität & Einheiten]]
:::
:::vbox
**Verwandte Artikel**
- [[Auf- und Entladung]]
:::
:::vbox
**Führt weiter zu**
- [[Bauteilauswahl]]
:::
:::

---

## ESR — Equivalent Series Resistance

Jeder reale Kondensator hat einen parasitären Serienwiderstand (ESR). Bei hohen Wechselströmen erzeugt er Wärme und begrenzt die Effizienz. In Schaltnetzteilen beeinflusst der ESR direkt die Restwelligkeit der Ausgangsspannung:

:::formel
U_ripple = I_ripple * ESR
:::
Niedrig-ESR-Kondensatoren sind in Netzteilen und DC/DC-Wandlern Pflicht. Im Datenblatt unter "ESR" oder "Impedanz bei 100 kHz" zu finden.

---

## Elektrolytkondensator (Elko)

Dünnes Aluminiumoxid als Dielektrikum, als Folie aufgewickelt. Grosse Kapazität auf kleinem Raum.

Polarisiert: muss mit der richtigen Polung eingebaut werden. Falsche Polung zerstört ihn, manchmal explosionsartig.

**Polungsmarkierungen THT:** Minus-Pol am Gehäuse markiert (Balken, Pfeil oder Ring). Das Minus-Pin ist kürzer.

**Polungsmarkierungen SMD (Al-Elko):** Plus-Markierung links auf der Oberseite.

**Achtung Tantal SMD:** Plus-Markierung ist ebenfalls links — aber die Markierungsrichtung kann je nach Hersteller variieren. Datenblatt prüfen.

:::warning
Falsch gepolte Elkos und Tantalkondensatoren können explodieren oder sich entzünden. Polarität immer vor dem Einbau prüfen.
:::

Typisch für Siebung in Netzteilen und grosse Pufferkondensatoren.

:::warning
Elkos altern. Nach 10 bis 20 Jahren sinkt die Kapazität und der ESR steigt. In alten Geräten oft die Ursache für Probleme.
:::

## Keramikkondensator (MLCC)

Kleine kompakte Bauform, unpolarisiert, sehr schnell. Typisch als 100 nF Bypass direkt am IC.

Achtung: C0G/NP0 ist stabil über Temperatur und Spannung. X7R und Y5V haben starke Kapazitätsänderungen bei Gleichspannung. Ein X7R mit 10 µF kann bei 5 V Vorspannung nur noch 5 µF haben.

## Folienkondensator

Kunststofffolie als Dielektrikum. Stabil, langlebig, kein Kapazitätsverlust durch Spannung. Typisch für Audio, Filter und Präzisionsanwendungen.

**Selbstheilung**: Bei einem lokalen Spannungsdurchschlag verdampft die metallisierte Schicht an der Fehlstelle und isoliert sie. Der Kondensator überlebt den Durchschlag und bleibt funktionsfähig — im Gegensatz zu Keramik- oder Elektrolytkondensatoren.

Grösser als Keramik, kleinere Kapazitäten als Elko.

## Tantalkondensator

Kompakt wie Elko, stabiler, aber teurer und empfindlicher gegen Verpolung und Überspannung. Explodiert bei Überlastung. In der Industrie häufig, in Hobbyprojekten selten.

## Superkondensator (Goldcap)

Sehr grosse Kapazität (Farad-Bereich) bei tiefer Spannung (2 bis 3 V). Für kurze Pufferung bei Stromausfall oder als Energiespeicher in kleinen Geräten.

## Glimmerkondensator

Glimmer (Mica) als Dielektrikum. Sehr stabil, präzise, hochfrequenztauglich. Teuer und nur in kleinen Kapazitäten (pF-Bereich). Für HF-Filter und Präzisionsoszillatoren.

## Variable Kondensatoren

**Drehkondensator:** Kapazität durch mechanisches Verdrehen einstellbar. Klassisch in Radioempfängern zur Senderabstimmung.

**Trimmkondensator:** Kleiner einstellbarer Kondensator, einmalig justiert (mit Schraubenzieher). Für Frequenzabgleich in HF-Schaltungen.

## Vergleich

| Typ | Kapazität | Polarisiert | Spannung | ESR | Stärke |
|---|---|---|---|---|---|
| Elko | 1 µF bis 100 mF | ja | bis 450 V | mittel–hoch | Grosse Kapazität |
| Keramik | 1 pF bis 100 µF | nein | bis 50 V | sehr niedrig | Klein, schnell |
| Folie | 1 nF bis 100 µF | nein | bis 600 V | niedrig | Stabil, selbstheilend |
| Tantal | 0.1 µF bis 1 mF | ja | bis 35 V | niedrig | Kompakt |
| Supercap | 0.1 F bis 100 F | ja | bis 5 V | mittel | Energie puffern |
