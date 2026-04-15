#!/usr/bin/env python3
"""Pretty-print JSON files."""

import json
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: json_pretty.py <file.json>", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as fh:
        data = json.load(fh)
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
