def sum_of_number(num):
    if num <= 1:
        return 1
    
    return num + sum_of_number(num - 1)
                    

num = 7
                    
print(sum_of_number(num))
