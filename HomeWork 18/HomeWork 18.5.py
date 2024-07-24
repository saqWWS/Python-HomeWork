def shopping_details(shirt, pants, shoes, coat):

    all_product = [("Shirt", shirt), ("Pants", pants), ("Shoes", shoes), ("Coat", coat)]

    for item_name, item_details in all_product:
        print(f"{item_name} details:")
        for key, value in item_details.items():
            if key == "price":
                print(f"  {key.capitalize()}: ${value}")
            else:
                print(f"  {key.capitalize()}: {value}")
        print()


dict_details = {
    "shirt": {
    "color": "Red",
    "size": "S",
    "made": "Vietnam",
    "price": 12.9,
    },

    "pants": {
    "color": "Blue",
    "size": 32,
    "made": "Bangladesh",
    "price": 32.9,
    },

    "shoes": {
    "color": "Black",
    "size": 39,
    "made": "Armenia",
    "price": 49.9,
    },

    "coat": {
    "color": "Brown",
    "size": "XXL",
    "made": "Italy",
    "price": 109.9,
    },
}

shopping_details(**dict_details)
