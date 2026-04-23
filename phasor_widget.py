"""phasor_widget.py — Phasor-Diagramm für den CAS-Rechner.

Zeigt komplexe Zeiger (Phasoren) in der Gaußschen Zahlenebene.
Jede komplexe Variable, die der CAS-Rechner kennt, erscheint hier
als farbiger Pfeil mit Winkelbogen und Beschriftung.

Phasor-Darstellung:
    Ein Phasor wird durch Betrag r und Winkel θ (in Radiant, mathematische
    Konvention: 0° = positive Realachse, positiv = entgegen dem Uhrzeigersinn)
    beschrieben.

Syntax im CAS (Beispiele):
    U := 5 * exp(j * pi / 6)         # 5∠30°
    I := 2 + 3*j                      # Kartesische Form
    Z := phasor(10, 45)               # 10∠45° (Grad)
"""
from __future__ import annotations

import math

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import (
    QBrush,
    QColor,
    QFont,
    QPainter,
    QPainterPath,
    QPen,
    QPolygonF,
)
from PySide6.QtWidgets import QSizePolicy, QWidget


# ── Phasor-Farben (reihum vergeben) ──────────────────────────────────────────
_COLORS: list[str] = [
    "#2563eb",  # Blau
    "#dc2626",  # Rot
    "#16a34a",  # Grün
    "#d97706",  # Orange
    "#7c3aed",  # Lila
    "#0891b2",  # Cyan
    "#be185d",  # Pink
    "#92400e",  # Braun
]


def _nice_step(max_val: float) -> float:
    """Berechnet eine 'schöne' Schrittweite für Gitter und Achsenbeschriftung."""
    if max_val <= 0:
        return 1.0
    raw = max_val / 4.0
    exp = math.floor(math.log10(raw))
    frac = raw / (10 ** exp)
    for nice in (1.0, 2.0, 2.5, 5.0, 10.0):
        if frac <= nice:
            return nice * (10 ** exp)
    return 10 ** (exp + 1)


class PhasorWidget(QWidget):
    """Zeichnet Phasoren (komplexe Zeiger) in der Gaußschen Zahlenebene.

    Wird über ``set_phasors()`` mit neuen Werten versorgt und ruft
    ``update()`` auf, sodass Qt die Neumaltung einplant.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # Liste der Phasoren: [(name, betrag, winkel_rad), ...]
        self._phasors: list[tuple[str, float, float]] = []
        self.setMinimumSize(200, 200)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # ── Öffentliche API ───────────────────────────────────────────────────────
    def set_phasors(self, phasors: list[tuple[str, float, float]]) -> None:
        """Aktualisiert die Phasorenliste und plant eine Neuzeichnung ein.

        Args:
            phasors: Liste von ``(name, betrag, winkel_rad)``.
        """
        self._phasors = phasors
        self.update()

    # ── Zeichnen ──────────────────────────────────────────────────────────────
    def paintEvent(self, _event) -> None:  # noqa: N802
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        w, h = self.width(), self.height()

        # ── Koordinatensystem ────────────────────────────────────────────
        # Zeichenbereich: Kreis mit Rand (Platz für Achsenbeschriftung).
        margin_px = 42.0
        cx, cy = w / 2.0, h / 2.0
        draw_r = min(w, h) / 2.0 - margin_px  # Radius des Plotbereichs [px]

        if self._phasors:
            max_r = max(r for _, r, _ in self._phasors) or 1.0
        else:
            max_r = 1.0
        scale = draw_r / max_r  # [px / Einheit]

        def to_screen(x: float, y: float) -> QPointF:
            """Mathematische Koordinaten → Bildschirmpixel."""
            return QPointF(cx + x * scale, cy - y * scale)

        # ── Hintergrund ──────────────────────────────────────────────────
        p.fillRect(self.rect(), QColor("white"))

        # ── Gitter ───────────────────────────────────────────────────────
        step = _nice_step(max_r)
        extent = max_r * 1.18
        grid_pen = QPen(QColor("#f1f5f9"))
        grid_pen.setWidthF(1.0)
        p.setPen(grid_pen)
        i = 1
        while True:
            v = i * step
            if v > extent:
                break
            for sign in (1.0, -1.0):
                vv = v * sign
                p.drawLine(to_screen(-extent, vv), to_screen(extent, vv))
                p.drawLine(to_screen(vv, -extent), to_screen(vv, extent))
            i += 1

        # ── Einheitskreis (gestrichelt, nur wenn sinnvoll) ────────────────
        if max_r >= 0.5:
            circ_pen = QPen(QColor("#cbd5e1"))
            circ_pen.setWidthF(1.0)
            circ_pen.setStyle(Qt.PenStyle.DashLine)
            p.setPen(circ_pen)
            r_px = 1.0 * scale
            p.drawEllipse(QPointF(cx, cy), r_px, r_px)

        # ── Achsen ────────────────────────────────────────────────────────
        axis_pen = QPen(QColor("#94a3b8"))
        axis_pen.setWidthF(1.5)
        p.setPen(axis_pen)
        p.drawLine(to_screen(-extent, 0.0), to_screen(extent, 0.0))
        p.drawLine(to_screen(0.0, -extent), to_screen(0.0, extent))

        # Achsenpfeile
        for tx, ty, ux, uy in [
            ( extent, 0.0,  1.0, 0.0),
            (-extent, 0.0, -1.0, 0.0),
            (0.0,  extent, 0.0,  1.0),
            (0.0, -extent, 0.0, -1.0),
        ]:
            _draw_arrowhead(p, to_screen(tx, ty),
                            ux, uy, QColor("#94a3b8"), size=6)

        # Achsenbeschriftung
        p.setPen(QColor("#64748b"))
        p.setFont(QFont("sans-serif", 8))
        re_pt = to_screen(extent, 0.0)
        im_pt = to_screen(0.0, extent)
        p.drawText(re_pt + QPointF(4, 5), "Re")
        p.drawText(im_pt + QPointF(4, -3), "Im")

        # Gitternetz-Beschriftung (Zahlenwerte auf den Achsen)
        p.setFont(QFont("sans-serif", 7))
        p.setPen(QColor("#94a3b8"))
        i = 1
        while True:
            v = i * step
            if v > extent:
                break
            lbl_pos = f"{v:g}"
            lbl_neg = f"-{v:g}"
            # Positive und negative Richtung beider Achsen
            for vv, lbl in [(v, lbl_pos), (-v, lbl_neg)]:
                pt_x = to_screen(vv, 0.0)
                pt_y = to_screen(0.0, vv)
                p.drawText(pt_x + QPointF(-12, 13), lbl)
                p.drawText(pt_y + QPointF(4, 4), lbl)
            i += 1

        # ── Phasoren ──────────────────────────────────────────────────────
        arc_max_px = 28.0  # Maximaler Winkelbogen-Radius [px]

        for idx, (name, r, theta) in enumerate(self._phasors):
            color = QColor(_COLORS[idx % len(_COLORS)])
            ex = r * math.cos(theta)
            ey = r * math.sin(theta)
            origin = to_screen(0.0, 0.0)
            tip = to_screen(ex, ey)

            # Pfeil (Körper)
            arrow_pen = QPen(color)
            arrow_pen.setWidthF(2.2)
            p.setPen(arrow_pen)
            p.drawLine(origin, tip)

            # Pfeilspitze
            dx = tip.x() - origin.x()
            dy = tip.y() - origin.y()
            _draw_arrowhead(p, tip, dx, dy, color, size=9)

            # Winkelbogen
            arc_r = min(arc_max_px, r * scale * 0.28)
            if arc_r > 5.0:
                arc_pen = QPen(color)
                arc_pen.setWidthF(1.0)
                p.setPen(arc_pen)
                rect = QRectF(cx - arc_r, cy - arc_r, 2 * arc_r, 2 * arc_r)
                # Qt: startAngle=0 → 3-Uhr-Position (= positive Realachse).
                # Positive spanAngle → gegen den Uhrzeigersinn (mathematisch).
                span_qt = int(round(math.degrees(theta) * 16))
                if span_qt != 0:
                    p.drawArc(rect, 0, span_qt)

            # Winkelbeschriftung (kleiner Text am Bogen)
            if arc_r > 10.0:
                angle_mid = theta / 2.0
                lbl_r = arc_r + 8
                lbl_x = cx + lbl_r * math.cos(angle_mid)
                lbl_y = cy - lbl_r * math.sin(angle_mid)
                deg = math.degrees(theta) % 360.0
                p.setPen(color)
                p.setFont(QFont("sans-serif", 7))
                p.drawText(QPointF(lbl_x - 8, lbl_y + 4), f"{deg:.0f}°")

            # Phasor-Label an der Spitze
            deg = math.degrees(theta) % 360.0
            mag_str = f"{r:.3g}"
            lbl = f"{name}  {mag_str}∠{deg:.1f}°"
            p.setPen(color)
            p.setFont(QFont("sans-serif", 9, QFont.Bold))

            # Label-Versatz je nach Quadrant
            off_x = 6.0 if ex >= 0 else -8.0 - len(lbl) * 5.5
            off_y = -6.0 if ey >= 0 else 14.0
            p.drawText(tip + QPointF(off_x, off_y), lbl)

        # ── Leer-Zustand ──────────────────────────────────────────────────
        if not self._phasors:
            p.setPen(QColor("#94a3b8"))
            p.setFont(QFont("sans-serif", 10))
            p.drawText(
                self.rect(),
                Qt.AlignmentFlag.AlignCenter,
                "Keine Phasoren.\n\n"
                "Komplexe Variablen (mit j oder I)\n"
                "erscheinen automatisch hier.\n\n"
                "Beispiele:\n"
                "  U := 5 * exp(j * pi/6)\n"
                "  I := 2 + 3*j\n"
                "  Z := phasor(10, 45)",
            )

        p.end()


# ── Zeichenhilfen ─────────────────────────────────────────────────────────────
def _draw_arrowhead(
    p: QPainter,
    tip: QPointF,
    dx: float,
    dy: float,
    color: QColor,
    size: float = 9,
) -> None:
    """Zeichnet eine gefüllte Pfeilspitze an ``tip`` in Richtung (dx, dy)."""
    length = math.hypot(dx, dy)
    if length < 0.5:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy, ux  # Senkrechter Normalenvektor
    p1 = tip - QPointF(ux * size + px * size * 0.38,
                       uy * size + py * size * 0.38)
    p2 = tip - QPointF(ux * size - px * size * 0.38,
                       uy * size - py * size * 0.38)
    poly = QPolygonF([tip, p1, p2])
    path = QPainterPath()
    path.addPolygon(poly)
    path.closeSubpath()
    p.fillPath(path, QBrush(color))
