#!/usr/bin/env python3
"""Filter log lines from stdin using a regex pattern."""

import argparse
import re
import sys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    parser.add_argument("-i", "--ignore-case", action="store_true")
    args = parser.parse_args()
    flags = re.IGNORECASE if args.ignore_case else 0
    regex = re.compile(args.pattern, flags)
    for line in sys.stdin:
        if regex.search(line):
            sys.stdout.write(line)


if __name__ == "__main__":
    main()
