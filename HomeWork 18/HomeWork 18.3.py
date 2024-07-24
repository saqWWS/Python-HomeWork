def user_profile(name, surename, age, city):

    print("Name:", name)
    print("Surename:", surename)
    print("Age:", age)
    print("City:", city, "\n")
    
    return f"I am {name} {surename}, {age} years old, I live in {city}."


name = input("Write a name:\t")
surename = input("Write a surename:\t")

print(user_profile(name, surename, age=23, city="Rome"))
