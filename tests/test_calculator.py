"""
Tests for the Calculator module.
These tests are CORRECT — the bugs are in the source code, not here.
The self-healing agent should fix the source, not the tests.
"""
import pytest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'python'))

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


class TestAdd:
    def test_add_positive(self, calc):
        assert calc.add(2, 3) == 5

    def test_add_negative(self, calc):
        assert calc.add(-1, -1) == -2

    def test_add_zero(self, calc):
        assert calc.add(0, 0) == 0

    def test_add_mixed(self, calc):
        assert calc.add(-5, 10) == 5


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
        with pytest.raises(ValueError, match="Cannot divide by"):
            calc.divide(10, 0)
