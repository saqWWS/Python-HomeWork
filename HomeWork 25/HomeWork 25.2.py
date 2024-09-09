class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.set_price(price)

    def get_title_auther(self):
        print("Book title is:", self.__title)
        print("Book auther is:", self.__author)
        print(f"Book price is: {self.__price} $")

    def set_price(self, min_price):

        if min_price < 15:
            print("You can't sell this book for less than $15")
        else:
            self.__price = min_price


book_1 = Book("Learning Python", "Mark Lutz", 16)

book_1.get_title_auther()
print()
book_1.set_price(98)
book_1.set_price(13)
book_1.set_price(13)
book_1.get_title_auther()
