def main():
    print("Python Calculator")

if __name__ == "__main__":
    main()

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b