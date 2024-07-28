def it_next(numbers):
    
    iterator = iter(numbers)

    while True:
        try:
            number = next(iterator)
            print(number)
        except StopIteration:
            break


numbers = [num for num in range(1, 11)]


it_next(numbers)