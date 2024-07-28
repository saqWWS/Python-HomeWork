import random

def get_nth_element(iterable, num):
 
    iterator = iter(iterable)
    
    for i in range(num):
        element = next(iterator) 
    
    return element, iterator

numbers = [random.randint(1,20) for _ in range(10)]
print(f"All generated numbers in the list: {numbers}")

num = int(input("Write a number:\t"))

try:
    nth_element, iterator = get_nth_element(numbers, num)
    print(f"The {num + 1}-th element in the list is: {nth_element}")

    print("Remaining elements in the list:")
    while True:
        try:
            number = next(iterator)
            print(number)
        except StopIteration:
            break
except StopIteration:
    print(f"Error: The list does not have an element at index {num}.")