import abc


class MenuItem:
    __slots__ = ("name", "price", "ingredients")

    def __init__(self, name: str, price: float, ingredients: list):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"MenuItem((name is: '{self.name}', price is: '{self.price}', ingredients are: '{self.ingredients}'"


class Appetizer(MenuItem):
    __slots__ = ("size_food",)

    def __init__(self, name: str, price: float, ingredients: list, size_food: float):
        super().__init__(name, price, ingredients)
        self.size_food = size_food
        if not (1.15 <= self.size_food <= 1.30):
            raise ValueError("You can't break the appetizer size")

    def __str__(self):
        return (f"Appetizer Menu: (name is: '{self.name}', price is: '{self.price}$', "
                f"ingredients are: '{self.ingredients}', weight is: '{self.size_food:.2f}g.')")


bruschetta = Appetizer("Bruschetta", 8.50, ["bread", "tomato", "basil"], 1.15)
stuffed_mushrooms = Appetizer("Stuffed Mushrooms", 10.00, ["mushrooms", "cream cheese", "garlic", "herbs"], 1.20)
spring_rolls = Appetizer("Spring Rolls", 7.25, ["rice paper", "vegetables", "shrimp", "vermicelli"], 1.30)


class Entree(MenuItem):
    __slots__ = ("size_food",)

    def __init__(self, name: str, price: float, ingredients: list, size_food: float):
        super().__init__(name, price, ingredients)
        self.size_food = size_food
        if not (150 <= self.size_food <= 300):
            raise ValueError("You can't break the appetizer size")

    def __str__(self):
        return (f"Entree Menu: (name is: '{self.name}', price is: '{self.price}$', "
                f"ingredients are: '{self.ingredients}', weight is: '{self.size_food:.2f}g.')")


grilled_salmon = Entree("Grilled Salmon", 19.99, ["salmon", "lemon", "herbs", "olive oil"], 200.0)
chicken_alfredo = Entree("Chicken Alfredo", 15.50, ["chicken", "fettuccine", "alfredo sauce", "parmesan"], 250.0)
vegetable_stir_fry = Entree("Vegetable Stir-Fry", 12.00, ["broccoli", "carrots", "bell peppers", "soy sauce"], 300.0)


class Dessert(MenuItem):
    __slots__ = ("calories",)

    def __init__(self, name: str, price: float, ingredients: list, calories: float):
        super().__init__(name, price, ingredients)
        self.calories = calories

    def __str__(self):
        return (f"Dessert Menu: (name is: '{self.name}', price is: '{self.price}$', "
                f"ingredients are: '{self.ingredients}', calories is: '{self.calories}' kcal)")


chocolate_lava_cake = Dessert("Chocolate Lava Cake", 7.50, ["chocolate", "butter", "sugar", "eggs", "flour"], 350)
cheesecake = Dessert("Cheesecake", 8.00, ["cream cheese", "sugar", "graham cracker crust", "eggs"], 450)
fruit_sorbet = Dessert("Fruit Sorbet", 5.00, ["fruit puree", "sugar", "water"], 150)


class Customer:
    __slots__ = ("name", "contact_info", "order_history")

    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def add_order(self, menu_item):
        self.order_history.append(menu_item)

    def history(self):
        print(f"Customer: {self.name}, Contact: {self.contact_info}")
        for order in self.order_history:
            print(order)

    def __str__(self):
        return f"Name is: {self.name}, contact info: {self.contact_info}"


class Order(abc.ABC):
    __slots__ = ("customer", "menu_items", "total_price")

    def __init__(self, customer: Customer):
        self.customer = customer
        self.menu_items = []
        self.total_price = 0.0

    @abc.abstractmethod
    def calculate_total(self):
        ...

    @abc.abstractmethod
    def add_menu_item(self):
        ...


class DineInOrder(Order):
    def __init__(self, customer: Customer):
        super().__init__(customer)

    def add_menu_item(self, itm):
        self.menu_items.append(itm)
        self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.menu_items)

    def __str__(self):
        menu_items_str = ', '.join([str(item) for item in self.menu_items])
        return f"Order for {self.customer.name}, Items: [{menu_items_str}]"


class TakeawayOrder(Order):
    def __init__(self, customer: Customer):
        super().__init__(customer)

    def add_menu_item(self, itm):
        self.menu_items.append(itm)
        self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.menu_items)

    def __str__(self):
        menu_items_str = ', '.join([str(item) for item in self.menu_items])
        return f"Order for {self.customer.name}, Items: [{menu_items_str}]"


class DeliveryOrder(Order):
    __slots__ = ("delivery", "address")

    def __init__(self, customer: Customer, address: str):
        super().__init__(customer)
        self.delivery = 5
        self.address = address

    def add_menu_item(self, itm):
        self.menu_items.append(itm)
        self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.menu_items) + self.delivery

    def __str__(self):
        menu_items_str = ', '.join([str(item) for item in self.menu_items])
        return f"Order for {self.customer.name}, delivery charge is {self.delivery}$, address: {self.address}. Items: [{menu_items_str}]"


class Review:
    __slots__ = ("customer_name", "order", "rating", "comments")

    def __init__(self, customer_name: Customer, order: Order, rating: int, comments: input):
        self.customer_name = customer_name
        self.order = order
        self.rating = rating
        self.comments = comments

    def __str__(self):
        menu_items_str = ', '.join([item.name for item in self.order.menu_items])
        return (f"Review by {self.customer_name}:\n"
                f"Order Items: [{menu_items_str}]\n"
                f"Rating: {self.rating}/5\n"
                f"Comments: {self.comments}")


customer_1 = Customer("Mauro", "98461285")
customer_2 = Customer("Michel", "55336478")
customer_3 = Customer("Bobi", "93744536")

dine_in = DineInOrder(customer_1)
dine_in.add_menu_item(bruschetta)

print(dine_in)

take = TakeawayOrder(customer_2)
take.add_menu_item(spring_rolls)

print(take)

take_and_send = DeliveryOrder(customer_3, "1801 N Pennsylvania Ave, Independence, KS 67301, USA")
take_and_send.add_menu_item(stuffed_mushrooms)
take_and_send.add_menu_item(cheesecake)

print(take_and_send)

review_1 = Review(customer_1.name, dine_in, rating=5, comments=input("Add a comment: \t"))
print(review_1)
