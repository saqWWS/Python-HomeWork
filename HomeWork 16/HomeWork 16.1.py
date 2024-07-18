
def one_five(num):
    if num < 1:
        return 
    one_five(num - 1)
    print(num)

num = 5

one_five(num)
