def custom_zip(*iterables):
    min_len = min((len(item) for item in iterables))
    res = [tuple([item[i] for item in iterables]) for i in range(min_len)]
    yield res


age = [32, 26, 56, 19, 21]
name = ["Smith", "Iulia", "Ioana", "Bob"]

gen_zip = custom_zip(age, name)
for elements in gen_zip:
    print(elements)
