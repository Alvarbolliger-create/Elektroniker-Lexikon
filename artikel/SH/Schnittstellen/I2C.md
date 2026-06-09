---
title: I2C
kategorie: SH
kapitel: Schnittstellen
tags: [i2c, inter-integrated circuit, sda, scl, master slave, adressierung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Serielle Datenübertragung (Grundlagen)]]
:::
:::vbox
**Verwandte Artikel**
- [[SPI]]
- [[Protokoll-Decoder]]
- [[Logikanalysator]]
:::
:::

---

→ [[SPI|SPI]] erkauft sich seine hohe Geschwindigkeit mit Verdrahtungsaufwand: vier gemeinsame Leitungen plus eine eigene Chip-Select-Leitung pro Slave. Was aber, wenn ein gutes Dutzend Sensoren, Displays und Speicherbausteine an einem einzigen Mikrocontroller hängen sollen — und kaum noch freie Pins übrig sind? Genau für diese Situation wurde **I2C** (Inter-Integrated Circuit) entwickelt: eine Schnittstelle, die mit nur **zwei** Leitungen auskommt und dabei dutzende Teilnehmer gleichzeitig verwalten kann.

## Nur zwei Leitungen für den ganzen Bus

:::merke
I2C kommt mit nur zwei Leitungen aus: **SDA** (Serial Data, die eigentlichen Nutzdaten) und **SCL** (Serial Clock, der gemeinsame Takt). Beide Leitungen sind **bidirektional** und elektrisch als **Open-Drain** ausgeführt — das bedeutet, jeder angeschlossene Baustein kann die Leitung aktiv auf LOW ziehen, sie aber nicht aktiv auf HIGH treiben. Damit die Leitung im Ruhezustand trotzdem zuverlässig auf HIGH liegt, sind an beiden Leitungen **Pull-up-Widerstände** nach VCC zwingend erforderlich — typisch 4,7 kΩ bei 100 kHz oder 2,2 kΩ bei 400 kHz. Ohne diese Pull-ups funktioniert I2C grundsätzlich nicht!

Alle Teilnehmer — ob Sensor, Display oder Speicherbaustein — hängen elektrisch **parallel** an denselben zwei Leitungen. Was sie unterscheidet, ist nicht die Verdrahtung, sondern eine eindeutige **Adresse**.
:::

## Adressierung: wie der Master den richtigen Teilnehmer findet

:::tip
Jeder Slave besitzt eine eindeutige **7-Bit-Adresse** (Wertebereich 0x00 bis 0x7F, also bis zu 127 mögliche Adressen). Der Master schickt diese Adresse zu Beginn jeder Transaktion auf den Bus — und nur der angesprochene Slave antwortet, alle anderen bleiben "stumm". Manche Adressbereiche sind für Sonderzwecke reserviert; viele ICs erlauben zudem, die eigene Adresse über zusätzliche Adress-Pins frei zu konfigurieren — so können sogar mehrere baugleiche Bausteine gleichzeitig am selben Bus betrieben werden, ohne sich gegenseitig zu stören.
:::

## Der Übertragungsablauf: Schritt für Schritt

Eine vollständige I2C-Transaktion folgt einem festen Muster, das stark an das im Artikel → [[Serielle Datenübertragung (Grundlagen)|Grundlagen der seriellen Datenübertragung]] beschriebene Schema mit Steuerzeichen und Bestätigung erinnert:

1. **Start-Condition**: SDA fällt von HIGH auf LOW, während SCL noch HIGH ist — das Signal für "jetzt beginnt eine Übertragung"
2. **7-Bit-Adresse + R/W-Bit**: Welcher Slave wird angesprochen, und soll gelesen oder geschrieben werden?
3. **ACK** (Acknowledge) vom angesprochenen Slave — die Bestätigung "ich bin da und habe verstanden"
4. **Datenbytes**, jeweils mit eigenem ACK quittiert
5. **Stop-Condition**: Die Übertragung wird sauber beendet

## Geschwindigkeit: bewusst langsamer, dafür schlanker

:::info
I2C kennt mehrere genormte Geschwindigkeitsstufen: **Standard Mode** mit 100 kBit/s, **Fast Mode** mit 400 kBit/s, **Fast-Plus** mit 1 MBit/s und — eher selten anzutreffen — **High-Speed Mode** mit bis zu 3,4 MBit/s. Das ist deutlich langsamer als SPI — ein bewusster Kompromiss: I2C tauscht Geschwindigkeit gegen die Möglichkeit, mit nur zwei Leitungen sehr viele Teilnehmer gleichzeitig zu verwalten und sauber zu adressieren.
:::

## Stolperstein Pull-up-Dimensionierung und Adresskonflikte

:::warning
Die Wahl der Pull-up-Widerstände ist ein Balanceakt: **Zu grosse** Widerstände lassen die Signalflanken so langsam ansteigen, dass die Kommunikation bei hohen Taktfrequenzen schlicht versagt; **zu kleine** Widerstände führen zu unnötig hohem Stromverbrauch (wenn auch zu saubereren, schnelleren Flanken).

Eine zweite, oft unterschätzte Fehlerquelle sind **Adresskonflikte**: Besitzen zwei Slaves dieselbe 7-Bit-Adresse, antworten beide gleichzeitig auf eine Anfrage — ihre Signale kollidieren auf dem Bus, und die Kommunikation schlägt komplett fehl. Vor der Inbetriebnahme eines I2C-Systems lohnt es sich deshalb immer, die Adressen sämtlicher Busteilnehmer sorgfältig zu prüfen — insbesondere, wenn mehrere baugleiche Module zum Einsatz kommen.
:::

## Das grosse Bild: drei Schnittstellen, drei Philosophien

Mit UART, SPI und I2C haben wir nun drei grundverschiedene Lösungsansätze für serielle Kommunikation kennengelernt: UART als denkbar einfachste Punkt-zu-Punkt-Verbindung, SPI als Geschwindigkeits-Champion mit grossem Verdrahtungsaufwand, und I2C als sparsamste Lösung für viele Teilnehmer an wenigen Leitungen. Welche Schnittstelle die richtige ist, hängt immer von der konkreten Anwendung ab — von der benötigten Geschwindigkeit, der Anzahl Teilnehmer und der verfügbaren Anzahl Pins. Wie sich diese Mikrocontroller-internen Schnittstellen zu den klassischen, oft über grössere Distanzen reichenden Industrie-Standards wie → [[RS232 & RS485|RS232 und RS485]] verhalten, zeigt der nächste Abschnitt des Kapitels.
