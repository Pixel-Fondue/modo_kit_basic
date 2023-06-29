from typing import Optional
from lx import out


def greet(name: Optional[str]) -> None:
    """Displays a greeting to the given name.

    Args:
        name: Name of the user to greet.
    """
    if name:
        out(f"Hello {name}, thanks for calling me.")
    else:
        out("Please add your name so that I may greet you.")
