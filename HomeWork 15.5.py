def capital_letter(letter):
    for i in letter:
        if i.isupper():
            print(i)
            break

    else:
        print("there is no capital letter in your sentence.")


letter = input("Write a sentence:\t")


capital_letter(letter)
