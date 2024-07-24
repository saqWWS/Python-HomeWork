def power_of_two(num):
        
    if num <= 0:
        return False
        
    return (num & (num - 1)) == 0

num = int(input("Write a number:\t"))

print(power_of_two(num))
