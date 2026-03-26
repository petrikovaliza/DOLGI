def filter_data(data, callback):
    result = []
    for item in data:
        if callback(item):
            result.append(item)
    return result

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0


numbers = [-5, 3, 8, -2, 10, 0, 7]

print(filter_data(numbers, is_even))
print(filter_data(numbers, is_positive))
