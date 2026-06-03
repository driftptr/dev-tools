#!/usr/bin/env python3
"""Merge two CSV files on a shared key column."""

import argparse
import csv
from pathlib import Path


def load_rows(path: Path, key: str) -> dict:
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return {row[key]: row for row in reader}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left")
    parser.add_argument("right")
    parser.add_argument("--key", required=True)
    args = parser.parse_args()

    left = load_rows(Path(args.left), args.key)
    right = load_rows(Path(args.right), args.key)
    keys = sorted(set(left) | set(right))
    fieldnames = sorted(set().union(*(row.keys() for row in left.values())))

    writer = csv.DictWriter(sys.stdout := __import__("sys").stdout, fieldnames=fieldnames)
    writer.writeheader()
    for key in keys:
        row = {}
        if key in left:
            row.update(left[key])
        if key in right:
            row.update(right[key])
        writer.writerow(row)


if __name__ == "__main__":
    main()
