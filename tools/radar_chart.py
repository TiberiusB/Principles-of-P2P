#!/usr/bin/env python3
"""Generate a P2P-ness layer-average radar chart (SVG always; PNG if matplotlib is available).

Intended for executive summaries. Do NOT use Mermaid for this chart — Cursor's
Markdown preview does not reliably render Mermaid radar/quadrant diagrams.

Example:
  python3 tools/radar_chart.py \\
    --org ChangePool \\
    --title "ChangePool FamilyDAO" \\
    --structural 0.3 --operational 1.2 --economic 1.0 --cultural 3.0 \\
    --overall 1.4 \\
    --out case-study/assets/
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path


DEFAULT_LABELS = ("Structural", "Operational", "Economic", "Cultural")
MAX_R = 5.0


def _points(n: int, radius: float, cx: float, cy: float) -> list[tuple[float, float]]:
    """Clockwise from top."""
    out = []
    for i in range(n):
        angle = -math.pi / 2 + (2 * math.pi * i / n)
        out.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
    return out


def write_svg(
    *,
    path: Path,
    title: str,
    labels: tuple[str, ...],
    values: list[float],
    overall: float | None,
) -> None:
    cx, cy, R = 220.0, 230.0, 150.0
    n = len(labels)
    width, height = 440, 480

    grids = []
    for g in range(1, 6):
        pts = _points(n, R * g / MAX_R, cx, cy)
        d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
        grids.append(f'<path d="{d}" fill="none" stroke="#d0d0d0" stroke-width="1"/>')

    axes = []
    for x, y in _points(n, R, cx, cy):
        axes.append(
            f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" '
            f'stroke="#bbbbbb" stroke-width="1"/>'
        )

    data_pts = []
    for i, v in enumerate(values):
        angle = -math.pi / 2 + (2 * math.pi * i / n)
        r = R * v / MAX_R
        data_pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    data_d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in data_pts) + " Z"
    data_poly = (
        f'<path d="{data_d}" fill="rgba(31,78,121,0.28)" '
        f'stroke="#1f4e79" stroke-width="2.5"/>'
    )

    dots = []
    for i, (v, (x, y)) in enumerate(zip(values, data_pts)):
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#1f4e79"/>')
        lx = cx + (R * v / MAX_R + 18) * math.cos(
            -math.pi / 2 + (2 * math.pi * i / n)
        )
        ly = cy + (R * v / MAX_R + 18) * math.sin(
            -math.pi / 2 + (2 * math.pi * i / n)
        )
        dots.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" '
            f'dominant-baseline="middle" font-family="Georgia, serif" '
            f'font-size="13" font-weight="700" fill="#1f4e79">{v:.1f}</text>'
        )

    lab_elems = []
    for i, lab in enumerate(labels):
        lx = cx + (R + 28) * math.cos(-math.pi / 2 + (2 * math.pi * i / n))
        ly = cy + (R + 28) * math.sin(-math.pi / 2 + (2 * math.pi * i / n))
        lab_elems.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" '
            f'dominant-baseline="middle" font-family="Georgia, serif" '
            f'font-size="14" fill="#222">{lab}</text>'
        )

    ticks = []
    for g in range(1, 6):
        x = cx + 10
        y = cy - R * g / MAX_R
        ticks.append(
            f'<text x="{x:.1f}" y="{y + 4:.1f}" font-family="sans-serif" '
            f'font-size="10" fill="#888">{g}</text>'
        )

    subtitle = "Project layer averages (0–5)"
    if overall is not None:
        subtitle += f" · overall index {overall:.1f}"
    scores_line = " · ".join(f"{lab} {v:.1f}" for lab, v in zip(labels, values))

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Radar chart of {title} layer averages">
  <rect width="{width}" height="{height}" fill="#ffffff"/>
  <text x="220" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="700" fill="#111">{title} — Layer averages (0–5)</text>
  <text x="220" y="48" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#555">{subtitle}</text>
  <g transform="translate(0,10)">
    {''.join(grids)}
    {''.join(axes)}
    {data_poly}
    {''.join(dots)}
    {''.join(lab_elems)}
    {''.join(ticks)}
  </g>
  <text x="220" y="465" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">{scores_line}</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def write_png(
    *,
    path: Path,
    title: str,
    labels: tuple[str, ...],
    values: list[float],
    overall: float | None,
) -> bool:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        return False

    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    values_cycle = values + values[:1]
    angles_cycle = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles)
    ax.set_xticklabels(list(labels), fontsize=12)
    ax.set_ylim(0, MAX_R)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=9, color="#666666")
    ax.plot(angles_cycle, values_cycle, color="#1f4e79", linewidth=2.2)
    ax.fill(angles_cycle, values_cycle, color="#1f4e79", alpha=0.25)
    for angle, value in zip(angles, values):
        ax.text(
            angle,
            min(value + 0.4, MAX_R),
            f"{value:.1f}",
            ha="center",
            va="center",
            fontsize=10,
            color="#1f4e79",
            fontweight="bold",
        )
    subtitle = "Layer averages (0–5)"
    if overall is not None:
        subtitle += f" · overall index {overall:.1f}"
    ax.set_title(f"{title} — {subtitle}", fontsize=13, pad=18)
    fig.tight_layout()
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return True


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--org", required=True, help="Org slug used in output filenames")
    p.add_argument("--title", default=None, help="Chart title (defaults to --org)")
    p.add_argument("--structural", type=float, required=True)
    p.add_argument("--operational", type=float, required=True)
    p.add_argument("--economic", type=float, required=True)
    p.add_argument("--cultural", type=float, required=True)
    p.add_argument("--overall", type=float, default=None, help="Optional secondary overall index")
    p.add_argument(
        "--out",
        type=Path,
        default=Path("case-study/assets"),
        help="Output directory (created if missing)",
    )
    p.add_argument(
        "--png-only-fail",
        action="store_true",
        help="Exit non-zero if PNG cannot be written (matplotlib missing)",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    title = args.title or args.org
    values = [args.structural, args.operational, args.economic, args.cultural]
    for name, v in zip(DEFAULT_LABELS, values):
        if not (0.0 <= v <= MAX_R):
            print(f"error: {name} score {v} out of range 0–{MAX_R}", file=sys.stderr)
            return 2

    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{args.org}_layer_radar"
    svg_path = out_dir / f"{stem}.svg"
    png_path = out_dir / f"{stem}.png"

    write_svg(
        path=svg_path,
        title=title,
        labels=DEFAULT_LABELS,
        values=values,
        overall=args.overall,
    )
    print(f"wrote {svg_path}")

    ok_png = write_png(
        path=png_path,
        title=title,
        labels=DEFAULT_LABELS,
        values=values,
        overall=args.overall,
    )
    if ok_png:
        print(f"wrote {png_path}")
        return 0

    print(
        "warning: matplotlib not installed; SVG written but PNG skipped.\n"
        "  For Cursor Markdown preview, install matplotlib and re-run, e.g.:\n"
        "    python3 -m venv .venv && .venv/bin/pip install -r tools/requirements-radar.txt\n"
        "    .venv/bin/python tools/radar_chart.py ...",
        file=sys.stderr,
    )
    return 1 if args.png_only_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
