---
title: Embedded Linux
kategorie: SH
kapitel: Prozessor
tags: [embedded linux, betriebssystem, kernel, treiber, bootloader, root-filesystem]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Boot-Vorgang]]
:::
:::vbox
**Verwandte Artikel**
- [[Device Tree]]
:::
:::

---

Der → [[Boot-Vorgang|Boot-Vorgang]] eines Mikrocontrollers endet nach wenigen Millisekunden in der `main()`-Funktion eines einzelnen, fest verdrahteten Programms. Manche Aufgaben verlangen jedoch nach mehr: einem Dateisystem, mehreren gleichzeitig laufenden Programmen, einem Netzwerk-Stack, grafischen Oberflächen. Wird diese Komplexität zu gross, kommt **Embedded Linux** ins Spiel — ein vollwertiges Betriebssystem auf einem eingebetteten Gerät.

## Wann lohnt sich Embedded Linux?

:::merke
Die Entscheidung zwischen "klassischem" Mikrocontroller-Programm und Embedded Linux hängt stark von den verfügbaren Ressourcen und Anforderungen ab. Als grobe Faustregel gilt: Reichen wenige zehn bis hundert Kilobyte RAM und Flash, ist ein Mikrocontroller ohne Betriebssystem (oder mit einem schlanken Echtzeitbetriebssystem, RTOS) meist die bessere Wahl — schnell startbereit, deterministisch, sparsam. Stehen dagegen mehrere zehn bis hundert Megabyte RAM zur Verfügung und werden Dateisysteme, Netzwerkprotokolle, grafische Oberflächen oder mehrere parallele Anwendungen benötigt, spielt Embedded Linux seine Stärken aus: ein riesiges Ökosystem an fertiger Software, Gerätetreibern und Bibliotheken, das nicht selbst entwickelt werden muss.
:::

## Der Bootprozess: vom Stromstoss zum Login-Prompt

Wie bereits im → [[Boot-Vorgang|Boot-Vorgang]] beschrieben, durchläuft ein Embedded-Linux-System eine mehrstufige Startsequenz — vom chipinternen ROM-Bootloader über einen vollwertigen Bootloader wie **U-Boot** bis zum Laden von Kernel und Root-Dateisystem. Jede dieser Stufen hat eine klar abgegrenzte Aufgabe, und jede Stufe muss erfolgreich abgeschlossen sein, bevor die nächste beginnen kann — fällt eine Stufe aus, bleibt das Gerät stumm.

## Der Device Tree: Hardware in Textform beschreiben

Damit ein und derselbe Linux-Kernel auf den unterschiedlichsten Hardware-Plattformen laufen kann, muss er erst einmal "wissen", welche Bausteine überhaupt vorhanden sind und wie sie verschaltet sind:

:::info
Anstatt diese Information fest in den Kernel einzukompilieren, beschreibt ein **Device Tree** die Hardware eines Geräts — Speicherbereiche, Busse, Peripheriebausteine, deren Adressen und Verbindungen — in einer eigenen, textuellen Beschreibungssprache. Der Bootloader übergibt dieses "Bauplan-Dokument" zusammen mit dem Kernel-Image — der Kernel liest daraus, was angeschlossen ist, und lädt die passenden Treiber. Wie genau ein solcher Device Tree aufgebaut ist und wie er in eine binäre Form übersetzt wird, vertieft der → [[Device Tree|Device-Tree]]-Artikel.
:::

## Distributionen: fertige Linux-Pakete für eingebettete Systeme

Ein vollständiges Embedded-Linux-System "von Hand" zusammenzustellen wäre ein enormer Aufwand — deshalb haben sich spezialisierte **Build-Systeme und Distributionen** etabliert:

| Distribution / Build-System | Eigenschaft |
|---|---|
| **Buildroot** | schlankes, schnell konfigurierbares Build-System für massgeschneiderte, minimale Images |
| **Yocto Project** | sehr flexibles, mächtiges Build-System für komplexe, produktionsreife Linux-Distributionen |
| **Raspberry Pi OS** | fertige Debian-basierte Distribution speziell für Raspberry-Pi-Hardware |
| **Alpine Linux** | sehr kompakte, sicherheitsorientierte Distribution mit minimalem Speicherbedarf |

## Typische Hardware-Plattformen

Embedded Linux läuft auf einer breiten Palette von Prozessoren und Boards — vom Hobby-Einplatinencomputer bis zur Industriesteuerung:

:::tip
Verbreitete Vertreter sind der **Raspberry Pi** (Broadcom-SoCs, grosse Community, ideal zum Einstieg), die **i.MX6**-Reihe von NXP (häufig in Industrie- und Automotive-Anwendungen) sowie die **AM335x**-Familie von Texas Instruments (z. B. auf dem BeagleBone Black). Allen gemeinsam ist ein ARM-Prozessorkern, ausreichend RAM für ein Linux-System und eine breite Palette an integrierten Schnittstellen.
:::

## Userspace: wo die eigentliche Anwendung lebt

Nach dem Hochfahren des Kernels und dem Mounten des Root-Dateisystems übernimmt der **Init-Prozess** (häufig systemd) die Kontrolle und startet die eigentlichen Anwendungsprogramme im **Userspace** — getrennt vom Kernel und gegeneinander durch Speicherschutz abgesichert. Hier laufen Webserver, grafische Oberflächen, Steuerungssoftware und all jene Programme, die das eingebettete Gerät am Ende ausmachen — schreibbar in praktisch jeder höheren Programmiersprache, mit Zugriff auf das riesige Software-Ökosystem von Linux.

Damit ein Embedded-Linux-System überhaupt weiss, welche Hardware es vor sich hat und welche Treiber es laden muss, braucht es jedoch genau jene "Bauplan-Beschreibung", die im nächsten Artikel im Mittelpunkt steht: den → [[Device Tree|Device Tree]].
