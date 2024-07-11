import random


contoset = int(input("Write the number of elements:\t"))

a_set = []
b_set = []

for i in range(contoset):
    first_input = random.randint(1, 30)
    second_input = random.randint(1, 30)
    a_set.append(first_input)
    b_set.append(second_input)
    
print("First Set: ", set(a_set))
print("Second Set: ", set(b_set))

a_set, b_set = set(a_set), set(b_set)

print(a_set == b_set)
print(f"A union B:\t {a_set.union(b_set)}")
print(f"A intersection B:\t {a_set.intersection(b_set)}")
print(f"A difference B:\t {a_set.difference(b_set)}")
print(f"B difference A:\t {b_set.difference(a_set)}")         

