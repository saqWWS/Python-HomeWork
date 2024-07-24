def flatten_list(nested_list):

    numbers = []
    for element in nested_list:
        if isinstance(element, (int)):
            numbers.append(element)
        elif isinstance(element, list):
            numbers.extend(flatten_list(element))  
    return numbers

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]

flattened = flatten_list(nested_list)

print(flattened)
