import pytest

from quick_calc.core import add, sub, mul, div


def test_addition_basic():
    assert add(5, 3) == 8


def test_subtraction_basic():
    assert sub(10, 4) == 6


def test_multiplication_basic():
    assert mul(6, 7) == 42


def test_division_basic():
    assert div(8, 2) == 4


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)


def test_negative_numbers():
    assert sub(-5, -2) == -3


def test_decimal_addition():
    # floating-point için approx kullanıyoruz
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_very_large_numbers():
    assert mul(10**9, 10**9) == 10**18