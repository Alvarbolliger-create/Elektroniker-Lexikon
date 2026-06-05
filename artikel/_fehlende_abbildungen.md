# Fehlende Abbildungen

Diese Datei listet alle Abbildungen (SVG), die noch erstellt werden müssen.
Nur neue oder zusammengeführte Artikel — Ports übernehmen ggf. vorhandene Grafiken aus ET_alt.

---

## ET/Spule/Selbstinduktion.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/spule/lenzsche_regel_gegenrichtung.svg | Spule (Wicklung, symbolisch) mit Stromrichtung I (Pfeil nach rechts, steigend — angedeutet durch "I ↑"). Daneben: induzierte Gegenspannung u_i als Pfeil entgegen der Ursache (Pfeil nach links). Beschriftung: "u_i wirkt der Ursache entgegen (Lenzsche Regel)". Optional zwei Zustände nebeneinander: Strom steigt → u_i bremst; Strom sinkt → u_i treibt. | Hoch |

---

## ET/Spule/Spule_Typen.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/spule/spule_typen_uebersicht.svg | Vier Spulentypen als Zeichnung nebeneinander: (1) Luftspule: freischwebende Zylinderspule ohne Kern, mehrere Windungen sichtbar. (2) Ferritkernspule: Stabkern aus Ferrit (grau), Wicklung darauf, I-Kern oder E-Kern-Form. (3) Ringkerndrossel: Toroid (Donut-Form) mit Wicklung. (4) Common-Mode Drossel: Ringkern mit zwei gegensinnigen Wicklungen, je eine Windungsrichtung mit Pfeil. Je Typ Bezeichnung darunter. | Hoch |

---

## ET/Spule/Spule_Verluste.md  *(Artikel: NEU)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/spule/spule_ersatzschaltbild.svg | Reales Spulen-Ersatzschaltbild: R_Cu in Serie mit L (Hauptpfad). Parallel über die gesamte Reihenschaltung R_Cu + L liegt die parasitäre Wicklungskapazität C_par. Anschlüsse links und rechts. Beschriftung aller drei Elemente. Optionaler Hinweis: Selbstresonanzfrequenz = 1/(2·pi·sqrt(L·C_par)). | Hoch |

---

## ET/Grundlagen/Strom_Spannung_Widerstand.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/grundlagen/differenzieller_widerstand.svg | Nichtlineare U-I-Kennlinie (Diodenkurve, exponentielle Form). Arbeitspunkt AP markiert. Zwei Linien eingezeichnet: (1) Gerade vom Ursprung durch AP = statischer Widerstand R = U/I (als gestrichelte Sekante). (2) Tangente an die Kennlinie im AP = differenzieller Widerstand r_dif = ΔU/ΔI (als durchgezogene Linie, flacher als die Sekante). Achsen: x = U (V), y = I (A). ΔU und ΔI als kleine Pfeile am Tangentenpunkt eingezeichnet. | Hoch |

---

## ET/Grundlagen/NTC_PTC.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/grundlagen/ntc_ptc_symbole.svg | Nebeneinander: (1) NTC-Symbol: Widerstandsrechteck, zwei schräge Pfeile von links-unten zeigend (Wärme), Beschriftung „−Θ" oder „NTC". (2) PTC-Symbol: identischer Aufbau, Beschriftung „+Θ" oder „PTC". (3) Pt100-Symbol: Widerstandsrechteck mit Beschriftung „Pt100". Alle drei auf gemeinsamem Hintergrund mit Bezeichnung darunter. | Hoch |

---

## ET/Magnetfelder/Lorentzkraft.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/magnetfelder/lorentzkraft_leiter.svg | Leiter im Magnetfeld mit Winkel alpha. B-Feldlinien horizontal (Pfeile von links nach rechts). Leiter (dicker Strich) schräg eingezeichnet, Winkel alpha zwischen Leiter und B-Feldrichtung beschriftet. Stromrichtung I als Pfeil am Leiter. Kraft F senkrecht zur Bildebene (Kreis mit Punkt = aus der Ebene heraus). Gestrichelte Hilfslinie zeigt die wirksame Komponente l·sin(alpha) senkrecht zu B. Links daneben: Spezialfall alpha=90° (Leiter senkrecht, F maximal) und alpha=0° (Leiter parallel, F=0). | Hoch |

---

## ET/Kondensator/Auf_und_Entladung.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/kondensator/rc_ladeschaltung.svg | RC-Ladeschaltung: Spannungsquelle U0 (links), Schalter S, Widerstand R (oben), Kondensator C (rechts nach unten gegen GND). Pfeile für Strom I(t) und Spannungen U_R, U_C eingezeichnet. | Hoch |
| /schaltplaene/kondensator/konstantstrom_ladeschaltung.svg | Konstantstrom-Ladeschaltung: Stromquelle I (Pfeil nach oben, links), parallel dazu Kondensator C. U_C als Spannungspfeil am Kondensator. Hinweis: U_C steigt linear. | Hoch |

---

## ET/Kondensator/Energie_Kondensator.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/kondensator/energie_dreieck.svg | U-Q-Diagramm: x-Achse Q (Ladung, 0 bis Q_max), y-Achse U (Spannung, 0 bis U_max). Gerade Linie U = Q/C vom Ursprung bis (Q_max, U_max). Dreiecksfläche darunter grau schattiert, beschriftet „W = Fläche = ½·U·Q = ½·C·U²". Seiten des Dreiecks beschriftet: Basis = Q_max = C·U, Höhe = U_max. | Hoch |

---

## ET/Kondensator/Kondensator_Uebersicht.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/kondensator/kondensator_symbol.svg | Kondensator-Schaltsymbole nebeneinander: (1) unpolarisiert: zwei parallele Striche gleicher Länge mit Anschlussdrähten. (2) Elektrolytkondensator (gepolt): ein Strich gerade, einer gebogen (oder mit + markiert). Beschriftung C unter jedem Symbol. | Hoch |
| /schaltplaene/kondensator/kondensator_serie.svg | Zwei Kondensatoren C1, C2 in Serie: Reihenschaltung mit Spannungsquelle, Spannungspfeile U1, U2 an je einem Kondensator. C_ges-Formel als Label. | Mittel |
| /schaltplaene/kondensator/kondensator_parallel.svg | Zwei Kondensatoren C1, C2 parallel: beide zwischen denselben Knoten. Spannungsquelle links. C_ges-Label. | Mittel |

---

## ET/Kondensator/Kondensator_Typen.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/kondensator/kondensator_typen_uebersicht.svg | Fünf Kondensator-Bauformen nebeneinander als Zeichnung: (1) Elko (Aluminium-Zylinder, + markiert). (2) MLCC-SMD (kleines Rechteck, Lötkappen). (3) Folienkondensator (rechteckig/quaderförmig). (4) Tantalkondensator (Tropfenform, + markiert). (5) Superkap (grosser Zylinder). Je Typ Beschriftung mit Namen darunter. | Hoch |

---

## ET/Kondensator/Kondensator_Wechselstrom.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/kondensator/kondensator_wechselstrom_zeiger.svg | Einfaches Zeigerdiagramm: I-Zeiger (rot, nach oben = 90°), U_C-Zeiger (blau, nach rechts = 0°). I eilt U um 90° vor. Beschriftung: I, U_C, phi = 90°. | Mittel |

---

## ET/Kondensator/Kondensator_Verluste.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/kondensator/kondensator_ersatzschaltbild.svg | Reales Kondensator-Ersatzschaltbild: in Serie ESR (Widerstand-Symbol, beschriftet ESR), ESL (Spule-Symbol, beschriftet ESL), C (Kondensator-Symbol, beschriftet C). Parallel zu C ein grosser Widerstand R_leck (gestrichelt, beschriftet R_leck). Anschlüsse links und rechts. | Hoch |

---

## ET/Magnetfelder/Magnetisierungskurve.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/magnetfelder/weisssche_bezirke.svg | Links: unmagnetisiertes Material — Domänen zufällig orientiert. Rechts: magnetisiertes Material — Domänen ausgerichtet. | Hoch |
| /abbildungen/magnetfelder/hysteresekurve.svg | B-H-Diagramm: Neukurve (gestrichelt), vollständige Hystereseschleife, Sättigungspunkt (B_sat), Remanenz B_r (Schnittpunkt mit B-Achse), Koerzitivfeldstärke H_c (Schnittpunkt mit H-Achse). Weich- und Hartmagnet als Vergleich (schmale vs. breite Schleife). | Hoch |
| /abbildungen/magnetfelder/barkhausen_spruenge.svg | Zoom-Ansicht: Die scheinbar glatte Neukurve zeigt vergrössert eine Treppenstruktur — viele kleine Sprünge durch diskontinuierliche Domänenausrichtung. | Mittel |

---

## ET/Kondensator/Plattenkondensator.md  *(Artikel: NEU)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/kondensator/plattenkondensator_feld.svg | Plattenkondensator mit eingezeichneten E-Feldlinien (homogen zwischen den Platten, Randeffekte angedeutet). Abstand d und Fläche A beschriftet. | Hoch |
| /abbildungen/kondensator/influenz.svg | Influenz: leitende Platte in externem Feld — Ladungsverschiebung, Feldabschirmung (Faradayscher Käfig). | Mittel |

---

## ET/Wechselstrom/RLC_Reihenschaltung.md  *(Artikel: NEU)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/wechselstrom/rlc_reihe_zeigerdiagramm.svg | Zeigerdiagramm RLC-Reihe: U_R (in Phase mit I), U_L (90° vor I), U_C (90° hinter I), resultierende Gesamtspannung U. | Hoch |

---

## ET/Wechselstrom/RLC_Parallelschaltung.md  *(Artikel: NEU)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/wechselstrom/rlc_parallel_zeigerdiagramm.svg | Stromzeigerdiagramm RLC-Parallel: I_R (in Phase mit U), I_L (90° hinter U), I_C (90° vor U), resultierender Gesamtstrom I. | Hoch |

---

## ET/Schaltkreise/Reihenschaltung.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/reihenschaltung.svg | Reihenschaltung: Spannungsquelle U_ges links, dann R1, R2, R3 in Serie (geschlossener Kreis). Stromrichtung I mit Pfeil. Teilspannungen U1, U2, U3 als Pfeile an je einem Widerstand. | Hoch |

---

## ET/Schaltkreise/Parallelschaltung.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/parallelschaltung.svg | Parallelschaltung: Spannungsquelle U links, drei Zweige R1, R2, R3 parallel zwischen oberer und unterer Sammelschiene. Teilströme I1, I2, I3 als Pfeile in den Zweigen. Gesamtstrom I_ges an der Quelle. | Hoch |

---

## ET/Schaltkreise/Spannungs_Stromteiler.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/spannungsteiler.svg | Unbelasteter Spannungsteiler: Quelle U_e oben, R1 oben, R2 unten gegen GND. Ausgang U_a zwischen R1 und R2 abgegriffen (gestrichelte Linie nach rechts). Spannungspfeile U_e, U_a beschriftet. | Hoch |
| /schaltplaene/schaltkreise/stromteiler.svg | Stromteiler: Stromquelle I_ges links, zwei parallele Zweige R1 und R2. Teilströme I1 und I2 als Pfeile in den Zweigen. | Hoch |

---

## ET/Schaltkreise/Kirchhoffsche_Gesetze.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/kirchhoff_gesetze.svg | Zwei Teilbilder nebeneinander. Links KCL: Knoten mit drei Strömen: I1 zufliessend, I2 und I3 abfliessend. Beschriftung: "I1 = I2 + I3". Rechts KVL: Einfache Masche: Quelle U_Q, Widerstände R1 (U1) und R2 (U2). Umlaufpfeil und Beschriftung "U_Q = U1 + U2". | Hoch |

---

## ET/Schaltkreise/Wheatstone_Bruecke.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/wheatstone_bruecke.svg | Wheatstone-Brücke als Raute: oben Speisespannung U_e, unten GND. Linker Ast: R1 (oben) und R2 (unten). Rechter Ast: R3 (oben) und R4 (unten). Diagonale: Messinstrument (Voltmeter-Symbol) zwischen den zwei Seitenknoten. Knotenbezeichnungen: oben=A, unten=B, links=C, rechts=D. Spannungspfeile Ua (an R1) und Ub (an R3). U_br zwischen C und D. | Hoch |

---

## ET/Schaltkreise/Erzeuger_Ersatzschaltung.md  *(Artikel: NEU)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/thevenin_ersatzschaltung.svg | Thévenin-Ersatzschaltbild: Spannungsquelle U0 in Reihe mit Innenwiderstand Ri, Klemmen A/B rechts, optionaler Lastwiderstand Ra angedeutet. | Mittel |
| /schaltplaene/schaltkreise/norton_ersatzschaltung.svg | Norton-Ersatzschaltbild: Stromquelle Ik (Pfeil aufwärts) parallel mit Innenwiderstand Ri, Klemmen A/B rechts. Daneben Vergleichsgegenüberstellung: Thévenin-Symbol und Norton-Symbol mit Doppelpfeil "äquivalent". | Mittel |

---

## ET/Schaltkreise/Stern_Dreieck_Transformation.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/stern_dreieck_transformation.svg | Zwei Schaltbilder nebeneinander, verbunden durch Doppelpfeil "⇔". Links: Stern (Y) — drei Widerstände R1, R2, R3 von Knoten 1, 2, 3 zum gemeinsamen Sternpunkt. Rechts: Dreieck (Δ) — drei Widerstände R12, R23, R31 zwischen den Knoten 1-2, 2-3, 3-1. Beide Varianten mit denselben äusseren Knoten 1, 2, 3. | Hoch |

---

## ET/Schaltkreise/Superposition.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/schaltkreise/superposition_beispiel.svg | Drei Teilbilder untereinander oder nebeneinander: (1) Originalschaltung: Knoten A links (U1 = 12V), R1 = 100Ω von A nach B, R2 = 200Ω von B nach GND, Stromquelle I_Q = 50mA von B nach GND. (2) Schritt 1 — nur U1 aktiv: Stromquelle unterbrochen (offene Klemme). (3) Schritt 2 — nur I_Q aktiv: U1 kurzgeschlossen (Drahtbrücke). Jedes Teilbild mit Knotenspannung U'_B bzw. U''_B beschriftet. | Hoch |

---

## ET/Drehstrom/Sternschaltung.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/drehstrom/sternschaltung.svg | Sternschaltung: drei Lasten (Z1, Z2, Z3) von L1, L2, L3 zum gemeinsamen Sternpunkt. Neutralleiter N vom Sternpunkt nach unten. U_str (je Phase–Sternpunkt) und U_L (zwischen zwei Phasen) eingezeichnet. Spannungspfeile beschriftet. | Hoch |

---

## ET/Drehstrom/Dreieckschaltung.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /schaltplaene/drehstrom/dreieckschaltung.svg | Dreieckschaltung: drei Lasten (Z12, Z23, Z31) je zwischen zwei Phasen. Kein Sternpunkt, kein Neutralleiter. I_str (durch jede Last) und I_L (in den Zuleitungen) mit Pfeilen eingezeichnet. U_str = U_L = 400 V beschriftet. | Hoch |

---

## ET/Grundlagen/Widerstand.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/grundlagen/widerstand_kohleschicht_aufbau.svg | Querschnitt Kohleschichtwiderstand: Keramikzylinder, aufgedampfte Kohleschicht, spiralförmige Nut (Lasereinschnitt), Kappenelektroden und Anschlussdrähte. Spiralnut hervorgehoben mit Pfeil "Wendelschnitt erhöht R". | Hoch |
| /abbildungen/grundlagen/widerstand_metallschicht_aufbau.svg | Wie Kohleschicht, aber Metalloxidschicht statt Kohleschicht — beschriften: geringeres Rauschen, engere Toleranz. | Mittel |
| /abbildungen/grundlagen/widerstand_draht_aufbau.svg | Drahtwiderstand: Keramikträger mit aufgewickeltem Widerstandsdraht (Nickel-Chrom), Schutzmasse aussen, Anschlüsse. Hinweis: parasitäre Induktivität durch Wicklung. | Mittel |
| /abbildungen/grundlagen/widerstand_smd_aufbau.svg | SMD-Widerstand (Dickschicht): Aluminiumoxid-Substrat, gedruckte Widerstandsschicht, Lötkappen. Draufsicht + Seitenansicht. Gehäusegrösse 0805 als Beispiel beschriftet. | Hoch |

---

## ET/Transformator/Transformator_Typen.md  *(Artikel: PORT)*

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/transformator/transformator_typen_uebersicht.svg | Sechs Trafo-Typen als Schaltplandarstellung nebeneinander: (1) Netztransformator: E/I-Kern (grau), zwei getrennte Wicklungen N1/N2, Klemmen mit 230V / U2. (2) Trenntransformator: wie Netztransformator, aber N1=N2, Klemmen "1:1", Trennlinie zwischen Primär/Sekundär betont. (3) Spartransformator: eine Wicklung, Anzapfung, kein Trennstrich — Primär und Sekundär teilen sich die Wicklung. (4) Stromwandler (CT): Hauptleiter (dicker Strich) als Primärwindung, viele Sekundärwindungen, Last am Ausgang. (5) Ringkerntransformator: Toroid (Donut) mit Wicklungen. (6) HF-Trafo (Ferritkern): kleiner Ferritkern mit wenigen Windungen. Je Typ Bezeichnung darunter. | Hoch |
| /abbildungen/transformator/netztransformator_kern.svg | E/I-Kern-Transformator: E-förmiges Eisenblechpaket (links) und I-Stück (rechts), Primärwicklung auf dem Mittelschenkel (links, blau, mit Windungszahl N1), Sekundärwicklung daneben (rechts, rot, N2). Magnetischer Fluss im Kern mit Pfeil angedeutet. Klemmen links (230V~) und rechts (z.B. 12V~) beschriftet. | Hoch |
| /abbildungen/transformator/trenntransformator_schaltplan.svg | Schaltplan Trenntransformator: Trafo-Symbol mit zwei Wicklungen, Primärseite links (L/N/PE angeschlossen, geerdetes Netz), Sekundärseite rechts (Last, kein Erdbezug). Doppelter Trennstrich zwischen den Wicklungen als Symbol für galvanische Trennung. N1=N2 beschriftet, U2=U1 = 230V. Hinweis: "Sekundärseite nicht geerdet". | Hoch |
| /abbildungen/transformator/spartransformator_schaltplan.svg | Schaltplan Spartransformator: eine einzige Wicklung mit Anzapfung. Eingang (U1) an den Enden der Gesamtwicklung, Ausgang (U2) zwischen Anzapfung und einem Ende. Pfeil an der Anzapfung (regelbar: Schleifer). Kein Trennstrich — Primär und Sekundär sind elektrisch verbunden. Beschriftung: "keine galvanische Trennung". | Hoch |

---

## EK/Oszillatoren/Quarz_Oszillator.md

| Pfad | Beschreibung | Priorität |
|---|---|---|
| /abbildungen/ek/oszillatoren/quarz_ersatzschaltbild.svg | Elektrisches Ersatzschaltbild eines Quarzes: Hauptzweig Ls (Induktivität, einige mH) + Cs (sehr kleine Kapazität, fF) + Rs (Verlustwiderstand, 5–100 Ohm) in Reihe. Parallel dazu C0 (Gehäusekapazität, pF). Klemmen links und rechts. Beschriftung aller vier Elemente mit Wertebereichen. Zwei Resonanzfrequenzen andeuten: f_s (Serienresonanz, Minimum-Impedanz) und f_p (Parallelresonanz, Maximum-Impedanz) als kleine Pfeile oder Anmerkung. | Hoch |
| /abbildungen/ek/oszillatoren/quarz_pierce_schaltung.svg | Pierce-Oszillator Schaltplan: Inverter (CMOS-Gatter oder Transistor) mit Quarz in der Rückkopplungsschleife. Quarz zwischen Eingang und Ausgang des Inverters. Zwei Lastkapazitäten C1 und C2 je von Pin zur Masse. Rückkopplungswiderstand Rf (1–10 MOhm) parallel zum Inverter. Ausgang mit Serienwiderstand Rs zur Last. Beschriftung: f_0 = nominale Quarzfrequenz, C1/C2 = Lastkapazitäten (8–20 pF typisch). | Hoch |
