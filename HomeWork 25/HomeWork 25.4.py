class ShoppingCart:
    def __init__(self):
        self.__list_of_items = dict()

    def add_item(self, item, price):

        self.__list_of_items[item] = price

    def remove_item(self, item):
        if item in self.__list_of_items:
            self.__list_of_items.pop(item)
            print(f"'{item}' removed from the list.")
        else:
            print(f"'{item}' not found in the list.")

    def total_items(self):
        print(f"All items in the list: {self.__list_of_items}: Items in cart: {len(self.__list_of_items)}")


shopping = ShoppingCart()

shopping.add_item("T-Shirt", 16)
shopping.add_item("Shoes", 27)
shopping.add_item("Scarf", 7)
shopping.add_item("Coat", 156)
shopping.total_items()
shopping.remove_item("Shoes")
shopping.remove_item("Coat")
shopping.total_items()
