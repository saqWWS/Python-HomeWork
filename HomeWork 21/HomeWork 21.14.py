def addition(a, b):
    return a + b
    
def subtraction(a, b):
    return a - b
    
def multiplication(a, b):
    return a * b
    
def division(a, b):
    if a == 0:
        return "Error: Division by zero is not allowed."
    elif b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

first_number = int(input("Enter the first number: "))

operator = input("Enter operator '+', '-', '*', '/': ")

second_number = int(input("Enter the second number: "))

dict_calculator = {"+": addition, "-": subtraction, "*": multiplication, "/": division}

if operator in dict_calculator:
    
    result = dict_calculator[operator](first_number, second_number)

    print(f"The result of {first_number} {operator} {second_number} is: {result}")
else:
    print("Invalid operator.")