def retry_func(func):
    time = 3

    def wrapper(*args, **kwargs):
        nonlocal time
        while True:
            if time:
                time -= 1
                result = func(*args, **kwargs)
                return result
            else:
                break

    return wrapper


import json


@retry_func
def read_from_file():
    file = open("person.json", 'r')
    data = json.load(file)
    file.close()

    user_input = input("Write a name: ")

    found = False
    for item in data:
        if item.get("name") == user_input:
            print(f"{user_input} found in the JSON data")
            print(item)
            found = True
            break

    if not found:
        print(f"{user_input} not found in the JSON data")


read_from_file()
read_from_file()
read_from_file()
read_from_file()
read_from_file()
