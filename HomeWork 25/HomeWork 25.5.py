class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def get_product(self):
        print("Product name:", self.__product_name)
        print("Product ID:", self.__product_id)
        print("Product quantity:", self.__quantity_in_stock)

    #
    def get_product_id(self):
        print(f"Product 'ID': {self.__product_id}")

    def get_product_name(self):
        print(f"Product 'NAME': {self.__product_name}")

    def get_quantity_in_stock(self):
        print(f"Product 'QUANTITY IN STOCK' are: {self.__quantity_in_stock}")

    def set_product_id(self):
        if self.set_product_name(self.__product_name) == self.set_product_name(self.__product_name):
            self.__product_id += 1
        else:
            print(f"Product name is the same. ID remains: {self.__product_id}")

    def set_product_name(self, value):
        if value != self.__product_name:
            self.__product_id += 1
            self.__product_name = value
            self.__quantity_in_stock += 1
            print(f"Adding new product: '{value}', New 'ID' is: {self.__product_id}")

    def adding_stock(self):
        if self.__quantity_in_stock >= 35:
            raise ValueError("You don't have enough space!")


product_1 = Product(1, "BMW", 30)
# product_1.get_product()
product_1.get_product_id()
product_1.get_product_name()
product_1.get_quantity_in_stock()
product_1.set_product_name("Alfa Romeo")
product_1.set_product_name("Subaru")
product_1.set_product_name("Mercedes-Bnez")
product_1.set_product_name("Lancia")
# product_1.set_product_name("Hyundai")
# product_1.set_product_name("Audi")

product_1.adding_stock()
product_1.set_product_id()
product_1.get_product()
