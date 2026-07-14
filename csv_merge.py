#!/usr/bin/env python3
"""Merge two CSV files on a shared key column."""

import argparse
import csv
import sys
from pathlib import Path


def load_rows(path: Path, key: str) -> dict:
    rows = {}
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            k = row[key]
            if k in rows:
                rows[k].update(row)
            else:
                rows[k] = dict(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left")
    parser.add_argument("right")
    parser.add_argument("--key", required=True)
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()

    left = load_rows(Path(args.left), args.key)
    right = load_rows(Path(args.right), args.key)
    keys = sorted(set(left) | set(right))
    fieldnames = sorted(set().union(*(row.keys() for row in left.values()), *(row.keys() for row in right.values())))

    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    for key in keys:
        row = {}
        if key in left:
            row.update(left[key])
        if key in right:
            row.update(right[key])
        writer.writerow(row)

    if not args.quiet:
        print(f"merged {len(keys)} rows", file=sys.stderr)


if __name__ == "__main__":
    main()
