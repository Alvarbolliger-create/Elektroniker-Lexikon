"""
Dreht ein SVG-Schaltplan-Symbol um 90°, 180° oder 270°.

Verwendung:
  python scripts/rotate_svg.py R.svg 90            → R_90.svg (im gleichen Ordner)
  python scripts/rotate_svg.py R.svg 90 R_v.svg    → R_v.svg
  python scripts/rotate_svg.py --batch 90           → alle Symbole im symbole/-Ordner

Winkel: 90 = im Uhrzeigersinn, 270 (oder -90) = gegen Uhrzeigersinn, 180 = umgedreht

Hinweis: Texte (z.B. +/− am OPV) werden mitgedreht. Für Symbole ohne Text
funktioniert das einwandfrei. Bei beschrifteten Symbolen ggf. manuell nachbearbeiten.
"""

import os
import re
import sys
import glob

SYMBOLE_DIR = os.path.join(os.path.dirname(__file__), '..', 'artikel', 'schaltplaene', 'symbole')


def parse_svg_dimensions(content: str):
    """Liest viewBox, width und height aus dem SVG-Header."""
    vb = re.search(r'viewBox=["\'](\S+)\s+(\S+)\s+(\S+)\s+(\S+)["\']', content)
    w  = re.search(r'\bwidth=["\'](\d+(?:\.\d+)?)["\']', content)
    h  = re.search(r'\bheight=["\'](\d+(?:\.\d+)?)["\']', content)

    if vb:
        W = float(vb.group(3))
        H = float(vb.group(4))
    elif w and h:
        W = float(w.group(1))
        H = float(h.group(1))
    else:
        raise ValueError("Keine viewBox oder width/height im SVG gefunden.")

    return W, H


def build_transform(angle: int, W: float, H: float):
    """
    Gibt (transform_str, new_W, new_H) zurück.

    Koordinatentransformationen:
      90° CW:  translate(H, 0) rotate(90)   → neue Grösse: H × W
     270° CCW: translate(0, W) rotate(-90)  → neue Grösse: H × W
     180°:     translate(W, H) rotate(180)  → neue Grösse: W × H
    """
    a = angle % 360
    if a == 90:
        return f"translate({H:g}, 0) rotate(90)", H, W
    elif a == 270:
        return f"translate(0, {W:g}) rotate(-90)", H, W
    elif a == 180:
        return f"translate({W:g}, {H:g}) rotate(180)", W, H
    else:
        raise ValueError(f"Ungültiger Winkel: {angle}. Erlaubt: 90, 180, 270.")


def rotate_svg(input_path: str, angle: int, output_path: str = None) -> str:
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    W, H = parse_svg_dimensions(content)
    transform, nW, nH = build_transform(angle, W, H)

    # Inhalt zwischen den SVG-Tags extrahieren
    inner_match = re.search(r'<svg[^>]*>(.*?)</svg>', content, re.DOTALL)
    if not inner_match:
        raise ValueError(f"Konnte SVG-Inhalt nicht parsen: {input_path}")
    inner = inner_match.group(1)

    new_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {nW:g} {nH:g}" width="{nW:g}" height="{nH:g}">\n'
        f'  <g transform="{transform}">\n'
        f'{inner}'
        f'  </g>\n'
        f'</svg>\n'
    )

    if output_path is None:
        stem, ext = os.path.splitext(input_path)
        output_path = f"{stem}_{angle}{ext}"

    with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_svg)

    return output_path


def main():
    args = sys.argv[1:]

    if not args or '--help' in args or '-h' in args:
        print(__doc__)
        return

    # Batch-Modus: --batch <winkel>
    if '--batch' in args:
        idx = args.index('--batch')
        angle = int(args[idx + 1])
        pattern = os.path.join(SYMBOLE_DIR, '*.svg')
        files = sorted(glob.glob(pattern))
        # Bereits rotierte Dateien überspringen (enthalten _90, _180, _270 im Namen)
        files = [f for f in files if not re.search(r'_(90|180|270)\.svg$', f)]
        print(f"Rotiere {len(files)} Symbole um {angle}°...\n")
        for f in files:
            out = rotate_svg(f, angle)
            print(f"  {os.path.basename(f)} → {os.path.basename(out)}")
        print(f"\nFertig: {len(files)} Dateien erstellt.")
        return

    # Einzeldatei-Modus
    if len(args) < 2:
        print("Verwendung: rotate_svg.py <datei.svg> <winkel> [ausgabe.svg]")
        return

    input_path = args[0]
    angle = int(args[1])
    output_path = args[2] if len(args) > 2 else None

    # Relativer Pfad: erst im symbole-Ordner suchen
    if not os.path.isfile(input_path):
        candidate = os.path.join(SYMBOLE_DIR, input_path)
        if os.path.isfile(candidate):
            input_path = candidate
            if output_path and not os.path.dirname(output_path):
                output_path = os.path.join(SYMBOLE_DIR, output_path)

    out = rotate_svg(input_path, angle, output_path)
    print(f"Gespeichert: {out}")


if __name__ == '__main__':
    main()
