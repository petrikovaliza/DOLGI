def apply_operations(data, callbacks):
    result = []
    for item in data:
        temp = item
        for callback in callbacks:
            temp = callback(temp)
        result.append(temp)
    return result

def inc(x):
    return x + 1

def mul2(x):
    return x * 2

def dec(x):
    return x - 1


numbers = [1, 2, 3, 4]

print(apply_operations(numbers, [inc, mul2]))
print(apply_operations(numbers, [mul2, dec]))
print(apply_operations(numbers, [inc, mul2, dec]))