#!/usr/bin/env python3
"""
Generiert 12 Schaltplan-SVGs: R/C/L in Serie und Parallel, RC/RL/RLC Kombinationen.
Ausgabe: artikel/schaltplaene/
"""

import os

OUT_DIR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', 'artikel', 'schaltplaene')
)

_C = '#1e293b'
_SW = '1.5'


def _ln(x1, y1, x2, y2):
    return (f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"'
            f' stroke="{_C}" stroke-width="{_SW}" stroke-linecap="round"/>')


def _tx(x, y, t, anchor='middle'):
    return (f'  <text x="{x}" y="{y}" font-size="11" font-family="sans-serif"'
            f' fill="{_C}" text-anchor="{anchor}" dominant-baseline="middle">{t}</text>')


def _dot(x, y):
    return f'  <circle cx="{x}" cy="{y}" r="2.5" fill="{_C}"/>'


def _vsource(cx, cy, r=18):
    """
    Norm-gerechte Spannungsquelle: Kreis mit vertikalem Innenstrich und + Zeichen.
    Proportionen aus V.svg (Originalkreis r=40, Strich ±30, Plus bei (-20,-20), Arm 5).
    """
    s = r / 40.0
    vl  = r * 0.75          # halbe Innenstrecklänge (30/40)
    px  = round(cx - 20*s)  # Plus-Mitte X
    py  = round(cy - 20*s)  # Plus-Mitte Y
    arm = max(3, round(5*s)) # Plusarm-Länge, mindestens 3 px
    return [
        f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none"'
        f' stroke="{_C}" stroke-width="{_SW}"/>',
        f'  <line x1="{cx}" y1="{round(cy-vl)}" x2="{cx}" y2="{round(cy+vl)}"'
        f' stroke="{_C}" stroke-width="{_SW}" stroke-linecap="round"/>',
        f'  <line x1="{px-arm}" y1="{py}" x2="{px+arm}" y2="{py}"'
        f' stroke="{_C}" stroke-width="{_SW}" stroke-linecap="round"/>',
        f'  <line x1="{px}" y1="{py-arm}" x2="{px}" y2="{py+arm}"'
        f' stroke="{_C}" stroke-width="{_SW}" stroke-linecap="round"/>',
    ]


def _comp_h(kind, cx, cy):
    """Horizontale Komponente mit +-21 px Footprint."""
    if kind == 'R':
        return [
            _ln(cx - 21, cy, cx - 18, cy),
            (f'  <rect x="{cx - 18}" y="{cy - 7}" width="36" height="14"'
             f' fill="none" stroke="{_C}" stroke-width="{_SW}"/>'),
            _ln(cx + 18, cy, cx + 21, cy),
        ]
    if kind == 'C':
        return [
            _ln(cx - 21, cy, cx - 4, cy),
            (f'  <line x1="{cx - 4}" y1="{cy - 9}" x2="{cx - 4}" y2="{cy + 9}"'
             f' stroke="{_C}" stroke-width="2.0" stroke-linecap="round"/>'),
            (f'  <line x1="{cx + 4}" y1="{cy - 9}" x2="{cx + 4}" y2="{cy + 9}"'
             f' stroke="{_C}" stroke-width="2.0" stroke-linecap="round"/>'),
            _ln(cx + 4, cy, cx + 21, cy),
        ]
    if kind == 'L':
        d = (f'M {cx - 21},{cy}'
             f' A 7,7 0 0 0 {cx - 7},{cy}'
             f' A 7,7 0 0 0 {cx + 7},{cy}'
             f' A 7,7 0 0 0 {cx + 21},{cy}')
        return [(f'  <path d="{d}" fill="none" stroke="{_C}"'
                 f' stroke-width="{_SW}" stroke-linecap="round"/>')]
    return []


def _comp_v(kind, cx, cy):
    """Vertikale Komponente mit +-21 px Footprint."""
    if kind == 'R':
        return [
            _ln(cx, cy - 21, cx, cy - 18),
            (f'  <rect x="{cx - 7}" y="{cy - 18}" width="14" height="36"'
             f' fill="none" stroke="{_C}" stroke-width="{_SW}"/>'),
            _ln(cx, cy + 18, cx, cy + 21),
        ]
    if kind == 'C':
        return [
            _ln(cx, cy - 21, cx, cy - 4),
            (f'  <line x1="{cx - 9}" y1="{cy - 4}" x2="{cx + 9}" y2="{cy - 4}"'
             f' stroke="{_C}" stroke-width="2.0" stroke-linecap="round"/>'),
            (f'  <line x1="{cx - 9}" y1="{cy + 4}" x2="{cx + 9}" y2="{cy + 4}"'
             f' stroke="{_C}" stroke-width="2.0" stroke-linecap="round"/>'),
            _ln(cx, cy + 4, cx, cy + 21),
        ]
    if kind == 'L':
        d = (f'M {cx},{cy - 21}'
             f' A 7,7 0 0 1 {cx},{cy - 7}'
             f' A 7,7 0 0 1 {cx},{cy + 7}'
             f' A 7,7 0 0 1 {cx},{cy + 21}')
        return [(f'  <path d="{d}" fill="none" stroke="{_C}"'
                 f' stroke-width="{_SW}" stroke-linecap="round"/>')]
    return []


def make_series(components, labels):
    n = len(components)
    if n == 2:
        W, comp_xs = 260, [80, 180]
    else:
        W, comp_xs = 320, [80, 160, 240]
    H = 120
    top_y, bot_y = 35, 105
    vs_cy = (top_y + bot_y) // 2   # 70
    vs_r = 18
    lx, rx = 20, W - 20

    els = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"'
           f' width="{W}" height="{H}">', '']

    # Linke Seite: Spannungsquelle
    els.append(_ln(lx, top_y, lx, vs_cy - vs_r))
    els.extend(_vsource(lx, vs_cy, vs_r))
    els.append(_ln(lx, vs_cy + vs_r, lx, bot_y))

    # Obere Schiene mit Bauteilen
    prev = lx
    for cx, kind in zip(comp_xs, components):
        els.append(_ln(prev, top_y, cx - 21, top_y))
        els.extend(_comp_h(kind, cx, top_y))
        prev = cx + 21
    els.append(_ln(prev, top_y, rx, top_y))

    # Rechte und untere Schiene
    els.append(_ln(rx, top_y, rx, bot_y))
    els.append(_ln(lx, bot_y, rx, bot_y))

    # Bauteilbeschriftung
    for cx, lbl in zip(comp_xs, labels):
        els.append(_tx(cx, top_y - 17, lbl))

    els += ['', '</svg>']
    return '\n'.join(els)


def make_parallel(components, labels):
    n = len(components)
    if n == 2:
        W, branch_xs = 220, [70, 150]
    else:
        W, branch_xs = 300, [70, 150, 230]
    H = 170
    top_y, bot_y = 20, 150
    comp_cy = (top_y + bot_y) // 2   # 85
    vs_r = 18
    lx, rx = 20, W - 20

    els = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"'
           f' width="{W}" height="{H}">', '']

    # Linke Seite: Spannungsquelle
    els.append(_ln(lx, top_y, lx, comp_cy - vs_r))
    els.extend(_vsource(lx, comp_cy, vs_r))
    els.append(_ln(lx, comp_cy + vs_r, lx, bot_y))

    # Obere und untere Sammelschiene
    els.append(_ln(lx, top_y, rx, top_y))
    els.append(_ln(lx, bot_y, rx, bot_y))

    # Rechte Schiene (Schlusskante)
    els.append(_ln(rx, top_y, rx, bot_y))

    # Zweige: Verbindungspunkte + Draht + Bauteil
    for bx, kind in zip(branch_xs, components):
        els.append(_dot(bx, top_y))
        els.append(_ln(bx, top_y, bx, comp_cy - 21))
        els.extend(_comp_v(kind, bx, comp_cy))
        els.append(_ln(bx, comp_cy + 21, bx, bot_y))
        els.append(_dot(bx, bot_y))

    # Bauteilbeschriftung
    for bx, lbl in zip(branch_xs, labels):
        els.append(_tx(bx + 13, comp_cy, lbl, anchor='start'))

    els += ['', '</svg>']
    return '\n'.join(els)


CIRCUITS = [
    ('r_reihe.svg',      make_series,   ['R', 'R', 'R'], ['R1', 'R2', 'R3']),
    ('c_reihe.svg',      make_series,   ['C', 'C', 'C'], ['C1', 'C2', 'C3']),
    ('l_reihe.svg',      make_series,   ['L', 'L', 'L'], ['L1', 'L2', 'L3']),
    ('rc_reihe.svg',     make_series,   ['R', 'C'],       ['R1', 'C1']),
    ('rl_reihe.svg',     make_series,   ['R', 'L'],       ['R1', 'L1']),
    ('rlc_reihe.svg',    make_series,   ['R', 'L', 'C'],  ['R1', 'L1', 'C1']),
    ('r_parallel.svg',   make_parallel, ['R', 'R', 'R'], ['R1', 'R2', 'R3']),
    ('c_parallel.svg',   make_parallel, ['C', 'C', 'C'], ['C1', 'C2', 'C3']),
    ('l_parallel.svg',   make_parallel, ['L', 'L', 'L'], ['L1', 'L2', 'L3']),
    ('rc_parallel.svg',  make_parallel, ['R', 'C'],       ['R1', 'C1']),
    ('rl_parallel.svg',  make_parallel, ['R', 'L'],       ['R1', 'L1']),
    ('rlc_parallel.svg', make_parallel, ['R', 'L', 'C'],  ['R1', 'L1', 'C1']),
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f'Ausgabe: {OUT_DIR}\n')
    for fname, fn, comps, lbls in CIRCUITS:
        svg = fn(comps, lbls)
        path = os.path.join(OUT_DIR, fname)
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(svg)
        print(f'  ok  {fname}')
    print(f'\n{len(CIRCUITS)} Schaltplaene neu generiert.')


if __name__ == '__main__':
    main()
