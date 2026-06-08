---
title: Digitale Codes (BCD, Gray, Hamming, ASCII)
kategorie: SH
kapitel: Grundlagen
tags: [bcd-code, gray-code, glixoncode, hamming-code, ascii, unicode, utf-8, fehlerkorrektur, fehlererkennung, dual-ergaenzter-code]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Zahlensysteme (Dual, Hexadezimal)]]
:::
:::vbox
**Verwandte Artikel**
- [[Code-Wandler (BCD-zu-7-Segment)]]
:::
:::vbox
**Führt weiter zu**
- [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)]]
:::
:::

---

Ein **Code** ist eine feste Zuordnungsvorschrift zwischen Information (Zahlen, Buchstaben, Sonderzeichen) und ihrer binären Darstellung. Je nach Anwendung — Anzeigen, Messen, Übertragen, Texte verarbeiten — kommen ganz unterschiedliche Codes zum Einsatz, die jeweils eine bestimmte Eigenschaft optimieren.

## BCD-Code — dezimale Ziffern binär darstellen

Der **BCD-Code** (*Binary Coded Decimal*, auch 8-4-2-1-Code) codiert jede Dezimalziffer (0…9) einzeln mit 4 Bit (einer **Tetrade**). Eine mehrstellige Dezimalzahl wird Tetrade für Tetrade dargestellt — z. B. 1978 als 0001 1001 0111 1000.

:::merke
Die Bitkombinationen 1010…1111 (10…15) werden im BCD-Code nicht verwendet — man nennt sie **Pseudotetraden**. Das macht den BCD-Code "verschwenderisch", aber sehr einfach auf 7-Segment-Anzeigen umzusetzen. → [[Code-Wandler (BCD-zu-7-Segment)]]
:::

## Gray-Code — nur ein Bit ändert sich

Beim **Gray-Code** unterscheiden sich zwei aufeinanderfolgende Werte immer in genau **einem** Bit. Das macht ihn **ablesesicher**: Wird eine Sensorzeile beim Übergang zwischen zwei Werten leicht schräg abgetastet, entsteht beim Gray-Code höchstens ein Fehler von ±1 — beim normalen Binärcode kann dagegen sogar das MSB kippen, was den abgelesenen Wert um die Hälfte des gesamten Messbereichs verfälscht.

| Dezimal | Binärcode | Gray-Code |
|---|---|---|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |

:::tip
Umrechnung Binär → Gray: Jedes Bit wird mit dem direkt links daneben stehenden Binärbit per EXOR verknüpft (das MSB bleibt unverändert). Umgekehrt (Gray → Binär) wird stufenweise von links nach rechts EXOR-verknüpft.
:::

**Anwendung**: Codierung von Dreh- und Längenmessgebern (Encoder-Scheiben), wo mechanische Toleranzen beim Ablesen sonst grobe Fehler verursachen würden. Eine Variante davon ist der **Glixon-Code**, der zusätzlich beim Übergang von 9 auf 0 zyklisch bleibt (9 → 1000).

![Gray-Code in der Praxis: links eine lineare Messskala (mm) mit mehrspurigen Gray-Code-Streifen — jede Querlinie entspricht einem anderen Binärwert, wobei benachbarte Streifen sich stets nur in einem Bit unterscheiden; rechts eine rotierende Winkelscheibe (Einer, Zehner, Hunderter) mit konzentrischen Gray-Code-Ringen für die Winkelabtastung](abbildungen/graycode_skala_laenge_winkel.png)

## Fehlererkennende und fehlerkorrigierende Codes

Damit ein Übertragungsfehler erkannt — oder sogar korrigiert — werden kann, muss mehr Information übertragen werden als zur reinen Darstellung nötig wäre. Diesen "Überschuss" nennt man **Redundanz**.

:::merke
Für die **Fehlererkennung** genügt eine geringe Redundanz (z. B. 1 Bit). Für die **Fehlerkorrektur** ist deutlich mehr Redundanz nötig.
:::

**Dual ergänzter Code (Paritätsbit)**: Dem BCD-Code wird ein zusätzliches **Prüfbit** (Paritätsbit) so hinzugefügt, dass die Anzahl der Einsen im Codewort stets gerade ist. Stimmt die Parität beim Empfänger nicht, liegt ein (einzelner) Übertragungsfehler vor — welches Bit betroffen ist, bleibt aber unbekannt. Zwei gleichzeitige Fehler bleiben unentdeckt.

**Hamming-Code**: Mit drei Kontrollbits (drei Paritätsgruppen mit je gerader Parität) lässt sich nicht nur ein Fehler **erkennen**, sondern auch **lokalisieren und korrigieren** — das fehlerhafte Bit wird einfach invertiert. Treten gleichzeitig mehrere Fehler auf, meldet das System "ERROR", kann den Fehler aber nicht mehr korrigieren.

:::info
Anwendung fehlererkennender/-korrigierender Codes: Datenübertragung über längere, störanfällige Leitungen — z. B. [[RS232 & RS485]], Speicherchips mit ECC, Funkstrecken.
:::

## ASCII, Unicode und UTF-8 — Zeichen codieren

**ASCII** (*American Standard Code for Information Interchange*) bildet 128 Zeichen (Buchstaben, Ziffern, Steuerzeichen) mit 7 Bit ab (2⁷ = 128). Gross- und Kleinbuchstaben unterscheiden sich durch ein konstantes Offset von 0x20 — z. B. 'X' = 0x58, 'x' = 0x78.

**Unicode** erweitert dieses Prinzip auf praktisch alle Schriftsysteme der Welt: Jedem Zeichen wird ein eindeutiger Code-Punkt U+XXYYZZ zugewiesen (Norm ISO 10646, *Universal Coded Character Set*). Block 00 von Unicode entspricht exakt dem ASCII-Code — das sichert Abwärtskompatibilität.

Da Unicode weit mehr als 256 Zeichen umfasst, braucht es eine **Kodierung** in Bytes:

| Kodierung | Prinzip | Eigenschaft |
|---|---|---|
| **UTF-16** | jedes Zeichen 2 Byte | deckt nicht alle Zeichen ab, nicht ASCII-kompatibel |
| **UTF-32** | jedes Zeichen 4 Byte | deckt alles ab, aber sehr speicherintensiv |
| **UTF-8** | "normale" Zeichen 1 Byte, "ausgefallene" mehrere Byte | voll ASCII-kompatibel, sparsam — Standard im Internet |

:::tip
UTF-8 ist deshalb so verbreitet, weil ein reiner ASCII-Text in UTF-8 byte-identisch bleibt. Nur Zeichen ausserhalb des ASCII-Bereichs (Umlaute, Sonderzeichen, asiatische Schriften) benötigen zusätzliche Bytes.
:::
