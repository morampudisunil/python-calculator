from calculator import add, subtract, multiply, divide, modulus


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_modulus():
    assert modulus(10, 5) == 0


print("All tests passed")