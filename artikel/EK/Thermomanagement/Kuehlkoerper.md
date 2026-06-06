---
title: Kühlkörper
kategorie: EK
kapitel: Thermomanagement
tags: [kühlkörper, wärmeleitpaste, r_thk, derating, naturkonvektion, zwangsbelüftung, to-220, wärmepad, thermisches design, heatsink]
groessen: R_thK|Wärmewiderstand Kühlkörper|K/W; theta_K|Kühlkörpertemperatur|°C; P_v|Verlustleistung|W; theta_U|Umgebungstemperatur|°C
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Wärmewiderstand]]
:::
:::vbox
**Verwandte Artikel**
- [[Spannungsstabilisierung]]
- [[MOSFET Anwendungen]]
:::
:::vbox
**Führt weiter zu**
- [[Sensorik Grundlagen]]
:::
:::

---

Ein Kühlkörper vergrössert die Oberfläche des Bauteils und senkt damit den Wärmewiderstand zur Umgebungsluft. Er ist nötig, wenn ein Bauteil mehr Verlustleistung erzeugt als es ohne zusätzliche Kühlung dauerhaft abführen kann.

## Wann braucht es einen Kühlkörper?

Ohne Kühlkörper muss das Gehäuse die gesamte Wärme direkt an die Luft abgeben. Der Wärmewiderstand Gehäuse–Luft (R_thJA, Junction-to-Ambient) ist im Datenblatt angegeben.

:::formel
P_v_max_ohne = (theta_J_max - theta_U) / R_thJA    # max. Verlustleistung ohne Kühlkörper
:::

Ist die tatsächliche P_v grösser → Kühlkörper erforderlich.

:::monospace
Beispiel TO-220: R_thJA = 62 K/W, T_j_max = 150 °C, T_U = 25 °C
P_v_max_ohne = (150-25) / 62 = 2 W

→ Bei mehr als 2 W Verlustleistung ist ein Kühlkörper nötig.
:::

## Kühlkörper dimensionieren

Aus dem Gesamtwiderstand der Kühlkette ergibt sich der nötige R_thK:

:::formel
R_thK = (theta_J_max - theta_U) / P_v - R_thG - R_thü    # aus Wärmewiderstand-Artikel
:::

Den Kühlkörper mit R_thK **kleiner oder gleich** dem berechneten Wert wählen.

## Übergangs­widerstand R_thü (Gehäuse–Kühlkörper)

Zwischen Gehäuse und Kühlkörper entsteht ein thermischer Übergangs­widerstand durch Luftspalte in der Oberflächen­rauheit. Wärmeleitpaste oder Wärmeleitpad füllen diese Spalte:

| Montage | R_thü typisch |
|---|---|
| Trocken (ohne Paste) | 1–3 K/W |
| Mit Wärmeleitpaste (Silikon-basiert) | 0.2–0.5 K/W |
| Mit Wärmeleitpad (Folie) | 0.5–1.5 K/W (je nach Dicke) |
| Direkte Lotverbindung (SMD) | < 0.1 K/W |

:::tip
Wärmeleitpaste dünn und gleichmässig auftragen (0.1–0.2 mm). Zu viel Paste verschlechtert die Wärmeleitung — Paste leitet besser als Luft, aber schlechter als Metall.
:::

## Isolierende Montage (elektrische Trennung)

Viele Leistungsbauteile haben ein elektrisch leitendes Gehäuse (z. B. MOSFET-Drain am TO-220-Tab). Soll der Kühlkörper mit dem Gehäuse verbunden werden, aber elektrisch von der Schaltung getrennt bleiben:

| Methode | R_thü typisch | Isolationsspannung |
|---|---|---|
| Glimmerscheibe + Paste | 0.5–1.0 K/W | 500 V |
| Keramikscheibe + Paste | 0.2–0.5 K/W | 1–2 kV |
| Wärmeleitpad (isolierend) | 1.0–2.0 K/W | 2–5 kV |

:::warning
Immer mit Multimeter prüfen ob die Isolation tatsächlich vorhanden ist — ein vergessenes Isolierpad oder falscher Anzug der Befestigungsschraube (Schraube durch Gehäuse leitend) kann Kurzschlüsse verursachen.
:::

## Kühlkörpertypen

| Typ | R_thK Bereich | Anwendung |
|---|---|---|
| Kleiner Kühlkörper (TO-220) | 5–20 K/W | < 5 W, Spannungsregler |
| Mittelgrosser Profilkörper | 1–5 K/W | 5–20 W, Leistungsstufen |
| Grosser Kühlkörper | 0.3–1 K/W | > 20 W, Audioendstufen |
| Wasserkühlkörper | < 0.1 K/W | > 100 W, Servoinverter |
| Zwangsbelüftung (Lüfter) | Faktor 2–5 besser | Alle Grössen |

## Derating

Bauteile dürfen nicht dauerhaft bis T_j_max betrieben werden — thermische Alterung und Sicherheitsmarge erfordern einen Abstand:

:::formel
theta_J_Betrieb <= theta_J_max - 20    # Mindest-Derating 20 K (besser 30 K)
:::

Derating-Kurven im Datenblatt zeigen, ab welcher Gehäusetemperatur die maximale Verlustleistung reduziert werden muss.

## Vollständiges Auslegungsbeispiel

:::monospace
Aufgabe: MOSFET IRF540, P_v = 15 W, T_U = 40 °C (Industrie)
Datenblatt: R_thJC = 1.3 K/W, T_j_max = 150 °C

Derating: Ziel theta_J ≤ 130 °C (20 K Marge)

R_thK = (130 - 40) / 15 - 1.3 - 0.5 = 6.0 - 1.8 = 4.2 K/W

→ Kühlkörper mit R_thK ≤ 4.2 K/W wählen.
   z.B. Fischer SK-104 (ca. 3.5 K/W für TO-220)

Probe: theta_J = 40 + 15*(1.3+0.5+3.5) = 40 + 15*5.3 = 40+79.5 = 119.5 °C
       Abstand zu T_j_max: 150-119.5 = 30.5 K ✓
:::

:::info
Der Wärme­widerstand eines Kühlkörpers gilt für Naturkonvektion (stehende Luft). Mit einem Lüfter sinkt R_thK um Faktor 2–5 — der gleiche Kühlkörper kann dann mehr Verlustleistung abführen.
:::
