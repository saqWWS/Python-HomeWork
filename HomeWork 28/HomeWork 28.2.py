selection_sort = [4, 9, 70, 3, 6, 45]

for item_one in range(len(selection_sort) - 1, 0, - 1):
    mid = item_one
    for item_two in range(item_one):
        if selection_sort[item_two] > selection_sort[mid]:
            mid = item_two
        selection_sort[item_one], selection_sort[mid] = selection_sort[mid], selection_sort[item_one]

print(selection_sort)
