def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"
