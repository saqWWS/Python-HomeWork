def gen_square(num):
    for i in range(1, num + 1):
        yield [i, i ** 2]


one_to_twenty = gen_square(20)

for sq in one_to_twenty:
    print(sq)
