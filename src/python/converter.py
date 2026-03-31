"""Unit converter module for common measurement conversions."""

from typing import Union

Number = Union[int, float]


class UnitConverter:
    """Converts between common measurement units."""

    # ── Temperature ──────────────────────────────────────────────────
    @staticmethod
    def celsius_to_fahrenheit(c: Number) -> float:
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f: Number) -> float:
        return (f - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(c: Number) -> float:
        result = c + 273.15
        if result < 0:
            raise ValueError(
                f"Temperature below absolute zero: {result}K "
                f"(input: {c}°C)"
            )
        return result

    # ── Distance ─────────────────────────────────────────────────────
    @staticmethod
    def km_to_miles(km: Number) -> float:
        if km < 0:
            raise ValueError("Distance cannot be negative")
        return km * 0.621371

    @staticmethod
    def miles_to_km(miles: Number) -> float:
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * 1.60934

    # ── Weight ───────────────────────────────────────────────────────
    @staticmethod
    def kg_to_pounds(kg: Number) -> float:
        if kg < 0:
            raise ValueError("Weight cannot be negative")
        return kg * 2.20462

    @staticmethod
    def pounds_to_kg(lbs: Number) -> float:
        if lbs < 0:
            raise ValueError("Weight cannot be negative")
        return lbs * 0.453592

    # ── Data size ────────────────────────────────────────────────────
    @staticmethod
    def bytes_to_human(size_bytes: int) -> str:
        """Convert bytes to human-readable format."""
        if size_bytes < 0:
            raise ValueError("Size cannot be negative")
        if size_bytes == 0:
            return "0 B"

        units = ["B", "KB", "MB", "GB", "TB", "PB"]
        # BUG: Uses 1000 instead of 1024 for binary conversion
        # This means 1 KB = 1000 B instead of 1024 B
        base = 1000
        for unit in units:
            if abs(size_bytes) < base:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= base
        return f"{size_bytes:.1f} EB"

    # ── Batch conversion ─────────────────────────────────────────────
    @staticmethod
    def batch_convert(
        values: list[Number],
        converter: str
    ) -> list[float]:
        """
        Convert a list of values using the named converter.
        Supported: 'c_to_f', 'f_to_c', 'km_to_mi', 'mi_to_km',
                   'kg_to_lb', 'lb_to_kg'
        """
        converters = {
            "c_to_f": UnitConverter.celsius_to_fahrenheit,
            "f_to_c": UnitConverter.fahrenheit_to_celsius,
            "km_to_mi": UnitConverter.km_to_miles,
            "mi_to_km": UnitConverter.miles_to_km,
            "kg_to_lb": UnitConverter.kg_to_pounds,
            "lb_to_kg": UnitConverter.pounds_to_kg,
        }

        if converter not in converters:
            raise ValueError(
                f"Unknown converter '{converter}'. "
                f"Supported: {', '.join(converters.keys())}"
            )

        fn = converters[converter]
        return [fn(v) for v in values]
