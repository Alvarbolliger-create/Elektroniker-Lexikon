---
title: Device Tree
kategorie: SH
tags: [device tree, DTS, DTB, kernel, linux, hardware-beschreibung, overlay, U-Boot, raspberry pi, compatible]
symbol: —
einheit: —
---

Der Device Tree ist eine Datenstruktur die dem Linux-Kernel beschreibt welche Hardware auf einem Board vorhanden ist. Ohne Device Tree weiss der Kernel nichts über die Peripherie.

:::hbox
:::vbox
**Voraussetzungen**
- [[Embedded Linux]]
:::
:::vbox
**Verwandte Artikel**
- [[Embedded Linux]]
:::
:::

---

## Warum Device Tree?

Früher war die Hardwarekonfiguration direkt im Kernel-Code eingebaut. Jede Boardvariante brauchte eine eigene Kernel-Version. Der Device Tree trennt Hardware-Beschreibung vom Kernel-Code.

Einmal geschriebener Kernel-Code läuft auf allen Boards wenn der Device Tree stimmt.

## DTS und DTB

**DTS (Device Tree Source)**: Lesbare Textdatei (.dts).  
**DTB (Device Tree Blob)**: Kompilierte Binärversion (.dtb). Wird beim Booten vom Bootloader an den Kernel übergeben.

Compiliert mit:
```
dtc -O dtb -o output.dtb input.dts
```

## Aufbau

```dts
/ {
    model = "Mein Board";
    compatible = "hersteller,meinboard";

    uart0: serial@1c28000 {
        compatible = "allwinner,sun4i-uart";
        reg = <0x01c28000 0x400>;
        clocks = <&apb2_clk>;
        status = "okay";
    };

    spi0: spi@1c68000 {
        compatible = "allwinner,sun6i-spi";
        status = "disabled";
    };
};
```

`reg` gibt die Basisadresse und Grösse der Register an. `compatible` verbindet den Knoten mit dem richtigen Treiber.

## Overlays

Device Tree Overlays erlauben das Hinzufügen von Knoten ohne das Haupt-DTS zu ändern. Raspberry Pi nutzt das extensiv für HATs.

Overlays werden im Bootloader geladen und mit dem Basis-DTS zusammengeführt.

## Praktisch

Für Raspberry Pi: Overlays in /boot/config.txt aktivieren. Für eigene Boards: DTS der Referenzplatine anpassen und neu kompilieren.
