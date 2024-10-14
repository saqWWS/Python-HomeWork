bubble_sort = [4, 9, 70, 3, 6, 45]

for item_one in range(len(bubble_sort) - 1, 0, -1):
    for item_two in range(item_one):
        if bubble_sort[item_two] > bubble_sort[item_two + 1]:
            bubble_sort[item_two], bubble_sort[item_two + 1] = bubble_sort[item_two + 1], bubble_sort[item_two]

print(bubble_sort)
