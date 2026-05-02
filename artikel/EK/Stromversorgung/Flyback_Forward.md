---
title: Flyback- & Forward-Converter
kategorie: EK
tags: [Flyback, Forward, Sperrwandler, Durchflusswandler, galvanische Trennung, Schaltnetzteil]
symbol: —
einheit: —
---

Flyback und Forward sind die häufigsten isolierten Schaltnetzteil-Topologien. Beide haben galvanische Trennung durch einen Übertrager, unterscheiden sich aber fundamental in der Energiespeicherung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Buck (Step-down)]]
- [[Boost (Step-up)]]
- [[Transformator Aufbau]]
:::
:::vbox
**Verwandte Artikel**
- [[Transformator Typen]]
- [[PWM Arten]]
- [[Wirkungsgrad und Verluste]]
:::
:::vbox
**Führt weiter zu**
- [[Soft-Switching (ZVS/ZCS)]]
- [[Aktive PFC]]
:::
:::

---

## Sperrwandler (Flyback)

### Funktionsprinzip

Der Flyback-Übertrager ist kein gewöhnlicher Transformator — er ist eine gekoppelte Drossel. Energie wird während der Einschaltphase im Kern gespeichert und während der Ausschaltphase an die Sekundärseite abgegeben.

**Einschaltphase** (Transistor leitet):
- Strom fliesst durch die Primärwicklung, Energie wird im Kern gespeichert
- Sekundärdiode sperrt (Wicklungspolung gegensätzlich)
- Kein Energietransfer in dieser Phase

**Ausschaltphase** (Transistor sperrt):
- Magnetfeld bricht zusammen, Spannung kehrt um
- Sekundärdiode leitet, Energie wird an den Ausgang abgegeben

### Vorteile Flyback

- Einfachste isolierte Topologie (ein Transistor, ein Übertrager, eine Diode)
- Mehrere Ausgänge einfach durch weitere Wicklungen
- Auch für sehr kleine Leistungen (< 5 W) geeignet
- Galvanische Trennung ohne Drossel auf der Sekundärseite

### Nachteile Flyback

- Übertrager muss Energie speichern → Luftspalt nötig → grosser Kern
- Höhere Spannungsbelastung auf dem Transistor (UCE_max = UIN + n × UOUT)
- Schlechterer Wirkungsgrad als Forward bei grossen Leistungen
- EMV schwieriger (durch diskontinuierlichen Energiefluss)

**Typischer Einsatz**: 1–200 W, USB-Netzteile, Laptopnetzteile, Hilfsspannungsversorgungen.

## Durchflusswandler (Forward-Converter)

### Funktionsprinzip

Der Forward-Converter überträgt Energie direkt während der Einschaltphase (wie ein Transformator). Auf der Sekundärseite ist eine Drossel nötig.

**Einschaltphase** (Transistor leitet):
- Energie wird direkt vom Eingang auf den Ausgang übertragen
- Sekundärseitige Drossel speichert den Rest
- Kern wird magnetisiert

**Ausschaltphase** (Transistor sperrt):
- Sekundärseitige Drossel liefert weiter Strom (Freilaufdiode)
- Kern muss entmagnetisiert werden (Rücksetzwicklung oder aktive Schaltung)

### Vorteile Forward

- Geringere Transistorbelastung als Flyback
- Besserer Wirkungsgrad bei mittleren und grossen Leistungen
- Geringeres Rauschen durch gleichmässigeren Energiefluss

### Nachteile Forward

- Rücksetzschaltung nötig (komplexer)
- Sekundärseitige Drossel nötig
- Schlechter bei sehr kleinen Leistungen

**Typischer Einsatz**: 100 W – 1 kW, industrielle Netzteile, Server-Netzteile.

## Vergleich

| Merkmal | Flyback | Forward |
|---|---|---|
| Energiespeicherung | Im Übertrager | In der sekundären Drossel |
| Galvanische Trennung | Ja | Ja |
| Minimalleistung | Sehr gut (< 1 W) | Schlecht |
| Leistungsbereich | 1–200 W | 100–1000 W |
| Transistorspannung | Hoch (> 2 × UIN) | Niedriger |
| Schaltungsaufwand | Gering | Mittel |
| Wirkungsgrad 100 W | 85–88 % | 88–92 % |
