def length_of_list(all_elements):
    if len(all_elements) == 0:
        return 0

    return 1 + length_of_list(all_elements[1:])


all_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(length_of_list(all_elements))

