def is_prime(num):
        
    for x in range(3, (num//2)+1):
        if num % x == 0:
            return False
    else:
        return True
            
                    
num = int(input("Write a number:\t"))

print(is_prime(num))
