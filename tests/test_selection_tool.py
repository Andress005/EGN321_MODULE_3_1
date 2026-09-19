import pytest

from src.selection_tool import select_coefficient


def test_exact_lookup():
    result = select_coefficient("VX-100", 20)

    assert result["coefficient"] == pytest.approx(0.88)
    assert result["method"] == "exact"


def test_interpolated_lookup():
    result = select_coefficient("VX-200", 65)

    assert result["coefficient"] == pytest.approx(1.36)
    assert result["method"] == "interpolation"


def test_lower_boundary_accepted():
    result = select_coefficient("VX-100", 20)

    assert result["coefficient"] == pytest.approx(0.88)


def test_upper_boundary_accepted():
    result = select_coefficient("VX-300", 125)

    assert result["coefficient"] == pytest.approx(2.12)


def test_below_range_refused():
    with pytest.raises(ValueError, match="supported minimum"):
        select_coefficient("VX-100", 5)


def test_above_range_refused():
    with pytest.raises(ValueError, match="supported maximum"):
        select_coefficient("VX-200", 95)


def test_unknown_family_refused():
    with pytest.raises(ValueError, match="Unsupported valve_family"):
        select_coefficient("VX-999", 50)

def test_vx100_interpolation_35():
    result = select_coefficient("VX-100", 35)

    assert result["coefficient"] == pytest.approx(0.9175)
    assert result["method"] == "interpolation"
    assert result["lower_point"] == (20, 0.88)
    assert result["upper_point"] == (40, 0.93)


def test_vx100_exact_maximum():
    result = select_coefficient("VX-100", 100)

    assert result["coefficient"] == pytest.approx(1.14)
    assert result["method"] == "exact"


def test_vx200_interpolation_65():
    result = select_coefficient("VX-200", 65)

    assert result["coefficient"] == pytest.approx(1.36)
    assert result["method"] == "interpolation"


def test_vx200_exact_maximum():
    result = select_coefficient("VX-200", 90)

    assert result["coefficient"] == pytest.approx(1.54)
    assert result["method"] == "exact"


def test_vx300_interpolation_62_5():
    result = select_coefficient("VX-300", 62.5)

    assert result["coefficient"] == pytest.approx(1.63)
    assert result["method"] == "interpolation"


def test_vx300_exact_maximum():
    result = select_coefficient("VX-300", 125)

    assert result["coefficient"] == pytest.approx(2.12)
    assert result["method"] == "exact"