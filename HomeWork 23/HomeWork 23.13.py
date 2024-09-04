def custom_filter(func, iterable):
    res = []

    if func is None:
        for i in iterable:
            res.append(i)

    else:
        for item in iterable:
            if func(item):
                res.append(item)

    yield res


def even_num(nums):
    if nums % 2 == 0:
        return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

gen_filter = custom_filter(even_num, numbers)
for element in gen_filter:
    print(element)
