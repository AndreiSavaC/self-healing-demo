"""
Calculator module with advanced mathematical operations.

Provides basic arithmetic plus power, factorial, and expression evaluation.
"""

import math
from typing import Union

Number = Union[int, float]


class Calculator:
    """Full-featured calculator with history tracking."""

    def __init__(self):
        self._history: list[str] = []

    @property
    def history(self) -> list[str]:
        return list(self._history)

    def _record(self, expr: str, result: Number) -> Number:
        self._history.append(f"{expr} = {result}")
        return result

    # ── Basic ops ────────────────────────────────────────────────────
    def add(self, a: Number, b: Number) -> Number:
        return self._record(f"{a} + {b}", a + b)

    def subtract(self, a: Number, b: Number) -> Number:
        return self._record(f"{a} - {b}", a - b)

    def multiply(self, a: Number, b: Number) -> Number:
        return self._record(f"{a} * {b}", a * b)

    def divide(self, a: Number, b: Number) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        return self._record(f"{a} / {b}", result)

    # ── Advanced ops ─────────────────────────────────────────────────
    def power(self, base: Number, exponent: Number) -> Number:
        result = base ** exponent
        return self._record(f"{base} ^ {exponent}", result)

    def sqrt(self, value: Number) -> float:
        if value < 0:
            raise ValueError("Cannot take square root of negative number")
        result = math.sqrt(value)
        return self._record(f"sqrt({value})", result)

    def factorial(self, n: int) -> int:
        """Calculate n! for non-negative integers."""
        if not isinstance(n, int):
            raise TypeError("Factorial requires an integer")
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        # BUG: off-by-one, starts product at 0 when n=0 this works (returns 1),
        # but for n>=1 the range is wrong: range(1, n) misses multiplying by n itself
        # e.g. factorial(5) returns 1*2*3*4 = 24 instead of 120
        result = 1
        for i in range(1, n):
            result *= i
        return self._record(f"{n}!", result)

    def modulo(self, a: Number, b: Number) -> Number:
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        return self._record(f"{a} % {b}", a % b)

    def negate(self, value: Number) -> Number:
        return self._record(f"-({value})", -value)

    def absolute(self, value: Number) -> Number:
        return self._record(f"|{value}|", abs(value))

    def clear_history(self) -> None:
        self._history.clear()

