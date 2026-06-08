---
title: R-2R-Netzwerk
kategorie: SH
kapitel: Wandler
tags: [r-2r-netzwerk, da-wandler, widerstandsnetzwerk, linearitaet, binaere wertigkeit]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[DA-Wandler (Digital-Analog-Umsetzer)]]
:::
:::

---

Der einfache → [[DA-Wandler (Digital-Analog-Umsetzer)|DA-Wandler mit gewichteten Widerständen]] hatte zwei hartnäckige Schwächen: Für jedes Bit braucht es einen eigenen, hochpräzisen Widerstandswert (2R, 4R, 8R, 16R, …), und die Referenzspannungsquelle wird je nach digitalem Wert ungleichmässig belastet. Das **R-2R-Netzwerk** (auch Leiternetzwerk genannt) löst beide Probleme mit einem einzigen, eleganten Kniff.

## Die Grundidee: nur noch zwei Widerstandswerte

:::merke
Anstatt für jedes Bit einen eigens dimensionierten Widerstand zu verwenden, kommt das R-2R-Netzwerk mit **nur zwei verschiedenen Widerstandswerten** aus: R und 2R — wobei sich 2R ganz einfach durch zwei in Serie geschaltete Widerstände der Grösse R realisieren lässt. Damit muss in der Fertigung nur noch **ein einziger Widerstandstyp** in grosser Stückzahl exakt produziert werden, was die Herstellung deutlich vereinfacht und die Bauteilkosten senkt — ein entscheidender Vorteil gegenüber dem Aufbau mit individuell gewichteten Widerständen.
:::

## Der Beweis: an jedem Knoten halbiert sich die Spannung

Das Netzwerk besteht aus einer Kette von Knotenpunkten A, B, C, …, an denen sich jeweils ein 2R-Widerstand zur digital geschalteten Leitung sowie ein R-Widerstand zum nächsten Knoten verzweigen. Der entscheidende Trick liegt in der cleveren **Ersatzwiderstands-Betrachtung**, die sich rückwärts durch die Kette arbeitet:

:::tip
Betrachtet man das Netzwerk von seinem offenen Ende her, ergibt sich am letzten Knoten ein Ersatzwiderstand R_Ersatz1 = 2R ∥ 2R = R. Dieser liegt nun in Serie mit dem nächsten R-Widerstand, sodass sich am vorletzten Knoten wieder R_Ersatz2 = (R_Ersatz1 + R) ∥ 2R = R ergibt — und so weiter, Knoten für Knoten zurück bis zum Eingang. An **jedem** Knoten entsteht so exakt derselbe Ersatzwiderstand R, was bedeutet: Die Referenzspannung U_Ref **halbiert sich an jedem Knoten** — von U_Ref über ½ U_Ref, ¼ U_Ref bis hin zu ⅛ U_Ref am letzten Abzweig. Da sich die Referenzspannung an den einzelnen Knoten halbiert, halbiert sich proportional dazu auch der Strom in jedem "Strompfad" — exakt jene binäre Gewichtung 2⁰, 2¹, 2², 2³, …, die für eine korrekte → [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)|binäre]] DA-Wandlung benötigt wird.
:::

## Gleichmässige Belastung der Referenzquelle

:::info
Der zweite grosse Vorteil ergibt sich praktisch von selbst: Weil das Netzwerk an jedem Knoten denselben Ersatzwiderstand "sieht" — unabhängig davon, welche Bits gerade gesetzt sind —, bleibt die **Belastung der Referenzspannungsquelle stets konstant**. Das verbessert die Linearität spürbar gegenüber der einfachen Widerstandsschaltung, bei der unterschiedliche Bitmuster unterschiedlich grosse Ströme aus der Referenzquelle zogen und so die Genauigkeit beeinträchtigten.
:::

## Dieselbe Formel — mit besserer Hardware

Da sich die Ströme in den einzelnen Pfaden weiterhin exakt nach der binären Wertigkeit staffeln, gilt für die Ausgangsspannung dieselbe Formel wie beim einfachen DA-Wandler:

:::formel
U_a = −U_Ref · Z / (Z_max + 1)        z. B. bei 8-Bit-Auflösung: Z = 0…255, Z_max = 255
:::

Das R-2R-Netzwerk verändert also nichts an der grundsätzlichen *Funktionsweise* — es liefert exakt dasselbe Ergebnis wie der Aufbau mit gewichteten Widerständen. Was sich ändert, ist die **Qualität der Hardware dahinter**: weniger unterschiedliche Bauteile, höhere Fertigungspräzision, gleichmässigere Belastung der Referenzquelle — und damit insgesamt ein deutlich linearerer, genauerer Wandler. Aus diesem Grund ist das R-2R-Netzwerk heute das in integrierten DA-Wandler-Bausteinen am häufigsten verwendete Schaltungsprinzip.

So lässt sich aus einer digitalen Zahl mit präziser Analogtechnik eine exakt proportionale Spannung gewinnen. Es geht aber auch ganz anders — nämlich fast vollständig **ohne** spezialisierte Analogbausteine, dafür mit cleverer digitaler Pulsformung: Wie sich eine analoge Spannung allein durch die geschickte zeitliche Steuerung digitaler Schaltimpulse erzeugen lässt, zeigt der Artikel → [[DA-Wandlung mit PWM|DA-Wandlung mit PWM]].
