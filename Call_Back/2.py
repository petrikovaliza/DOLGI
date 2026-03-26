def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def calculate(a, b, operation):
    return operation(a, b)


print(calculate(5, 3, add))
print(calculate(5, 3, multiply))
print(calculate(10, 4, subtract))