def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    yield value


list_of_elements = [4, 6, 3, 5, 7]

gen_list = reduce(lambda x, y: x + y, list_of_elements)

for item in gen_list:
    print(item)
