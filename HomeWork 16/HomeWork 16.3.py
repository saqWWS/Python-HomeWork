def factorial(num):
    if num <= 1:
        return num

    return num * factorial(num - 1)

num = 7

print(factorial(num))
