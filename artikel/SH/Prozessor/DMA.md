---
title: DMA (Direct Memory Access)
kategorie: SH
kapitel: Prozessor
tags: [dma, direct memory access, datentransfer, speicherzugriff, busmatrix]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Mikrocontroller]]
:::
:::vbox
**Verwandte Artikel**
- [[Interrupt]]
:::
:::

---

Der → [[Interrupt|Interrupt]] befreit die CPU davon, ständig nachzufragen, ob ein Ereignis eingetreten ist. Doch sobald es um die Übertragung **grosser Datenmengen** geht — etwa das Auslesen eines ADC-Pufferspeichers oder das Senden eines ganzen Datenblocks per UART — bringt selbst die interruptgesteuerte Lösung die CPU an ihre Grenzen: Für jedes einzelne Byte muss sie kurz innehalten, das Datum übernehmen und es weiterleiten. Genau hier setzt der **DMA-Controller** an.

## Das Problem ohne DMA

```c
// CPU kopiert jedes Byte einzeln - blockiert dabei das Hauptprogramm
for (int i = 0; i < 1024; i++) {
    while (!ADC_DATA_READY());      // warten...
    buffer[i] = ADC_READ();          // ein Byte übernehmen
}
// 1024-mal warten, lesen, schreiben - die CPU kann nichts anderes tun
```

:::warning
Auch mit Interrupt-Unterstützung muss die CPU bei einem grossen Datentransfer **jedes einzelne Datum** persönlich von der Quelle zum Ziel kopieren — das bindet Rechenzeit, die für andere Aufgaben fehlt, und verursacht bei jedem Byte zusätzlich den Verwaltungsaufwand eines vollständigen Interrupt-Durchlaufs (Kontext sichern, ISR aufrufen, Kontext wiederherstellen).
:::

## Die DMA-Lösung: Datentransfer ohne CPU

Ein **DMA-Controller** (Direct Memory Access) ist eine eigenständige Recheneinheit, die Daten **selbstständig** zwischen Speicher und Peripherie verschiebt — die CPU muss den Transfer nur noch anstossen:

```c
// CPU konfiguriert den DMA-Kanal einmalig...
DMA_Config(channel = 1,
           source = &ADC->DATA,
           dest   = buffer,
           count  = 1024,
           mode   = PERIPHERAL_TO_MEMORY);
DMA_Start(channel = 1);
// ...und kann sofort weiterarbeiten - der Transfer läuft im Hintergrund
```

:::merke
Die CPU **konfiguriert** den DMA-Kanal einmalig — Quelladresse, Zieladresse, Anzahl der zu übertragenden Worte, Übertragungsrichtung — und stösst den Transfer an. Ab diesem Moment übernimmt der DMA-Controller die komplette Übertragung selbstständig, **ohne** dass die CPU für jedes einzelne Datum eingreifen muss. Erst wenn der gesamte Block übertragen ist, meldet sich der Controller per → [[Interrupt|Interrupt]] und teilt der CPU mit: "fertig". So bleibt die CPU während der gesamten Übertragung frei für andere Aufgaben.
:::

## Architektur: die Busmatrix

Damit DMA-Controller und CPU nicht ständig um denselben Bus konkurrieren, sind moderne Mikrocontroller mit einer **Busmatrix** ausgestattet — einem Schaltnetz, das mehrere Bus-Master (CPU, DMA-Kanäle, …) gleichzeitig mit mehreren Bus-Slaves (Speicher, Peripherie) verbinden kann:

:::info
Solange CPU und DMA-Controller auf unterschiedliche Speicherbereiche zugreifen, können beide **gleichzeitig** über die Busmatrix arbeiten — die CPU rechnet weiter, während der DMA-Controller im Hintergrund Daten verschiebt. Erst wenn beide auf denselben Speicherblock zugreifen wollen, muss die Busmatrix den Zugriff zeitlich verschachteln (Arbitrierung) — meist mit einer leichten Bevorzugung der CPU oder nach einem festgelegten Prioritätsschema.
:::

## Transfermodi

Je nach Anwendung lässt sich ein DMA-Kanal auf unterschiedliche Übertragungsarten konfigurieren:

| Modus | Beschreibung | Typische Anwendung |
|---|---|---|
| **Memory-to-Memory** | Daten werden zwischen zwei Speicherbereichen kopiert | Pufferkopien, Bildverarbeitung |
| **Peripherie-to-Memory** | Daten von einem Peripheriebaustein in den Speicher | ADC-Abtastwerte, empfangene UART-Bytes |
| **Memory-to-Peripherie** | Daten aus dem Speicher zu einem Peripheriebaustein | DAC-Ausgabe, zu sendende UART-Daten |
| **Circular-Modus** | Nach Erreichen des Endes beginnt die Übertragung automatisch erneut am Anfang | kontinuierliche Audio- oder Sensordaten |
| **Double-Buffer-Modus** | Zwei Puffer werden abwechselnd befüllt — während einer übertragen wird, kann der andere verarbeitet werden | Streaming ohne Datenverlust |

## DMA-Kanäle und Prioritäten

Ein DMA-Controller verfügt in der Regel über **mehrere Kanäle**, die parallel und unabhängig voneinander konfiguriert werden können. Da auch hier mehrere Anfragen gleichzeitig auftreten können, lässt sich — ganz ähnlich wie beim → [[Interrupt|NVIC]] — jedem Kanal eine eigene **Priorität** zuweisen, die bestimmt, welcher Transfer bei einer Konkurrenzsituation Vorrang erhält.

## Cache-Kohärenz: eine Falle für Unaufmerksame

Verfügt der Mikrocontroller über einen **Cache**, lauert eine subtile Gefahr:

:::warning
Schreibt der DMA-Controller Daten direkt in den Hauptspeicher, "weiss" der Cache der CPU davon zunächst nichts — er hält möglicherweise weiterhin die *alten* Werte für denselben Speicherbereich vor. Liest die CPU anschliessend aus dem Cache, erhält sie veraltete Daten, obwohl im Speicher längst neue stehen (und umgekehrt: schreibt die CPU in den Cache, bevor der DMA-Controller den Speicher liest, überträgt dieser die alten Werte). Software muss diese **Cache-Kohärenz** deshalb aktiv sicherstellen — etwa durch gezieltes Invalidieren des betroffenen Speicherbereichs:

```c
SCB_InvalidateDCache_by_Addr((uint32_t*)buffer, sizeof(buffer));
```

Ohne diesen Schritt entstehen schwer auffindbare Fehler, bei denen Daten "korrekt aussehen", aber inhaltlich veraltet sind.
:::

Damit ergänzen sich Interrupt und DMA zu einem leistungsfähigen Team: Der Interrupt sorgt dafür, dass die CPU auf einzelne Ereignisse reagieren kann, ohne zu warten — der DMA-Controller übernimmt die eigentliche Datenbewegung, sodass die CPU ihre Rechenzeit voll für die eigentliche Aufgabe nutzen kann. Wie ein Mikrocontroller-System aber überhaupt erst in einen funktionsfähigen Zustand gelangt — was beim Einschalten genau passiert, bevor das erste Programm überhaupt starten kann —, klärt der → [[Boot-Vorgang|Boot-Vorgang]].
