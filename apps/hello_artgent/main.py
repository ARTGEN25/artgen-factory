"""Minimal greeting helper with a small argparse CLI."""

import argparse
import sys

DEFAULT_NAME = "Artgent"


def get_greeting(name: str = DEFAULT_NAME) -> str:
    """Return ``Hello <name>`` with surrounding whitespace removed.

    Args:
        name: Name to greet. Leading/trailing whitespace is trimmed.

    Raises:
        ValueError: if ``name`` is not a string, or is empty/whitespace only.
    """
    if not isinstance(name, str):
        raise ValueError("name must be a string")
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must not be empty")
    return f"Hello {cleaned_name}"


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint: print a greeting and return a process exit code."""
    parser = argparse.ArgumentParser(
        prog="hello_artgent",
        description="Print a greeting (default: Hello Artgent).",
    )
    parser.add_argument(
        "--name",
        default=DEFAULT_NAME,
        help=f"Name to greet (default: {DEFAULT_NAME})",
    )
    args = parser.parse_args(argv)

    try:
        greeting = get_greeting(args.name)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(greeting)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
