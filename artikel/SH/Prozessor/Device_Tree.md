---
title: Device Tree
kategorie: SH
kapitel: Prozessor
tags: [device tree, hardwarebeschreibung, kernel, treiberbindung, dtb, dts]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Embedded Linux]]
:::
:::

---

Im Artikel über → [[Embedded Linux|Embedded Linux]] tauchte bereits die Frage auf: Woher weiss ein und derselbe Linux-Kernel, welche Hardware auf einem ganz bestimmten Board überhaupt verbaut ist — welche UART an welcher Adresse hängt, wie viel RAM zur Verfügung steht, welcher SPI-Bus mit welchem Sensor verbunden ist? Die Antwort liefert der **Device Tree**.

## Warum überhaupt ein Device Tree?

:::merke
Früher musste für jedes einzelne Board eine eigene, fest kompilierte Kernel-Variante gebaut werden, die sämtliche Hardware-Details — Adressen, Interrupt-Leitungen, Bus-Zuordnungen — direkt im Programmcode enthielt. Das führte zu einer kaum noch wartbaren Vielzahl praktisch identischer Kernel-Versionen. Der **Device Tree** löst dieses Problem, indem er die Hardware-Beschreibung vollständig vom Kernel-Code **trennt**: Ein einziges Kernel-Image kann so auf den unterschiedlichsten Boards laufen — es liest beim Start einfach die mitgelieferte "Bauplan-Datei" und passt sich entsprechend an.
:::

## DTS und DTB: lesbare Quelle, kompiliertes Binärformat

Wie bei der Übersetzung eines Hochsprachenprogramms in → [[Befehlszyklus & Maschinencode|Maschinencode]] gibt es auch beim Device Tree eine für Menschen lesbare und eine für die Maschine bestimmte Form:

:::formel
DTS (Device Tree Source, Textform) → Compiler `dtc -O dtb` → DTB (Device Tree Blob, Binärform für den Bootloader)
:::

Der Entwickler schreibt die Hardware-Beschreibung in der lesbaren **DTS**-Syntax (Dateiendung `.dts`), der **Device Tree Compiler** (`dtc`) übersetzt sie in eine kompakte binäre **DTB**-Datei. Diese wird zusammen mit dem Kernel-Image in den Speicher geladen und vom → [[Boot-Vorgang|Bootloader]] übergeben.

## Aufbau: Knoten, Eigenschaften, Adressen

Ein Device Tree gliedert sich in eine Baumstruktur aus **Knoten** — jeder Knoten beschreibt einen Hardware-Baustein mit seinen Eigenschaften:

:::tip
```
uart0: serial@40010000 {
    compatible = "vendor,my-uart";
    reg = <0x40010000 0x1000>;
    interrupts = <5>;
    status = "okay";
};

spi0: spi@40020000 {
    compatible = "vendor,my-spi";
    reg = <0x40020000 0x1000>;
    #address-cells = <1>;
    #size-cells = <0>;
    status = "okay";
};
```

Die Eigenschaft `compatible` benennt den genauen Baustein und erlaubt dem Kernel, den passenden Treiber zu finden; `reg` gibt Basisadresse und Grösse des zugehörigen Registerbereichs an; `interrupts` legt fest, welche Interrupt-Leitung der Baustein verwendet; `status = "okay"` aktiviert den Knoten — `"disabled"` würde ihn deaktivieren, ohne ihn aus der Beschreibung entfernen zu müssen.
:::

## Overlays: gezielte Erweiterungen ohne Neukompilierung

Gerade bei modular aufgebauten Systemen — etwa einem Raspberry Pi mit wechselbaren Aufsteckplatinen ("HATs") — wäre es unpraktisch, für jede mögliche Kombination einen eigenen, vollständigen Device Tree zu pflegen:

:::info
Ein **Device Tree Overlay** ergänzt einen bestehenden Device Tree zur Laufzeit um zusätzliche oder veränderte Knoten — etwa um einen neu angeschlossenen Sensor oder ein Display zu beschreiben — ohne dass der Basis-Device-Tree dafür neu kompiliert werden müsste. Overlays lassen sich beim Booten gezielt einbinden und wieder entfernen, was die Konfiguration eines Geräts deutlich flexibler macht — ein Prinzip, das in seiner Grundidee an die → [[FPGA (Field Programmable Gate Array)|nachträgliche Rekonfiguration eines FPGA]] erinnert: Die zugrundeliegende Hardware bleibt gleich, ihre Beschreibung beziehungsweise Konfiguration lässt sich aber flexibel anpassen.
:::

Damit schliesst sich der Bogen vom kompakten Mikrocontroller-Programm bis zum vollwertigen Linux-System: Ein Device Tree macht den Kernel hardwareunabhängig, ein Bootloader lädt ihn passgenau, und der Kernel "verdrahtet" anhand dieser Beschreibung Treiber mit realer Hardware. Wie sich digitale Schaltungen — die letztlich genau jene Hardware bilden, die ein Device Tree beschreibt — direkt in einer Hardwarebeschreibungssprache entwerfen lassen, zeigt der Artikel zu → [[VHDL & Verilog|VHDL und Verilog]].
