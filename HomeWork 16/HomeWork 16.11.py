def given_number(num):
        
    if num < 10:
        return num
            
    return num % 10 + given_number(num // 10)
                

num = int(input("Enter a number:\t"))    


print(given_number(num))
