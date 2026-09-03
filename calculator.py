def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# New Feature
def modulus(a, b):
    return a % b

def square(a):
    return a * a
def squareroot(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return a ** 0.5


# Sample calculations
a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Modulus:", modulus(a, b))
print("Square:", square(a))
print("Square Root:", squareroot(a))