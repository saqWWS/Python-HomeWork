def sum_of_str(num):
    num_str = str(num)
    all_sum = 0

    if len(num_str) <= 1:
        return "Error: Number should have more than one digits."

    for i in num_str:
        all_sum += int(i)

    return all_sum

num = int(input("Write a number:\t"))

print(sum_of_str(num))
