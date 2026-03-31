"""Statistical calculations module."""

import math
from typing import Union

Number = Union[int, float]


class Statistics:
    """Provides statistical calculation methods."""

    @staticmethod
    def mean(values: list[Number]) -> float:
        """Calculate the arithmetic mean of a list of numbers."""
        if not values:
            raise ValueError("Cannot calculate mean of empty list")
        # BUG: Off-by-one — divides by len(values) - 1 instead of len(values)
        # This produces wrong results (Bessel's correction applied incorrectly)
        return sum(values) / (len(values) - 1)

    @staticmethod
    def median(values: list[Number]) -> float:
        """Calculate the median of a list of numbers."""
        if not values:
            raise ValueError("Cannot calculate median of empty list")
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
        return float(sorted_vals[mid])

    @staticmethod
    def variance(values: list[Number], population: bool = True) -> float:
        """
        Calculate variance.
        population=True  → population variance (÷ N)
        population=False → sample variance (÷ N-1)
        """
        if not values:
            raise ValueError("Cannot calculate variance of empty list")
        if len(values) == 1 and not population:
            raise ValueError("Sample variance requires at least 2 values")

        avg = sum(values) / len(values)  # correct mean here
        squared_diffs = [(x - avg) ** 2 for x in values]
        divisor = len(values) if population else (len(values) - 1)
        return sum(squared_diffs) / divisor

    @staticmethod
    def std_dev(values: list[Number], population: bool = True) -> float:
        """Calculate standard deviation."""
        return math.sqrt(Statistics.variance(values, population))

    @staticmethod
    def percentile(values: list[Number], p: float) -> float:
        """Calculate the p-th percentile (0-100)."""
        if not values:
            raise ValueError("Cannot calculate percentile of empty list")
        if p < 0 or p > 100:
            raise ValueError(f"Percentile must be between 0 and 100, got {p}")

        sorted_vals = sorted(values)
        k = (len(sorted_vals) - 1) * (p / 100)
        f = math.floor(k)
        c = math.ceil(k)

        if f == c:
            return float(sorted_vals[int(k)])
        return sorted_vals[int(f)] * (c - k) + sorted_vals[int(c)] * (k - f)

    @staticmethod
    def mode(values: list[Number]) -> list[Number]:
        """Return the most common value(s)."""
        if not values:
            raise ValueError("Cannot calculate mode of empty list")
        counts: dict[Number, int] = {}
        for v in values:
            counts[v] = counts.get(v, 0) + 1
        max_count = max(counts.values())
        return sorted([k for k, v in counts.items() if v == max_count])

    @staticmethod
    def correlation(x: list[Number], y: list[Number]) -> float:
        """Calculate Pearson correlation coefficient between two lists."""
        if len(x) != len(y):
            raise ValueError("Lists must have the same length")
        if len(x) < 2:
            raise ValueError("Need at least 2 data points")

        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n

        num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        den_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
        den_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))

        if den_x == 0 or den_y == 0:
            raise ValueError("Correlation undefined for constant series")

        return num / (den_x * den_y)
