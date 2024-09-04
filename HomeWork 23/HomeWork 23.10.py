def exception_propagator(iterable: list) -> int:
    for i in iterable:
        if i == "error":
            raise ValueError("An error occurred!")
        yield i


list_of_elements = [1, 2, 3, 4, 5, 6, "error", 7, 8, 9, 10]

error_message = exception_propagator(list_of_elements)

try:
    for c in error_message:
        print(c)
except ValueError:
    print("You have string in your list!")
