import random

numbers = [random.randint(1, 100) for _ in range(6)]

print("All generated numbers", numbers)


squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)