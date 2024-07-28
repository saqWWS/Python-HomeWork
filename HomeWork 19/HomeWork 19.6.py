def apply_function(iterable, func):
    return [func(item) for item in iterable]


def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

result = apply_function(numbers, square)

print(result)