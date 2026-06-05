---
title: Transformator Typen
kategorie: ET
tags: [transformator, typen, netztransformator, trenntransformator, spar, ringkern, schaltnetzteil, messwandler]
_status: PORT  # ET_alt/Transformator/Transformator_Typen.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Transformator Aufbau]]
:::
:::

---

Transformatoren gibt es in vielen Ausführungen — jede für bestimmte Anwendungen optimiert. Die wichtigsten Typen für das EFZ sind Netz-, Trenn-, Spar- und Messwandler.

:::schematic
/abbildungen/transformator/transformator_typen_uebersicht.svg
:::

## Netztransformator

Wandelt die Netzspannung (230 V / 400 V, 50 Hz) in die benötigte Betriebsspannung um. Standardbauweise mit Trafoblech-Kern (E/I oder M-Kern). Wirkungsgrad 95–99 %.

**Typische Anwendungen:** Netzteile, Klingeltrafo (230 V → 8–12 V), Schweisstrafo.

:::schematic
/abbildungen/transformator/netztransformator_kern.svg
:::

## Trenntransformator

Übersetzungsverhältnis 1:1 — keine Spannungsänderung, aber galvanische Trennung zwischen Primär- und Sekundärseite. Erhöhte Sicherheit, da kein Direktkontakt mit dem Netz möglich ist.

**Anwendungen:** Medizinische Geräte, Werkstatt-Schutztrafo, Prüfstände, EMV-Isolation.

:::schematic
/abbildungen/transformator/trenntransformator_schaltplan.svg
:::

:::tip
Im Betrieb an einem Trenntransformator ist Berühren eines Leiters weniger gefährlich — der Körper bildet keinen Stromkreis zur Erde, weil die Sekundärseite nicht geerdet ist. Trotzdem gilt: Beide Leiter gleichzeitig anfassen → Stromschlag!
:::

## Spartransformator (Autotransformator)

Primär- und Sekundärwicklung sind nicht getrennt, sondern teilen sich eine gemeinsame Wicklung. Nur der "Differenzstrom" (zwischen Übersetzungsverhältnis und 1:1) fliesst durch den nichtteilbaren Wicklungsabschnitt.

**Vorteil:** Kleiner, leichter, günstiger als Trenntransformator bei ähnlicher Leistung.

**Nachteil:** Keine galvanische Trennung — bei Kurzschluss der Primärwicklung erscheint die volle Netzspannung auf der Sekundärseite.

**Anwendungen:** Stelltransformator (regelbar), Spannungsanpassung, Motoranlasser.

:::schematic
/abbildungen/transformator/spartransformator_schaltplan.svg
:::

## Messwandler

**Stromwandler (CT):** Übersetzt grosse Ströme (kA) auf messbare Werte (5 A oder 1 A). Der Primär-"Leiter" ist oft der zu messende Hauptleiter selbst (eine Windung). Sekundärseite darf **nie offen** sein — ohne Last entstehen gefährlich hohe Spannungen.

**Spannungswandler (VT):** Übersetzt hohe Spannungen (kV) auf sichere Messpegel (100 V). Ermöglicht Messung von Mittel- und Hochspannungsnetzen mit normalen Messgeräten.

:::warning
Stromwandler niemals mit offenem Sekundärkreis betreiben! Die gesamte Magnetisierungsenergie wird dann in eine hohe Impulsspannung umgesetzt — Lebensgefahr und Zerstörung des Wandlers.
:::

## Ringkerntransformator

Wicklungen auf einem ringförmigen Kern. Sehr kleiner Streufluss, hervorragende EMV-Eigenschaften, leiser Betrieb (kein Brummen). Teurer in der Herstellung, aber besonders für Audio- und Messgeräte beliebt.

## Hochfrequenztransformator (Schaltnetzteil)

In Schaltnetzteilen wird der Netzstrom zunächst gleichgerichtet, dann mit typisch 50–500 kHz geschaltet. Bei diesen hohen Frequenzen kann ein sehr kleiner Ferritkern dieselbe Leistung übertragen wie ein grosser Eisenkern bei 50 Hz.

**Vorteil:** Sehr kompakt und leicht (Smartphone-Ladegerät statt grossem Trafo).

**Nachteil:** Komplexere Schaltung, potenzielle EMV-Probleme durch die schnellen Schaltvorgänge.
