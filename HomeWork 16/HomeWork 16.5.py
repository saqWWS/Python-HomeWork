def list_elements(element):
    if not element:
        return
    print(element[0])
    list_elements(element[1:])


element = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_elements(element)
