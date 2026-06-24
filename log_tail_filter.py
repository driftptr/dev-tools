#!/usr/bin/env python3
"""Filter log lines from stdin using a regex pattern."""

import argparse
import re
import sys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    args = parser.parse_args()
    regex = re.compile(args.pattern)
    for line in sys.stdin:
        if regex.search(line):
            sys.stdout.write(line)


if __name__ == "__main__":
    main()
