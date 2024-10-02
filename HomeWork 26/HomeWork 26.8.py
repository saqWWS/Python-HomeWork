class PasswordValidator:
    def __init__(self):
        self.__min_length = 8
        self.__contains_numbers = "123456789"
        self.__symbols = ("~`!@#$%^&*()_-+={[}]|\:;'<,>.?/")

    def __get__(self, instance, owner):
        return instance.password

    def __set__(self, instance, value):
        if len(value) <= self.__min_length:
            raise ValueError(f"Password must be at least {self.__min_length} characters long.")

        if not any(num in self.__contains_numbers for num in value):
            raise ValueError("Password must contain at least one number.")

        if not any(char in self.__symbols for char in value):
            raise ValueError("Password must contain at least one special symbol.")

        instance.password = value


class Account:
    valid_password = PasswordValidator()


password_1 = Account()
password_1.valid_password = "Iflessthanmore1@"
print(password_1.valid_password)
