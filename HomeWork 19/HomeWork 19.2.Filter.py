import random

def my_filter(func, iterable):
    even = []
    odd = []
    
    if func is None:
        for i in iterable:
            if bool(i) == True:
                even.append(i)
            elif bool(i) == False:
                odd.append(i)
    else:
        for i in iterable:
            a_bool = func(i)
            if a_bool == True:
                even.append(i)
            elif a_bool == False:
                odd.append(i)

    return even, odd, bool(even), bool(odd)

def even_odd(numbers):
    
    if numbers % 2 == 0:
        return True
    elif numbers % 2 != 0:
        return False

numbers = [random.randint(1, 100) for _ in range(10)]
print(f"All generated numbers in the list: {numbers}")

filtered_list, not_filtered_list, bool_even, bool_odd = my_filter(even_odd, numbers)

print("Filtered list:", bool_even, filtered_list) 
print("Not filtered list:", bool_odd, not_filtered_list)
