dont_use = ["admin", "root", "system"]

special_characters = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"

all_emails = set()

count = int(input("Please enter the count of people:\t"))

add_person = []


for i in range(count):

    person = {"first_name": None, "last_name": None, "email": None, "phone": None, "password": None}

    while True:
        person["first_name"] = input(f"Please enter your First Name: {i+1} \t")

        if not person["first_name"].isalpha():
            print("The name should contain only alphabetic characters. Please try aganin.")
        
        elif person["first_name"].lower() in dont_use:
            print(f"You can not use '{person['first_name']}' for first name. Please choose a different name.")

        elif len(person["first_name"]) <= 4:
            print("The name is too SHORT. It should be at least 4 characters long. Please try again.")

        elif len(person["first_name"]) >= 20:
            print("The name is too LONG. It should not be more than 20 characters. Please try again.")

        else:
            break

    while True:
        person["last_name"] = input(f"Please enter your Last Name: {i+1} \t")

        if not person["last_name"].isalpha():
            print("The surname should contain only alphabetic characters. Please try again")

        elif person["last_name"].lower() in dont_use:
            print(f"You can not use '{person['last_name']}' for last name. Please choose a different name.")

        elif len(person["last_name"]) <= 5:
            print("The surname is to SHORT. It should be at least 5 characters long. Please try again")

        elif len(person["last_name"]) >= 20:
            print("The surname is to LONG. It should not be more than 20 characters. Please try again")

        else:
            break

    while True:
        person["email"] = input(f"Please enter your e-mail address: {i+1} \t")

        if person["email"] in all_emails:
            print("E-mail already registered.")
            continue

        email = person["email"]

        if "@" and "." in email:
            all_emails.add(person["email"])
            break

        else:
            print("Invalid e-mail address. Please try again.")

    while True:
        person["phone"] = input(f"Please enter your phone number: {i+1} \t")

        phone = person["phone"]

        if "+374" in phone:
            if len(person["phone"]) == 10:
                break

        if person["phone"][0] == "0":
            if len(person["phone"]) == 9:
                break

        else:
            print("Invalid phone number. Please enter 9 digits or start with '+374'")


    while True:
        password1 = input(f"Please enter your password: {i+1} \t")
        password2 = input("Pkease re-enter your password: \t")

        if password1 != password2:
            print("Passwords do not match. Please try again.")
            continue

        person["password"] = password1

        has_upper = any(c.isupper() for c in person["password"])
        has_lower = any(c.islower() for c in person["password"])
        has_digit = any(c.isdigit() for c in person["password"])
        has_special = any(c in special_characters for c in person["password"])

        is_valid = has_upper and has_lower and has_digit and has_special and len(person["password"]) >= 8

        if is_valid:
            break

        else:
            print("Password is NOT valid. Please try again")


    add_person.append(person)

print(add_person)

for person in add_person:
    print(f"Your name is {person['first_name']}")
    print(f"Your Surname is {person['last_name']}")
    print(f"Your E-mail is {person['email']}")
    print(f"Your phone number is {person['phone']}")
    print(f"Your password os {person['password']}")



