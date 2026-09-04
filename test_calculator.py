import pytest

from calculator import add, subtract, multiply, divide, modulus, square, squareroot, power


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2
    assert divide(10, 0) == "Error: Cannot divide by zero"
werfdgerhg

def test_modulus():
    assert modulus(10, 5) == 0

    assert modulus(10, 0) == "Error: Cannot take modulus by zero"


def test_square():
    assert square(10) == 100


def test_squareroot():
    assert squareroot(10) == pytest.approx(3.1622776601683795)
    assert squareroot(-1) == "Error: Cannot take square root of negative number"


def test_power():
    assert power(10, 5) == 100000