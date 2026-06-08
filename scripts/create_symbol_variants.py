"""
Erstellt alle Rotations-Varianten der Grundsymbole im Ordner symbole/rotiert/.

Namensschema:
  [Bauteil]_h.svg          symmetrisch, horizontal
  [Bauteil]_v.svg          symmetrisch, vertikal
  [Bauteil]_hl.svg         gerichtet, horizontal, Anode/+ links
  [Bauteil]_hr.svg         gerichtet, horizontal, Anode/+ rechts  (180°)
  [Bauteil]_vo.svg         gerichtet, vertikal,   Anode/+ oben    (90° CW)
  [Bauteil]_vu.svg         gerichtet, vertikal,   Anode/+ unten   (270° CW)
"""

import os
import sys
import shutil

sys.path.insert(0, os.path.dirname(__file__))
from rotate_svg import rotate_svg

SYMBOLE = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', 'artikel', 'schaltplaene', 'symbole')
)
OUT_DIR = os.path.join(SYMBOLE, 'rotiert')
os.makedirs(OUT_DIR, exist_ok=True)


def copy_as(src_name, dst_name):
    src = os.path.join(SYMBOLE, src_name)
    dst = os.path.join(OUT_DIR, dst_name)
    shutil.copy2(src, dst)
    print(f'    copy       {src_name:<40} -> {dst_name}')


def rotate_as(src_name, angle, dst_name):
    src = os.path.join(SYMBOLE, src_name)
    dst = os.path.join(OUT_DIR, dst_name)
    rotate_svg(src, angle, dst)
    label = f'{angle}° CW' if angle != 180 else '180°  '
    print(f'    {label:<10} {src_name:<40} -> {dst_name}')


# ── Symmetrische Bauelemente (h + v reicht) ────────────────────────────────
SYMMETRIC = [
    # (Quelldatei,                          Kurzname)
    ('widerstand_fest.svg',              'R'),
    ('widerstand_variabel.svg',          'R_var'),
    ('potentiometer.svg',                'R_pot'),
    ('kondensator_unpolarisiert_v2.svg', 'C'),
    ('kondensator_variabel.svg',         'C_var'),
    ('spule_fest.svg',                   'L'),
    ('spule_variabel.svg',               'L_var'),
    ('transformator_v5.svg',             'TR'),
]

# ── Gerichtete Bauelemente (alle 4 Richtungen) ─────────────────────────────
# Annahme: linker Pin = Anode / Plus im Original
DIRECTIONAL = [
    # (Quelldatei,                     Kurzname)
    ('diode_standard_v2.svg',       'D'),
    ('diode_zener_v2.svg',          'D_Z'),
    ('diode_schottky_v2.svg',       'D_S'),
    ('diode_led_v3.svg',            'D_LED'),
    ('diode_foto_v5.svg',           'D_Foto'),
    ('diac_v6.svg',                 'D_DIAC'),
    ('kondensator_polarisiert_v2.svg', 'C_pol'),
]


def main():
    print(f'Ziel-Ordner: {OUT_DIR}\n')

    print('-- Symmetrische Bauelemente ------------------------------------')
    for src, name in SYMMETRIC:
        if not os.path.isfile(os.path.join(SYMBOLE, src)):
            print(f'    FEHLT     {src}')
            continue
        copy_as(src, f'{name}_h.svg')
        rotate_as(src, 90, f'{name}_v.svg')

    print()
    print('-- Gerichtete Bauelemente --------------------------------------')
    for src, name in DIRECTIONAL:
        if not os.path.isfile(os.path.join(SYMBOLE, src)):
            print(f'    FEHLT     {src}')
            continue
        copy_as(src,   f'{name}_hl.svg')       # Anode/+ links   (Original)
        rotate_as(src, 90,  f'{name}_vo.svg')  # Anode/+ oben    (90° CW)
        rotate_as(src, 270, f'{name}_vu.svg')  # Anode/+ unten   (270° CW)
        rotate_as(src, 180, f'{name}_hr.svg')  # Anode/+ rechts  (180°)

    count = len(os.listdir(OUT_DIR))
    print(f'\nFertig — {count} Dateien in rotiert/')


if __name__ == '__main__':
    main()
