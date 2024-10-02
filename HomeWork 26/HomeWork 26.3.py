class Temperature:
    def __init__(self, value: float):
        self.__celsius = value

    @property
    def to_fahrenheit(self):
        fahrenheit = (self.__celsius * 9 / 5) + 32
        return f" Fahrenheit is: {fahrenheit:.2f}"

    @to_fahrenheit.setter
    def to_fahrenheit(self, value):
        self.__celsius = value


temp = Temperature(36.6)
print(f"Initial Fahrenheit: {temp.to_fahrenheit}")

temp.to_fahrenheit = 12
print(f"Updated Fahrenheit: {temp.to_fahrenheit}")
