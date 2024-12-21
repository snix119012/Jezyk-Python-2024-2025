import pytest
from ZADANIE3.zadanie3 import Zespolona

def test_repr_and_str():
    a = Zespolona(2, 5)
    assert repr(a) == "Zespolona(2, 5)"
    assert str(a) == "(2+5j)"

def test_conjugate():
    a = Zespolona(3, -4)
    assert a.conjugate() == Zespolona(3, 4)

def test_addition():
    a = Zespolona(2, 3)
    b = Zespolona(1, -1)
    assert a + b == Zespolona(3, 2)
    assert a + 5 == Zespolona(7, 3)

def test_subtraction():
    a = Zespolona(2, 3)
    b = Zespolona(1, -1)
    assert a - b == Zespolona(1, 4)
    assert 10 - a == Zespolona(8, -3)

def test_multiplication():
    a = Zespolona(2, 3)
    b = Zespolona(4, -5)
    assert a * b == Zespolona(23, 2)
    assert a * 3 == Zespolona(6, 9)

def test_abs():
    a = Zespolona(3, 4)
    assert abs(a) == 5

def test_argz():
    a = Zespolona(1, 1)
    assert pytest.approx(a.argz(), rel=1e-2) == 0.7854  # pi/4 radians

def test_power():
    a = Zespolona(1, 1)
    assert a ** 2 == Zespolona(0, 2)
    assert a ** 3 == Zespolona(-2, 2)

def test_equality():
    a = Zespolona(2, 5)
    b = Zespolona(2, 5)
    c = Zespolona(2, -5)
    assert a == b
    assert a != c

def test_division():
    a = Zespolona(4, 2)
    b = Zespolona(1, -1)
    result = a / b
    assert pytest.approx(result.r, rel=1e-2) == 1
    assert pytest.approx(result.i, rel=1e-2) == 3

    # Test division by an integer
    result = a / 2
    assert result == Zespolona(2, 1)

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = Zespolona(1, 2) / Zespolona(0, 0)
