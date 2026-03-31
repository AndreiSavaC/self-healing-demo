"""Tests for the UnitConverter module."""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "python"))

from converter import UnitConverter


# ── Temperature ─────────────────────────────────────────────────────


class TestTemperature:
    def test_c_to_f_freezing(self):
        assert UnitConverter.celsius_to_fahrenheit(0) == pytest.approx(32.0)

    def test_c_to_f_boiling(self):
        assert UnitConverter.celsius_to_fahrenheit(100) == pytest.approx(212.0)

    def test_f_to_c_body(self):
        assert UnitConverter.fahrenheit_to_celsius(98.6) == pytest.approx(37.0)

    def test_c_to_k(self):
        assert UnitConverter.celsius_to_kelvin(0) == pytest.approx(273.15)

    def test_c_to_k_absolute_zero(self):
        assert UnitConverter.celsius_to_kelvin(-273.15) == pytest.approx(0.0)

    def test_c_to_k_below_absolute_zero(self):
        with pytest.raises(ValueError, match="absolute zero"):
            UnitConverter.celsius_to_kelvin(-300)


# ── Distance ────────────────────────────────────────────────────────


class TestDistance:
    def test_km_to_miles(self):
        assert UnitConverter.km_to_miles(1) == pytest.approx(0.621371)

    def test_miles_to_km(self):
        assert UnitConverter.miles_to_km(1) == pytest.approx(1.60934)

    def test_marathon(self):
        assert UnitConverter.km_to_miles(42.195) == pytest.approx(26.219, rel=1e-2)

    def test_negative_distance(self):
        with pytest.raises(ValueError, match="negative"):
            UnitConverter.km_to_miles(-5)


# ── Weight ──────────────────────────────────────────────────────────


class TestWeight:
    def test_kg_to_pounds(self):
        assert UnitConverter.kg_to_pounds(1) == pytest.approx(2.20462)

    def test_pounds_to_kg(self):
        assert UnitConverter.pounds_to_kg(1) == pytest.approx(0.453592)


# ── Bytes ───────────────────────────────────────────────────────────


class TestBytes:
    """Tests that WILL FAIL due to the 1000-vs-1024 bug."""

    def test_bytes(self):
        assert UnitConverter.bytes_to_human(500) == "500.0 B"

    def test_kilobytes(self):
        # BUG CAUGHT HERE: 1024 bytes should be "1.0 KB"
        # but buggy code uses base=1000 so 1024 shows as "1.0 KB" only at 1000
        assert UnitConverter.bytes_to_human(1024) == "1.0 KB"

    def test_megabytes(self):
        # 1048576 bytes = 1 MB (1024*1024)
        assert UnitConverter.bytes_to_human(1048576) == "1.0 MB"

    def test_gigabytes(self):
        assert UnitConverter.bytes_to_human(1073741824) == "1.0 GB"

    def test_zero(self):
        assert UnitConverter.bytes_to_human(0) == "0 B"

    def test_negative(self):
        with pytest.raises(ValueError, match="negative"):
            UnitConverter.bytes_to_human(-1)


# ── Batch conversion ────────────────────────────────────────────────


class TestBatchConvert:
    def test_batch_c_to_f(self):
        results = UnitConverter.batch_convert([0, 100], "c_to_f")
        assert results[0] == pytest.approx(32.0)
        assert results[1] == pytest.approx(212.0)

    def test_unknown_converter(self):
        with pytest.raises(ValueError, match="Unknown converter"):
            UnitConverter.batch_convert([1, 2], "bogus")
