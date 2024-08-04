def make_greeting(greeting):
    def person_1(name):
        return name + greeting
        def person_2(name):
            return name + greeting
            def person_3(name):
                return name + greeting
                def person_4(name):
                    return name + greeting
                return person_4
            return person_3
        return person_2
    return person_1
    

first_ = make_greeting("Hello Team!")
second_ = make_greeting("Hi! Ann.")
third_ = make_greeting("How are you Ann?")
fourth_ = make_greeting("What are your plans for today?")
third_again = make_greeting("You have to work hard today.")

person_one = first_("Ann:\t")
person_two = second_("Bob:\t")
person_three = third_("Mr. Rodríguez:\t")
person_four = fourth_("Dias:\t")
three_again = third_again("Mr. Rodríguez:\t")


print(person_one)
print(person_two)
print(person_three)
print(person_four)
print(three_again)