def sum_list(numbers):
        
    if not numbers:
        return 0
            
    return numbers[0] + sum_list(numbers[1:])

                
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

all_sum = sum_list(numbers)

print("The sum of all elements:", all_sum)
