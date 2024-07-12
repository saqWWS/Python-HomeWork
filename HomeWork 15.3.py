import random



def list_elements(empty_list):
    for gen in range(5):
        empty_list.append(random.randint(1, 15))

    for i in empty_list:
        print(i)


empty_list = []


list_elements(empty_list)
