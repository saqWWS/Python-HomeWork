import random

def large_small(random_list):
    for gen in range(8):
        random_list.append(random.randint(1, 150))

    print(random_list)

    small = random_list[0]
    large = random_list[0]

    for i in random_list:
        if i < small:
            small = i

        if i > large:
            large = i

    print(f"Smallest element: {small}")
    print(f"Largest element: {large}")

random_list = []

large_small(random_list)
