---
title: Opencollector & Open-Drain
kategorie: SH
kapitel: Logik
tags: [opencollector, open-drain, wired-and, wired-or, pull-up, busankopplung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikfamilien (TTL, CMOS, BiCMOS, ECL)]]
:::
:::vbox
**Verwandte Artikel**
- [[Tristate-Ausgänge]]
:::
:::

---

Ein gewöhnliches Logikgatter zieht seinen Ausgang aktiv sowohl auf High als auch auf Low. Bei **Opencollector**- (TTL) bzw. **Open-Drain**-Gattern (CMOS) fehlt dagegen der "obere" Treibertransistor — der Ausgang kann nur aktiv auf Low gezogen werden, für den High-Pegel ist ein externer Widerstand nötig. Diese auf den ersten Blick unvollständige Bauweise eröffnet überraschend nützliche Schaltungsmöglichkeiten.

## Aufbau und Funktionsweise

Bei einem TTL-NAND mit Opencollector-Ausgang endet die Ausgangsstufe in einem einzelnen Transistor, dessen Kollektor offen herausgeführt ist (daher der Name). Ist das Gatter im Low-Zustand aktiv, leitet dieser Transistor und zieht den Ausgang auf Low. Im "High-Fall" sperrt er lediglich — ohne einen externen **Pull-Up-Widerstand** nach V_CC bliebe der Ausgang dann hochohmig und undefiniert.

:::merke
Der grosse Vorteil von Opencollector: Am Ausgang können auch Lasten betrieben werden, die an einer **anderen** Betriebsspannung als V_CC liegen — z. B. Relais (Freilaufdiode nicht vergessen!), Lampen oder andere Kleinverbraucher lassen sich so direkt ansteuern, ohne dass die Versorgungsspannungen der Logik und der Last übereinstimmen müssen.
:::

## Wired-AND und Wired-OR: Verknüpfen durch Zusammenschalten

Schliesst man mehrere Opencollector-Ausgänge **direkt zusammen** und versieht die gemeinsame Leitung mit einem einzigen Pull-Up-Widerstand R_C, entsteht ohne ein einziges zusätzliches Gatter eine logische Verknüpfung:

:::tip
**Wired-AND**: Liegt auch nur ein einziger Opencollector-Transistor durchgeschaltet (Low) vor, wird die gemeinsame Leitung auf Low gezogen. Nur wenn **alle** Ausgänge gleichzeitig sperren (High), bleibt die Leitung über den Pull-Up auf High. In positiver Logik ergibt sich damit Y = y₁ ∧ y₂ ∧ … ∧ yₙ — eine UND-Verknüpfung allein durch das Zusammenschalten der Ausgänge!

**Wired-OR**: Negiert man (nach den Morganschen Gesetzen, → [[Schaltalgebra (Boolesche Algebra)]]) beide Seiten dieser Gleichung, ergibt sich eine ODER-Verknüpfung Y = y₁ ∨ y₂ ∨ … ∨ yₙ — realisiert durch dieselbe Hardware, lediglich mit invertierten Eingangssignalen.
:::

Diese Eigenschaft macht Opencollector-Ausgänge zu einem klassischen Mittel für **Busankopplungen**: Mehrere Bausteine können sich eine gemeinsame Leitung "teilen", ohne dass ein aktiver Ausgang einen anderen kurzschliesst — ein Prinzip, das z. B. beim I²C-Bus konsequent genutzt wird, dessen Leitungen SDA und SCL beide als Open-Drain mit Pull-Up betrieben werden.

:::info
Eng verwandt mit Opencollector ist der → [[Tristate-Ausgänge|Tristate-Ausgang]]: Während Opencollector den High-Pegel passiv über einen Pull-Up erzeugt, schaltet ein Tristate-Ausgang aktiv in einen dritten, hochohmigen Zustand um — beide Konzepte lösen das Problem, mehrere Treiber an eine gemeinsame Leitung anzuschliessen, jedoch auf unterschiedliche Weise.
:::
