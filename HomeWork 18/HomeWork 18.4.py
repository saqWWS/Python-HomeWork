import random


def different_process(data, operation="sum"):

    if operation == "sum":
        result = 0
        for num in data:
            result += num
        return f"The sum of all elements: {result}"

    elif operation == "max":
        result = data[0]
        for num in data:
            if num > result:
                result = num
        return f"The largest element: {result}"

    elif operation == "min":
        result = data[0]
        for num in data:
            if num < result:
                result = num
        return f"The smallest element: {result}"

    elif operation == "average":
        total = 0
        count = 0
        for num in data:
            total += num
            count += 1
        result = total / count
        return f"Average result: {result}"


data = [random.randint(15, 99) for _ in range(5)]

print("All elements of the list:", data)

print(different_process(data))
print(different_process(data, operation="max"))
print(different_process(data, operation="min"))
print(different_process(data, operation="average"))
