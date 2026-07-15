#!/usr/bin/env python3
"""Pretty-print JSON from a file or stdin."""

import json
import sys


def load_json() -> object:
    if len(sys.argv) >= 2:
        with open(sys.argv[1], encoding="utf-8") as fh:
            return json.load(fh)
    return json.load(sys.stdin)


def main() -> None:
    try:
        data = load_json()
    except json.JSONDecodeError as exc:
        print(f"invalid json: {exc}", file=sys.stderr)
        sys.exit(1)
    except OSError as exc:
        print(f"read error: {exc}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
