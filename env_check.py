#!/usr/bin/env python3
"""Check that required environment variables are set."""

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path.cwd() / ".env")
except ImportError:
    pass


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: env_check.py VAR1 VAR2 ...", file=sys.stderr)
        sys.exit(2)
    missing = [name for name in sys.argv[1:] if not os.environ.get(name)]
    if missing:
        print("missing:", ", ".join(missing), file=sys.stderr)
        sys.exit(1)
    print("ok")


if __name__ == "__main__":
    main()
