"""Setzt die :::hbox Navigations-Blöcke in alle ET-Stub-Dateien.

Jeder Artikel bekommt drei Spalten:
  - Voraussetzungen  (was man vorher kennen sollte)
  - Verwandte Artikel (gleichwertige Themen)
  - Führt weiter zu  (was als nächstes kommt)

Bestehender Inhalt unter dem zweiten '---' bleibt erhalten.
"""

from pathlib import Path

BASE = Path(__file__).parent.parent / "artikel" / "ET"

# Format: "Datei (relativ zu BASE)": (voraussetzungen, verwandt, weiter)
# Leere Liste = Abschnitt wird weggelassen.

LINKS: dict[str, tuple[list, list, list]] = {

    # ── GRUNDLAGEN ────────────────────────────────────────────────────────────
    "Grundlagen/Strom_Spannung_Widerstand.md": (
        [],
        ["[[Kirchhoffsche Gesetze]]"],
        ["[[Reihenschaltung]]", "[[Parallelschaltung]]",
         "[[Elektrische Leistung]]", "[[Leiterwiderstand]]"],
    ),
    "Grundlagen/Leiterwiderstand.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Elektrische Leistung]]", "[[NTC & PTC]]"],
        ["[[Skin-Effekt]]"],
    ),
    "Grundlagen/Elektrische_Leistung.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Wechselstromleistung]]"],
        ["[[Elektrische Arbeit & Tarif]]"],
    ),
    "Grundlagen/Elektrische_Arbeit_Tarif.md": (
        ["[[Elektrische Leistung]]"],
        [],
        [],
    ),
    "Grundlagen/Elektrisches_Feld.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Kondensator (Übersicht)]]"],
        ["[[Plattenkondensator & Influenz]]"],
    ),
    "Grundlagen/Elektrische_Ladung.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Kapazität & Einheiten]]"],
        [],
    ),
    "Grundlagen/Wellenlaenge.md": (
        ["[[Sinuswellen & Effektivwert]]"],
        [],
        [],
    ),
    "Grundlagen/Skineffekt.md": (
        ["[[Leiterwiderstand]]", "[[Sinuswellen & Effektivwert]]"],
        ["[[Magnetfelder]]"],
        [],
    ),

    # ── SCHALTKREISE ─────────────────────────────────────────────────────────
    "Schaltkreise/Reihenschaltung.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Parallelschaltung]]"],
        ["[[Spannungs- & Stromteiler]]", "[[Kirchhoffsche Gesetze]]"],
    ),
    "Schaltkreise/Parallelschaltung.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Reihenschaltung]]"],
        ["[[Spannungs- & Stromteiler]]", "[[Kirchhoffsche Gesetze]]"],
    ),
    "Schaltkreise/Spannungs_Stromteiler.md": (
        ["[[Reihenschaltung]]", "[[Parallelschaltung]]"],
        ["[[Erzeuger-Ersatzschaltung (Thévenin)]]"],
        ["[[Leistungsanpassung]]", "[[Brückenschaltung (Wheatstone)]]"],
    ),
    "Schaltkreise/Kirchhoffsche_Gesetze.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Reihenschaltung]]", "[[Parallelschaltung]]"],
        ["[[Knotenpotenzialanalyse]]", "[[Superposition (Mehrere Quellen)]]"],
    ),
    "Schaltkreise/Knotenpotenzialanalyse.md": (
        ["[[Kirchhoffsche Gesetze]]"],
        ["[[Superposition (Mehrere Quellen)]]"],
        [],
    ),
    "Schaltkreise/Superposition.md": (
        ["[[Kirchhoffsche Gesetze]]"],
        ["[[Erzeuger-Ersatzschaltung (Thévenin)]]"],
        ["[[Knotenpotenzialanalyse]]"],
    ),
    "Schaltkreise/Erzeuger_Ersatzschaltung.md": (
        ["[[Strom, Spannung, Widerstand]]", "[[Spannungs- & Stromteiler]]"],
        ["[[Superposition (Mehrere Quellen)]]"],
        ["[[Leistungsanpassung]]"],
    ),
    "Schaltkreise/Leistungsanpassung.md": (
        ["[[Erzeuger-Ersatzschaltung (Thévenin)]]", "[[Spannungs- & Stromteiler]]"],
        ["[[Elektrische Leistung]]"],
        [],
    ),
    "Schaltkreise/Wheatstone_Bruecke.md": (
        ["[[Reihenschaltung]]", "[[Parallelschaltung]]"],
        ["[[Spannungs- & Stromteiler]]"],
        [],
    ),
    "Schaltkreise/Stern_Dreieck_Transformation.md": (
        ["[[Reihenschaltung]]", "[[Parallelschaltung]]"],
        ["[[Drehstrom Grundlagen]]"],
        [],
    ),

    # ── WECHSELSTROM ─────────────────────────────────────────────────────────
    "Wechselstrom/Sinuswellen.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Zeigerdiagramm]]"],
        ["[[Impedanz]]", "[[Wellenlänge]]", "[[Wechselstromleistung]]"],
    ),
    "Wechselstrom/Zeigerdiagramm.md": (
        ["[[Sinuswellen & Effektivwert]]"],
        ["[[Impedanz]]"],
        ["[[RL-Reihenschaltung]]", "[[RC-Reihenschaltung]]"],
    ),
    "Wechselstrom/Impedanz.md": (
        ["[[Sinuswellen & Effektivwert]]",
         "[[Kondensator im Wechselstrom]]",
         "[[Spule im Wechselstrom]]"],
        ["[[Zeigerdiagramm]]"],
        ["[[RL-Reihenschaltung]]", "[[RC-Reihenschaltung]]"],
    ),
    "Wechselstrom/RL_Reihenschaltung.md": (
        ["[[Impedanz]]", "[[Spule im Wechselstrom]]"],
        ["[[RC-Reihenschaltung]]"],
        ["[[RL-Parallelschaltung]]", "[[RLC-Reihenschaltung (Serieschwingkreis)]]"],
    ),
    "Wechselstrom/RC_Reihenschaltung.md": (
        ["[[Impedanz]]", "[[Kondensator im Wechselstrom]]"],
        ["[[RL-Reihenschaltung]]"],
        ["[[RC-Parallelschaltung]]", "[[RLC-Reihenschaltung (Serieschwingkreis)]]"],
    ),
    "Wechselstrom/RL_Parallelschaltung.md": (
        ["[[RL-Reihenschaltung]]"],
        ["[[RC-Parallelschaltung]]"],
        ["[[RLC-Parallelschaltung (Parallelschwingkreis)]]"],
    ),
    "Wechselstrom/RC_Parallelschaltung.md": (
        ["[[RC-Reihenschaltung]]"],
        ["[[RL-Parallelschaltung]]"],
        ["[[RLC-Parallelschaltung (Parallelschwingkreis)]]"],
    ),
    "Wechselstrom/RLC_Reihenschaltung.md": (
        ["[[RL-Reihenschaltung]]", "[[RC-Reihenschaltung]]"],
        ["[[RLC-Parallelschaltung (Parallelschwingkreis)]]"],
        ["[[Resonanz & Schwingkreise]]"],
    ),
    "Wechselstrom/RLC_Parallelschaltung.md": (
        ["[[RL-Parallelschaltung]]", "[[RC-Parallelschaltung]]"],
        ["[[RLC-Reihenschaltung (Serieschwingkreis)]]"],
        ["[[Resonanz & Schwingkreise]]"],
    ),
    "Wechselstrom/Resonanz.md": (
        ["[[RLC-Reihenschaltung (Serieschwingkreis)]]",
         "[[RLC-Parallelschaltung (Parallelschwingkreis)]]"],
        [],
        ["[[LC-Filter]]", "[[Quarz-Oszillator]]"],
    ),
    "Wechselstrom/Wechselstromleistung.md": (
        ["[[Sinuswellen & Effektivwert]]", "[[Impedanz]]"],
        ["[[Elektrische Leistung]]"],
        ["[[Blindleistungskompensation]]"],
    ),
    "Wechselstrom/Blindleistungskompensation.md": (
        ["[[Wechselstromleistung]]"],
        ["[[Kondensator (Übersicht)]]"],
        [],
    ),
    "Wechselstrom/LC_Filter.md": (
        ["[[Resonanz & Schwingkreise]]"],
        [],
        ["[[Quarz-Oszillator]]"],
    ),
    "Wechselstrom/Quarz_Oszillator.md": (
        ["[[Resonanz & Schwingkreise]]"],
        [],
        [],
    ),

    # ── KONDENSATOR ──────────────────────────────────────────────────────────
    "Kondensator/Kondensator_Uebersicht.md": (
        ["[[Strom, Spannung, Widerstand]]", "[[Elektrisches Feld]]"],
        ["[[Spule (Übersicht)]]"],
        ["[[Kondensator Typen]]", "[[Plattenkondensator & Influenz]]",
         "[[Kapazität & Einheiten]]"],
    ),
    "Kondensator/Kondensator_Typen.md": (
        ["[[Kondensator (Übersicht)]]"],
        [],
        [],
    ),
    "Kondensator/Plattenkondensator.md": (
        ["[[Elektrisches Feld]]", "[[Kondensator (Übersicht)]]"],
        [],
        ["[[Kapazität & Einheiten]]"],
    ),
    "Kondensator/Kapazitaet_Einheiten.md": (
        ["[[Kondensator (Übersicht)]]"],
        ["[[Elektrische Ladung & Elementarladung]]"],
        [],
    ),
    "Kondensator/Energie_Kondensator.md": (
        ["[[Kapazität & Einheiten]]"],
        ["[[Spule (Übersicht)]]"],
        [],
    ),
    "Kondensator/Konstantstrom_Laden.md": (
        ["[[Auf- und Entladung (RC)]]"],
        [],
        [],
    ),
    "Kondensator/Auf_und_Entladung.md": (
        ["[[Kapazität & Einheiten]]", "[[Strom, Spannung, Widerstand]]"],
        ["[[Auf- und Entladung (RL)]]"],
        ["[[Energie im Kondensator]]", "[[RC-Reihenschaltung]]"],
    ),
    "Kondensator/Kondensator_Wechselstrom.md": (
        ["[[Kondensator (Übersicht)]]", "[[Sinuswellen & Effektivwert]]"],
        ["[[Spule im Wechselstrom]]"],
        ["[[RC-Reihenschaltung]]", "[[RC-Parallelschaltung]]"],
    ),
    "Kondensator/Kondensator_Verluste.md": (
        ["[[Kondensator im Wechselstrom]]"],
        ["[[Verluste in der Spule (Güte, Wicklungswiderstand)]]"],
        ["[[RC-Reihenschaltung]]"],
    ),

    # ── SPULE ────────────────────────────────────────────────────────────────
    "Spule/Spule_Uebersicht.md": (
        ["[[Magnetfelder]]"],
        ["[[Kondensator (Übersicht)]]"],
        ["[[Spule Typen]]", "[[Induktivität & Einheiten]]", "[[Selbstinduktion & Induzierte Spannung]]"],
    ),
    "Spule/Spule_Typen.md": (
        ["[[Spule (Übersicht)]]"],
        [],
        [],
    ),
    "Spule/Induktivitaet_Einheiten.md": (
        ["[[Spule (Übersicht)]]"],
        [],
        [],
    ),
    "Spule/Selbstinduktion.md": (
        ["[[Magnetfelder]]", "[[Spule (Übersicht)]]"],
        ["[[Magnetisierungskurve & Hysterese]]"],
        ["[[Auf- und Entladung (RL)]]"],
    ),
    "Spule/Auf_und_Entladung_RL.md": (
        ["[[Induktivität & Einheiten]]", "[[Strom, Spannung, Widerstand]]"],
        ["[[Auf- und Entladung (RC)]]"],
        ["[[RL-Reihenschaltung]]"],
    ),
    "Spule/Spule_Wechselstrom.md": (
        ["[[Selbstinduktion & Induzierte Spannung]]", "[[Sinuswellen & Effektivwert]]"],
        ["[[Kondensator im Wechselstrom]]"],
        ["[[RL-Reihenschaltung]]", "[[RL-Parallelschaltung]]"],
    ),
    "Spule/Spule_Verluste.md": (
        ["[[Spule im Wechselstrom]]"],
        ["[[Verluste im Kondensator (Güte, ESR)]]"],
        ["[[RL-Reihenschaltung]]"],
    ),

    # ── TRANSFORMATOR ────────────────────────────────────────────────────────
    "Transformator/Transformator_Aufbau.md": (
        ["[[Spule (Übersicht)]]", "[[Magnetfelder]]",
         "[[Magnetisierungskurve & Hysterese]]"],
        ["[[Transformator Typen]]"],
        ["[[Übersetzungsverhältnis]]"],
    ),
    "Transformator/Transformator_Typen.md": (
        ["[[Transformator Aufbau]]"],
        [],
        [],
    ),
    "Transformator/Uebersetzungsverhaeltnis.md": (
        ["[[Transformator Aufbau]]"],
        [],
        ["[[Wirkungsgrad & Verluste]]"],
    ),
    "Transformator/Wirkungsgrad_Verluste.md": (
        ["[[Übersetzungsverhältnis]]", "[[Magnetisierungskurve & Hysterese]]"],
        ["[[Elektrische Leistung]]"],
        [],
    ),

    # ── MAGNETFELDER ─────────────────────────────────────────────────────────
    "Magnetfelder/Magnetfelder.md": (
        ["[[Strom, Spannung, Widerstand]]"],
        ["[[Elektromagnet]]", "[[Lorentzkraft]]",
         "[[Magnetisierungskurve & Hysterese]]"],
        ["[[Spule (Übersicht)]]", "[[Transformator Aufbau]]"],
    ),
    "Magnetfelder/Magnetisierungskurve.md": (
        ["[[Magnetfelder]]"],
        ["[[Elektromagnet]]"],
        ["[[Transformator Aufbau]]", "[[Spule Typen]]"],
    ),
    "Magnetfelder/Elektromagnet.md": (
        ["[[Magnetfelder]]"],
        [],
        ["[[Magnetischer Widerstand]]"],
    ),
    "Magnetfelder/Lorentzkraft.md": (
        ["[[Magnetfelder]]"],
        [],
        [],
    ),
    "Magnetfelder/Magnetische_Flussdichte.md": (
        ["[[Magnetfelder]]"],
        [],
        [],
    ),
    "Magnetfelder/Magnetischer_Widerstand.md": (
        ["[[Magnetfelder]]"],
        ["[[Elektromagnet]]"],
        [],
    ),

    # ── DREHSTROM ────────────────────────────────────────────────────────────
    "Drehstrom/Drehstrom_Grundlagen.md": (
        ["[[Sinuswellen & Effektivwert]]", "[[Wechselstromleistung]]"],
        [],
        ["[[Sternschaltung]]", "[[Dreieckschaltung]]",
         "[[Verkettete Spannung]]"],
    ),
    "Drehstrom/Sternschaltung.md": (
        ["[[Drehstrom Grundlagen]]"],
        ["[[Dreieckschaltung]]", "[[Stern-Dreieck-Transformation]]"],
        [],
    ),
    "Drehstrom/Dreieckschaltung.md": (
        ["[[Drehstrom Grundlagen]]"],
        ["[[Sternschaltung]]", "[[Stern-Dreieck-Transformation]]"],
        [],
    ),
    "Drehstrom/Verkettete_Spannung.md": (
        ["[[Drehstrom Grundlagen]]"],
        ["[[Sternschaltung]]", "[[Dreieckschaltung]]"],
        [],
    ),
}


def make_hbox(voraussetzungen: list, verwandt: list, weiter: list) -> str:
    """Erstellt den :::hbox Block mit nur nicht-leeren Spalten."""
    cols = []
    if voraussetzungen:
        items = "\n".join(f"- {v}" for v in voraussetzungen)
        cols.append(f":::vbox\n**Voraussetzungen**\n{items}\n:::")
    if verwandt:
        items = "\n".join(f"- {v}" for v in verwandt)
        cols.append(f":::vbox\n**Verwandte Artikel**\n{items}\n:::")
    if weiter:
        items = "\n".join(f"- {v}" for v in weiter)
        cols.append(f":::vbox\n**Führt weiter zu**\n{items}\n:::")
    if not cols:
        return ""
    return ":::hbox\n" + "\n".join(cols) + "\n:::"


def update_file(rel_path: str, vor: list, ver: list, wei: list) -> None:
    path = BASE / rel_path
    if not path.exists():
        print(f"  FEHLT: {rel_path}")
        return

    text = path.read_text(encoding="utf-8")

    # Frontmatter extrahieren (zwischen erstem und zweitem ---)
    parts = text.split("---", 2)
    if len(parts) < 3:
        print(f"  KEIN FRONTMATTER: {rel_path}")
        return

    frontmatter = parts[1]
    body = parts[2].lstrip("\n")

    # Alten hbox Block entfernen falls vorhanden
    if body.startswith(":::hbox"):
        end = body.find("\n:::\n", body.find(":::hbox"))
        if end != -1:
            body = body[end + 5:].lstrip("\n")

    hbox = make_hbox(vor, ver, wei)
    if hbox:
        new_body = hbox + "\n\n---\n\n" + body
    else:
        new_body = "---\n\n" + body

    new_text = f"---{frontmatter}---\n\n{new_body}"
    path.write_text(new_text, encoding="utf-8")
    print(f"  OK: {rel_path}")


if __name__ == "__main__":
    print("Setze Links...\n")
    for rel, (v, vw, w) in LINKS.items():
        update_file(rel, v, vw, w)
    print(f"\nFertig — {len(LINKS)} Dateien verarbeitet.")
