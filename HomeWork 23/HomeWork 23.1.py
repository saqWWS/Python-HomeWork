def fibonacci_generator(num: int) -> int:
    num_1 = 0
    num_2 = 1

    for i in range(2, num + 1):
        yield num_2 + num_1
        num_1, num_2 = num_2, num_1 + num_2


input_number = int(input("Write a number:\t"))
gen_fibo_num = fibonacci_generator(input_number)

for item in gen_fibo_num:
    print(item)
