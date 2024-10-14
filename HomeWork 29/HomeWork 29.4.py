import abc


class Car(abc.ABC):
    def __init__(self, mark: str, year: int, colour: str):
        self.mark = mark
        self.year = year
        self.colour = colour

    @abc.abstractmethod
    def display_features(self):
        ...

    @abc.abstractmethod
    def drive(self):
        ...

    @abc.abstractmethod
    def play_music(self):
        ...


class CruiseControl(abc.ABC):
    @abc.abstractmethod
    def cruise_control(self):
        ...


class CarsMT(Car):
    def __init__(self, mark: str, year: int, colour: str):
        super().__init__(mark, year, colour)
        self.transmission = "Manual Transmission"

    def display_features(self):
        return f"The car is a {self.mark}, built in {self.year}, and it's color is {self.colour}."

    def drive(self):
        return f"You can drive the {self.mark} with {self.transmission}."

    def play_music(self):
        return f"{self.mark} has a music system."


class CarsAT(Car, CruiseControl):
    def __init__(self, mark: str, year: int, colour: str):
        super().__init__(mark, year, colour)
        self.transmission = "Automatic Transmission"

    def display_features(self):
        return f"The car is a {self.mark}, built in {self.year}, and it's color is {self.colour}."

    def drive(self):
        return f"You can drive the {self.mark} with {self.transmission}."

    def play_music(self):
        return f"{self.mark} has a music system."

    def cruise_control(self):
        return f"{self.mark} supports cruise control."


mt_car = CarsMT("Subaru", 2004, "Blue")

print(f" {mt_car.display_features()} \n {mt_car.drive()} \n {mt_car.play_music()}")

at_car = CarsAT("Alfa Romeo", 2021, "Red")

print(f" {at_car.display_features()} \n {at_car.drive()} \n {at_car.play_music()} \n {at_car.cruise_control()}")


# GOOD VERSION


class Car(abc.ABC):
    """
    This way we avoid code duplication and more volume,
    and it's easier for the programmer and the user to understand the code.
    The other point is that if the child class is not going to use all the methods of the main class,
    you don't need to overload it, it's easier to have classes,
    which will have their own interface, a container, from which methods will be inherited as needed.
    """

    def __init__(self, mark: str, year: int, colour: str):
        self.mark = mark
        self.year = year
        self.colour = colour

    @abc.abstractmethod
    def display_features(self):
        ...

    @abc.abstractmethod
    def drive(self):
        ...

    @abc.abstractmethod
    def play_music(self):
        ...

    @abc.abstractmethod
    def cruise_control(self):
        ...


class CarsMT(Car):
    def __init__(self, mark, year, colour):
        super().__init__(mark, year, colour)
        self.transmission = "Manual Transmission"

    def display_features(self):
        return f"The car is a {self.mark} brand, built in {self.year}, and it's color is {self.colour}."

    def drive(self):
        return f"You can drive the {self.mark} with {self.transmission}."

    def play_music(self):
        return f"{self.mark} has a music system."

    def cruise_control(self):
        ...


#
#
class CarsAT(Car):
    def __init__(self, mark, year, colour):
        super().__init__(mark, year, colour)
        self.transmission = "Automatic Transmission"

    def display_features(self):
        return f"The car is a {self.mark} brand, built in {self.year}, and it's color is {self.colour}."

    def drive(self):
        return f"You can drive the {self.mark} with {self.transmission}."

    def play_music(self):
        return f"{self.mark} has a music system."

    def cruise_control(self):
        return f"{self.mark} supports cruise control."


mt_car = CarsMT("Subaru", 2004, "Blue")

print(f" {mt_car.display_features()} \n {mt_car.drive()} \n {mt_car.play_music()}")

at_car = CarsAT("Alfa Romeo", 2021, "Red")

print(f" {at_car.display_features()} \n {at_car.drive()} \n {at_car.play_music()} \n {at_car.cruise_control()}")

# BAD VERSION
