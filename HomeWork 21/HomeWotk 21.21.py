import random

def sort_list(data):
    return sorted(data)

def reverse_list(data):
    return list(reversed(data))

def filter_list(data, condition):
    return [x for x in data if condition(x)]

def map_list(data, transformation):
    return [transformation(x) for x in data]
    
def max_num(data):
    return max(data)
    
def min_num(data):
    return min(data)
    

def transform_list(lst, operation, **kwargs):
    if operation in list_transformation_functions:
        return list_transformation_functions[operation](lst, **kwargs)
        


list_transformation_functions = {
    "sort": sort_list,
    "reverse": reverse_list,
    "filter": filter_list,
    "map": map_list,
    "max": max_num,
    "min": min_num
    
}

data = [random.randint(1, 100) for _ in range(12)]
print("All generated numbers:", data)

condition = lambda x: x % 2 == 0
transformation = lambda x: x ** 2

sorted_data = transform_list(data, "sort")
reversed_data = transform_list(data, "reverse")
filtered_data = transform_list(data, "filter", condition=condition)
mapped_data = transform_list(data, "map", transformation=transformation)
max_data = transform_list(data, "max")
min_data = transform_list(data, "min")


print("Sorted:", sorted_data)
print("Reversed:", reversed_data)
print("Filtered (even numbers):", filtered_data)
print("Mapped (squared):", mapped_data)
print("Max number:", max_data)
print("Min number:", min_data)
