---
title: Lötverfahren im Vergleich
kategorie: FT
tags: [reflowlöten, wellenlöten, selektivlöten, SMD, THT, lotpaste, lötprozess, temperaturprofil, flux, schablone, reflow-ofen]
symbol: —
einheit: —
---

In der Serienfertigung werden drei Hauptverfahren eingesetzt: Reflowlöten für SMD, Wellenlöten für THT und Selektivlöten für Mischbaugruppen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Weichlöten]]
- [[SMD vs. THT]]
:::
:::vbox
**Verwandte Artikel**
- [[Bleifreies Lot]]
- [[Fehlerbilder Löten]]
- [[IPC-Kriterien]]
:::
:::

---

## Reflowlöten

**Einsatz**: SMD-Bauteile auf Leiterplatten.

**Ablauf**:
1. Lotpaste wird per Schablone (Stencil) auf die Pads aufgedruckt
2. Bauteile werden mit Bestückungsautomat platziert (die Paste hält sie)
3. Leiterplatte fährt durch einen Reflow-Ofen mit definiertem Temperaturprofil
4. Lot schmilzt, benetzt Pads und Anschlüsse, kühlt zu Verbindungen aus

**Temperaturprofil** (bleifrei):
- Vorheizzone: 150–180 °C (Lösungsmittel verdampfen, Flux aktiviert)
- Soakzone: 180 °C (Temperatur angleichen)
- Reflow-Zone: 235–260 °C (Lot schmilzt, Peak typisch 250 °C)
- Kühlzone: Kontrolliert abkühlen, nicht zu schnell

**Vorteile**: Hohe Bestückdichte, beidseitige Bestückung möglich, reproduzierbar, automatisierbar.

**Nachteile**: Empfindliche Bauteile können durch Temperaturen beschädigt werden. Profil muss für jede Baugruppe angepasst werden.

## Wellenlöten

**Einsatz**: THT-Bauteile (bedrahtete Bauelemente), einseitige SMD-Bestückung auf der Unterseite.

**Ablauf**:
1. Leiterplatte wird von oben mit THT-Bauteilen bestückt
2. Unterseite wird mit Flux besprüht
3. Leiterplatte fährt über eine stehende Lotwelle (flüssiges Lot, 260–270 °C)
4. Die Welle benetzt Pins und Pads gleichzeitig

**Vorteile**: Schnell für viele THT-Bauteile gleichzeitig, kostengünstig bei grossen Stückzahlen.

**Nachteile**: Schatten-Effekt (hinter grossen Bauteilen bleibt Lot aus). Nicht geeignet für SMD-Bauteile auf der Unterseite (ausser geklebte SMDs). Lot kann unter IC-Sockel kriechen.

:::warning
Beim Wellenlöten darf keine Lotpaste verwendet werden. SMD-Bauteile auf der Wellenunterseite müssen mit Klebstoff fixiert werden.
:::

## Selektivlöten

**Einsatz**: Gemischte Baugruppen (SMD + THT), wenn Wellenlöten nicht geht.

**Ablauf**:
1. SMD-Seite bereits reflowgelötet
2. Einzelne THT-Punkte werden gezielt mit einer kleinen Lotwelle oder Lötdüse angelötet
3. CNC-gesteuert, nur ausgewählte Stellen werden benetzt

**Vorteile**: Thermisch empfindliche SMD-Bauteile auf der Unterseite werden nicht beschädigt. Flexibel für kleine Stückzahlen und komplexe Mischbaugruppen.

**Nachteile**: Langsam, teuer, Programmiertaufwand.

## Vergleich

| Merkmal | Reflowlöten | Wellenlöten | Selektivlöten |
|---|---|---|---|
| Bauteiltyp | SMD | THT | THT auf Mischbaugruppe |
| Durchsatz | Hoch | Sehr hoch | Niedrig |
| Kosten | Mittel | Niedrig | Hoch |
| Flexibilität | Mittel | Niedrig | Hoch |
| Typische Anwendung | Serienproduktion SMD | Serienproduktion THT | Prototypen, Mischbaugruppen |

## Handbetrieb

Für Prototypen, Reparaturen und Einzelstücke wird von Hand gelötet (Lötkolben). Für SMD-Rework werden Heissluft-Stationen und Lötpasten-Spritzen eingesetzt.
