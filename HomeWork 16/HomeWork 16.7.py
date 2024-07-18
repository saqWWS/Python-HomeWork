def reverse_str(input_str):
    if not input_str:
        return ""
                        
    return reverse_str(input_str[1:]) + input_str[0]


input_str = input("Write something: \t")

print(reverse_str(input_str))
