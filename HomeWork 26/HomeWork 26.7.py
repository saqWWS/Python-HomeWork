class RangeDescriptor:
    def __get__(self, instance, owner):
        return instance.one_to_hundred

    def __set__(self, instance, value):
        if not isinstance(value, int) or not 1 <= value <= 100:
            raise ValueError("Value must be an integer between 1 and 100.")

        instance.one_to_hundred = value


class Product:
    price = RangeDescriptor()


less = Product()
less.price = 13
print(less.price)

more = Product()
more.price = 103
print(more.price)
