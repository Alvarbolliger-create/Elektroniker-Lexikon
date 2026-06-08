---
title: Boot-Vorgang
kategorie: SH
kapitel: Prozessor
tags: [boot, bootloader, firmware, reset, initialisierung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Mikrocontroller]]
:::
:::vbox
**Führt weiter zu**
- [[Embedded Linux]]
:::
:::

---

Bevor ein → [[Mikrocontroller|Mikrocontroller]] auch nur einen einzigen Befehl seines → [[Befehlszyklus & Maschinencode|Befehlszyklus]] ausführen kann, muss er sich erst einmal in einen wohldefinierten Ausgangszustand versetzen. Dieser Vorgang — vom Anlegen der Versorgungsspannung bis zum ersten ausgeführten Programmbefehl — heisst **Boot-Vorgang** oder **Reset-Sequenz**.

## Reset-Ursachen: woher kommt der "Neustart-Befehl"?

Ein Reset kann auf ganz unterschiedliche Weise ausgelöst werden:

| Ursache | Kürzel | Beschreibung |
|---|---|---|
| Power-on Reset | POR | Reset beim Anlegen der Versorgungsspannung |
| Brown-out Reset | BOD | Reset bei zu niedriger Versorgungsspannung |
| Externer Reset | NRST | Reset über einen externen Reset-Pin |
| Watchdog-Reset | — | Reset durch einen abgelaufenen → [[Interrupt|Watchdog-Timer]] |
| Software-Reset | SW | Reset, vom Programm selbst ausgelöst |
| Lock-up-Reset | — | Reset bei einem nicht behebbaren internen Prozessorfehler |

:::merke
**Power-on Reset (POR)** und **Brown-out Detection (BOD)** sind die wichtigsten Schutzmechanismen beim Einschalten: Der POR hält die CPU so lange im Reset-Zustand, bis die Versorgungsspannung einen sicheren Schwellwert überschritten hat — andernfalls könnten Register und Speicher in einem undefinierten Zustand "hochfahren". Die BOD-Schaltung überwacht die Versorgungsspannung auch im laufenden Betrieb und löst einen Reset aus, sobald sie unter einen kritischen Wert sinkt — etwa bei einem kurzen Spannungseinbruch im Stromnetz. Ohne diese Mechanismen könnte ein Mikrocontroller bei instabiler Versorgung in einen undefinierten, potenziell gefährlichen Zustand geraten.
:::

## Clock-Startup: bevor der Takt überhaupt steht

Direkt nach einem Reset läuft zunächst die **Taktinitialisierung**, denn ohne stabilen Takt kann keine einzige Schaltung im Chip korrekt arbeiten:

:::tip
**1.** Der interne RC-Oszillator startet — er liefert sofort, aber ungenau, einen ersten Takt. **2.** Mit diesem Takt beginnt die CPU bereits mit den allerersten Initialisierungsschritten. **3.** Parallel dazu startet, falls vorhanden, der externe Quarzoszillator — er braucht typischerweise einige Millisekunden, bis er stabil schwingt. **4.** Eine PLL (Phase-Locked Loop) vervielfacht den Quarztakt auf die gewünschte Systemfrequenz. **5.** Sobald die PLL eingerastet ist ("Lock"), schaltet das System auf den präzisen, hochfrequenten Systemtakt um. **6.** Erst jetzt läuft der Mikrocontroller mit seiner vollen, spezifizierten Taktfrequenz.
:::

## Der Reset-Handler: die ersten Schritte in Software

Sobald der Prozessorkern lauffähig ist, übernimmt eine kleine, in Assembler geschriebene Startup-Routine (oft `startup.s` genannt) die Kontrolle:

:::merke
**1.** Der **Stackpointer** wird auf das Ende des RAM-Bereichs gesetzt — ohne funktionierenden Stack kann kein C-Programm laufen. **2.** Der **Programcounter** wird auf die Adresse des Reset-Handlers geladen — den allerersten Eintrag der → [[Interrupt|Vektortabelle]]. **3.** Initialisierte globale Variablen werden aus dem Flash ins RAM kopiert (Daten-Segment, `.data`). **4.** Nicht initialisierte globale Variablen werden im RAM mit Nullen vorbelegt (`.bss`-Segment). **5.** Erst danach wird die Funktion `main()` aufgerufen — das eigentliche Anwendungsprogramm beginnt.
:::

## Reset-Ursache auslesen

Welcher der oben genannten Gründe einen Reset tatsächlich ausgelöst hat, lässt sich im laufenden Programm nachträglich feststellen — viele Mikrocontroller speichern diese Information in einem dedizierten Statusregister:

```c
if (RCC->CSR & RCC_CSR_PORRSTF)   { /* Power-on Reset */ }
if (RCC->CSR & RCC_CSR_BORRSTF)   { /* Brown-out Reset */ }
if (RCC->CSR & RCC_CSR_PINRSTF)   { /* externer Reset (NRST-Pin) */ }
if (RCC->CSR & RCC_CSR_IWDGRSTF)  { /* Watchdog-Reset */ }
RCC->CSR |= RCC_CSR_RMVF;          // Flags zurücksetzen
```

:::info
Diese Information ist gerade bei der Fehlersuche im Feld Gold wert: Stürzt ein Gerät beim Kunden gelegentlich ab und startet neu, lässt sich anhand der protokollierten Reset-Ursache oft schon eingrenzen, ob ein Spannungsproblem (BOD), ein Software-Fehler (Watchdog) oder ein mechanischer Defekt (NRST) vorliegt — ganz ohne dass das Gerät dafür an ein Labor geschickt werden müsste.
:::

## Startup bei Embedded Linux: ein deutlich längerer Weg

Während ein einfacher Mikrocontroller nach wenigen Millisekunden sein Anwendungsprogramm startet, durchläuft ein System mit → [[Embedded Linux|Embedded Linux]] eine deutlich vielschichtigere Startsequenz:

:::warning
**1.** Ein im Chip fest verankerter **ROM-Bootloader** wird beim Einschalten automatisch ausgeführt — er kennt nur die allernötigsten Schritte, um den nächsten Stufenloader zu laden. **2.** Dieser lädt einen ersten, minimalen **Bootloader** (z. B. SPL — Secondary Program Loader), der die externe RAM-Initialisierung übernimmt. **3.** Erst danach kann der vollständige Bootloader (häufig **U-Boot**) geladen werden — er bietet eine Kommandozeile, kann Firmware-Updates einspielen und wählt das zu startende Betriebssystem-Image aus. **4.** U-Boot lädt den **Linux-Kernel** sowie den → [[Device Tree|Device Tree]] in den Speicher und übergibt die Kontrolle. **5.** Der Kernel initialisiert sämtliche Hardwarekomponenten anhand der Device-Tree-Beschreibung und mountet das Root-Dateisystem. **6.** Schliesslich startet der **Init-Prozess** (z. B. systemd) und damit die eigentlichen Anwendungsprogramme im Userspace.

Vom ersten Stromimpuls bis zur lauffähigen Anwendung vergehen bei einem solchen System je nach Hardware mehrere Sekunden — eine Ewigkeit verglichen mit den wenigen Millisekunden eines Mikrocontroller-Bootvorgangs.
:::

So unterschiedlich die beiden Welten auch starten — am Ende steht in beiden Fällen ein lauffähiges System, bereit für seine eigentliche Aufgabe. Wann sich der Sprung von der schlanken Mikrocontroller-Firmware zum vollwertigen Betriebssystem überhaupt lohnt und was ein solches System unter der Haube von einem Mikrocontroller unterscheidet, zeigt der → [[Embedded Linux|Embedded-Linux]]-Artikel.
