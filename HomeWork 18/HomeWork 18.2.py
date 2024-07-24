def shopping(shirt, pants, shoes, coat, tax_rate=0.09):
    shirt_tax = shirt * tax_rate
    pants_tax = pants * tax_rate
    shoes_tax = shoes * tax_rate
    coat_tax = coat * tax_rate

    total_tax = shirt_tax + pants_tax + shoes_tax + coat_tax
    total_price = shirt + pants + shoes + coat + total_tax

    print(f"The cost of the shirt is: ${shirt:.2f}, tax is: ${shirt_tax:.2f}")
    print(f"The cost of the pants is: ${pants:.2f}, tax is: ${pants_tax:.2f}")
    print(f"The cost of the shoes is: ${shoes:.2f}, tax is: ${shoes_tax:.2f}")
    print(f"The cost of the coat is: ${coat:.2f}, tax is: ${coat_tax:.2f}")
    print(f"Total TAX is: ${total_tax:.2f}")
        
    return f"The total amount is ${total_price:.2f}, including tax ${total_tax:.2f}"


shirt = float(input("Write the price of the shirt:\t"))
pants = float(input("Write the price of the pants:\t"))
shoes = float(input("Write the price of the shoes:\t"))
coat = float(input("Write the price of the coat:\t"))

print(shopping(shirt, pants, shoes, coat))
