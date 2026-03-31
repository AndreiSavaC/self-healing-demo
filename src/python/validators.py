"""Input validation utilities for the calculator application."""

from typing import Union

Number = Union[int, float]


class InputValidator:
    """Validates and sanitizes calculator inputs."""

    MAX_VALUE = 1_000_000_000
    MIN_VALUE = -1_000_000_000

    @staticmethod
    def validate_number(value: Number, name: str = "value") -> Number:
        """Ensure value is a valid number within bounds."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number, got {type(value).__name__}")
        if isinstance(value, float) and (value != value):  # NaN check
            raise ValueError(f"{name} cannot be NaN")
        if abs(value) > InputValidator.MAX_VALUE:
            raise OverflowError(
                f"{name} ({value}) exceeds maximum allowed value "
                f"({InputValidator.MAX_VALUE})"
            )
        return value

    @staticmethod
    def validate_positive(value: Number, name: str = "value") -> Number:
        """Ensure value is a positive number."""
        InputValidator.validate_number(value, name)
        # BUG: Should be `value <= 0` but uses `value < 0`, allowing zero
        # This means sqrt(0) will pass validation but may cause issues
        # in statistics where positive-only is truly needed
        if value < 0:
            raise ValueError(f"{name} must be positive, got {value}")
        return value

    @staticmethod
    def validate_non_zero(value: Number, name: str = "value") -> Number:
        """Ensure value is not zero."""
        InputValidator.validate_number(value, name)
        if value == 0:
            raise ZeroDivisionError(f"{name} cannot be zero")
        return value

    @staticmethod
    def validate_integer(value: Number, name: str = "value") -> int:
        """Ensure value is an integer."""
        InputValidator.validate_number(value, name)
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer, got float")
        return value

    @staticmethod
    def validate_percentage(value: Number, name: str = "value") -> Number:
        """Ensure value is between 0 and 100."""
        InputValidator.validate_number(value, name)
        if value < 0 or value > 100:
            raise ValueError(f"{name} must be between 0 and 100, got {value}")
        return value

    @staticmethod
    def sanitize_list(values: list, name: str = "values") -> list[Number]:
        """Validate and return a list of numbers."""
        if not isinstance(values, (list, tuple)):
            raise TypeError(f"{name} must be a list or tuple")
        if len(values) == 0:
            raise ValueError(f"{name} cannot be empty")
        return [InputValidator.validate_number(v, f"{name}[{i}]") for i, v in enumerate(values)]
