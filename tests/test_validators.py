"""Tests for the InputValidator module."""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "python"))

from validators import InputValidator


class TestValidateNumber:
    def test_valid_int(self):
        assert InputValidator.validate_number(42) == 42

    def test_valid_float(self):
        assert InputValidator.validate_number(3.14) == 3.14

    def test_string_rejected(self):
        with pytest.raises(TypeError, match="must be a number"):
            InputValidator.validate_number("hello")

    def test_nan_rejected(self):
        with pytest.raises(ValueError, match="NaN"):
            InputValidator.validate_number(float("nan"))

    def test_overflow(self):
        with pytest.raises(OverflowError, match="exceeds maximum"):
            InputValidator.validate_number(2_000_000_000)


class TestValidatePositive:
    def test_positive(self):
        assert InputValidator.validate_positive(5) == 5

    def test_zero_rejected(self):
        """BUG CAUGHT: validate_positive allows zero (uses < instead of <=)."""
        with pytest.raises(ValueError, match="must be positive"):
            InputValidator.validate_positive(0)

    def test_negative_rejected(self):
        with pytest.raises(ValueError, match="must be positive"):
            InputValidator.validate_positive(-1)


class TestValidateNonZero:
    def test_non_zero(self):
        assert InputValidator.validate_non_zero(7) == 7

    def test_zero_raises(self):
        with pytest.raises(ZeroDivisionError, match="cannot be zero"):
            InputValidator.validate_non_zero(0)


class TestValidateInteger:
    def test_int(self):
        assert InputValidator.validate_integer(10) == 10

    def test_float_rejected(self):
        with pytest.raises(TypeError, match="must be an integer"):
            InputValidator.validate_integer(3.14)


class TestValidatePercentage:
    def test_valid(self):
        assert InputValidator.validate_percentage(50) == 50

    def test_boundary_zero(self):
        assert InputValidator.validate_percentage(0) == 0

    def test_boundary_hundred(self):
        assert InputValidator.validate_percentage(100) == 100

    def test_over_100(self):
        with pytest.raises(ValueError, match="between 0 and 100"):
            InputValidator.validate_percentage(101)

    def test_negative(self):
        with pytest.raises(ValueError, match="between 0 and 100"):
            InputValidator.validate_percentage(-5)


class TestSanitizeList:
    def test_valid_list(self):
        assert InputValidator.sanitize_list([1, 2.5, 3]) == [1, 2.5, 3]

    def test_empty_list(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            InputValidator.sanitize_list([])

    def test_not_a_list(self):
        with pytest.raises(TypeError, match="must be a list"):
            InputValidator.sanitize_list("not a list")

    def test_invalid_element(self):
        with pytest.raises(TypeError, match="must be a number"):
            InputValidator.sanitize_list([1, "two", 3])
