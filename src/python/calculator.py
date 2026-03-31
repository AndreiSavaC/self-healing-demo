# ┌─────────────────────────────────────────────────────────────────┐
# │  DEMO: This file contains INTENTIONAL BUGS for the             │
# │  self-healing agent to detect and fix.                         │
# │                                                                │
# │  Bug 1: NameError - 'reslt' typo on line 18                   │
# │  Bug 2: TypeError - wrong concatenation on line 28            │
# └─────────────────────────────────────────────────────────────────┘

"""Simple calculator module with intentional bugs."""


class Calculator:
    """A simple calculator with intentional bugs for demo purposes."""

    def add(self, a: int, b: int) -> int:
        # BUG: 'reslt' is a typo for 'result' → NameError
        reslt = a + b
        return result  # noqa: F821 — this will fail at runtime

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        # BUG: Trying to concatenate string + number → TypeError
        if b == 0:
            raise ValueError("Cannot divide by " + b)  # Should be str(b)
        return a / b
