def positive_numbers(func):
    def filtered_numbers(*args, **kwargs):
        if all(isinstance(arg, int) and arg >= 0 for arg in args if isinstance(arg, int)):
            result = func(*args, **kwargs)
            return result
        return "Please only use positive numbers, thank you!"

    return filtered_numbers


@positive_numbers
def mathematical_operations(operator, first_num, second_num):
    if operator == "+":
        return first_num + second_num
    elif operator == "-":
        return first_num - second_num
    elif operator == "*":
        return first_num * second_num
    elif operator == "/":
        if second_num == 0:
            print("Division by zero is not allowed")
        return first_num / second_num


# Input
first_num = int(input("Write a number:\t"))
operator = input("Write only these ( '+' '-' '*' '/'):\t")
second_num = int(input("Write a number:\t"))

result = mathematical_operations(operator, first_num, second_num)

print(f"Result is: {result}")
