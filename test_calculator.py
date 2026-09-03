from calculator import add, subtract, multiply, divide, modulus, square, squareroot, power


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
def test_square():
    assert square(10) == 100    
def test_squareroot():
    assert squareroot(10) == 3.1622776601683795
def test_power():
    assert power(10, 5) == 100000
    
print("All tests passed")