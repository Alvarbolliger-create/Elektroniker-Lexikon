---
title: Programmierbare Logikbausteine (PROM, PAL, PLA)
kategorie: SH
kapitel: Programmierbare_Logik
tags: [prom, pal, pla, programmable array logic, programmable logic array, programmierbare logik, olmc]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Code-Wandler (BCD-zu-7-Segment)]]
:::
:::vbox
**Führt weiter zu**
- [[GAL (Generic Array Logic)]]
:::
:::

---

Jede kombinatorische Schaltung — vom einfachen → [[Code-Wandler (BCD-zu-7-Segment)|Code-Wandler]] bis zum komplexen Steuerwerk — lässt sich grundsätzlich aus diskreten Logikgattern aufbauen. Mit wachsender Komplexität wird dieser Weg jedoch schnell unpraktikabel: zu viele Bauteile, zu viel Verdrahtungsaufwand, zu wenig Flexibilität bei nachträglichen Änderungen. Die Antwort der Industrie war die Entwicklung **programmierbarer Logikbausteine** — Chips, deren innere Verknüpfungsstruktur erst nach der Fertigung durch den Anwender festgelegt wird.

## Grundidee: eine Wahrheitstabelle als Speicherinhalt

Den Einstieg liefert ein einfaches Beispiel: Ein **Codewandler** soll den Excess-3-Code in den BCD-Code umsetzen. Die Wahrheitstabelle dieses Wandlers hat eine auffällige Eigenschaft — sie lässt sich genauso gut als **Speicherinhalt** lesen:

:::merke
Betrachtet man das 4-Bit-Muster des Excess-3-Codes als **Adresse** und das 4-Bit-Muster des zugehörigen BCD-Codes als **gespeicherte Daten**, erinnert die Struktur unmittelbar an einen Speicherbaustein! Genau diese Beobachtung führt zum **PROM** (Programmable Read-Only Memory): Legt man die Eingangsvariablen einer Logikfunktion als Adresse an, liefert der Speicher an seinem Datenausgang exakt den vorprogrammierten Funktionswert — eine beliebige Wahrheitstabelle wird so direkt "abgespeichert", ganz ohne eigens entworfene Gatterschaltung.
:::

Intern besteht ein PROM aus zwei Verknüpfungsfeldern: einem **fest verdrahteten UND-Feld**, das aus den n Eingängen (und ihren invertierten Varianten) sämtliche 2ⁿ möglichen Adresskombinationen bildet, und einem **programmierbaren ODER-Feld**, in dem für jeden Ausgang festgelegt wird, welche dieser Adresskombinationen ihn auf 1 setzen sollen — ein 16 × 4-Bit-PROM realisiert so vier Funktionen mit je vier Eingangsvariablen.

:::warning
Speicherbausteine als Ersatz für kombinatorische Logik haben auch Nachteile: Sie werden relativ schlecht ausgenutzt, da für **jede** Zeile der Wahrheitstabelle ein eigener Speicherplatz reserviert werden muss — eine Vereinfachung mit Hilfe des KV-Diagramms bringt hier nichts, denn die Struktur des PROM verlangt zwingend alle 2ⁿ Adresskombinationen. Ausserdem sind Speicherbausteine vergleichsweise "langsame" Bauelemente: Ihre Zugriffszeit ist deutlich grösser als die durchschnittliche Laufzeit eines einzelnen Logikgatters.
:::

## PAL: das programmierbare UND-Feld

1978 brachte die Firma Monolithic Memories Incorporated (MMI) mit dem **PAL** (Programmable Array Logic) einen wesentlichen Fortschritt auf den Markt — Bausteine dieser Art werden allgemein auch als **PLD** (Programmable Logic Device) bezeichnet. Beim PAL ist die Aufteilung gegenüber dem PROM **umgekehrt**:

:::tip
Beim PAL ist das **UND-Feld programmierbar**, das **ODER-Feld hingegen fest verdrahtet** — jeweils eine feste Gruppe von UND-Verknüpfungen (typischerweise vier) ist auf ein gemeinsames ODER-Gatter geführt. Da es keinen Sinn ergibt, eine Eingangsvariable und ihre Negation gleichzeitig auf dasselbe UND-Gatter zu führen, wird von jedem Eingang stets nur entweder die normale oder die negierte Form verwendet — bei vier Eingangsvariablen liegen so maximal vier Terme an jedem UND-Gatter an. Diese Struktur entspricht **exakt der disjunktiven Normalform**, also genau jener Form, die sich auch beim Vereinfachen einer Wahrheitstabelle mit dem KV-Diagramm ergibt — ein PAL ist damit ideal geeignet, um bereits "vereinfachte" Schaltfunktionen direkt zu programmieren.
:::

Realisiert man den Excess-3-zu-BCD-Wandler mit einem PAL, zeigt sich allerdings auch dessen Schwäche: Da jede Gruppe von UND-Gattern fest auf "ihr" ODER-Gatter geführt ist, lassen sich nicht benötigte UND-Terme nicht anderweitig nutzen — ein PAL-Baustein wird wegen dieser starren Zuordnung nur selten zu 100 % ausgenutzt. Bekannte Vertreter sind das **PAL16L8** (rein kombinatorisch, mit teilweise zurückgeführten Ausgängen für Logik mit Rückführungen) und das **PAL16R8**, das an seinen Ausgängen zusätzlich → [[Flipflops (SR, D, JK, T)|D-Flipflops]] besitzt und sich damit auch für sequenzielle Logik wie Zähler oder Schieberegister eignet — mit gemeinsamem Systemtakt an allen Registern und Tristate-Ausgängen für die Buskopplung.

## PLA: maximale Flexibilität

Mehr Flexibilität und eine bessere Ausnutzung des Siliziums bietet das **PLA** (Programmable Logic Array):

:::info
Beim PLA sind sowohl das **UND-Feld als auch das ODER-Feld frei programmierbar**. Dadurch lässt sich nahezu jede beliebige Verknüpfungsstruktur abbilden — allerdings auf Kosten eines deutlich höheren Programmieraufwands, denn die Anzahl der zu setzenden "Sicherungen" und damit auch die Anzahl möglicher Kombinationen steigt erheblich. Ein wesentlicher Vorteil: Ungenutzte UND-Terme lassen sich beliebigen ODER-Gattern zuordnen — ein PLA-Baustein erreicht dadurch die höchsten Ausnutzungsgrade aller drei Bausteinfamilien (PROM, PAL, PLA).
:::

Damit ist die Reihe der "klassischen" PLD-Strukturen vollständig — vom starren PROM über das teilflexible PAL bis zum vollständig programmierbaren PLA. Allen drei Technologien ist jedoch ein entscheidender Nachteil gemeinsam: Sie basieren auf einmalig programmierbaren **Sicherungen** (Fuse-Technologie) und lassen sich danach nicht mehr korrigieren. Wie dieses Problem gelöst wurde, zeigt der nächste Schritt in der Entwicklung programmierbarer Logik — der → [[GAL (Generic Array Logic)|GAL-Baustein]].
