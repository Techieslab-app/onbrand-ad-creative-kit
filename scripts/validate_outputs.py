#!/usr/bin/env python3
from __future__ import annotations

import struct
import sys
from pathlib import Path

EXPECTED = {
    "1x1": (1080, 1080),
    "4x5": (1080, 1350),
    "9x16": (1080, 1920),
    "16x9": (1920, 1080),
}

REQUIRED_PACKAGE_FILES = [
    "README.md",
    "PACKAGE-SPEC.md",
    "skill/ad-creative-recipe/SKILL.md",
    "templates/brand.md",
    "templates/tokens.json",
    "templates/design-rules.md",
    "templates/hooks.csv",
    "templates/ad-batch.yaml",
]


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as f:
        header = f.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", header[16:24])


def validate_package(root: Path) -> list[str]:
    failures = []
    for file_name in REQUIRED_PACKAGE_FILES:
        if not (root / file_name).exists():
            failures.append(f"missing package file: {file_name}")
    return failures


def validate_outputs(output_root: Path) -> tuple[int, list[str]]:
    failures: list[str] = []
    checked = 0

    if not output_root.exists():
        return checked, failures

    for ratio, expected in EXPECTED.items():
        folder = output_root / ratio
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.png")):
            checked += 1
            try:
                actual = png_size(path)
            except Exception as exc:
                failures.append(f"{path}: {exc}")
                continue
            if actual != expected:
                failures.append(
                    f"{path}: expected {expected[0]}x{expected[1]}, got {actual[0]}x{actual[1]}"
                )
    return checked, failures


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    output_root = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "outputs"

    failures = validate_package(root)
    checked, output_failures = validate_outputs(output_root)
    failures.extend(output_failures)

    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Package validation passed. Checked {checked} PNG output files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
