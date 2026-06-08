---
title: Interrupt
kategorie: SH
kapitel: Prozessor
tags: [interrupt, interrupt service routine, isr, interruptvektor, prioritaet, unterbrechung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Mikrocontroller]]
:::
:::vbox
**Verwandte Artikel**
- [[DMA (Direct Memory Access)]]
:::
:::

---

Ein → [[Mikrocontroller|Mikrocontroller]] muss ständig auf Ereignisse aus seiner Umgebung reagieren — ein eintreffendes UART-Byte, ein Tastendruck, ein abgelaufener Timer. Die naheliegendste Lösung dafür ist denkbar einfach: die CPU fragt in einer Schleife immer wieder nach, ob das Ereignis schon eingetreten ist. Dieses **Polling** hat jedoch einen entscheidenden Haken.

## Polling vs. Interrupt

```c
// Polling: die CPU fragt ständig nach
while (1) {
    if (UART_DATA_READY()) {
        char c = UART_READ();
        verarbeite(c);
    }
    // in der Zwischenzeit: nichts anderes möglich
}
```

:::warning
Beim **Polling** verbringt die CPU den Grossteil ihrer Zeit damit, immer wieder dieselbe Frage zu stellen — "ist das Ereignis schon da?" — meist mit "Nein" als Antwort. Diese Zeit steht für andere Aufgaben nicht zur Verfügung, und die Reaktionszeit hängt unkontrolliert davon ab, an welcher Stelle des Programms sich die CPU gerade befindet. Bei zeitkritischen oder seltenen Ereignissen ist das eine enorme Verschwendung von Rechenleistung.
:::

Der **Interrupt** kehrt dieses Prinzip um: Nicht die CPU fragt nach, sondern das Ereignis meldet sich selbst — die CPU kann bis dahin ungestört ihrer eigentlichen Arbeit nachgehen.

```c
// Interrupt: das Ereignis meldet sich von selbst
void main(void) {
    UART_enable_interrupt();
    while (1) {
        // CPU kann andere Aufgaben erledigen
        tu_irgendwas_anderes();
    }
}

void UART_IRQHandler(void) {     // wird automatisch aufgerufen
    char c = UART_READ();
    verarbeite(c);
}
```

## Ablauf eines Hardware-Interrupts

Trifft ein Interrupt ein, läuft im Hintergrund eine exakt festgelegte Sequenz ab — hier am Beispiel eines ARM-Cortex-M-Mikrocontrollers:

:::merke
**1.** Ein Peripheriebaustein (z. B. die UART) setzt sein Interrupt-Flag, sobald das Ereignis eintritt. **2.** Der **NVIC** (Nested Vectored Interrupt Controller) erkennt die anstehende Anfrage und vergleicht ihre Priorität mit der aktuell laufenden Aufgabe. **3.** Ist die Priorität höher, unterbricht die CPU den laufenden → [[Befehlszyklus & Maschinencode|Befehlszyklus]] nach dem aktuellen Befehl. **4.** Der aktuelle Prozessorzustand (Register, Programcounter, PSW) wird automatisch auf den Stack gerettet. **5.** Über die **Vektortabelle** ermittelt die CPU die Einsprungadresse der zuständigen Behandlungsroutine. **6.** Die **Interrupt Service Routine (ISR)** wird ausgeführt und erledigt die eigentliche Reaktion auf das Ereignis. **7.** Das auslösende Flag wird gelöscht — sonst würde derselbe Interrupt sofort erneut ausgelöst. **8.** Der gerettete Prozessorzustand wird vom Stack zurückgeholt. **9.** Das unterbrochene Programm läuft an exakt der Stelle weiter, an der es unterbrochen wurde — als wäre nichts geschehen.
:::

## Die Vektortabelle: wer ruft welche Routine?

Damit die CPU bei einem Interrupt sofort weiss, *welche* Routine zuständig ist, liegt am Anfang des Programmspeichers eine **Vektortabelle** — eine Liste von Adressen, an denen die jeweiligen ISRs beginnen. Jedem Interrupt-Typ (Reset, externe Leitung, Timer-Überlauf, UART-Empfang, …) ist darin ein fester Platz zugeordnet. Löst z. B. Timer 2 einen Interrupt aus, springt die CPU automatisch zur Adresse, die in der Vektortabelle für "Timer-2-Interrupt" eingetragen ist.

## Prioritäten und der NVIC

In einem realen System können mehrere Interrupts gleichzeitig oder kurz nacheinander auftreten. Damit nicht ein unwichtiges Ereignis ein dringendes verdrängt, lassen sich Prioritäten vergeben:

:::tip
Über den **NVIC** (Nested Vectored Interrupt Controller) kann jedem Interrupt eine eigene Priorität zugewiesen und er einzeln aktiviert oder gesperrt werden:

```c
NVIC_SetPriority(USART2_IRQn, 1);   // hohe Priorität (kleine Zahl = hoch)
NVIC_SetPriority(TIM6_IRQn, 3);     // niedrigere Priorität
NVIC_EnableIRQ(USART2_IRQn);
NVIC_EnableIRQ(TIM6_IRQn);
```

Tritt während der Bearbeitung eines niederpriorisierten Interrupts ein höherpriorisierter auf, unterbricht der NVIC die laufende ISR zugunsten der dringenderen — daher auch die Bezeichnung *Nested* (verschachtelt): Interrupts können sich gegenseitig unterbrechen, solange die Prioritätsreihenfolge das zulässt.
:::

## Regeln für eine saubere ISR

Eine Interrupt Service Routine läuft "neben" dem eigentlichen Programm — das verlangt nach besonderer Disziplin:

:::warning
Eine ISR sollte **so kurz wie möglich** gehalten werden, denn solange sie läuft, bleiben (gleich- oder niedrigpriorisierte) andere Interrupts blockiert. Variablen, die sowohl im Hauptprogramm als auch in einer ISR verwendet werden, müssen als `volatile` deklariert werden — sonst könnte der Compiler ihren Wert in einem Register zwischenspeichern und Änderungen durch die ISR schlicht "übersehen". Zeitintensive Funktionen wie `delay()` haben in einer ISR nichts verloren — sie würden das gesamte System für die Dauer der Wartezeit lahmlegen. Aufwendige Verarbeitungsschritte gehören stattdessen ins Hauptprogramm: Die ISR setzt nur ein Flag oder legt Daten in einen Puffer, die eigentliche Verarbeitung übernimmt dann die `while`-Schleife im Hauptprogramm.
:::

## Der Watchdog: ein Interrupt, der das System rettet

Eine besondere Anwendung des Interrupt-Prinzips ist der **Watchdog** — ein unabhängiger Hardware-Timer, der das Programm ständig im Auge behält:

:::info
Das laufende Programm muss den Watchdog-Timer in regelmässigen Abständen "füttern" (zurücksetzen), indem es ein bestimmtes Register beschreibt. Bleibt diese Rückmeldung aus — etwa weil sich das Programm in einer Endlosschleife verfangen hat oder abgestürzt ist — läuft der Timer ab und löst einen **Reset** des gesamten Systems aus. Ein **Window-Watchdog** verschärft dieses Prinzip zusätzlich: Hier darf das Rücksetzen weder zu spät *noch zu früh* erfolgen — beide Fälle lösen einen Reset aus. Das deckt zusätzlich den Fehlerfall ab, in dem ein Programm fälschlicherweise viel zu schnell durchläuft, etwa weil ein Schleifenzähler übersprungen wurde.
:::

Damit ist klar, *wie* ein Mikrocontroller auf einzelne Ereignisse reagiert, ohne seine Zeit mit Warten zu verschwenden. Geht es jedoch nicht nur um die Reaktion auf ein Ereignis, sondern um die *Übertragung grosser Datenmengen* zwischen Speicher und Peripherie, stösst auch der Interrupt an seine Grenzen — hier kommt der → [[DMA (Direct Memory Access)|DMA-Controller]] ins Spiel.
