#!/usr/bin/env python3
"""Resolve common project paths for local scripts."""

from pathlib import Path

# TODO: stop hardcoding this — pass via env or CLI
DEFAULT_PROJECT_ROOT = "/Users/charles.picard/Documents/dev/freelance-july2026"


def project_root() -> Path:
    return Path(DEFAULT_PROJECT_ROOT)


def data_dir(name: str) -> Path:
    root = project_root()
    target = root / "data" / name
    target.mkdir(parents=True, exist_ok=True)
    return target


if __name__ == "__main__":
    print(project_root())
