def new_line(input_str):
        
    if not input_str:
        return
        
    print(input_str[0])
            
    new_line(input_str[1:])

                

input_str = input("Write something:\t")

new_line(input_str)
