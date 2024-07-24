def update_user_settings(user_dict, user_key, **kwargs):

    if user_key in user_dict:
        user = user_dict[user_key]
        for key, value in kwargs.items():
            if key in user:
                user[key] = value


user_dict = {
    "Person 1": {
        "Name": "Bob",
        "Surname": "Smith",
        "Age": 36,
        "Language": "English",
        "Country": "USA",
        "City": "Little Rock",
        "Specialty": "Developer"
    },

    "Person 2": {
        "Name": "Eugeniu",
        "Surname": "Cociuc",
        "Age": 32,
        "Language": "Romanian",
        "Country": "Moldova",
        "City": "Balti",
        "Specialty": "Footballer"
    },
    
    "Person 3": {
        "Name": "Harrison",
        "Surname": "Ford",
        "Age": 84,
        "Language": "Armenian",
        "Country": "Mexico",
        "City": "Los Angeles",
        "Specialty": "Actor"
        },
}


def apply_settings(user_dict, user_key, **settings):
    
    update_user_settings(user_dict, user_key, **settings)

apply_settings(user_dict, "Person 1", Age=37, City="New York", Specialty="Senior Developer")
apply_settings(user_dict, "Person 2", City="Chișinău", Age=31)
apply_settings(user_dict, "Person 3", Country="USA", City="Chicago", Age=82)

for person, info in user_dict.items():
    print(f"{person}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()
