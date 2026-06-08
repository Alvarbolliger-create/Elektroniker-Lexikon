"""
Entfernt Hintergrund, Gitter und Debug-Elemente aus Schaltplan-SVG-Symbolen.

Was wird entfernt:
  - <defs> Block mit Gitter-Pattern
  - Hintergrund-<rect> Elemente (200x200 ohne x/y-Offset)
  - Inline style="..." Attribute (überschreiben CSS-Variablen mit hardcodierten Farben)
  - Rote Verbindungspunkt-Kreise (fill="#E24B4A") -- optional, siehe REMOVE_DOTS

Verwendung:
  python scripts/clean_svg_backgrounds.py
  python scripts/clean_svg_backgrounds.py --keep-dots    (Verbindungspunkte behalten)
  python scripts/clean_svg_backgrounds.py --dry-run      (nur anzeigen, nichts schreiben)
"""

import os
import re
import glob
import sys

SYMBOLE_DIR = os.path.join(os.path.dirname(__file__), '..', 'artikel', 'schaltplaene', 'symbole')

REMOVE_DOTS = '--keep-dots' not in sys.argv
DRY_RUN = '--dry-run' in sys.argv


def clean_svg(content: str, remove_dots: bool = True) -> str:
    # 1. <defs>...</defs> Block entfernen
    content = re.sub(r'\n?\s*<defs[^>]*>.*?</defs>', '', content, flags=re.DOTALL)

    # 2. Hintergrund-Rechtecke entfernen (width="200" height="200" ohne x/y-Offset)
    content = re.sub(r'\n?\s*<rect width="200" height="200"[^>]*/>', '', content)

    # 3. Inline style="..." Attribute entfernen (auf allen Elementen)
    content = re.sub(r'\s+style="[^"]*"', '', content)

    # 4. Rote Verbindungspunkte entfernen (optionale Debug-Marker)
    if remove_dots:
        content = re.sub(r'\n?\s*<circle[^>]*fill="#E24B4A"[^>]*/>', '', content)

    # CSS-Variablen durch hardcodierte Farben ersetzen (sonst unsichtbar ohne Lexikon-CSS)
    content = content.replace('var(--color-text-primary)',       '#1e293b')
    content = content.replace('var(--color-background-primary)', 'none')

    # Mehrfache Leerzeilen auf eine reduzieren
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def process_file(filepath: str, remove_dots: bool, dry_run: bool) -> bool:
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    cleaned = clean_svg(original, remove_dots)

    if cleaned == original:
        return False

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(cleaned)

    return True


def main():
    pattern = os.path.join(SYMBOLE_DIR, '*.svg')
    files = sorted(glob.glob(pattern))

    if not files:
        print(f'Keine SVG-Dateien gefunden in: {SYMBOLE_DIR}')
        return

    mode = '(DRY RUN) ' if DRY_RUN else ''
    dots = 'behalten' if not REMOVE_DOTS else 'entfernen'
    print(f'{mode}Verarbeite {len(files)} SVG-Dateien | Verbindungspunkte: {dots}\n')

    modified = 0
    skipped = 0
    for filepath in files:
        name = os.path.basename(filepath)
        changed = process_file(filepath, REMOVE_DOTS, DRY_RUN)
        if changed:
            prefix = '~' if DRY_RUN else 'ok'
            print(f'  [{prefix}] {name}')
            modified += 1
        else:
            print(f'  [--] {name}  (bereits sauber)')
            skipped += 1

    action = 'werden geändert' if DRY_RUN else 'geändert'
    print(f'\n{modified} Dateien {action}, {skipped} bereits sauber.')


if __name__ == '__main__':
    main()
