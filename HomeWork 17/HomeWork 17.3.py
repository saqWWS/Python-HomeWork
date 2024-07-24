def is_sorted(lst):

    if len(lst) <= 1:
        return True
        
    if lst[0] > lst[1]:
        return False
            
    return is_sorted(lst[1:])

example_list = [1, 2, 3, 4, 46, 5, 6, 7, 156]

print(is_sorted(example_list))
