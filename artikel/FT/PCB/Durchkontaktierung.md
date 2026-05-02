---
title: Durchkontaktierung (Via)
kategorie: FT
tags: [via, durchkontaktierung, PCB, blind via, buried via, HDI, micro via, through-hole, thermal via, BGA, annular ring]
symbol: —
einheit: —
---

Eine Durchkontaktierung (Via) verbindet Kupferflächen auf verschiedenen Lagen einer Leiterplatte. Ohne Vias wäre Multilayer-Design nicht möglich.

:::hbox
:::vbox
**Voraussetzungen**
- [[PCB Aufbau & Material]]
:::
:::vbox
**Verwandte Artikel**
- [[SMD vs. THT]]
- [[DFM (Design for Manufacturing)]]
:::
:::

---

## Arten von Vias

**Through-hole Via**: Durchgehende Bohrung durch alle Lagen. Einfachste und günstigste Variante. Typischer Durchmesser: 0.3-1.0 mm.

**Blind Via**: Verbindet die Aussenlage mit einer inneren Lage, ohne vollständig durch die Platine zu gehen. Teurer, spart Platz.

**Buried Via**: Verbindet zwei innere Lagen ohne auf der Aussenoberfläche sichtbar zu sein. Wird nur in HDI-Platinen verwendet.

**Micro Via**: Sehr kleine Blind Via (Durchmesser < 0.15 mm), mit Laser gebohrt. Standard in HDI-Platinen für BGA-Bauteile.

## Fertigung

Through-hole Vias werden mechanisch gebohrt und galvanisch verkupfert. Innenwanddicke typisch 17-35 µm.

Micro Vias werden mit CO2- oder UV-Laser gebohrt. Erlaubt sehr feine Strukturen und stacked vias.

## Thermische Vias

Vias unter thermischen Pads (QFN, D-PAK) leiten Wärme von der Bauteilunterseite zur Kupferfläche auf der Rückseite. Raster typisch 0.5-1.0 mm, Durchmesser 0.3-0.5 mm.

Ohne thermische Vias überhitzt der Chip, selbst wenn der Kühlkörper auf der Rückseite gross ist.

## Design-Regeln

- Mindestabstand Via-Bohrung zu Pad: herstellerabhängig (typisch 0.15 mm)
- Via-Annular-Ring: Kupferring um die Bohrung, mindestens 0.05-0.15 mm
- Tented Vias: Lötstopplack über der Via verhindert ungewolltes Verlöten

:::tip
Tented Vias in thermischen Via-Felder vermeiden, wenn der Lötstopplack die Wärmeleitung nicht beeinträchtigen soll. Alternativ: Via-in-Pad mit Kupferfüllung durch Galvanik.
:::
