#!/usr/bin/env python3
"""Search the distributed business-model pattern library CSV.

Example:
  python3 tools/patterns.py search "open source|crowdfunding|licen"
  python3 tools/patterns.py list --limit 20
  python3 tools/patterns.py show "Open Source"
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = (
    ROOT
    / "Foundation"
    / "Distributed business model patterns - Models.csv"
)


def load_patterns(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help="Path to patterns CSV",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("search", help="Regex search across pattern fields")
    sp.add_argument("query", help="Regex (case-insensitive)")
    sp.add_argument("--limit", type=int, default=25)

    lp = sub.add_parser("list", help="List pattern names")
    lp.add_argument("--limit", type=int, default=0, help="0 = all")

    sh = sub.add_parser("show", help="Show one pattern by name substring")
    sh.add_argument("name")

    args = p.parse_args(argv)
    if not args.csv.exists():
        print(f"error: CSV not found: {args.csv}", file=sys.stderr)
        return 2
    rows = load_patterns(args.csv)
    name_key = "Pattern name"

    if args.cmd == "list":
        names = [r.get(name_key, "") for r in rows]
        if args.limit:
            names = names[: args.limit]
        for n in names:
            print(n)
        print(f"\n({len(names)} patterns)", file=sys.stderr)
        return 0

    if args.cmd == "show":
        q = args.name.lower()
        hits = [r for r in rows if q in (r.get(name_key) or "").lower()]
        if not hits:
            print(f"no match for {args.name!r}", file=sys.stderr)
            return 1
        for r in hits:
            print(f"# {r.get(name_key)}")
            for k, v in r.items():
                if k == name_key:
                    continue
                val = (v or "").strip()
                if val:
                    print(f"\n## {k}\n{val}")
            print("\n---\n")
        return 0

    if args.cmd == "search":
        try:
            rx = re.compile(args.query, re.I)
        except re.error as e:
            print(f"invalid regex: {e}", file=sys.stderr)
            return 2
        hits = []
        for r in rows:
            blob = "\n".join(f"{k}: {v}" for k, v in r.items() if v)
            if rx.search(blob):
                hits.append(r)
        hits = hits[: args.limit]
        if not hits:
            print("no matches", file=sys.stderr)
            return 1
        print("| Pattern | Traditional (trunc) | P2P update (trunc) |")
        print("| ----- | ----- | ----- |")
        for r in hits:
            name = (r.get(name_key) or "").replace("|", "/")
            trad = re.sub(r"\s+", " ", (r.get("Traditional description") or ""))[:90]
            p2p = re.sub(r"\s+", " ", (r.get("Description updated for p2p") or ""))[:90]
            print(f"| {name} | {trad} | {p2p} |")
        print(f"\n({len(hits)} shown) — use `show <name>` for full text", file=sys.stderr)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
