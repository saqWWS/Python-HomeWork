def make_config(key, value):
    def new_dict():
        return {key: value}
    return new_dict

dictionary = make_config("Ann", 31)
dictionary_two = make_config("Bob", "Marley")

config_dict = dictionary(), dictionary_two()

print(config_dict)