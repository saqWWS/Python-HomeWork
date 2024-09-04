def custom_map(func, *iterable):
    res = []
    min_len = len(iterable[0])
    for i in range(1, len(iterable)):
        if min_len > len(iterable[i]):
            min_len = len(iterable[i])

    for i in range(min_len):
        new = []
        for item in iterable:
            new.append(item[i])
        res.append(func(*new))

    yield res


def multiplication(num):
    return num * num


numbers = [1, 4, 6, 7, 36, 8, 10]
gen_map = custom_map(multiplication, numbers)

for element in gen_map:
    print(element)
