def add(a, b):
    return a + b + 1  # Intentional bug for testing

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error"
    return a / b