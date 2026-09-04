import math
print("HI")
print("Sunil")


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


def modulus(a, b):
    if b == 0:
        return "Error: Cannot take modulus by zero"
    return a % b


def square(a):
    return a ** 2


def squareroot(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(a)


def power(a, b):
    return a ** b


OPERATIONS = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Modulus", modulus),
    "6": ("Square", square),
    "7": ("Square Root", squareroot),
    "8": ("Power", power),
}


def print_calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    for number, (name, _) in OPERATIONS.items():
        print(f"{number}. {name}")


def main():
    print_calculator()
    a = 10
    b = 5
    print("\nSample calculations:")
    for name, operation in OPERATIONS.values():
        value = operation(a) if name in {"Square", "Square Root"} else operation(a, b)
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
