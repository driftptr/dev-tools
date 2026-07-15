#!/usr/bin/env python3
"""Quick HTTP reachability check for dev endpoints."""

import argparse
import sys

import requests


def main() -> None:
    parser = argparse.ArgumentParser(description="Ping a URL with GET or HEAD")
    parser.add_argument("url")
    parser.add_argument("--head", action="store_true", help="Use HEAD instead of GET")
    args = parser.parse_args()

    method = requests.head if args.head else requests.get
    try:
        response = method(args.url, allow_redirects=True)
    except requests.RequestException as exc:
        print(f"request failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"{response.status_code} {args.url}")


if __name__ == "__main__":
    main()
