def gen1():
    num = 1

    while num != 6:
        yield num
        num += 1


def gen2():
    form_1_to_5 = gen1()

    for num in form_1_to_5:
        print(num)

    for i in range(6, 11):
        yield i


from_6_to_10 = gen2()
for i in from_6_to_10:
    print(i)
