import pytest

from src.interpolation import linear_interpolate


def test_midpoint_interpolation():
    result = linear_interpolate(
        x=25,
        x1=20,
        y1=100,
        x2=30,
        y2=140,
    )

    assert result == pytest.approx(120)


def test_non_midpoint_interpolation():
    result = linear_interpolate(
        x=35,
        x1=30,
        y1=1.18,
        x2=50,
        y2=1.27,
    )

    assert result == pytest.approx(1.2025)
