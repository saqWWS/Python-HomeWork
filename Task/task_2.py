import abc


class Cars(abc.ABC):

    def __init__(self, make: str, model: str, price: float):
        self.make = make
        self.model = model
        self.price = price


class ElectricCar(Cars):
    def __init__(self, make: str, model: str, price: float):
        super().__init__(make, model, price)

    def __repr__(self):
        return f"Electric Car - Make: {self.make}, Model: {self.model}, Price: {self.price}"


class HybridCar(Cars):
    def __init__(self, make: str, model: str, price: float):
        super().__init__(make, model, price)

    def __repr__(self):
        return f"Hybrid Car - Make: {self.make}, Model: {self.model}, Price: {self.price}"


class GasolineCar(Cars):
    def __init__(self, make: str, model: str, price: float):
        super().__init__(make, model, price)

    def __repr__(self):
        return f"Gasoline Car - Make: {self.make}, Model: {self.model}, Price: {self.price}"


class CarsStock:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Cars):
        self.cars.append(car)

    def show_cars(self):
        return [str(car) for car in self.cars]

    def __repr__(self):
        return f"Cars in Stock: {self.cars}"


class Customers:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def search_car(self, car: Cars, stock: CarsStock):
        if car in stock.cars:
            print(f"We have {car} in stock!")
        else:
            print("Sorry, this car is not available.")

    def __repr__(self):
        return f"Customer: {self.name}, Contact: {self.contact_info}"


class Salespeople:
    def __init__(self, name: str, commission_rate: float):
        self.name = name
        self.commission_rate = commission_rate
        self.cars = []

    def add_car(self, car: Cars):
        self.cars.append(car)

    def view_inventory(self):
        return [str(car) for car in self.cars]

    def remove_car(self, car: Cars):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed {car} from inventory.")

    def show_cars(self):
        for car in self.cars:
            print(car)

    def __repr__(self):
        return f"Salesperson: {self.name}, Commission Rate: {self.commission_rate}"


electric_1 = ElectricCar("Mercedes-Bnez", "EQS", 12000)
electric_2 = ElectricCar("BMW", "iX", 13000)

hybrid_1 = HybridCar("Toyota", "Prius", 9000)
hybrid_2 = HybridCar("Audi", "A3 Sportback", 11000)

gasoline_1 = GasolineCar("Alfa Romeo", "Giulia", 15000)
gasoline_2 = GasolineCar("Subaru", "Imreza WRX STI", 14000)

car_stock = CarsStock()

car_stock.add_car(electric_1)
car_stock.add_car(electric_2)
car_stock.add_car(hybrid_1)
car_stock.add_car(hybrid_2)
car_stock.add_car(gasoline_1)
car_stock.add_car(gasoline_2)

print(car_stock.show_cars())

alice = Customers("Alice", "+369459654")

alice.search_car(gasoline_2, car_stock)

salesperson_lili = Salespeople("Lili", 0.5)

salesperson_lili.add_car(gasoline_1)
salesperson_lili.add_car(hybrid_2)

salesperson_lili.show_cars()


salesperson_lili.remove_car(gasoline_1)

salesperson_lili.show_cars()
