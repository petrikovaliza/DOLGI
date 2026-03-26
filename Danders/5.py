def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

def show_calculation(a, b, operation):
    result = operation(a, b)
    op_name = operation.__name__
    print(f"{a} {op_name} {b} = {result}")

if __name__ == "__main__":
    print("=== Demonstrating all operations ===\n")
    
    show_calculation(10, 5, add)
    show_calculation(10, 5, subtract)
    show_calculation(10, 5, multiply)
    show_calculation(10, 5, divide)
    
    print("\n=== Using calculate function ===")
    print(f"10 + 5 = {calculate(10, 5, add)}")
    print(f"10 * 5 = {calculate(10, 5, multiply)}")
    
    print("\n=== Testing imported behavior (simulated) ===")
    print("If this was imported, only functions would be available")