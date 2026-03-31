"""
Tests for the Calculator module.

These tests are CORRECT — the bugs are in the source code.
The self-healing agent should fix the source, not the tests.
"""

import math
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "python"))

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ── Basic operations ────────────────────────────────────────────────


class TestAdd:
    def test_add_positive(self, calc):
        assert calc.add(2, 3) == 5

    def test_add_negative(self, calc):
        assert calc.add(-1, -1) == -2

    def test_add_zero(self, calc):
        assert calc.add(0, 0) == 0

    def test_add_mixed(self, calc):
        assert calc.add(-5, 10) == 5

    def test_add_floats(self, calc):
        assert calc.add(1.5, 2.5) == pytest.approx(4.0)


class TestSubtract:
    def test_subtract_positive(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_subtract_negative(self, calc):
        assert calc.subtract(-1, -1) == 0

    def test_subtract_result_negative(self, calc):
        assert calc.subtract(3, 10) == -7


class TestMultiply:
    def test_multiply_positive(self, calc):
        assert calc.multiply(5, 6) == 30

    def test_multiply_by_zero(self, calc):
        assert calc.multiply(5, 0) == 0

    def test_multiply_negative(self, calc):
        assert calc.multiply(-3, 4) == -12


class TestDivide:
    def test_divide_exact(self, calc):
        assert calc.divide(15, 3) == 5.0

    def test_divide_decimal(self, calc):
        assert calc.divide(10, 3) == pytest.approx(3.333, rel=1e-2)

    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)


# ── Advanced operations ─────────────────────────────────────────────


class TestPower:
    def test_power_positive(self, calc):
        assert calc.power(2, 10) == 1024

    def test_power_zero(self, calc):
        assert calc.power(5, 0) == 1

    def test_power_negative_exponent(self, calc):
        assert calc.power(2, -1) == pytest.approx(0.5)


class TestSqrt:
    def test_sqrt_perfect_square(self, calc):
        assert calc.sqrt(144) == 12.0

    def test_sqrt_non_perfect(self, calc):
        assert calc.sqrt(2) == pytest.approx(math.sqrt(2))

    def test_sqrt_zero(self, calc):
        assert calc.sqrt(0) == 0.0

    def test_sqrt_negative(self, calc):
        with pytest.raises(ValueError, match="negative"):
            calc.sqrt(-4)


class TestFactorial:
    """Tests that WILL FAIL due to the off-by-one bug in factorial."""

    def test_factorial_zero(self, calc):
        assert calc.factorial(0) == 1

    def test_factorial_one(self, calc):
        assert calc.factorial(1) == 1

    def test_factorial_five(self, calc):
        # BUG CAUGHT HERE: factorial(5) should be 120
        # but buggy code returns 24 (range(1,5) = 1*2*3*4)
        assert calc.factorial(5) == 120

    def test_factorial_ten(self, calc):
        assert calc.factorial(10) == 3628800

    def test_factorial_negative(self, calc):
        with pytest.raises(ValueError, match="negative"):
            calc.factorial(-1)

    def test_factorial_float_rejected(self, calc):
        with pytest.raises(TypeError, match="integer"):
            calc.factorial(3.5)


class TestModulo:
    def test_modulo_basic(self, calc):
        assert calc.modulo(10, 3) == 1

    def test_modulo_even(self, calc):
        assert calc.modulo(10, 5) == 0

    def test_modulo_by_zero(self, calc):
        with pytest.raises(ValueError, match="zero"):
            calc.modulo(5, 0)


# ── History ─────────────────────────────────────────────────────────


class TestHistory:
    def test_history_records_operations(self, calc):
        calc.add(1, 2)
        calc.multiply(3, 4)
        assert len(calc.history) == 2

    def test_clear_history(self, calc):
        calc.add(1, 1)
        calc.clear_history()
        assert len(calc.history) == 0

    def test_history_is_copy(self, calc):
        calc.add(1, 2)
        h = calc.history
        h.clear()
        assert len(calc.history) == 1  # original not affected

