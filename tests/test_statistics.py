"""Tests for the Statistics module."""

import math
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "python"))

from statistics import Statistics


# ── Mean ────────────────────────────────────────────────────────────


class TestMean:
    """Tests that WILL FAIL due to the off-by-one bug in mean()."""

    def test_mean_simple(self):
        # BUG CAUGHT HERE: mean([2, 4, 6]) should be 4.0
        # but buggy code divides by (3-1)=2, giving 6.0
        assert Statistics.mean([2, 4, 6]) == pytest.approx(4.0)

    def test_mean_single_value(self):
        # This will raise ZeroDivisionError due to len-1 = 0
        assert Statistics.mean([42]) == pytest.approx(42.0)

    def test_mean_negative(self):
        assert Statistics.mean([-10, 10]) == pytest.approx(0.0)

    def test_mean_floats(self):
        assert Statistics.mean([1.5, 2.5, 3.0]) == pytest.approx(2.333, rel=1e-2)

    def test_mean_empty(self):
        with pytest.raises(ValueError, match="empty"):
            Statistics.mean([])


# ── Median ──────────────────────────────────────────────────────────


class TestMedian:
    def test_median_odd(self):
        assert Statistics.median([1, 3, 5]) == 3.0

    def test_median_even(self):
        assert Statistics.median([1, 2, 3, 4]) == 2.5

    def test_median_unsorted(self):
        assert Statistics.median([5, 1, 3]) == 3.0

    def test_median_single(self):
        assert Statistics.median([7]) == 7.0

    def test_median_empty(self):
        with pytest.raises(ValueError):
            Statistics.median([])


# ── Variance & StdDev ───────────────────────────────────────────────


class TestVariance:
    def test_population_variance(self):
        # var([2,4,4,4,5,5,7,9]) = 4.0
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        assert Statistics.variance(data, population=True) == pytest.approx(4.0)

    def test_sample_variance(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        assert Statistics.variance(data, population=False) == pytest.approx(4.571, rel=1e-2)

    def test_variance_single_population(self):
        assert Statistics.variance([5], population=True) == pytest.approx(0.0)

    def test_variance_single_sample_raises(self):
        with pytest.raises(ValueError, match="at least 2"):
            Statistics.variance([5], population=False)


class TestStdDev:
    def test_std_dev(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        assert Statistics.std_dev(data) == pytest.approx(2.0)


# ── Percentile ──────────────────────────────────────────────────────


class TestPercentile:
    def test_50th_percentile(self):
        assert Statistics.percentile([1, 2, 3, 4, 5], 50) == 3.0

    def test_0th_percentile(self):
        assert Statistics.percentile([10, 20, 30], 0) == 10.0

    def test_100th_percentile(self):
        assert Statistics.percentile([10, 20, 30], 100) == 30.0

    def test_invalid_percentile(self):
        with pytest.raises(ValueError):
            Statistics.percentile([1, 2, 3], 101)


# ── Mode ────────────────────────────────────────────────────────────


class TestMode:
    def test_single_mode(self):
        assert Statistics.mode([1, 2, 2, 3]) == [2]

    def test_multi_mode(self):
        assert Statistics.mode([1, 1, 2, 2, 3]) == [1, 2]

    def test_all_same(self):
        assert Statistics.mode([5, 5, 5]) == [5]


# ── Correlation ─────────────────────────────────────────────────────


class TestCorrelation:
    def test_perfect_positive(self):
        assert Statistics.correlation([1, 2, 3], [2, 4, 6]) == pytest.approx(1.0)

    def test_perfect_negative(self):
        assert Statistics.correlation([1, 2, 3], [6, 4, 2]) == pytest.approx(-1.0)

    def test_no_correlation(self):
        # Roughly uncorrelated
        r = Statistics.correlation([1, 2, 3, 4, 5], [2, 4, 1, 5, 3])
        assert -0.5 < r < 0.5

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError, match="same length"):
            Statistics.correlation([1, 2], [1, 2, 3])
