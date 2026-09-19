import pytest

from src.selection_tool import select_coefficient


def test_challenge_cases_c01_c03():
    assert select_coefficient("VX-100", 20)["coefficient"] == pytest.approx(0.88)
    assert select_coefficient("VX-100", 100)["coefficient"] == pytest.approx(1.14)


def test_challenge_case_c02():
    result = select_coefficient("VX-100", 35)

    assert result["coefficient"] == pytest.approx(0.9175)
    assert result["method"] == "interpolation"


def test_challenge_cases_c04_c05():
    with pytest.raises(ValueError):
        select_coefficient("VX-100", 5)

    with pytest.raises(ValueError):
        select_coefficient("VX-100", 110)


def test_challenge_cases_c06_c07():
    assert select_coefficient("VX-200", 65)["coefficient"] == pytest.approx(1.36)
    assert select_coefficient("VX-200", 90)["coefficient"] == pytest.approx(1.54)


def test_challenge_case_c08():
    with pytest.raises(ValueError):
        select_coefficient("VX-200", 95)


def test_challenge_case_c09():
    result = select_coefficient("VX-300", 62.5)

    assert result["coefficient"] == pytest.approx(1.63)
    assert result["method"] == "interpolation"


def test_challenge_case_c10():
    assert select_coefficient("VX-300", 125)["coefficient"] == pytest.approx(2.12)


def test_challenge_case_c11():
    with pytest.raises(ValueError, match="Unsupported valve_family"):
        select_coefficient("VX-999", 50)