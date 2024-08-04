def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier_of_3 = make_multiplier_of(3)
multiplier_of_5 = make_multiplier_of(5)
multiplier_of_10 = make_multiplier_of(7)

print(multiplier_of_3(10))   
print(multiplier_of_5(20))   
print(multiplier_of_10(30))

