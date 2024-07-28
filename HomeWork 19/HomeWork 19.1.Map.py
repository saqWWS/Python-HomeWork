import random

def my_map(func, *iterables):
    res = []
    min_l = len(iterables[0])
    for i in range(1, len(iterables)):
        if min_l > len(iterables[i]):
            min_l = len(iterables[i])
    
    for i in range(min_l):
        new_ls = []
        for x in iterables:
            new_ls.append(x[i])
        res.append(func(*new_ls))
    return res

def if_duplicate(numbers: int) -> list:
    
    """
    function responsible for not 
    allowing duplicate elements in the same 
    list returns numbers and a list
    
    """
    
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)
    

def min_num(numbers: int):
    
    """ 
    A function that finds
    the smallest element
    
    """
    
    if numbers:
        return min(numbers)
    return None
    

def max_num(numbers: int):
    
    """ 
    A function that finds
    the largest element
    
    """
    
    if numbers:
        return max(numbers)
    return None
    

def improvisation(a: int, b: int):
    
    """
    a function that, using my_map() function, 
    sums the elements in the first position of 
    two different lists together
    
    """
    
    return a + b 


def multiply_min_max(min_val: int, max_val: int):
    
    """
    Multiplies the smallest element of the first
    list by the largest element of the second list,
    first checking that they are not None.
    
    """
    
    if min_val is not None and max_val is not None:
        return min_val * max_val
    return None


numbers_list_1 = [random.randint(1, 9) for _ in range(12)]
numbers_list_2 = [random.randint(10, 19) for _ in range(12)]
print(f"All generated numbers in the first list: {numbers_list_1}")
print(f"All generated numbers in the second list: {numbers_list_2}")


numbers_ls_1 = if_duplicate(numbers_list_1)
numbers_ls_2 = if_duplicate(numbers_list_2)

print(f"Duplicates in first list: {numbers_ls_1}")
print(f"Duplicates in second list: {numbers_ls_2}")


mapped_together = my_map(improvisation, numbers_ls_1, numbers_ls_2)


print("Mapped duplicates together:", mapped_together)


min_mapped_num_1 = min_num(mapped_together)
max_mapped_num_2 = max_num(mapped_together)

print("Minimum of mapped duplicates:", min_mapped_num_1)
print("Maximum of mapped duplicates:", max_mapped_num_2)


result = my_map(multiply_min_max, [min_mapped_num_1], [max_mapped_num_2])

print(f"Result of multiplication:{result}")
