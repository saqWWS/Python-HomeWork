def even_numbers(list_of_numbers: int) -> int:
    for num in range(list_of_numbers + 1):
        if num % 2 == 0:
            yield num


even_num = even_numbers(50)

for i in even_num:
    print(i, end=" ")
