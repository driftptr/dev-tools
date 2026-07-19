#!/usr/bin/env python3
"""Quick HTTP reachability check for dev endpoints."""

import argparse
import sys
import time

import requests


def main() -> None:
    parser = argparse.ArgumentParser(description="Ping a URL with GET or HEAD")
    parser.add_argument("url")
    parser.add_argument("--head", action="store_true", help="Use HEAD instead of GET")
    parser.add_argument("--timeout", type=float, default=10.0, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=2, help="Retries on transient errors")
    args = parser.parse_args()

    method = requests.head if args.head else requests.get
    last_exc = None
    for attempt in range(args.retries + 1):
        try:
            response = method(args.url, allow_redirects=True, timeout=args.timeout)
            print(f"{response.status_code} {args.url}")
            return
        except requests.RequestException as exc:
            last_exc = exc
            if attempt < args.retries:
                time.sleep(0.5 * (attempt + 1))
    print(f"request failed: {last_exc}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
