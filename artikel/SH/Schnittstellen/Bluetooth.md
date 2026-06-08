---
title: Bluetooth
kategorie: SH
kapitel: Schnittstellen
tags: [bluetooth, funktechnik, pairing, profile, bluetooth low energy]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Serielle Datenübertragung (Grundlagen)]]
:::
:::

---

Alle bisher behandelten Schnittstellen — UART, SPI, I2C, RS232/485, CAN-Bus — haben eines gemeinsam: Sie übertragen ihre Daten über **Kabel**. Doch immer mehr Geräte sollen sich kabellos verbinden — Kopfhörer, Tastaturen, Fitness-Tracker, Sensoren. Eine der bekanntesten und am weitesten verbreiteten Funktechnologien für genau diesen Nahbereich ist **Bluetooth**.

## Zwei Welten unter demselben Namen

:::merke
Hinter dem Namen "Bluetooth" verbergen sich heute eigentlich **zwei unterschiedliche Technologien**:

- **Bluetooth Classic**: für Anwendungen mit kontinuierlichem, eher hohem Datendurchsatz — etwa Audio-Streaming zu Kopfhörern oder Lautsprechern. Reichweite etwa 10 m.
- **Bluetooth Low Energy (BLE)**: speziell für batteriebetriebene Geräte entwickelt, die nur gelegentlich kleine Datenmengen übertragen — etwa Sensoren, Fitness-Tracker oder Smart-Home-Geräte. Der Name ist Programm: extrem **niedriger Energieverbrauch**, dafür geringerer Datendurchsatz. Reichweite ähnlich, bei manchen Anwendungen bis etwa 100 m, mit Bluetooth 5 sogar deutlich mehr.

Für die allermeisten modernen IoT- und Mikrocontroller-Projekte ist heute BLE die relevantere der beiden Varianten — kein Wunder, dass praktisch jeder aktuelle Smartphone- und Mikrocontroller-Chip BLE-fähig ist.
:::

## Die Architektur von BLE: GAP und GATT

:::tip
Die Funktionsweise von BLE lässt sich anhand zweier zentraler Konzepte verstehen:

- **GAP (Generic Access Profile)** regelt, *wie* sich Geräte überhaupt finden und verbinden. Ein Gerät kann dabei als **Peripheral** (sendet "Advertising"-Pakete, in denen es seine Anwesenheit bekannt gibt — etwa ein Sensor) oder als **Central** (durchsucht aktiv die Umgebung nach solchen Advertising-Paketen — etwa ein Smartphone) auftreten.
- **GATT (Generic Attribute Profile)** regelt, *wie* nach erfolgter Verbindung Daten ausgetauscht werden. Die Daten werden dabei in **Services** (thematische Gruppen, z. B. "Herzfrequenz-Service") und darin enthaltene **Characteristics** (einzelne Datenwerte, z. B. der aktuelle Herzfrequenz-Messwert) organisiert — ein bisschen wie ein strukturiertes Inhaltsverzeichnis, durch das sich ein Central-Gerät "durchblättern" kann.

Dieses **Advertising** ist der erste Schritt jeder BLE-Verbindung: Ein Peripheral sendet in regelmässigen Abständen kleine Pakete aus, die seinen Namen, seine Fähigkeiten (Services) und weitere Kennungen enthalten — sichtbar für jedes in der Nähe lauschende Central-Gerät.
:::

## Pairing: zwei Geräte lernen sich kennen

Bevor zwei Geräte regelmässig und sicher miteinander kommunizieren können, müssen sie sich **koppeln (pairen)**. Dabei tauschen sie Sicherheitsschlüssel aus, mit denen die nachfolgende Kommunikation verschlüsselt werden kann — wichtig etwa bei sensiblen Daten wie Gesundheitswerten oder Zugangscodes. Einmal gekoppelt, "erinnern" sich die Geräte in der Regel aneinander und verbinden sich bei künftigen Begegnungen automatisch wieder.

## Verbreitete Module für eigene Projekte

:::info
Für eigene Mikrocontroller-Projekte gibt es zahlreiche fertige Bluetooth-Module, die sich unkompliziert über → [[UART|UART]] oder direkt über eine integrierte Funkschnittstelle ansteuern lassen:

| Modul | Variante | Bemerkung |
|---|---|---|
| HC-05 / HC-06 | Bluetooth Classic | Klassiker für UART-Funkbrücken, sehr verbreitet und günstig |
| HM-10 | BLE | Einfache BLE-Anbindung über AT-Befehle |
| nRF52840 | BLE (System-on-Chip) | Leistungsfähiger BLE-Chip mit eigenem ARM-Cortex-Kern, oft direkt als Mikrocontroller einsetzbar |

Solche Module übersetzen die komplexe Funkkommunikation nach aussen oft auf eine simple serielle UART-Schnittstelle — ein Mikrocontroller "sieht" dann nur ein gewohntes serielles Interface, während das Modul im Hintergrund die gesamte Funktechnik abwickelt.
:::

## Grenzen von Bluetooth

:::warning
So praktisch Bluetooth auch ist — es hat klare Grenzen: Die Reichweite bleibt auf den **Nahbereich** beschränkt (typischerweise 10 bis 100 m, in Innenräumen oft deutlich weniger durch Wände und Störungen), und die Anzahl gleichzeitig verbundener Geräte ist begrenzt. Für Anwendungen, die grössere Reichweiten überbrücken müssen — etwa Sensoren, die über ein ganzes Stadtgebiet oder eine grosse Industrieanlage verteilt sind — braucht es andere Funktechnologien. Eine davon, die speziell für solche Langstrecken-Anwendungen mit geringem Datenaufkommen entwickelt wurde, lernen wir im nächsten Artikel kennen: → [[LoRaWAN|LoRaWAN]].
:::
