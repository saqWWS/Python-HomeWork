import random

count = int(input("Please input count of persons:\t"))

add_person = []

person = {"first_name": None, "last_name": None, "email": None, "phone_number": None, "password": None}

for user in range(count):
    for key in person.keys():
        person[key] = input(f"Please enter {key} for {user + 1} person:\t")
    add_person.append(person.copy())


for person in add_person:
    person.update({"ID": random.randint(11, 35)})

print(add_person)


search_name = input("Search by name:\t")

for val in add_person:
    if search_name.upper() in (val["first_name"].upper(), val["last_name"].upper()):
        print(f"ID: {val['ID']}")
        print(f"First Name: {val['first_name']}")
        print(f"Last Name: {val['last_name']}")
        print(f"E-mail: {val['email']}")
        print(f"Phone Number: {val['phone_number']}")
        print(f"Password: {val['password']}")
        break
else:
    print("Such a person does not exist.")

