def process_data(data, callback):
    result = []
    for item in data:
        result.append(callback(item))
    return result

def square(x):
    return x * x

def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]

print(process_data(numbers, square))
print(process_data(numbers, double))