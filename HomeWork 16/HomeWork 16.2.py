
def five_one(num):
    if num < 1:
        return 
    print(num)
    five_one(num - 1)

num = 5

five_one(num)
