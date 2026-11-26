"""Greeting helper with a small argparse CLI."""

import argparse
from typing import List, Optional

DEFAULT_GREETING = "Hello Artgent"


def get_greeting(name: Optional[str] = None) -> str:
    """Return a greeting for ``name``, defaulting to ``Hello Artgent``.

    Args:
        name: Optional name to greet. Surrounding whitespace is trimmed.

    Raises:
        TypeError: if ``name`` is neither ``None`` nor a string.
        ValueError: if ``name`` is empty or only whitespace.
    """
    if name is None:
        return DEFAULT_GREETING
    if not isinstance(name, str):
        raise TypeError("name must be a string or None")
    text = name.strip()
    if not text:
        raise ValueError("name must not be empty")
    return f"Hello {text}"


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entrypoint: print a greeting and return a process exit code."""
    parser = argparse.ArgumentParser(
        prog="hello_artgent",
        description="Print a greeting (default: Hello Artgent).",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default=None,
        help=f"Name to greet (default: {DEFAULT_GREETING})",
    )
    args = parser.parse_args(argv)

    try:
        print(get_greeting(args.name))
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
