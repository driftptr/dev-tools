#!/usr/bin/env python3
"""Resolve common project paths for local scripts."""

from pathlib import Path


def project_root() -> Path:
    return Path.cwd()


def data_dir(name: str) -> Path:
    root = project_root()
    target = root / "data" / name
    target.mkdir(parents=True, exist_ok=True)
    return target


if __name__ == "__main__":
    print(project_root())
