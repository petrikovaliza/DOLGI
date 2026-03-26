def safe_calculate(a, b, operation):
    try:
        return operation(a, b)
    except ZeroDivisionError:
        return "Error: division by zero"
    except Exception as e:
        return f"Error: {e}"

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b


print(safe_calculate(10, 2, divide))
print(safe_calculate(10, 0, divide))
print(safe_calculate(10, 3, mod))
