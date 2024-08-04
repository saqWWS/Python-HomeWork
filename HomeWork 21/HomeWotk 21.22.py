import math
import random

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)


def math_operations(number, operation):
    if operation in math_functions:
        return math_functions[operation](number)

math_functions = {
    'square': square,
    'cube': cube,
    'square_root': square_root,
    'factorial': factorial
}

number = int(input("Write a number:\t"))

num_square = math_operations(number, "square")
num_cube = math_operations(number, "cube")
num_sq_root = math_operations(number, "square_root")
num_factorial = math_operations(number, "factorial")



print(f"{number} Square is: {num_square}")
print(f"{number} Cube is: {num_cube}")
print(f"{number} Square root is: {num_sq_root}")
print(f"{number} Factorial is: {num_factorial}")