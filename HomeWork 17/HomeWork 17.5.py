def maximum(new_list):

    for i in range(3):
        num = int(input(f"Write a number {i + 1}:\t"))
        new_list.append(num)
        
    print(new_list)
                
    max_element = new_list[0]

                    
    for element in new_list:
        if element > max_element:
            max_element = element
                                
    print(f"Largest element is: {max_element}")
                                        

new_list = []

maximum(new_list)
